# W13 分段学习指南：从 eager 到 compile，再回到模型

[本周范围与验收](README.md) · [自学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

详细学习指南：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md) · [2026-10-01 资料复核](refresh-2026-10-01.md)。每段先作答，再读图例与折叠核对说明，最后在本周同一实验目录验证；AI 提示词可跳过。未来实际开始学习仍须重查资料。

原文选读预算：45 + 60 + 45 = 150 分钟；本地例子与自查另计 60 分钟，动手与正确性检查 240 分钟。含资料复核、分析和报告，本单元约 10.5 小时，详见 [时间表](../../docs/study-guide.md#time-budget)。

## 学习目标与前置检查

本单元知识点：eager/compile、首次成本、稳态、graph break。学完应当能对齐编译前后结果，估算成本回收，并用模型区段解释整体收益。

**开始前检查**：通过 W6 的正确性对照与时间线；能给异步 GPU 操作选择同步计时边界。 缺项按 [基础补学入口](../../docs/prerequisites.md) 的材料、范围和练习完成；补学时间另计。

<details>
<summary>前置问题核对</summary>

首次调用包含编译等一次性成本，不能与预热后的 eager 单次延迟直接比较；回 W2 计时与 W6 时间线。

</details>

资源的难度、语言、前置要求、原始 URL 和停止位置统一保存在 [资源索引](../../resources/README.md)，下文按学习顺序链接。先读必读范围，卡点材料替换复习时间，可选拓展不影响基础完成。

## 1. 编译前后是否仍计算相同结果（45 分钟）

资源定位：[eager、编译和变化输入](../../resources/README.md#r-compile) → [测量、Triton 与编译的讲义例子](../../resources/README.md#r-l6)。

**先看/读**：[CS336 Lecture 6](../../resources/README.md#r-l6) 配 [lecture_06.py](../../resources/README.md#r-l6) 的 `naive_vs_builtin_vs_compiled_gelu`，约 15 分钟，只理解比较方式，不另加一个 GELU 项目。

**立即联读**：[Introduction to torch.compile](../../resources/README.md#r-compile) 的 `Basic Usage`，核对函数/模块包装方式。

**动手练习**：将已有表达式或 Block 加入 compile 路径，统一输入、dtype、设备、autograd 与 dropout 条件；先保存 eager/compile 误差，再测速度。

**检查结果**：结果对齐，支持条件清楚；已有 Triton 实现只有在数学与精度语义可比时才加入第三组。

## 2. 首次成本和稳态收益分别是什么（60 分钟）

资源定位：[eager、编译和变化输入](../../resources/README.md#r-compile)。

**先读**：同一教程 `Demonstrating Speedups` 的计时与预热示例，再回 Lecture 6 的 `benchmarking` 核对同步。关注方法，不复制教程的加速比。

**接着想一想**：沿用 W6 模型区段与时间线，观察减少 Python 调用或 kernel 启动是否改变实际关键路径。kernel 数变少是线索，最终仍以整体计时为准。

**动手练习**：分开记录首次调用、预热、稳态；注明首次调用是否使用已有编译缓存及是否为新进程。对算子与模型区段分别比较，保存原始测量。

**检查结果**：若稳态更快，估算多少次调用后能摊平额外首次成本；若首次更慢且稳态没有更快，不能靠增加调用次数摊平首次差额；具体推导见 [第二段](session-02.md)。

## 3. 形状变化和 graph break 怎样改变结论（45 分钟）

资源定位：[eager、编译和变化输入](../../resources/README.md#r-compile)。

**先读**：同一教程 `Graph Breaks`，只跟踪一个不支持的 Python 行为示例；用 `Troubleshooting` 查自己遇到的问题。

**接着想一想**：图中断和重编译是不同现象。第二个 shape 变慢只说明发生了额外成本，需要日志或工具证据才能归因为重编译。

**动手练习**：增加第二个形状，记录实际编译行为；另对一个 graph break 示例说明被切断的位置及影响。没有发生重编译也记录，不为制造预期结果反复调参。

**完成后检查**：报告说明固定/变化形状、首次/稳态的适用条件，算子收益与模型收益各有证据。

## 整理记录与可选拓展

在 `labs/03-triton-attention/systems-study/` 保存对照与报告，接入 `projects/gpu-performance-lab/` 的同一复现入口。

进阶入口：[CS336 Assignment 2](../../resources/README.md#x-navigation)，仓库中题面名为 `cs336_assignment2_systems.pdf`。本轮核验了文件入口，PDF 内容抓取未成功，因此不指定未经核验的题号或页码。后续选题时先锁 commit 再核对题面；完整作业不计入主线预算。
