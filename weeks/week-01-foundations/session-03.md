# W1 第三段备课：Linear 的参数、字节与 FLOPs

[单元范围](README.md) · [三段导学](study-guide.md) · [资料复核](refresh-2026-10-01.md) · [上一段](session-02.md)

备课日期：2026-10-01。资料预算：50 分钟。状态：备课已准备；计算器与报告待完成。

## 目标与先修

回答：batch、输入/输出维度与 dtype 分别改变 Linear 的哪些资源？需要前两段字节与布局知识，以及矩阵乘法维度推导。CPU 可完成，GPU 测量不计入本段验收。

## 读哪里，在哪里停

| 预算 | 原始来源 | 指定位置与停止点 |
| --- | --- | --- |
| 20 分钟 | [CS336 Lecture 2 固定讲义](https://github.com/stanford-cs336/lectures/blob/6ff836dd5dfcbe7e848fe1a1734f1886f1116a7a/lecture_02.py) | `tensor_operations_flops` 的 FLOPs / FLOP/s 区分与 Linear model 计数；到 `actual_num_flops` 后暂停 |
| 20 分钟 | 同一函数，配 [官方视频](https://www.youtube.com/watch?v=kuYAsz7zspQ) | 将矩阵维度、存储与乘加次数联系起来；本段不运行讲义的大矩阵和 GPU benchmark |
| 10 分钟 | [本周补充阅读](context.md) 的报告假设算例 | 只读 4-bit 值与分组 scale 的计数范围，写出遗漏项后停 |

讲义固定提交，访问日为 2026-10-01。没有已核对的视频分钟数；按函数定位。梯度、优化器、MFU 和完整大模型估算后置。

## 中文助读

约定输入为 `(batch, in_features)`，权重为 `(out_features, in_features)`，输出为 `(batch, out_features)`。权重参数数为 `in_features × out_features`；有 bias 时再加 `out_features`。

矩阵乘法使用一次乘加计 2 FLOPs 的常用账本约定，得到 `2 × batch × in_features × out_features`；若另计 bias 加法，再加输出元素数。这个约定与逐个输出恰好 `K` 次乘法、`K−1` 次加法的严格次数分开说明。

| 资源项 | 怎样计算 | 哪些变量影响它 |
| --- | --- | --- |
| 参数元素数 | 权重加可选 bias | 输入/输出维度、bias |
| 参数数据字节 | 参数元素数乘每元素字节数 | 参数 dtype |
| 输入/输出逻辑字节 | 各自元素数乘每元素字节数 | batch、维度、dtype |
| 前向 GEMM FLOPs | 本段 2 乘加约定 | batch、三个矩阵维度 |

这些项不是训练全状态或实测峰值。第二段的共享存储知识帮助判断哪些逻辑 Tensor 可以共用数据。

## 暂停题与预测

1. 对有 bias 的 `Linear(128, 256)` 与输入 `(32, 128)`，分别手算参数元素、FP32 参数字节、输入/输出字节和前向 GEMM FLOPs。
2. batch 翻倍后，哪些项翻倍？参数数量是否改变？参数/输入/输出都改为 FP16 时字节与数学 FLOPs 分别怎样变化？
3. 假设 1024 个 4-bit 值，每 32 个值带一个 FP32 scale，忽略 padding，数据加 scale 的总量是多少？为何不能把它当成真实 NVFP4 存储公式？

## 动手与检查

入口为 `labs/01-foundations/resource-accounting/`，动手时建立 `resource_accounting.py` 和一个 `report.md`。计算器支持 batch、输入/输出维度、dtype 字节数和 bias 选项，输出各项单位与计数约定。

用周诊断题作参考，另选小型维度、有/无 bias、两种 batch 和两种 dtype 核对；检查参数数不随 batch 变化。可以用小型 PyTorch Linear 的参数 `numel` 验证参数账本，非连续输入的数学语义沿用第二段知识，不能据此宣称没有临时复制。

## 卡点与过关

| 具体卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 不知道权重为什么转置 | 原函数 Linear model 的矩阵维度 | 写出单个输出的求和下标 |
| 把 FLOPs 当成速度 | 函数中的两种单位解释 | 区分操作总数与操作/秒 |
| 把账本称作峰值显存 | 第一段逻辑字节和第二段共享关系 | 列出未统计的分配项 |

- [ ] 手算与计算器逐项一致，bias 与乘加约定明确。
- [ ] 能独立解释 batch 和 dtype 对各项的影响。
- [ ] 报告保留格式假设、scale 开销与未计项，周验收仍需前两段真实检查。

<details>
<summary>完成推导后核对</summary>

诊断题参数为 33,024 个，FP32 参数数据 132,096 字节；输入 16,384 字节，输出 32,768 字节；GEMM 为 2,097,152 FLOPs，未计 bias 加法。格式假设是 512 字节打包数据加 128 字节 scale，共 640 字节。这些为推导值，完整程序结果尚未产生。

</details>

按 `W1-S03` 留下实际阅读、预测、代码/命令、核对和卡点，合并三段报告后按 [W1 验收](README.md) 更新真实学习状态。
