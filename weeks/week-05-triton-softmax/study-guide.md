# W5 分段学习指南：从 Triton 数据块到在线 Softmax

[本周范围与验收](README.md) · [自学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

详细学习指南：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md) · [2026-10-01 资料复核](refresh-2026-10-01.md)。每段先作答，再读图例与折叠核对说明，最后在本周同一实验目录验证；AI 提示词可跳过。未来实际开始学习仍须重查资料。

原文选读预算：45 + 60 + 45 = 150 分钟；本地例子与自查另计 60 分钟，动手与正确性检查 270 分钟。含资料复核、分析和报告，本单元约 11 小时，详见 [时间表](../../docs/study-guide.md#time-budget)。

## 学习目标与前置检查

本单元知识点：program/mask、广播与类型、稳定 Softmax、在线状态。学完应当能写稳定的行 Softmax，解释融合减少的搬运，并核对分块状态合并。

**开始前检查**：通过 W4；完成先修 M2。先算 softmax([0, ln 3])，解释为何可先减最大值。 缺项按 [基础补学入口](../../docs/prerequisites.md) 的材料、范围和练习完成；补学时间另计。

<details>
<summary>前置问题核对</summary>

结果为 [1/4, 3/4]；同时减一个常数不改变比例，减最大值限制指数范围。

</details>

资源的难度、语言、前置要求、原始 URL 和停止位置统一保存在 [资源索引](../../resources/README.md)，下文按学习顺序链接。先读必读范围，卡点材料替换复习时间，可选拓展不影响基础完成。

## 1. CUDA 线程映射怎样换成 Triton 数据块（45 分钟）

资源定位：[测量、Triton 与编译的讲义例子](../../resources/README.md#r-l6) → [Triton program、mask 与类型](../../resources/README.md#r-triton)。

**先看/读**：[CS336 Lecture 6](../../resources/README.md#r-l6) 配 [lecture_06.py](../../resources/README.md#r-l6) 的 `triton_introduction`，约 15 分钟。

**立即联读**：[Vector Addition 教程](../../resources/README.md#r-triton) 的 `Compute Kernel`：定位 `add_kernel` 与 Python 封装 `add`；重点追踪 program ID、`arange`、mask 和 grid。这部分 20 分钟；再用 10 分钟读 [Semantics](../../resources/README.md#r-triton) 的 Broadcasting、Type Promotion，用第一段例子核对形状与类型。不要把一个 Triton program 直接等同于一个 CUDA 线程。

**动手练习**：复用 W2 的输入和正确性检查，写 Triton Vector Add；手画长度 10、数据块大小 4 时每个 program 负责的位置。性能比较沿用相同计时边界。

**检查结果**：能独立改输入长度而不越界，知道哪些参数在编译时确定。

## 2. 稳定 Softmax 与融合分别解决什么（60 分钟）

资源定位：[稳定 Softmax 与融合](../../resources/README.md#r-softmax)。

**先读**：[Fused Softmax](../../resources/README.md#r-softmax) 的 `Motivations`、`Compute Kernel`，随后看 `Unit Test`、`Benchmark`。对照 `naive_softmax` 与 `softmax_kernel`，逐项标记中间 Tensor 和读写。

**接着想一想**：W3 的 max/sum 归约解释一行内的计算；W4 的搬运模型解释为什么融合值得尝试。教程封装中的 occupancy/持久化启动优化先沿用并记录版本，不要求自行调优整套启动策略。

**动手练习**：先写减最大值的参考，再完成 Triton 逐行 Softmax；覆盖普通输入、大幅值与非 2 的幂列宽，比较朴素表达式、`torch.softmax` 和自己的版本。

**检查结果**：误差和每行和都检查，支持范围明确；不能只凭行和约等于 1 判定实现正确。

## 3. 一行分两块后，旧结果怎样重新缩放（45 分钟）

资源定位：[分块 Softmax 的状态合并](../../resources/README.md#r-online)。

**先读**：[Online normalizer 论文 PDF](../../resources/README.md#r-online)，§2 的 Algorithm 2，然后 §3 的 Algorithm 3、§3.1 的并行合并。版本为本轮读取的 v2；Top-k 融合暂不读。

**接着想一想**：用第二段的“全行最大值”提出问题：后读到更大的值时，前一块的归一化因子如何修正？分别保存块最大值与指数和，再合并，不能直接相加原指数和。

**动手练习**：对 `[1, 2]` 和 `[3, 4]` 手算两个状态，再写小型 CPU/PyTorch 状态合并验证；与整行稳定计算对齐。这里不要求新写分块 GPU Softmax。

**完成后检查**：不看论文能解释为什么需要重缩放；把状态递推记录留给 W6 的 FlashAttention。

## 整理记录与可选拓展

在 `labs/03-triton-attention/softmax/` 整理融合实现、状态合并验证、误差与列宽曲线。

进阶：考察一行过大时的资源限制，设计分块方案；先写接口和不支持条件，不以完整 FlashAttention 为本周目标。
