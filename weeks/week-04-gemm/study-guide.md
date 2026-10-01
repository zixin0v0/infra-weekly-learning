# W4 章节导学：从访存地址推到 GEMM 性能

[本周范围与验收](README.md) · [导学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

资料预算：45 + 60 + 45 = 150 分钟。延用 W2 的计时、W3 的检查与采样，只新增 GEMM 的数据复用问题。

## 1. 一个 warp 实际访问哪些地址（45 分钟）

**先读**：[CUDA Best Practices](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html) §10.2.1，重点 §10.2.1.1 连续访问与 §10.2.1.2 错位访问；只画访问模式，不记历史带宽数字。

**接着想一想**：回到 W1 的 stride 图，把矩阵行列索引写成线性地址；用 W2 的线程映射确定同一 warp 中相邻线程访问的位置。

**动手练习**：写朴素 GEMM，选择一个小矩阵打印或手工列出负责某一行输出的线程如何访问 A、B。先过正确性，再测试方形和长方形尺寸。

**检查结果**：能指出合并访存与数据复用分别解决什么问题，不把二者混成同一概念。

## 2. tile 复用了什么，增加了什么（60 分钟）

**先读**：同一指南 §10.2.3.1 的 memory banks 与 §10.2.3.2 的 C=AB 案例。停在同步后的 tile 计算处，自己补出多 tile 循环与边界条件。

**配套解释**：仍不清楚为什么 padding 有用时，查 §10.2.3.3 的 C=AAᵀ 示例，或 [NVIDIA 转置博客](https://developer.nvidia.com/blog/efficient-matrix-transpose-cuda-cc/) 中共享内存 tile 改为额外一列的代码段；二选一，替换本段 15 分钟，不增加新项目。

**动手练习**：写一个固定 tile 大小的 shared-memory GEMM，解释加载结束与复用结束的同步点；覆盖至少一个 M/N/K 非 tile 整数倍的形状。

**检查结果**：两个版本同精度通过对齐；能画出每次 global load 服务哪些输出，并说明 shared memory 使用量的代价。

## 3. 在计时之前预测性能限制（45 分钟）

**先看/读**：[CS336 Lecture 2](https://www.youtube.com/watch?v=kuYAsz7zspQ) 配 [讲义](https://github.com/stanford-cs336/lectures/blob/main/lecture_02.py) 的 `arithmetic_intensity_matmul`、`roofline_plots`，约 15 分钟；硬件层次不清楚才补第 5 讲。

**配合阅读**：[Scaling Book Part 1](https://jax-ml.github.io/scaling-book/roofline/) 的 `Visualizing rooflines` 和 `Matrix multiplication`。用本机与当前精度的数据代入，书中的其他硬件参数仅作示例。

**动手练习**：用 `2MNK` 算 FLOPs；分别写理想搬运下界与自己实现的搬运估算，得到算术强度。比较朴素版、tile 版和库基线，记录 TF32/精度设置；采样和正式计时分开。

**完成后检查**：画预测与实测，解释差距可能来自复用、缓存、启动或硬件执行路径；只将已测证据写成结论。要读硬件 Roofline 图时查 [Nsight Compute §2.9](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html)。

## 课后整理与选修

在 `labs/02-cuda/gemm/` 交付两种 GEMM、库基线、边界检查与性能报告，逐步整合到 `projects/gpu-performance-lab/`。W8 将复用算术强度分析推理阶段。

进阶选第二个 tile 大小，验证预测是否成立；Tensor Core、CUTLASS 和异步流水线另开后续单元。
