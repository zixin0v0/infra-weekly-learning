# W14 分段学习指南：用两层 MLP 串起 TP 和 PP

[本周范围与验收](README.md) · [自学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

原文选读预算：50 + 50 + 50 = 150 分钟；本地例子与自查另计 60 分钟，动手与正确性检查 240 分钟。含资料复核、分析和报告，本单元约 10.5 小时，详见 [时间表](../../docs/study-guide.md#time-budget)。

## 学习目标与前置检查

本单元知识点：TP 代数、非线性与合并、PP 气泡、DP/TP/PP。学完应当能验证两层 MLP 切分等价，标明通信并手算前向流水线。

**开始前检查**：通过 W4 矩阵计算与 W7 通信语义，按顺序完成 W12 状态分析；CPU 代数验证不要求额外 GPU。 缺项按 [基础补学入口](../../docs/prerequisites.md) 的材料、范围和练习完成；补学时间另计。

<details>
<summary>前置问题核对</summary>

矩阵按输出列切分后，局部非线性可各自执行；若切的是求和维，须先考虑是否应合并再做非线性。下方用反例核对。

</details>

资源的难度、语言、前置要求、原始 URL 和停止位置统一保存在 [资源索引](../../resources/README.md)，下文按学习顺序链接。先读必读范围，卡点材料替换复习时间，可选拓展不影响基础完成。

## 1. 权重如何切，非线性放在哪里（50 分钟）

资源定位：[TP 的两层 MLP 代数](../../resources/README.md#r-megatron) → [通信、TP 和 PP 讲义](../../resources/README.md#r-l7)。

**先读**：[Megatron-LM PDF](../../resources/README.md#r-megatron)，本轮 v4 的 §3 `Model Parallel Transformers`，只读两层 MLP 与 Attention 的切分部分，暂不读大模型训练结果。

**联读/看**：[CS336 第 7 讲讲义](../../resources/README.md#r-l7) 的 `tensor_parallelism`、`tensor_parallelism_main`，视频使用 [官方列表](../../resources/README.md#x-navigation) 第 7 讲对应主题；第 8 讲留作深入。

**例子与图解：两层 MLP 的列切与行切**

采用数学权重形状输入维×输出维，无 bias：
x=[−1,2]，W₁ 为 2×2 单位矩阵，激活 ReLU，W₂=[[1],[3]]。
第一层按列切给两个分片，各输出 −1 与 2，局部激活后为 0 与 2。

~~~text
                 列分片 0 → ReLU(-1)=0 → W₂ 行 0 → 部分输出 0
x（双方可见） ──┤                                             → 求和 → 6
                 列分片 1 → ReLU( 2)=2 → W₂ 行 1 → 部分输出 6
~~~

**暂停题**：ReLU(−1+2) 是否等于 ReLU(−1)+ReLU(2)？这个反例限制了什么切分顺序？

<details>
<summary>核对答案</summary>

左边 1，右边 2，不相等。沿求和维拆出的部分和通常要先合并，再做非线性；不能随意把激活分发到未合并的部分和。上述第一层按输出列切，各片负责完整输出元素，所以能各自激活；第二层沿输入行切后将线性部分输出求和，得到未切分结果 6。

</details>

**动手练习**：先约定数学权重形状为输入维×输出维，用无 bias 的两层 MLP 画列切第一层、行切第二层。若代码使用 `nn.Linear.weight`，显式转换其转置存储约定。

**检查结果**：能解释为什么不能随意交换局部求和与非线性运算，每个中间 shape 都写得出来。

## 2. 通信应该放在何处（50 分钟）

资源定位：[TP 通信与 PP 流水线](../../resources/README.md#r-parallel)。

**先读**：[Megatron Bridge Parallelisms Guide](../../resources/README.md#r-parallel) 的 `Model Parallelism → Tensor Parallelism`。配置示例只帮助理解维度，不要求部署 Megatron。

**接着想一想**：回 W7 的 collective 图，为每次通信标数据 shape 与目的；回 W4 计算局部 GEMM 的工作量，避免只看到每卡计算变少。

**暂停题：输出与通信形状**

沿上例，输入是 (1,2)，两片第一层输出各为 (1,1)，第二层部分输出也各为 (1,1)。最后用 SUM AllReduce 后，两片是否都拿到最终结果？若两片各自先加同一个输出 bias=1 再求和，得到什么？

<details>
<summary>核对依据</summary>

AllReduce 后双方均有 6；各先加 bias 会得到 (0+1)+(6+1)=8，而正确输出为 6+1=7。bias 应只计一次。CPU 用显式求和检验代数，2 卡才检验通信；记录元素数、dtype、各次 collective 的 shape，而不是把 CPU 合并耗时当成 NCCL 测量。

</details>

**动手练习**：用固定权重和输入比较未切分 MLP 与两个分片组合。CPU 路径用显式合并验证，2 卡路径使用对应 collective；bias 若加入，单独检查是否被重复求和。

**检查结果**：数值误差通过，通信量估算明确，CPU 模拟与真实通信结果分开记录。

## 3. 从层内切分转到层间流水线（50 分钟）

资源定位：[TP 通信与 PP 流水线](../../resources/README.md#r-parallel) → [通信、TP 和 PP 讲义](../../resources/README.md#r-l7)。

**先读**：Bridge 同页 `Pipeline Parallelism` 与 `Interleaved Pipeline Parallel Schedule` 的概念说明；后者只用于认识还有其他调度。配 CS336 第 7 讲的 `pipeline_parallelism`、`pipeline_parallelism_main` 理解基础示例。

**接着想一想**：TP 在层内切张量，PP 在阶段间传激活；不要将两种通信图混画。训练中的 backward 和参数更新约束比前向演示更多。

**例子与图解：只看前向的流水线**

2 个 stage，各 microbatch 在每个 stage 用 1 个时间单位，传输暂忽略，连续送入 3 个 microbatch：

| 时间槽 | stage A | stage B |
| --- | --- | --- |
| 0～1 | micro1 | 空闲 |
| 1～2 | micro2 | micro1 |
| 2～3 | micro3 | micro2 |
| 3～4 | 空闲 | micro3 |

**暂停题**：总时长、吞吐、槽位空闲比例是多少？若 B 每个 microbatch 用时 2，总时长又是多少？

<details>
<summary>核对答案</summary>

均衡时总时长 4，吞吐 3/4 个 microbatch/时间单位；共 8 个 stage 时间槽，空闲 2 个，比例 25%。B 变慢时执行区间为 1～3、3～5、5～7，总时长 7。A 是否受缓冲容量阻塞需要另外声明；此例假定能暂存中间结果。图未含 backward、通信或优化器更新，不能用来宣称训练流水线的实测效率。

</details>

**动手练习**：画 2 stage、多个 microbatch 的时间线，先声明是前向演示还是训练调度，再标计算、传输和气泡；手算一个均衡例子及一个慢 stage 例子。

**完成后检查**：能比较 DP/TP/PP 的切分对象，指出模型估算与实测的边界。完整 PP 训练作为扩展。

## 独立完成与可选 AI 帮助

三段都先遮住答案作答，再核对推导；答错保留原答案，回资源卡指定小节，用不同输入重做。每段“检查结果”连同 [单元完成标准](README.md) 都需要真实笔记或运行记录支持。纸面例子正确只能说明该例的理解，不能替代实验。记录在本单元实验目录的 notes.md，按 W14-S01～S03 分节。

可选提示词：

> 我正在学习 W14 的TP 代数。我的推导是【粘贴】，我与本段核对说明不同的一步是【填写】。请只用本段的小例子检查这一步，给一个改变单项条件的反例，先让我回答。不要假设我做过实验，也不要用未核验的接口填补解释。

## 整理记录与可选拓展

在 `labs/06-training/parallelism/` 交付 MLP shape/通信图、切分对齐脚本与 pipeline 时间线。

进阶增加一种 stage 不均衡或 TP 分片数，先提出预测再验证；CP、EP、3D 并行训练另排单元。
