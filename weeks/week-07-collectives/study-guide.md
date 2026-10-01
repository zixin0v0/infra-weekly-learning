# W7 章节导学：先确定各 rank 拿到什么，再看带宽

[本周范围与验收](README.md) · [导学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

资料预算：45 + 60 + 45 = 150 分钟，包含配置与拓扑记录的准备。主线 2 卡，4 卡另列扩展。

## 1. collective 是数据变换，不是一个黑盒命令（45 分钟）

**先读**：[NCCL Collective Operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html) 的 `AllReduce`、`Broadcast`、`AllGather`、`ReduceScatter`，按每个 rank 的输入和输出画图。

**联读/看**：[CS336 第 7 讲讲义](https://github.com/stanford-cs336/lectures/blob/main/lecture_07.py) 的 `torch_distributed`、`collective_operations_main`，视频使用 [2026 官方列表](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV) 第 7 讲。只找 collective 示例，数据并行实现留到 W11。

**动手练习**：为 2 个 rank 各给一个小向量，先手算四类操作；将输出 shape、元素含义与 rank 顺序写成表。手算完成后再运行可用的最小通信示例。

**检查结果**：区分 ReduceScatter 的归约与切分，能说明 AllGather 为什么不是求和。

## 2. nccl-tests 的三列数字各回答什么（60 分钟）

**先读**：[nccl-tests README](https://github.com/NVIDIA/nccl-tests) 的构建与运行说明，再读 [doc/PERFORMANCE.md](https://github.com/NVIDIA/nccl-tests/blob/master/doc/PERFORMANCE.md) 的 `Time`、`Algorithm bandwidth`、`Bus bandwidth → AllReduce`。

**接着想一想**：用第一段各 rank 的数据量推导计量口径。`busbw` 是按 collective 和 rank 数归一化后的指标，不是网卡或 PCIe 链路的直接采样值。

**动手练习**：先做最小 2 卡正确性运行，再扫消息大小。每一行保存字节数、dtype、卡数、时间、algbw、busbw 和错误数，保留原始日志。构建方式和命令以所用 commit 为准。

**检查结果**：随机选一行，用文档中的换算关系核对带宽；明确发送元素数与字节数的关系。

## 3. 从曲线形状回到拓扑和成本（45 分钟）

**先读/看**：Lecture 7 的 `hardware`、`benchmarking`、`all_reduce`，观察消息规模与计时方法。机器拓扑以自己的记录为准，讲义设备示例不作为本机结论。

**动手练习**：保存 GPU 拓扑、选卡、版本和运行条件，画消息大小—延迟/带宽曲线；用“固定开销 + 数据量相关开销”的简化模型描述两段趋势，再指出未验证因素。

**完成后检查**：能解释小消息区间为何不能只看峰值带宽，并将代表数据量留给 W11 的梯度通信估算。

## 课后整理与选修

在 `labs/04-collectives/allreduce/` 交付语义图、运行配置、日志和曲线。基础通过后选 4 卡对照；DDP 仅在单卡训练先修已通过时尝试，否则放到 W11，不阻塞 W8 的单卡服务学习。
