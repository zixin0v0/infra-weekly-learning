# W1 章节导学：从地址到 Tensor 资源账本

[本周范围与验收](README.md) · [导学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

详细备课：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md) · [2026-10-01 资料复核](refresh-2026-10-01.md)。先按备课单预测，再在本周同一实验目录核对；未来实际开课仍须重查资料。

资料预算：50 + 50 + 50 = 150 分钟。先做周 README 的 20 分钟诊断；已掌握的章节跳过，用同一练习验证。

2026-10-01 [开课更新](refresh-2026-10-01.md) 已完成；今天按 [第一段备课与暂停题](session-01.md) 推进。学习练习与段内验收尚未完成。

## 1. 类型和地址怎样约束存储（50 分钟）

**先读**：[CS106L 第 2 讲 PDF](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-02-TypesAndStructs.pdf)，阅读器第 35～48 页：类型、静态类型检查和小练习；第 44 页先暂停作答，第 48 页结束。再读 [第 6 讲 PDF](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-06-Iterators.pdf) 第 70～85 页，聚焦地址、指针和解引用，以第 85 页 `Array pointer` 为停止点。略过过场问答页和容器 API 的完整巡览；新增一页使用原阅读预算，不增加本段时间。

**配合阅读**：[CS336 Lecture 2 视频](https://www.youtube.com/watch?v=kuYAsz7zspQ) 的 Tensor 类型主题，配 [lecture_02.py 固定版本](https://github.com/stanford-cs336/lectures/blob/6ff836dd5dfcbe7e848fe1a1734f1886f1116a7a/lecture_02.py) 中 `tensors_basics`、`tensors_memory` 的 FP32/FP16 小例子；跳过大矩阵实际分配，到 `## bf16` 前结束。讲义函数用于定位，视频时间轴未核验；两类材料分别解释 C++ 对象与 Tensor 元素，不能把 Tensor 对象身份当成数据地址。

**重点问题**：同样 6 个元素，FP32 和 FP16 的数据区各占多少字节？地址差的单位是字节还是元素？

**动手练习**：用 `std::array<float, 6>` 写求和，打印相邻元素地址；用 Tensor 的 `numel()` 和 `element_size()` 计算数据量。C++ 生命周期还不清楚时回 [CS106L 课表](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/) 第 3 讲补引用概念；该讲本轮只核验入口，未核验 PDF 页码。

**检查结果**：能解释数据类型、元素数、连续存储的关系，且程序结果与手算一致。

## 2. shape 相同为什么不代表布局相同（50 分钟）

**先读**：[Tensor Views](https://docs.pytorch.org/docs/2.14/tensor_view.html) 正文开头的共享存储说明与 `base` / `view` 示例，再读转置导致不连续的示例，以及末尾关于 `reshape`、`flatten`、`contiguous` 的说明。该页面没有细分节号，用这些代码词定位。

**接着想一想**：拿上一段的地址图，画出 `(2, 3)` 连续 Tensor 和转置视图的逻辑索引；只改变访问规则，不预设发生复制。

**重点问题**：`transpose`、`view`、`reshape`、`contiguous` 各保证什么？为什么不能依赖 `reshape` 一定返回视图？

**动手练习**：逐个打印 shape、stride、连续性与数据指针；修改一个视图元素，观察基张量。再显式生成连续副本并比较；把失败的 `view` 调用与原因记录下来。

**检查结果**：先预测再运行，至少解释一个共享存储案例和一个复制案例。

## 3. 把存储账本接到 Linear 计算（50 分钟）

**先看/读**：沿用 Lecture 2，定位 `tensor_operations_flops`；只跟随矩阵乘法计数。梯度和优化器部分留到训练先修，不在本周展开。

**接着想一想**：从 `(batch, in_features) × (in_features, out_features)` 写出维度和每个输出元素的操作数；与前两段的字节计算放在同一张表。

**动手练习**：完成 Linear 参数、输入/输出存储与前向 FLOPs 计算器；比较两种 dtype、两个 batch，并核对周 README 的诊断题。参数量应不随 batch 改变。

**完成后检查**：区分参数存储、激活大小和实际峰值显存；记录乘加按 2 FLOPs、bias 是否计入。将账本留给 W4 的算术强度和 W12 的训练状态计算。

## 课后整理与选修

在 `labs/01-foundations/resource-accounting/` 整理数组示例、Tensor 布局脚本、资源计算脚本和一页报告。文件名可在实现时确定，代码尚未创建。

进阶只选一个：给计算器增加 GQA 的 KV Cache 字节估算，先写符号公式，到 W9 再核对；本周不要求估算整个大模型。
