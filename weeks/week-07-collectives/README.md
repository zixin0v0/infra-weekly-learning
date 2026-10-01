# 单元 W7：集合通信与 NCCL

[总路线](../../README.md) · [学习方式](../../docs/learning-workflow.md) · [资源索引](../../resources/README.md) · [当前做法与相关进展](context.md)

建议学习位置：第 8 个学习周。W7 是固定单元 ID，按下方导航推进。

状态：未开始。预算：约 10.5 小时（[分项](../../docs/study-guide.md#time-budget)）。环境：Linux 服务器，2 卡基础，4 卡选做。

## 本周要解决什么

理解集合通信的数据语义，并测量消息大小、卡数与 AllReduce 成本的关系。

先修：W1～W6 的张量、执行和测量知识，以及可用的多卡环境；W13 的编译实验不是通信实验的硬性前置。要回答：每个 rank 通信前后持有什么？小消息和大消息为何表现不同？多卡开销可能来自哪里？

## 按顺序学习

先用 30 分钟按 [资料复核流程](../../docs/weekly-refresh.md) 核对必读材料、版本和运行条件。[补充阅读](context.md) 在基础完成后选读，单独安排时间.

按 [分段学习指南](study-guide.md) 分三段学习，每段读完就动手。各段学习指南包含原文定位、图例、暂停题与折叠核对说明；先自行作答，再检查理由和运行结果。AI 理解提示词可以跳过，完成要求不依赖 AI 评价。

学习指南已整理：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md)。[本次资料复核](refresh-2026-10-01.md) 已完成；学习未开始，实际开始学习日仍按更新流程复查。

| 学习段 | 指定范围 | 读后立即做 | 资料预算 |
| --- | --- | --- | --- |
| 1. 数据语义 | NCCL 四类 collective；CS336 L7 指定函数 | 每个 rank 的输入输出图 | 45 分钟 |
| 2. 通信计量 | nccl-tests README 与 PERFORMANCE.md 指定项 | 2 卡正确性与消息扫描 | 60 分钟 |
| 3. 成本与拓扑 | L7 hardware/benchmarking/all_reduce | 拓扑记录与曲线解释 | 45 分钟 |

原文选读共 150 分钟，本地图解与自查另计 60 分钟。材料元信息统一在资源索引；可选拓展另排时间。

## 遇到问题再看

示例与带宽列含义优先回 [NCCL 语义](../../resources/README.md#r-collective) 和 [nccl-tests](../../resources/README.md#r-nccl-tests) 的指定范围。

通过 [单卡训练检查 D](../../docs/prerequisites.md) 后，可选 [PyTorch DDP 入门](../../resources/README.md#r-ddp)；否则移到 W11。

## 实践任务

建议目录：labs/04-collectives/allreduce/。

1. 记录服务器 GPU 拓扑、通信后端、NCCL 版本与可用卡数。
2. 用 nccl-tests 测 2 卡的多个消息大小，先从 KiB 到较小 MiB 范围开始，再视显存扩展。4 卡是进阶对照，单独记录完成状态。
3. 保存命令、原始日志与整理后的数据；注明 MB/MiB、延迟单位及带宽定义。
4. 扩展：跑通最小 DDP 示例并验证梯度同步；训练先修不足时将本项与完整训练对比一起放到W11。

## 验收

- [ ] 能画出四类 collective 的输入输出。
- [ ] 2 卡正确性检查与消息大小曲线完成，数据对应明确的 GPU 拓扑。
- [ ] 图表区分延迟、algbw 和 busbw。
- [ ] 能解释至少一项通信开销；4 卡和 DDP 扩展未做时单独标记，不用估算补数据。

可选：完成基础后，从补充阅读选一个实际问题写进报告；未选不影响本单元完成。

## 实验记录

实验与报告：尚未创建。自评与验收日期：待完成。

[上一单元](../week-13-systems/README.md) · [下一单元](../week-08-serving-baseline/README.md)
