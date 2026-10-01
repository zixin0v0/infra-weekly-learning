# W15 章节导学：让 Ray 任务执行可观察

[本周范围与验收](README.md) · [导学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

资料预算：50 + 50 + 50 = 150 分钟。本周用短小的官方文本示例串联实践，不额外加入一套视频课程。

## 1. 把函数和状态变成 Task 与 Actor（50 分钟）

**先读**：[What's Ray Core?](https://docs.ray.io/en/latest/ray-core/walkthrough.html) 的 `Running a Task`、`Calling an Actor`、`Passing Objects`。每节只运行并修改一个最小示例。

**接着想一想**：把 Python 返回值与 ObjectRef 画成两种对象，标出真正等待结果的位置。Actor 用于持有状态，不能仅因语法相似就当成普通无状态函数。

**动手练习**：写数值计算 Task 和计数 Actor，提交多个任务后收集返回；将结果与本地函数计算对齐。不要在每提交一个任务后立即等待它，从而意外串行化全部工作。

**检查结果**：能解释异步提交、等待与依赖关系，结果正确。

## 2. 资源声明限制的是什么（50 分钟）

**先读**：[Resources](https://docs.ray.io/en/latest/ray-core/scheduling/resources.html) 的 `Physical Resources and Logical Resources`、`Specifying Node Resources`，再定位 `num_cpus` / `num_gpus` 的任务声明示例。

**接着想一想**：把 W7/W11 的实际 GPU 使用与 Ray 的逻辑令牌分开。申请到 GPU 不等于限制显存占用，也不意味着 GPU 一直忙碌。

**动手练习**：先用 CPU 任务与显式资源声明验证并发限制，记录开始/结束和可见设备。GPU 可用后再加一个小型计算任务，真实占用另行采样。

**检查结果**：能区分逻辑资源、设备可见性与实际占用；模拟令牌的实验明确标注为模拟。

## 3. 从排队现象得到完整事件记录（50 分钟）

**先读**：[Scheduling](https://docs.ray.io/en/latest/ray-core/scheduling/index.html) 的 `Resources`，区分 feasible、available、infeasible；再看 `Scheduling Strategies → DEFAULT`，暂不尝试所有放置策略。

**接着想一想**：W10 记录请求等待，这里记录作业等待；虽然都需要时间轴，测量对象和机制不同。Ray 的节点放置也不自动等于自己想要的 FIFO/SJF 队列策略。

**动手练习**：给每个任务记录 ID、资源、提交/开始/结束、结果或失败。主线单机统一时钟口径，改变资源请求与任务数，解释何时等待；保留失败记录，不能只保存成功样本。

**完成后检查**：从日志可重建等待时间与执行时间，区分资源不足和任务尚未完成；W16 将直接复用事件字段。

## 课后整理与选修

在 `labs/07-scheduling/ray-basics/` 交付 Task/Actor 示例和事件记录器。CPU sleep 只能验证日志与排队逻辑，不能作为 GPU 利用率结论。

进阶才读 [Placement Groups](https://docs.ray.io/en/latest/ray-core/scheduling/placement-group.html) 的 `Key Concepts → Bundles`，解释多 GPU 任务为什么可能需要成组预留，本周不实现集群级调度器。
