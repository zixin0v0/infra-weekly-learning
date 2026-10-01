# W6 第二段学习指南：FlashAttention 的 IO 与资源账本

[单元范围](README.md) · [三段学习导航](study-guide.md) · [资料复核](refresh-2026-10-01.md) · [上一段](session-01.md)

整理日期：2026-10-01。原文选读预算：50 分钟。状态：学习指南已整理；账本与实现核对待完成。

本地图解、暂停题与核对另计入本单元的自查时段，完整时间见 [分项预算](../../docs/study-guide.md#time-budget)。

## 目标与先修

用 W4 的 tile 和 W5 的在线状态解释哪些中间矩阵可以不完整写回显存。先通过 Attention 语义，主线固定一个小 Block 的前向。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 15 分钟 | [FlashAttention 原论文的 arXiv v2](../../resources/README.md#r-flash) §2.1～2.2 | Attention 与硬件存储层次结束 |
| 25 分钟 | 同 PDF §3.1、Algorithm 1 | 前向 tile、最大值、归一化与输出状态；反向后置 |
| 10 分钟 | 同 PDF §3.2 | IO 复杂度结论；证明与稀疏扩展后置 |

访问日：2026-10-01；v2 提交于 2022-06-23，表示原论文的修订版本，不是 FlashAttention-2。论文 HBM/SRAM 是分析层次，本机消费级显存介质不同，不照搬带宽数字。

## 概念说明

```mermaid
flowchart LR
    qkv["Q / K / V tile"] --> score["片内 score 与概率"]
    score --> state["更新最大值 / 分母 / 加权输出"]
    state --> next["处理下一组 K / V tile"]
    next --> state
    state --> output["最终输出"]
```

图是前向依赖示意。经典显式路径存放完整 S×S score/概率；分块算法维护状态，避免把这两张矩阵完整写回显存。W5 的分母状态还需配合加权输出状态，不能只合并分母就得到 Attention。

设模型宽度 W=H×D，MLP 中间宽度 F。忽略 bias/LayerNorm，QKV 与输出投影参数共 4W²，两层 MLP 参数 2WF；前向线性层 FLOPs 为 8BSW²+4BSWF，QKᵀ 和 PV 为 4BHS²D。Softmax、激活、归一化另列，不藏入“全模型精确 FLOPs”。

## 暂停题与预测

1. 固定 B/H/D，S 翻倍时 score 存储与 Attention 矩阵乘 FLOPs 各变几倍？投影与 MLP 呢？
2. 省去完整 score 写回是否代表数学注意力近似化？为何不同浮点顺序仍可能有误差？

先列 shape，再分线性/S² 项，最后回 Algorithm 1 的状态。

## 读图与自查

```text
X[B,S,W] ─→ LayerNorm → QKV / Attention / 输出投影 ─→ 加 X ─→ R[B,S,W]
R[B,S,W] ─→ LayerNorm → Linear(W,F) → GELU → Linear(F,W) ─→ 加 R ─→ Y[B,S,W]
```

这是主线小型 pre-norm Block 的结构图：Q/K/V、输出投影和 MLP 的两个 Linear 均不使用 bias，dropout=0，不加 KV Cache；两处 LayerNorm 的可学习参数单列。先按图逐项核对 shape，再汇总资源，W=H×D。

<details>
<summary>写下预测后，再核对本段问题</summary>

**题 1**：B/H/D 固定时，score 元素数 BHS² 与 Attention 两次矩阵乘 FLOPs 都变为 4 倍；投影和 MLP 随 token 数 S 线性增长，变为 2 倍；参数数不变。

**题 2**：分块重排计算与存储，并不自动把精确 Attention 改成近似算法。浮点舍入仍可能使结果有小差别，要按设定容差检查。

**账本参照**：W=128、F=512 时，投影参数=65,536，MLP 参数=131,072，共 196,608（未计 LayerNorm）。B=1、S=128 的线性层为 50,331,648 FLOPs，Attention 两次矩阵乘为 8,388,608 FLOPs；单张 FP32 score 为 262,144 字节。两处标准 LayerNorm 若各含 weight 与 bias，共另加 4W=512 个参数。先核对层定义，再用这些推导值检查程序，不把它们称为峰值显存。

这些说明用于核对推导；运行结果仍需自己验证。答错时保留原答案，回看本段“读哪里”或“卡点”指向的位置，再换一个小输入重做。

</details>

## 可选：问 AI

先独立作答和核对，仍有疑问时再使用；跳过本节不影响完成本段。

> 我根据这个小型 pre-norm Block 画了形状和资源表：【粘贴】。请先找一项线性随 S 增长和一项随 S² 增长的量，让我解释原因；再追问在线 Attention 为什么连加权输出也要重新缩放。不要替我实现 FlashAttention，也不要把理论字节相加成实测峰值。

## 动手与检查

继续 `labs/03-triton-attention/decoder-profiling/`。可选固定 B=1、S=128、H=4、D=32、F=512 的小 Block，按本段结构图固定层定义。保存参数表、激活形状表、FLOPs 表，bias/残差/归一化按实际实现单列。

FP32 下单张 score 的理论字节为 1×4×128²×4=262144；概率矩阵另列。账本不等于峰值分配，不能把所有生命周期不同的 Tensor 简单相加。先与真实 shape、numel 核对，S 翻倍只作纸面预测，可选实测另安排；不新增手写 FlashAttention。

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 分块输出解释不清 | Algorithm 1、W5 在线状态 | 加权输出为什么也重缩放 |
| 账本与峰值不符 | 自己的 Tensor 生命周期 | 分配、共享与临时工作区 |

- [ ] 参数、激活和 FLOPs 有明确的计数范围。
- [ ] 区分 IO 改善、数学语义和浮点误差。
- [ ] 理论存储与实际分配分别记录。

在 `notes.md` 的 `W6-S02` 保存推导和未验证项；通过后进入 [第三段](session-03.md)。
