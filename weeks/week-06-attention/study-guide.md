# W6 章节导学：把 Attention 公式接到模型时间线

[本周范围与验收](README.md) · [导学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

资料预算：40 + 50 + 60 = 150 分钟。先通过模型结构检查 C；本周固定小型 Decoder Block 的前向，backward 为扩展。

## 1. 先让两个 Attention 路径算同一件事（40 分钟）

**先读**：[PyTorch SDPA 教程](https://docs.pytorch.org/tutorials/intermediate/scaled_dot_product_attention_tutorial.html) 开头的接口示例和 `Explicit Dispatcher Control`。跟踪 Q/K/V 形状、causal 条件、dtype 与后端限制；不必运行整篇教程。

**接着想一想**：将 W5 的 Softmax 放到 QKᵀ 与乘 V 之间，写每一步的 shape。后端选择 API 用来核对执行路径；不能仅凭调用了 SDPA 就将结果称为 FlashAttention。

**动手练习**：写显式 Attention 参考与 SDPA 对照，使用相同输入、缩放、mask，主线将 dropout 设为 0，明确 eval 和 autograd 状态。记录输出误差及后端证据。

**检查结果**：语义对齐完成；后端无法确认时如实记录，不阻止先做资源分析。

## 2. 为什么多做一点计算仍可能更快（50 分钟）

**先读**：[FlashAttention PDF](https://arxiv.org/pdf/2205.14135) §2.1～2.2、§3.1 和 Algorithm 1，再读 §3.2 的 IO 分析结论。停在前向算法；证明、反向和稀疏扩展后置。

**接着想一想**：将 W4 的 tile 图用于 Q/K/V，把 W5 的在线状态放到每个 tile 迭代之间。论文以 HBM/SRAM 描述层次；本机消费级 GPU 的显存介质不同，关注搬运路径与容量关系。

**动手练习**：为同一个 Block 画三张表：参数与激活尺寸、Attention/MLP FLOPs、显式中间矩阵大小。主线固定一个输入形状；序列长度翻倍先作纸面预测，再作为可选实测。

**检查结果**：能指出哪张大矩阵不必完整写回显存，并区分 IO 改善与数学计算量变化。

## 3. 从算子热点走到 CPU—GPU 时间线（60 分钟）

**先读**：[PyTorch Profiler](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html) 的步骤 3（执行时间）、4（内存）、以及 `export_chrome_trace` 示例。只把工具接入自己的 Block，不增加 ResNet 实验。

**立即联读**：[Nsight Systems](https://docs.nvidia.com/nsight-systems/UserGuide/index.html#cuda-trace) 的 `CUDA Trace → Basic CUDA trace`；需要区段标记时查 `Marking and Labeling Regions`。W3 的 Nsight Compute 回答单 kernel 指标，这里观察调用、拷贝和等待的关系。

**动手练习**：标出 Attention 与 MLP 区段，导出算子表和一段时间线；正式延迟另行无 profiler 测量。区分 allocated、reserved 和设备占用，报告前向是否建立 autograd 图。

**完成后检查**：用一条时间线解释“GPU 空档”与“某个 kernel 慢”的区别，资源账本和观测能够相互核对。

## 课后整理与选修

在 `labs/03-triton-attention/decoder-profiling/` 交付 Block、两条 Attention 路径、资源表与报告；W13 直接复用同一模型区段。

卡点补充：回 W5 的在线递推，先用小数组验证。进阶阅读 [FlashAttention-2 作者博客](https://crfm.stanford.edu/2023/07/17/flash2.html) 的工作划分讨论，解释 IO 优化之后还能改什么，暂不实现完整 FA2。
