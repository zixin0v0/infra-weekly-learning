# W6 分段学习指南：把 Attention 公式接到模型时间线

[本周范围与验收](README.md) · [自学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

详细学习指南：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md) · [2026-10-01 资料复核](refresh-2026-10-01.md)。每段先作答，再读图例与折叠核对说明，最后在本周同一实验目录验证；AI 提示词可跳过。未来实际开始学习仍须重查资料。

原文选读预算：40 + 50 + 60 = 150 分钟；本地例子与自查另计 90 分钟，动手与正确性检查 330 分钟。含资料复核、分析和报告，本单元约 12.5 小时，详见 [时间表](../../docs/study-guide.md#time-budget)。

## 学习目标与前置检查

本单元知识点：Attention 语义、因果 mask、在线 IO、Block 时间线。学完应当能对齐显式 Attention 与 SDPA，完成小 Block 的形状、资源和耗时分析。

**开始前检查**：通过 W5，并完成先修 C。说出 Q/K/V、head、残差与 LayerNorm 的位置；分清 eval 与禁用梯度。 缺项按 [基础补学入口](../../docs/prerequisites.md) 的材料、范围和练习完成；补学时间另计。

<details>
<summary>前置问题核对</summary>

QKᵀ 产生每个 head 的 S×S 分数；eval 改变部分模块行为，no_grad/inference_mode 才控制梯度记录。形状例子见先修 C。

</details>

资源的难度、语言、前置要求、原始 URL 和停止位置统一保存在 [资源索引](../../resources/README.md)，下文按学习顺序链接。先读必读范围，卡点材料替换复习时间，可选拓展不影响基础完成。

## 1. 先让两个 Attention 路径算同一件事（40 分钟）

资源定位：[Attention 语义和后端](../../resources/README.md#r-sdpa)。

**先读**：[PyTorch SDPA 教程](../../resources/README.md#r-sdpa) 开头的接口示例和 `Explicit Dispatcher Control`。跟踪 Q/K/V 形状、causal 条件、dtype 与后端限制；不必运行整篇教程。

**接着想一想**：将 W5 的 Softmax 放到 QKᵀ 与乘 V 之间，写每一步的 shape。后端选择 API 用来核对执行路径；不能仅凭调用了 SDPA 就将结果称为 FlashAttention。

**动手练习**：写显式 Attention 参考与 SDPA 对照，使用相同输入、缩放、mask，主线将 dropout 设为 0，明确 eval 和 autograd 状态。记录输出误差及后端证据。

**检查结果**：语义对齐完成；后端无法确认时如实记录，不阻止先做资源分析。

## 2. 为什么多做一点计算仍可能更快（50 分钟）

资源定位：[Attention 的 IO 与在线分块](../../resources/README.md#r-flash)。

**先读**：[FlashAttention PDF](../../resources/README.md#r-flash) §2.1～2.2、§3.1 和 Algorithm 1，再读 §3.2 的 IO 分析结论。停在前向算法；证明、反向和稀疏扩展后置。

**接着想一想**：将 W4 的 tile 图用于 Q/K/V，把 W5 的在线状态放到每个 tile 迭代之间。论文以 HBM/SRAM 描述层次；本机消费级 GPU 的显存介质不同，关注搬运路径与容量关系。

**动手练习**：按 [第二段结构图](session-02.md) 固定小型 pre-norm Block，为它画三张表：参数与激活尺寸、Attention/MLP FLOPs、显式中间矩阵大小。主线固定一个输入形状；序列长度翻倍先作纸面预测，再作为可选实测。

**检查结果**：能指出哪张大矩阵不必完整写回显存，并区分 IO 改善与数学计算量变化。

## 3. 从算子热点走到 CPU—GPU 时间线（60 分钟）

资源定位：[模型区段与 CPU/GPU 时间线](../../resources/README.md#r-trace)。

**先读**：[PyTorch Profiler](../../resources/README.md#r-trace) 的步骤 3（执行时间）、4（内存）、以及 `export_chrome_trace` 示例。只把工具接入自己的 Block，不增加 ResNet 实验。

**立即联读**：[Nsight Systems](../../resources/README.md#r-trace) 的 `CUDA Trace → Basic CUDA trace`；需要区段标记时查 `Marking and Labeling Regions`。W3 的 Nsight Compute 回答单 kernel 指标，这里观察调用、拷贝和等待的关系。

**动手练习**：标出 Attention 与 MLP 区段，导出算子表和一段时间线；正式延迟另行无 profiler 测量。区分 allocated、reserved 和设备占用，报告前向是否建立 autograd 图。

**完成后检查**：用一条时间线解释“GPU 空档”与“某个 kernel 慢”的区别，资源账本和观测能够相互核对。

## 整理记录与可选拓展

在 `labs/03-triton-attention/decoder-profiling/` 交付 Block、两条 Attention 路径、资源表与报告；W13 直接复用同一模型区段。

卡点补充：回 W5 的在线递推，先用小数组验证。进阶阅读 [FlashAttention-2 作者博客](../../resources/README.md#x-fa2) 的工作划分讨论，解释 IO 优化之后还能改什么，暂不实现完整 FA2。
