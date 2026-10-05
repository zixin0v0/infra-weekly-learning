# 任务与调度资料

[资料目录](README.md)

任务依赖决定“能不能开始”，资源决定“现在能不能开始”，队列策略决定“先选谁”。下面的材料分别解释这些问题，配合 W15/W16 的同一套任务记录。

<a id="r-ray-task"></a>

### R-RAY-TASK · Task、Actor 与 ObjectRef

**中文补充（按需，暂缺）：** Task/Actor/ObjectRef 的合适外部中文材料待补。 [对应范围](#cn-ray-gap)。

W15-S01 必读；入门到中等；英文；Python 函数/类、A。

**来源**：[Ray Tasks](https://docs.ray.io/en/latest/ray-core/tasks.html)；[ray.remote API](https://docs.ray.io/en/latest/ray-core/api/doc/ray.remote.html)。

**读到哪里**：Tasks 开头 Python 示例 → Passing object refs to Ray tasks → Waiting for Partial Results，30 分钟；remote 页开头函数与 Foo actor 示例，20 分钟。到示例结束，不读全部 API 参数。

**带着什么问题读**：Task 和 Actor 都从可读的官方示例开始；结果检查和计数 Actor 在 W15 完成。 [打开练习与自查](../weeks/week-15-ray/README.md)。

<a id="r-ray-resource"></a>

### R-RAY-RESOURCE · 逻辑资源与实际设备

**中文补充（按需，暂缺）：** 逻辑资源与实际隔离的准确中文对应待补。 [对应范围](#cn-ray-gap)。

W15-S02 必读；中等；英文；R-RAY-TASK。

**来源**：[Ray Resources](https://docs.ray.io/en/latest/ray-core/scheduling/resources.html)。

**读到哪里**：Physical Resources and Logical Resources → Specifying Node Resources → Specifying Task or Actor Resource Requirements，50 分钟。停止于 num_cpus/num_gpus 和自定义资源；分数 GPU 按需另读。

**带着什么问题读**：从任务事件计算并发，区分准入令牌、可见设备与显存隔离。 [打开练习与自查](../weeks/week-15-ray/README.md)。

<a id="r-ray-schedule"></a>

### R-RAY-SCHEDULE · 可行性、可用性与节点选择

**中文补充（按需，暂缺）：** Ray 可行性/可用性及 DEFAULT 策略缺匹配中文对应。 [对应范围](#cn-ray-gap)。

W15-S03/W16-S03 必读指定范围；中等；英文；资源/日志。

**来源**：[Ray Scheduling](https://docs.ray.io/en/latest/ray-core/scheduling/index.html)。

**读到哪里**：W15：Resources 与 DEFAULT，50 分钟；W16 只复查 Resources 和策略开头约 10 分钟，另用本地自查时段的 40 分钟做字段映射与检查，不重复全文。SPREAD、节点亲和性后置。

**带着什么问题读**：待提交队列的 FIFO/SJF 与 Ray 内部节点选择不同；日志分出提交层和执行层等待。 [打开练习与自查](../weeks/week-16-scheduling/README.md)。

<a id="r-ostep"></a>

### R-OSTEP · 排队指标、FIFO 与 SJF

**中文补充（按需，部分）：** 中文 FCFS/SJF；STCF 区分和本课事件轨迹仍读原文。 [对应范围](#cn-scheduling)。

W16-S01/S02 必读；中等；英文作者教材；Python、M4、W15 日志。

**来源**：[OSTEP 第 7 章](https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf)。

**读到哪里**：S01：§7.1～7.4，50 分钟；S02：§7.4 晚到达例子与 §7.5 STCF 的区别，原文 30 分钟；策略推演另计入本地自查。§7.6 只按需区分 response time；这里先不实现抢占。

**带着什么问题读**：用同一轨迹算等待/周转/makespan，再实现离散事件；SJF 只能选择已到达任务。 [打开练习与自查](../weeks/week-16-scheduling/README.md)。

后续系统方向见 [选读资料](optional.md)，先把当前任务轨迹解释清楚。

<a id="r-retry"></a>

### R-RETRY · 超时、重复效果与有界重试

**中文补充（按需，部分）：** AWS 同范围官方中文译文；ray.get timeout 仍查原接口。 [对应范围](#cn-retry)。

W15 第三段必学；P4 异常、P8 对象、任务 ID 和状态后。

**来源与范围**：[AWS Retry with backoff](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html) 的 Intent、Motivation、Applicability、Issues and considerations，到 Implementation 前停；[ray.get](https://docs.ray.io/en/latest/ray-core/api/doc/ray.get.html) 只查 timeout 与 GetTimeoutError。合计约 15 分钟，计入 W15 故障练习 2～4 小时。

**检查**：[本地串行故障模拟](../weeks/week-15-ray/session-03.md#retry) 复现效果已发生而确认丢失，补全业务 ID 去重，检查不同参数、不同尝试及非法输入。去重表与计数在崩溃/并发时的原子性不由普通字典保证；不把模拟等同于分布式恰好一次。正文已预读，真实 Ray 故障集成另记运行状态。

## 中文补充：等待、重试与资源配置

<a id="cn-scheduling"></a>

### CN-Scheduling：先用两种顺序比较同一批任务

**中文图文：** 小林 coding《图解系统》[6.1 进程调度/页面置换/磁盘调度算法](https://xiaolincoding.com/os/5_schedule/schedule.html)，只读“先来先服务调度算法”和“最短作业优先调度算法”，到“高响应比优先”前。

这是作者中文讲解，指定段落已预读，用于 W16 在读 OSTEP 前形成直觉。它讨论 CPU 进程；本课借用顺序规则，仍在自己的非抢占任务队列里比较。文章概括“提高吞吐”的说法不能代替固定轨迹计算；同时到达且无空闲的同一批任务，换顺序可以降低平均等待而不改变总工作量。估计误差、晚到达、最长等待与 Ray 资源等待继续按原课检查。

<a id="cn-kubernetes"></a>

### CN-Kubernetes：从期望配置找到实际等待原因

**来源：** Kubernetes 官方站点的中文社区译文，对应 S6 的英文对象和资源文档。

| 需要理解 | 中文范围 | 回到本课检查 |
| --- | --- | --- |
| 配置与实际状态 | [Kubernetes 对象](https://kubernetes.io/zh-cn/docs/concepts/overview/working-with-objects/)：“理解 Kubernetes 对象”“对象规约与状态”“描述对象”“必需字段” | 在现有 YAML 标出 apiVersion、kind、metadata、spec；不运行原文部署示例 |
| 能否放下、能用多少 | [为 Pod 和容器管理资源](https://kubernetes.io/zh-cn/docs/concepts/configuration/manage-resources-containers/)：“请求和限制”、CPU/内存资源单位、Pod 带资源请求时如何调度 | 比较 requests 与可分配资源；不要把它与 limits 混为一谈 |
| 失败发生在哪一步 | [调试 Pod](https://kubernetes.io/zh-cn/docs/tasks/debug/debug-application/debug-pods/)：查看 describe/Events、资源不足、镜像拉取失败的段落 | 区分 FailedScheduling、镜像等待、程序退出；跳过删除/重建建议 |

指定正文已预读，中文页可能滞后。Pending 不只意味着尚未调度，容器 Waiting 也不是单独一种 Pod phase；必须结合调度条件和 Events 判断。S6/W16 仍只要求读配置和诊断示例事件，不把集群操作变成新的前提。中文视频的具体分集尚未核验。

<a id="cn-retry"></a>

### CN-Retry：收不到确认时，再做一次会怎样

**中文正文：** AWS [使用退避模式重试](https://docs.aws.amazon.com/zh_cn/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html)的“意图”“动机”“适用性”“问题和注意事项”，到“实施”前。与 R-RETRY 的英文材料直接对应，是 AWS 标明的机器翻译版本。

指定范围已预读。W15 第三段用它区分暂时错误、重试间隔和幂等效果；不需要 AWS Step Functions。Ray 超时不会自动撤销已经发生的业务效果，退避也不自动提供去重。自己的故障模拟、业务 ID、参数一致性检查继续保留。

<a id="cn-ray-gap"></a>

### Ray 专题仍保留缺项

已经查找中文 Task/Actor、ObjectRef、资源声明和重试说明，但候选中有漏写 remote 装饰器、把 Task 称为无副作用、把 ray.wait 一概写成非阻塞、将申请多 CPU 理解为自动拆任务等问题；未据此新增推荐。另有视频关联会员私有代码，字幕和分集内容无法确认，未作为学习依赖。

W15 第一/二段和 W16 的 Ray 字段映射继续使用原官方英文与本地中文例子；不能把上述 Kubernetes 补充当成 Ray 调度接口说明。[具体候选与缺项](../docs/audits/2026-10-05-chinese-resources.md#pending)留在核验记录，找到合适原作者材料后再接入。
