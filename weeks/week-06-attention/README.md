# 单元 W6：Attention 资源账本

[总路线](../../README.md) · [学习方式](../../docs/learning-workflow.md) · [资源索引](../../resources/README.md) · [当前做法与相关进展](context.md)

建议学习位置：第 6 个学习周。W6 是固定单元 ID，按下方导航推进。

状态：未开始。预算：约 12.5 小时（[分项](../../docs/study-guide.md#time-budget)）。环境：本地 GPU，小型 Decoder Block。

## 本周要解决什么

建立 Attention 与 Decoder Block 的资源账本，理解 FlashAttention 的 IO 动机。

先修：W5通过，并通过 [模型结构检查 C](../../docs/prerequisites.md)。要回答：序列长度如何影响计算与显存？哪些中间结果可以不完整存储？模型热点是否就是自己猜的算子？

## 按顺序学习

先用 30 分钟按 [资料复核流程](../../docs/weekly-refresh.md) 核对必读材料、版本和运行条件。[补充阅读](context.md) 在基础完成后选读，单独安排时间.

按 [分段学习指南](study-guide.md) 分三段学习，每段读完就动手。各段学习指南包含原文定位、图例、暂停题与折叠核对说明；先自行作答，再检查理由和运行结果。AI 理解提示词可以跳过，完成要求不依赖 AI 评价。

学习指南已整理：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md)。[本次资料复核](refresh-2026-10-01.md) 已完成；学习未开始，实际开始学习日仍按更新流程复查。

| 学习段 | 指定范围 | 读后立即做 | 资料预算 |
| --- | --- | --- | --- |
| 1. Attention 语义 | SDPA 接口与 Explicit Dispatcher Control | 显式 Attention/SDPA 对齐 | 40 分钟 |
| 2. IO 与分块 | FlashAttention §2.1～2.2、§3.1～3.2、Algorithm 1 | 资源账本与数据路径图 | 50 分钟 |
| 3. 模型时间线 | Profiler 步骤 3/4 和 trace；Nsight CUDA Trace | Block 算子表与时间线 | 60 分钟 |

原文选读共 150 分钟，本地图解与自查另计 90 分钟。材料元信息统一在资源索引；可选拓展另排时间。

## 遇到问题再看

作者机构博客：[FlashAttention-2](../../resources/README.md#x-fa2)，用于理解 IO 优化后为何还要优化工作划分；基础完成后另排 30 分钟。

视频可复看 [CS336 2026 Lecture 6](../../resources/README.md#r-l6) 的相关部分。本周主线是论文加模型测量，不增加整讲观看任务。

## 实践任务

建议目录：labs/03-triton-attention/decoder-profiling/。

1. 按 [第二段的结构图](session-02.md) 建立小型 pre-norm Decoder Block，写明 batch、序列长度、隐藏维度、头数和 dtype。主线只分析固定形状的前向，明确 eval、dropout 和 autograd 状态；backward 留作扩展。
2. 估算参数、Attention/MLP FLOPs 与显存项，再采集算子耗时。
3. 比较显式 Attention 与 PyTorch SDPA：统一 causal mask、dropout、输入与 dtype，检查输出误差。
4. 记录实际选到的 SDPA 后端；无法确认时写“未确认”，不将所有 SDPA 结果都称为 FlashAttention。
5. 整理短报告《一个 Decoder Block 的计算和显存花在哪里？》。

在报告中加入一段 CPU—拷贝—GPU 时间线，区分 kernel 忙碌与 GPU 空档。优先采一次 Nsight Systems CUDA trace；受平台限制时用 PyTorch trace 标注可见范围，并保留 Nsight 补测项。显存记录区分 allocated、reserved 与设备整体占用，不能将它们直接相加。

## 验收

- [ ] 资源账本区分参数、激活、中间矩阵与实测峰值。
- [ ] 明确前向或训练计时范围，两个实现语义一致。
- [ ] 有算子表、原始测量和一段时间线，能区分热点算子与等待时间。
- [ ] 能解释分块与在线 Softmax 的联系；本周不要求完整实现 FlashAttention2。

可选：完成基础后，从补充阅读选一个实际问题写进报告；未选不影响本单元完成。

## 实验记录

实验与报告：尚未创建。自评与验收日期：待完成。

[上一单元](../week-05-triton-softmax/README.md) · [下一单元](../week-13-systems/README.md)
