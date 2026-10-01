# W7 分段学习指南：先确定各 rank 拿到什么，再看带宽

[本周范围与验收](README.md) · [自学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

详细学习指南：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md) · [2026-10-01 资料复核](refresh-2026-10-01.md)。每段先作答，再读图例与折叠核对说明，最后在本周同一实验目录验证；AI 提示词可跳过。未来实际开始学习仍须重查资料。

原文选读预算：45 + 60 + 45 = 150 分钟；本地例子与自查另计 60 分钟，动手与正确性检查 240 分钟。含资料复核、分析和报告，本单元约 10.5 小时，详见 [时间表](../../docs/study-guide.md#time-budget)。

## 学习目标与前置检查

本单元知识点：rank、collective 语义、algbw/busbw、拓扑。学完应当能验证 2 卡 collective，解释随消息大小变化的延迟与带宽。

**开始前检查**：通过 W2 的同步计时即可开始通信概念；主线按 W13 后推进。确认至少两张可用 GPU；训练基础不在本单元强制使用。 缺项按 [基础补学入口](../../docs/prerequisites.md) 的材料、范围和练习完成；补学时间另计。

<details>
<summary>前置问题核对</summary>

rank0=[1,2]、rank1=[3,4] 做 SUM AllReduce 后双方都是 [4,6]。没有 2 卡只能完成纸面检查，不能标记通信实验完成。

</details>

资源的难度、语言、前置要求、原始 URL 和停止位置统一保存在 [资源索引](../../resources/README.md)，下文按学习顺序链接。先读必读范围，卡点材料替换复习时间，可选拓展不影响基础完成。

## 1. collective 是数据变换，不是一个黑盒命令（45 分钟）

资源定位：[各 rank 的输入输出](../../resources/README.md#r-collective) → [通信、TP 和 PP 讲义](../../resources/README.md#r-l7)。

**先读**：[NCCL Collective Operations](../../resources/README.md#r-collective) 的 `AllReduce`、`Broadcast`、`AllGather`、`ReduceScatter`，按每个 rank 的输入和输出画图。

**联读/看**：[CS336 第 7 讲讲义](../../resources/README.md#r-l7) 的 `torch_distributed`、`collective_operations_main`，视频使用 [2026 官方列表](../../resources/README.md#x-navigation) 第 7 讲。只找 collective 示例，数据并行实现留到 W11。

**动手练习**：为 2 个 rank 各给一个小向量，先手算四类操作；将输出 shape、元素含义与 rank 顺序写成表。手算完成后再运行可用的最小通信示例。

**检查结果**：区分 ReduceScatter 的归约与切分，能说明 AllGather 为什么不是求和。

## 2. nccl-tests 的三列数字各回答什么（60 分钟）

资源定位：[通信计时与两种带宽](../../resources/README.md#r-nccl-tests)。

**先读**：[nccl-tests README](../../resources/README.md#r-nccl-tests) 的构建与运行说明，再读 [doc/PERFORMANCE.md](../../resources/README.md#r-nccl-tests) 的 `Time`、`Algorithm bandwidth`、`Bus bandwidth → AllReduce`。

**接着想一想**：用第一段各 rank 的数据量推导计量口径。`busbw` 是按 collective 和 rank 数归一化后的指标，不是网卡或 PCIe 链路的直接采样值。

**动手练习**：先做最小 2 卡正确性运行，再扫消息大小。每一行保存字节数、dtype、卡数、时间、algbw、busbw 和错误数，保留原始日志。构建方式和命令以所用 commit 为准。

**检查结果**：随机选一行，用文档中的换算关系核对带宽；明确发送元素数与字节数的关系。

## 3. 从曲线形状回到拓扑和成本（45 分钟）

资源定位：[通信、TP 和 PP 讲义](../../resources/README.md#r-l7) → [通信计时与两种带宽](../../resources/README.md#r-nccl-tests)。

**先读/看**：Lecture 7 的 `hardware`、`benchmarking`、`all_reduce`，观察消息规模与计时方法。机器拓扑以自己的记录为准，讲义设备示例不作为本机结论。

**动手练习**：保存 GPU 拓扑、选卡、版本和运行条件，画消息大小—延迟/带宽曲线；用“固定开销 + 数据量相关开销”的简化模型描述两段趋势，再指出未验证因素。

**完成后检查**：能解释小消息区间为何不能只看峰值带宽，并将代表数据量留给 W11 的梯度通信估算。

## 整理记录与可选拓展

在 `labs/04-collectives/allreduce/` 交付语义图、运行配置、日志和曲线。基础通过后选 4 卡对照；DDP 仅在单卡训练先修已通过时尝试，否则放到 W11，不阻塞 W8 的单卡服务学习。
