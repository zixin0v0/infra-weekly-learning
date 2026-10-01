# W6 第一段备课：Attention 语义与后端

[单元范围](README.md) · [三段导学](study-guide.md) · [资料复核](refresh-2026-10-01.md)

备课日期：2026-10-01。资料预算：40 分钟。状态：备课已准备；模型与后端验证待完成。

## 目标与先修

让显式 Attention 和 SDPA 在相同条件下计算同一输出。先通过 W5，以及 [模型结构检查 C](../../docs/prerequisites.md)；shape 和 mask 可先纸面分析，GPU 后端需实际证据。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 15 分钟 | [SDPA 教程](https://docs.pytorch.org/tutorials/intermediate/scaled_dot_product_attention_tutorial.html) 的开头接口示例 | Q/K/V 调用结束；不运行整篇模型示例 |
| 15 分钟 | 同页 Explicit Dispatcher Control | SDPBackend、sdpa_kernel 的选择与限制结束 |
| 10 分钟 | [PyTorch 2.14 SDPA API](https://docs.pytorch.org/docs/2.14/generated/torch.nn.functional.scaled_dot_product_attention.html) 的 dropout 警告、布尔 mask、shape | 三项契约核对完成即停 |

访问日：2026-10-01。API 页标 beta；网页 2.14 不代表本机 2.5.1 或目标 GPU 环境版本。

## 中文助读

主线自注意力 Q/K/V 为 [B,H,S,D]，score 为 [B,H,S,S]；除以 sqrt(D)，施加 mask，沿最后一维 Softmax，再乘 V 得到 [B,H,S,D]。

SDPA 布尔 mask 的 True 表示允许参与，不能直接套用其他接口“True 表示屏蔽”的约定。模块 eval 并不会自动覆盖传给函数的 dropout_p；本段显式设 0。调用 SDPA 只说明接口，实际 fused/math 路径受设备、dtype、shape 等条件影响。

## 暂停题与预测

1. B=1、H=2、S=3、D=4 时，score 和输出各有多少元素？causal 下第一个 query 能看到哪些 key？
2. 只把模块设 eval，却传 dropout_p=0.1，会保证重复输出一致吗？若强制 fused 后端失败，应记录什么？

先按维度写矩阵乘法，再用三位置 mask 表，最后回 API 契约。

## 动手与检查

唯一入口：`labs/03-triton-attention/decoder-profiling/`。动手时写显式参考、SDPA 路径和小 Block；先使用小 shape、FP32、dropout=0，固定输入与 seed、eval/autograd 条件。

测试 causal 开/关以及一组明确布尔 mask，主线各 query 至少有一个有效 key；逐元素误差和容差记录。选择 math 作为可解释对照，另检查当前设备支持的 fused 路径；不支持时保留警告与回退，不能把两次不同语义当加速。

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| mask 后输出反了 | API 布尔 mask Note | True 的含义 |
| 同一输入重复不同 | dropout Warning | 实际传入值和随机状态 |
| 后端身份不明 | Explicit Dispatcher Control | 请求后端与实际可用性证据 |

- [ ] shape、缩放、mask、dropout 与 autograd 对齐。
- [ ] 参考误差和后端限制有实际记录。
- [ ] 未覆盖功能单列，SDPA 不直接标作 FA4。

在 `notes.md` 的 `W6-S01` 留下预测、命令和限制；通过后进入 [第二段](session-02.md)。
