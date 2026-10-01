# 单元 W4：GEMM 与数据复用

[总路线](../../README.md) · [学习方式](../../docs/learning-workflow.md) · [资源索引](../../resources/README.md) · [当前做法与相关进展](context.md)

建议学习位置：第 4 个学习周。W4 是固定单元 ID，按下方导航推进。

状态：未开始。预算：约 11 小时（[分项](../../docs/study-guide.md#time-budget)）。环境：本地 GPU。

## 本周要解决什么

通过 GEMM 理解算术强度、合并访存与 Shared Memory Tiling。

先修：W3通过。要回答：一个 tile 复用了哪些数据？tile 增大有什么代价？与库实现比较时怎样控制精度？

## 按顺序学习

先用 30 分钟按 [资料复核流程](../../docs/weekly-refresh.md) 核对必读材料、版本和运行条件。[补充阅读](context.md) 在基础完成后选读，单独安排时间.

按 [分段学习指南](study-guide.md) 分三段学习，每段读完就动手。各段学习指南包含原文定位、图例、暂停题与折叠核对说明；先自行作答，再检查理由和运行结果。AI 理解提示词可以跳过，完成要求不依赖 AI 评价。

学习指南已整理：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md)。[本次资料复核](refresh-2026-10-01.md) 已完成；学习未开始，实际开始学习日仍按更新流程复查。

| 学习段 | 指定范围 | 读后立即做 | 资料预算 |
| --- | --- | --- | --- |
| 1. 地址与访存 | Best Practices §10.2.1 | 朴素 GEMM 与访问图 | 45 分钟 |
| 2. tile 复用 | Best Practices §10.2.3.1～2 | 分块 GEMM 与边界检查 | 60 分钟 |
| 3. Roofline | CS336 L2 指定函数；Scaling Book Part 1 两节 | 预测、计时与库基线对照 | 45 分钟 |

原文选读共 150 分钟，本地图解与自查另计 60 分钟。材料元信息统一在资源索引；可选拓展另排时间。

## 遇到问题再看

博客：[An Efficient Matrix Transpose in CUDA C/C++](../../resources/README.md#x-cuda)。用转置理解合并访存和 shared memory padding；历史设备上的数字不作为本机目标。可用 15 分钟替换卡点复习。

## 实践任务

建议目录：labs/02-cuda/gemm/。

1. 写朴素 GEMM 和 shared-memory 分块版本，支持至少一种非 tile 整数倍尺寸。
2. 比较小/大、方形/长方形输入；固定数据类型、转置设置与计时范围。
3. 对照 PyTorch matmul 或 cuBLAS，记录 TF32/混合精度策略，使结果语义和精度要求一致。
4. 用 2 × M × N × K 约定估算 FLOPs，记录实际延迟并画性能曲线。
5. 画出一个 tile 的加载与复用过程，区分理论数据搬运估算与 profiler 实测。

用算术强度（FLOPs/字节）建立简化 Roofline 预测：性能上界取计算上限与带宽乘算术强度的较小者。理论上限、估算字节和实测值分别标明；可沿用 [Nsight Compute 指南](../../resources/README.md#r-ncu) 的 Roofline 说明。先做一组预测与观察的核对，不额外加入大量 tile 搜索。

工程对照加入同输入的 `torch.matmul`，记录输入/累加精度、TF32 设置和计时范围。练习实现用于解释复用，不以击败库实现作为通过条件。

## 验收

- [ ] 正确性覆盖边界 tile，参考与手写实现使用可比较的精度。
- [ ] 能解释分块减少访存的路径及同步代价。
- [ ] 报告写明计时范围和 FLOPs 约定。
- [ ] 能提出手写版本仍落后库实现的合理解释，并标出哪些尚未验证。

可选：完成基础后，从补充阅读选一个实际问题写进报告；未选不影响本单元完成。

## 实验记录

实验与报告：尚未创建。自评与验收日期：待完成。

[上一单元](../week-03-reduction-profiling/README.md) · [下一单元](../week-05-triton-softmax/README.md)
