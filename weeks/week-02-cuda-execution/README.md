# 单元 W2：GPU 执行与内存

[课程目录](../../course/README.md) · [我的进度](../../course/progress.md) · [环境准备](../../course/environment.md)

预计 11～20 小时用于本单元，变式与排错另留 1～3 小时；桥接只计新发生的时间。按实际掌握推进，记录规则见 [学习方法](../../course/guide.md#time-budget)。

## 这一单元要弄清什么

把一个 CPU 循环改成 CUDA kernel，难点不只在启动更多线程：每个线程要找到自己的元素，最后一块要避开越界，CPU 还必须等到 GPU 真正做完才能计时。你会用向量相加逐一检查这些关系，再比较计算本身与包含数据搬运的总耗时。

## 开始前

先完成 W1、[S1 的进程与环境操作](../../course/bridges/s01.md#s1)，以及 [先修 A/B](../../course/prerequisites.md) 的 C++ 指针、引用、生命周期与边界练习。开始前画出 N=10、每块 4 个线程的覆盖表，并解释指针变量和它指向的数据有什么区别。

<details>
<summary>先解释，再展开核对</summary>

需要 3 个 block；最后一块只有索引 8、9 有效。host 指针变量的存在不证明 device 数据已经分配或复制。

</details>

## 按顺序学习

- [补齐 S1 进程、权限和环境诊断](../../course/bridges/s01.md)。
- [W2 第 1 段：线程编号，怎样变成数组下标？](session-01.md)。
- [W2 第 2 段：算完以后，结果为什么还没回到 CPU？](session-02.md)。
- [W2 第 3 段：你计到的是提交时间，还是完成时间？](session-03.md)。

- [本单元掌握检查](assessment.md)：实验完成要求、变式与排错题。

## 实践任务

建议目录：labs/02-cuda/vector-add/。

1. 写 CPU 参考与 CUDA Vector Add，覆盖小数组、非 block 整数倍长度和大数组。
2. 显式检查索引边界及 CUDA 调用错误，对小型边界输入运行 memcheck。分配和数据拷贝不放进 kernel 单独计时区间；sanitizer 运行与性能计时分开。
3. 用 CUDA Event 预热并重复计时，固定 dtype，扫描至少 4 个输入规模。
4. 计算有效带宽：读取两个输入并写一个输出，共 3 × N × 每元素字节数，再除以执行时间。
5. 另外记录一次含数据传输的端到端时间，解释两种指标各自回答什么问题。

## 按需回看

博客：[An Even Easier Introduction to CUDA](../../resources/optional.md#x-cuda)，用于 CPU/GPU 工作分工仍不清楚时，替换 20 分钟复习时间。示例使用的内存管理方式要与自己的代码区分。

实现时沿第二段的 host/device 步骤逐项检查；不额外编译整套示例库。

[上一单元](../week-01-foundations/README.md) · [下一步](../week-03-reduction-profiling/README.md)
