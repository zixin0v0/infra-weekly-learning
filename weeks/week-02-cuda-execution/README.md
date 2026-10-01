# 单元 W2：GPU 执行与内存

[总路线](../../README.md) · [学习方式](../../docs/learning-workflow.md) · [资源索引](../../resources/README.md) · [当前做法与相关进展](context.md)

建议学习位置：第 2 个学习周。W2 是固定单元 ID，按下方导航推进。

状态：未开始。预算：9 小时。环境：本地 4060；工具链安排见环境说明。

## 本周要解决什么

理解 thread、warp、block 与内存层次，完成第一个可靠计时的 CUDA kernel。

先修：W1通过。要回答：线程如何映射数组？越界如何处理？异步执行为何影响计时？

## 按顺序学习

先用30分钟看 [本周补充阅读](context.md)，按 [更新流程](../../docs/weekly-refresh.md) 核对资料。时间从原报告时段划出，总预算不变。

按 [章节导学](study-guide.md) 分三段学习，每段读完就动手。下面只列安排，具体链接、阅读位置和检查方法都在导学里。

备课已准备：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md)。[本次资料复核](refresh-2026-10-01.md) 已完成；学习未开始，实际开课日仍按更新流程复查。

| 学习段 | 指定范围 | 读后立即做 | 资料预算 |
| --- | --- | --- | --- |
| 1. 线程映射 | CUDA §1.2、§2.1.2、§2.3.2；入门视频 | 索引表与 Vector Add | 60 分钟 |
| 2. 内存与错误 | CUDA §2.1.3.2、§2.1.4；Using Memcheck | 边界输入与内存检查 | 45 分钟 |
| 3. 可信计时 | Best Practices §9.1.2、§9.2 | kernel/端到端计时与带宽 | 45 分钟 |

阅读共150分钟，包含视频、教程和论文。补充材料按需替换阅读内容；选修另排时间。

## 遇到问题再看

博客：[An Even Easier Introduction to CUDA](https://developer.nvidia.com/blog/even-easier-introduction-cuda/)，用于 CPU/GPU 工作分工仍不清楚时，替换 30 分钟资料时间。示例使用的内存管理方式要与自己的代码区分。

项目：[NVIDIA cuda-samples](https://github.com/NVIDIA/cuda-samples)，查 Vector Add 示例及其构建说明，不要求编译全部样例。

## 实践任务

建议目录：labs/02-cuda/vector-add/。

1. 写 CPU 参考与 CUDA Vector Add，覆盖小数组、非 block 整数倍长度和大数组。
2. 显式检查索引边界及 CUDA 调用错误，对小型边界输入运行 memcheck。分配和数据拷贝不放进 kernel 单独计时区间；sanitizer 运行与性能计时分开。
3. 用 CUDA Event 预热并重复计时，固定 dtype，扫描至少 4 个输入规模。
4. 计算有效带宽：读取两个输入并写一个输出，共 3 × N × 每元素字节数，再除以执行时间。
5. 另外记录一次含数据传输的端到端时间，解释两种指标各自回答什么问题。

## 验收

- [ ] 所有形状通过正确性检查，包含非整除输入。
- [ ] 保存 memcheck 检查结果；工具不可用时记录环境限制并安排补测，不标为已通过内存检查。
- [ ] 保存计时范围、预热与重复次数、原始延迟。
- [ ] 画输入规模—延迟/有效带宽曲线，单位明确。
- [ ] 能解释小输入开销与大输入带宽表现，不把有效带宽直接称为实测 DRAM 带宽。
- [ ] 按补充阅读的要求，在报告中解释一个实际使用问题，注明哪些结论还没验证。

## 实验记录

实验与报告：尚未创建。自评与验收日期：待完成。

[上一单元](../week-01-foundations/README.md) · [下一单元](../week-03-reduction-profiling/README.md)
