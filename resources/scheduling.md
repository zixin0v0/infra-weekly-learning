# 任务与调度资料

[资料目录](README.md)

任务依赖决定“能不能开始”，资源决定“现在能不能开始”，队列策略决定“先选谁”。下面的材料分别解释这些问题，配合 W15/W16 的同一套任务记录。

<a id="r-ray-task"></a>

### R-RAY-TASK · Task、Actor 与 ObjectRef

W15-S01 必读；入门到中等；英文；Python 函数/类、A。

**来源**：[Ray Tasks](https://docs.ray.io/en/latest/ray-core/tasks.html)；[ray.remote API](https://docs.ray.io/en/latest/ray-core/api/doc/ray.remote.html)。

**读到哪里**：Tasks 开头 Python 示例 → Passing object refs to Ray tasks → Waiting for Partial Results，30 分钟；remote 页开头函数与 Foo actor 示例，20 分钟。到示例结束，不读全部 API 参数。

**带着什么问题读**：Task 和 Actor 都从可读的官方示例开始；结果检查和计数 Actor 在 W15 完成。 [打开练习与自查](../weeks/week-15-ray/README.md)。

<a id="r-ray-resource"></a>

### R-RAY-RESOURCE · 逻辑资源与实际设备

W15-S02 必读；中等；英文；R-RAY-TASK。

**来源**：[Ray Resources](https://docs.ray.io/en/latest/ray-core/scheduling/resources.html)。

**读到哪里**：Physical Resources and Logical Resources → Specifying Node Resources → Specifying Task or Actor Resource Requirements，50 分钟。停止于 num_cpus/num_gpus 和自定义资源；分数 GPU 按需另读。

**带着什么问题读**：从任务事件计算并发，区分准入令牌、可见设备与显存隔离。 [打开练习与自查](../weeks/week-15-ray/README.md)。

<a id="r-ray-schedule"></a>

### R-RAY-SCHEDULE · 可行性、可用性与节点选择

W15-S03/W16-S03 必读指定范围；中等；英文；资源/日志。

**来源**：[Ray Scheduling](https://docs.ray.io/en/latest/ray-core/scheduling/index.html)。

**读到哪里**：W15：Resources 与 DEFAULT，50 分钟；W16 只复查 Resources 和策略开头约 10 分钟，另用本地自查时段的 40 分钟做字段映射与检查，不重复全文。SPREAD、节点亲和性后置。

**带着什么问题读**：待提交队列的 FIFO/SJF 与 Ray 内部节点选择不同；日志分出提交层和执行层等待。 [打开练习与自查](../weeks/week-16-scheduling/README.md)。

<a id="r-ostep"></a>

### R-OSTEP · 排队指标、FIFO 与 SJF

W16-S01/S02 必读；中等；英文作者教材；Python、M4、W15 日志。

**来源**：[OSTEP 第 7 章](https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf)。

**读到哪里**：S01：§7.1～7.4，50 分钟；S02：§7.4 晚到达例子与 §7.5 STCF 的区别，原文 30 分钟；策略推演另计入本地自查。§7.6 只按需区分 response time；这里先不实现抢占。

**带着什么问题读**：用同一轨迹算等待/周转/makespan，再实现离散事件；SJF 只能选择已到达任务。 [打开练习与自查](../weeks/week-16-scheduling/README.md)。

后续系统方向见 [选读资料](optional.md)，先把当前任务轨迹解释清楚。

<a id="r-retry"></a>

### R-RETRY · 超时、重复效果与有界重试

W15 第三段必学；P4 异常、P8 对象、任务 ID 和状态后。

**来源与范围**：[AWS Retry with backoff](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html) 的 Intent、Motivation、Applicability、Issues and considerations，到 Implementation 前停；[ray.get](https://docs.ray.io/en/latest/ray-core/api/doc/ray.get.html) 只查 timeout 与 GetTimeoutError。合计约 15 分钟，计入 W15 故障练习 2～4 小时。

**检查**：[本地串行故障模拟](../weeks/week-15-ray/session-03.md#retry) 复现效果已发生而确认丢失，补全业务 ID 去重，检查不同参数、不同尝试及非法输入。去重表与计数在崩溃/并发时的原子性不由普通字典保证；不把模拟等同于分布式恰好一次。正文已预读，真实 Ray 故障集成另记运行状态。
