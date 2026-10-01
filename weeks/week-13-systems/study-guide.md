# W13 章节导学：从 eager 到 compile，再回到模型

[本周范围与验收](README.md) · [导学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

资料预算：45 + 60 + 45 = 150 分钟。复用 W5 表达式或 W6 Block，固定形状前向先通过；这里是本仓库练习，不是 CS336 官方作业提交。

## 1. 编译前后是否仍计算相同结果（45 分钟）

**先看/读**：[CS336 Lecture 6](https://www.youtube.com/watch?v=xnDHaNUvHBg) 配 [lecture_06.py](https://github.com/stanford-cs336/lectures/blob/main/lecture_06.py) 的 `naive_vs_builtin_vs_compiled_gelu`，约 15 分钟，只理解比较方式，不另加一个 GELU 项目。

**立即联读**：[Introduction to torch.compile](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html) 的 `Basic Usage`，核对函数/模块包装方式。

**动手练习**：将已有表达式或 Block 加入 compile 路径，统一输入、dtype、设备、autograd 与 dropout 条件；先保存 eager/compile 误差，再测速度。

**检查结果**：结果对齐，支持条件清楚；已有 Triton 实现只有在数学与精度语义可比时才加入第三组。

## 2. 首次成本和稳态收益分别是什么（60 分钟）

**先读**：同一教程 `Demonstrating Speedups` 的计时与预热示例，再回 Lecture 6 的 `benchmarking` 核对同步。关注方法，不复制教程的加速比。

**接着想一想**：沿用 W6 模型区段与时间线，观察减少 Python 调用或 kernel 启动是否改变实际关键路径。kernel 数变少是线索，最终仍以整体计时为准。

**动手练习**：分开记录首次调用、预热、稳态；注明首次调用是否使用已有编译缓存及是否为新进程。对算子与模型区段分别比较，保存原始测量。

**检查结果**：若稳态更快，估算多少次调用后能摊平额外首次成本；若没有更快，说明不存在该配置下的回本点，不强求正收益。

## 3. 形状变化和 graph break 怎样改变结论（45 分钟）

**先读**：同一教程 `Graph Breaks`，只跟踪一个不支持的 Python 行为示例；用 `Troubleshooting` 查自己遇到的问题。

**接着想一想**：图中断和重编译是不同现象。第二个 shape 变慢只说明发生了额外成本，需要日志或工具证据才能归因为重编译。

**动手练习**：增加第二个形状，记录实际编译行为；另对一个 graph break 示例说明被切断的位置及影响。没有发生重编译也记录，不为制造预期结果反复调参。

**完成后检查**：报告说明固定/变化形状、首次/稳态的适用条件，算子收益与模型收益各有证据。

## 课后整理与选修

在 `labs/03-triton-attention/systems-study/` 保存对照与报告，接入 `projects/gpu-performance-lab/` 的同一复现入口。

进阶入口：[CS336 Assignment 2](https://github.com/stanford-cs336/assignment2-systems)，仓库中题面名为 `cs336_assignment2_systems.pdf`。本轮核验了文件入口，PDF 内容抓取未成功，因此不指定未经核验的题号或页码。后续选题时先锁 commit 再核对题面；完整作业不计入本周 9 小时。
