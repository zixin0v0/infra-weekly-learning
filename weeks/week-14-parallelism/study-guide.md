# W14 章节导学：用两层 MLP 串起 TP 和 PP

[本周范围与验收](README.md) · [导学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

资料预算：50 + 50 + 50 = 150 分钟。主线可以用 CPU 张量验证代数，2 卡通信为有环境时的实现路径；不把模拟算作多卡性能结果。

## 1. 权重如何切，非线性放在哪里（50 分钟）

**先读**：[Megatron-LM PDF](https://arxiv.org/pdf/1909.08053)，本轮 v4 的 §3 `Model Parallel Transformers`，只读两层 MLP 与 Attention 的切分部分，暂不读大模型训练结果。

**联读/看**：[CS336 第 7 讲讲义](https://github.com/stanford-cs336/lectures/blob/main/lecture_07.py) 的 `tensor_parallelism`、`tensor_parallelism_main`，视频使用 [官方列表](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV) 第 7 讲对应主题；第 8 讲留作深入。

**动手练习**：先约定数学权重形状为输入维×输出维，用无 bias 的两层 MLP 画列切第一层、行切第二层。若代码使用 `nn.Linear.weight`，显式转换其转置存储约定。

**检查结果**：能解释为什么不能随意交换局部求和与非线性运算，每个中间 shape 都写得出来。

## 2. 通信应该放在何处（50 分钟）

**先读**：[Megatron Bridge Parallelisms Guide](https://docs.nvidia.com/nemo/megatron-bridge/latest/parallelisms.html) 的 `Model Parallelism → Tensor Parallelism`。配置示例只帮助理解维度，不要求部署 Megatron。

**接着想一想**：回 W7 的 collective 图，为每次通信标数据 shape 与目的；回 W4 计算局部 GEMM 的工作量，避免只看到每卡计算变少。

**动手练习**：用固定权重和输入比较未切分 MLP 与两个分片组合。CPU 路径用显式合并验证，2 卡路径使用对应 collective；bias 若加入，单独检查是否被重复求和。

**检查结果**：数值误差通过，通信量估算明确，CPU 模拟与真实通信结果分开记录。

## 3. 从层内切分转到层间流水线（50 分钟）

**先读**：Bridge 同页 `Pipeline Parallelism` 与 `Interleaved Pipeline Parallel Schedule` 的概念说明；后者只用于认识还有其他调度。配 CS336 第 7 讲的 `pipeline_parallelism`、`pipeline_parallelism_main` 理解基础示例。

**接着想一想**：TP 在层内切张量，PP 在阶段间传激活；不要将两种通信图混画。训练中的 backward 和参数更新约束比前向演示更多。

**动手练习**：画 2 stage、多个 microbatch 的时间线，先声明是前向演示还是训练调度，再标计算、传输和气泡；手算一个均衡例子及一个慢 stage 例子。

**完成后检查**：能比较 DP/TP/PP 的切分对象，指出模型估算与实测的边界。完整 PP 训练作为扩展。

## 课后整理与选修

在 `labs/06-training/parallelism/` 交付 MLP shape/通信图、切分对齐脚本与 pipeline 时间线。

进阶增加一种 stage 不均衡或 TP 分片数，先提出预测再验证；CP、EP、3D 并行训练另排单元。
