# W4 分段学习指南：从访存地址推到 GEMM 性能

[本周范围与验收](README.md) · [自学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

详细学习指南：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md) · [2026-10-01 资料复核](refresh-2026-10-01.md)。每段先作答，再读图例与折叠核对说明，最后在本周同一实验目录验证；AI 提示词可跳过。未来实际开始学习仍须重查资料。

原文选读预算：45 + 60 + 45 = 150 分钟；本地例子与自查另计 60 分钟，动手与正确性检查 270 分钟。含资料复核、分析和报告，本单元约 11 小时，详见 [时间表](../../docs/study-guide.md#time-budget)。

## 学习目标与前置检查

本单元知识点：访存连续性、共享 tile、算术强度、Roofline。学完应当能实现朴素/分块 GEMM，说明复用、边界和性能上限的关系。

**开始前检查**：通过 W3；能手算 2×3 乘 3×2，并按 W1 约定数乘加。 缺项按 [基础补学入口](../../docs/prerequisites.md) 的材料、范围和练习完成；补学时间另计。

<details>
<summary>前置问题核对</summary>

输出 4 个元素，每个执行 3 次乘加，按每次 2 FLOPs 计共 24 FLOPs；性能上限还受搬运量与硬件限制。

</details>

资源的难度、语言、前置要求、原始 URL 和停止位置统一保存在 [资源索引](../../resources/README.md)，下文按学习顺序链接。先读必读范围，卡点材料替换复习时间，可选拓展不影响基础完成。

## 1. 一个 warp 实际访问哪些地址（45 分钟）

资源定位：[计时、有效带宽与 GEMM 数据复用](../../resources/README.md#r-best)。

**先读**：[CUDA Best Practices](../../resources/README.md#r-best) §10.2.1，重点 §10.2.1.1 连续访问与 §10.2.1.2 错位访问；只画访问模式，不记历史带宽数字。

**接着想一想**：回到 W1 的 stride 图，把矩阵行列索引写成线性地址；用 W2 的线程映射确定同一 warp 中相邻线程访问的位置。

**动手练习**：写朴素 GEMM，选择一个小矩阵打印或手工列出负责某一行输出的线程如何访问 A、B。先过正确性，再测试方形和长方形尺寸。

**检查结果**：能指出合并访存与数据复用分别解决什么问题，不把二者混成同一概念。

## 2. tile 复用了什么，增加了什么（60 分钟）

资源定位：[计时、有效带宽与 GEMM 数据复用](../../resources/README.md#r-best)。

**先读**：同一指南 §10.2.3.1 的 memory banks 与 §10.2.3.2 的 C=AB 案例。停在同步后的 tile 计算处，自己补出多 tile 循环与边界条件。

**配套解释**：仍不清楚为什么 padding 有用时，查 §10.2.3.3 的 C=AAᵀ 示例，或 [NVIDIA 转置博客](../../resources/README.md#x-cuda) 中共享内存 tile 改为额外一列的代码段；二选一，替换本段 15 分钟，不增加新项目。

**动手练习**：写一个固定 tile 大小的 shared-memory GEMM，解释加载结束与复用结束的同步点；覆盖至少一个 M/N/K 非 tile 整数倍的形状。

**检查结果**：两个版本同精度通过对齐；能画出每次 global load 服务哪些输出，并说明 shared memory 使用量的代价。

## 3. 在计时之前预测性能限制（45 分钟）

资源定位：[用 Roofline 连接 FLOPs 与搬运](../../resources/README.md#r-roofline) → [Tensor 存储、FLOPs 与 Roofline 讲义](../../resources/README.md#r-l2)。

**先看/读**：[CS336 Lecture 2](../../resources/README.md#r-l2) 配 [讲义](../../resources/README.md#r-l2) 的 `arithmetic_intensity_matmul`、`roofline_plots`，约 15 分钟；硬件层次不清楚才补第 5 讲。

**配合阅读**：[Scaling Book Part 1](../../resources/README.md#r-roofline) 的 `Visualizing rooflines` 和 `Matrix multiplication`。用本机与当前精度的数据代入，书中的其他硬件参数仅作示例。

**动手练习**：用 `2MNK` 算 FLOPs；分别写理想搬运下界与自己实现的搬运估算，得到算术强度。比较朴素版、tile 版和库基线，记录 TF32/精度设置；采样和正式计时分开。

**完成后检查**：画预测与实测，解释差距可能来自复用、缓存、启动或硬件执行路径；只将已测证据写成结论。要读硬件 Roofline 图时查 [Nsight Compute §2.9](../../resources/README.md#r-ncu)。

## 整理记录与可选拓展

在 `labs/02-cuda/gemm/` 交付两种 GEMM、库基线、边界检查与性能报告，逐步整合到 `projects/gpu-performance-lab/`。W8 将复用算术强度分析推理阶段。

进阶选第二个 tile 大小，验证预测是否成立；Tensor Core、CUTLASS 和异步流水线另开后续单元。
