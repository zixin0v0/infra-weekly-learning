# 单元 W1：Tensor、内存与资源账本

[课程目录](../../course/README.md) · [我的进度](../../course/progress.md) · [环境准备](../../course/environment.md)

预计 12～22 小时用于本单元，变式与排错另留 1～3 小时；桥接只计新发生的时间。按实际掌握推进，记录规则见 [学习方法](../../course/guide.md#time-budget)。

## 这一单元要弄清什么

为什么转置后看起来换了行列，底层数据却可能没搬动？从一个 C++ 数组和一个小 Tensor 出发，这里把元素地址、shape、stride 连起来，再计算 Linear 的参数、输入输出和矩阵乘法开销。做完后，你应能先手算，再用程序解释每一个数字。

## 开始前

先完成 [P1～P7](../../course/foundations/README.md)，以及 [先修 B / M1](../../course/prerequisites.md) 的最小 C++、Tensor 和矩阵诊断。试着写数组求和，说明 2×3 乘 3×2 的输出形状。先做 [S1](../../course/bridges/s01.md#s1) 的解释器与工作目录部分，线程和权限在 W2 前补齐。这里不需要 CUDA；类和模型结构在 W6 前学，训练、验证与权重重载在 W6 前学，Adam 恢复在 W11 前补齐。

<details>
<summary>先解释，再展开核对</summary>

输出是 2×2；FP32 的 6 个元素占 24 字节。不能说明计算过程时，回先修 P/B/M1 的练习。

</details>

## 快速自测

- 用自己的话区分指针与引用，说明局部变量的生命周期。
- 对形状为 (2, 3) 的连续 Tensor，预测转置前后的 shape、stride 和连续性。
- 对有 bias 的 Linear(128, 256)，计算参数个数、FP32 参数字节数，以及输入 (32, 128) 的矩阵乘法 FLOPs。

完成先修后，用这些题找出本单元需要重点练习的部分。记录卡点；已能独立解释的部分缩短补学时间，把时间用于实现和核对。

## 按顺序学习

- [先完成 S1 的解释器与工作目录部分；进程/权限可在 W2 前完成](../../course/bridges/s01.md)。
- [W1 第 1 段：类型改变时，地址为什么也会变？](session-01.md)。
- [W1 第 2 段：形状变了，数据搬动了吗？](session-02.md)。
- [W1 第 3 段：Linear 多处理一行输入，要多存一份权重吗？](session-03.md)。
- [W1 第 4 段：同样占两字节，为什么算出的数不一样？](session-04.md)。

- [本单元掌握检查](assessment.md)：实验完成要求、变式与排错题。

## 实践任务

建议开始时创建实验目录：labs/01-foundations/resource-accounting/。

1. 写一个可编译的 C++ 连续数组求和示例，打印地址间距并说明边界与生命周期。
2. 用 PyTorch 打印 Tensor 的 shape、stride、dtype、element_size、numel 与连续性；比较转置、reshape、contiguous 的结果。
3. 建一个资源账本：参数个数、参数字节数、输入/输出字节数、前向矩阵乘法 FLOPs，手算与代码逐项核对。
4. 用 FP16/BF16 小例子解释范围和精度；实现有限性与容差检查，保留加法顺序对照。
5. 写明计数约定：一次乘加按 2 FLOPs；是否包含 bias；本周账本不包含梯度、优化器状态或实际峰值显存。

<details>
<summary>展开核对 Linear 自测</summary>

参数为 `128×256+256=33,024` 个，FP32 参数占 `33,024×4=132,096 B`；矩阵乘法为 `2×32×128×256=2,097,152 FLOPs`，未计 bias 加法。batch 改变计算量和激活大小，但不改变这层参数个数。

</details>

## 按需回看

[AIInfraGuide](../../resources/optional.md#x-navigation) 的前置基础中，按诊断卡点查编程语言与 PyTorch 章节；只作中文辅助导航。本周不额外要求论文。

[下一步](../week-02-cuda-execution/README.md)
