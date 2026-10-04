# 单元 W4：GEMM 与数据复用

[课程目录](../../course/README.md) · [我的进度](../../course/progress.md) · [环境准备](../../course/environment.md)

预计 10～18 小时用于本单元，变式与排错另留 1～3 小时；桥接只计新发生的时间。按实际掌握推进，记录规则见 [学习方法](../../course/guide.md#time-budget)。

## 这一单元要弄清什么

矩阵乘法做相同数量的乘加，为什么换一种分块方式就可能更快？先观察相邻线程读哪些地址，再把会反复使用的数据放进共享内存。你会实现朴素与分块 GEMM，用算术强度和 Roofline 解释搬运、计算与同步各自的限制。

## 开始前

完成 W3 的同步和边界检查。用 [M1](../../course/prerequisites.md) 与 [W1 的计算约定](../week-01-foundations/session-03.md)，手算 2×3 乘 3×2 的输出形状和 FLOPs；已会这部分可直接继续。

<details>
<summary>先解释，再展开核对</summary>

输出 4 个元素，每个执行 3 次乘加，按每次 2 FLOPs 计共 24 FLOPs；性能上限还受搬运量与硬件限制。

</details>

## 按顺序学习

- [W4 第 1 段：相邻线程读得连续，就没有重复搬运了吗？](session-01.md)。
- [W4 第 2 段：读进来的 tile，什么时候才能被下一轮覆盖？](session-02.md)。
- [W4 第 3 段：计算更少，为什么不一定更快？](session-03.md)。

- [本单元掌握检查](assessment.md)：实验完成要求、变式与排错题。

## 实践任务

建议目录：labs/02-cuda/gemm/。

1. 写朴素 GEMM 和 shared-memory 分块版本，支持至少一种非 tile 整数倍尺寸。
2. 比较小/大、方形/长方形输入；固定数据类型、转置设置与计时范围。
3. 对照 PyTorch matmul 或 cuBLAS，记录 TF32/混合精度策略，使结果语义和精度要求一致。
4. 用 2 × M × N × K 约定估算 FLOPs，记录实际延迟并画性能曲线。
5. 画出一个 tile 的加载与复用过程，区分理论数据搬运估算与 profiler 实测。

用算术强度（FLOPs/字节）建立简化 Roofline 预测：性能上界取计算上限与带宽乘算术强度的较小者。理论上限、估算字节和实测值分别标明；可沿用 [Nsight Compute 指南](../../resources/gpu.md#r-ncu) 的 Roofline 说明。先做一组预测与观察的核对，不额外加入大量 tile 搜索。

工程对照加入同输入的 `torch.matmul`，记录输入/累加精度、TF32 设置和计时范围。练习实现用于解释复用，不以击败库实现作为通过条件。

## 按需回看

博客：[An Efficient Matrix Transpose in CUDA C/C++](../../resources/optional.md#x-cuda)。用转置理解合并访存和 shared memory padding；历史设备上的数字不作为本机目标。可用 15 分钟替换卡点复习。

[上一单元](../week-03-reduction-profiling/README.md) · [下一步](../week-05-triton-softmax/README.md)
