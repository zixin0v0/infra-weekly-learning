# W15 分段学习指南：让 Ray 任务执行可观察

[本周范围与验收](README.md) · [自学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

原文选读预算：50 + 50 + 50 = 150 分钟；本地例子与自查另计 60 分钟，动手与正确性检查 240 分钟。含资料复核、分析和报告，本单元约 10.5 小时，详见 [时间表](../../docs/study-guide.md#time-budget)。

## 学习目标与前置检查

本单元知识点：Task/Actor、ObjectRef、资源声明、排队日志。学完应当能写可核对结果的任务与状态对象，区分逻辑资源和实际占用，重建执行事件。

**开始前检查**：完成先修 P 的函数、类、JSON 和先修 A；沿主线在 W14 后学习，但不以训练性能实验为 CPU Task 的技术前提。 缺项按 [基础补学入口](../../docs/prerequisites.md) 的材料、范围和练习完成；补学时间另计。

<details>
<summary>前置问题核对</summary>

两个独立 Counter 对象应各自保存计数；函数返回值和指向未来结果的引用不是同一种对象。先修 P 可补 Python 类。

</details>

资源的难度、语言、前置要求、原始 URL 和停止位置统一保存在 [资源索引](../../resources/README.md)，下文按学习顺序链接。先读必读范围，卡点材料替换复习时间，可选拓展不影响基础完成。

## 1. 把函数和状态变成 Task 与 Actor（50 分钟）

资源定位：[Task、Actor 与 ObjectRef](../../resources/README.md#r-ray-task)。

**先读**：[Task / Actor 资源卡](../../resources/README.md#r-ray-task)：Tasks 的首个 remote 函数、执行/取结果和 Passing Object References，约 30 分钟；ray.remote API 中 Foo Actor 的创建、方法调用和 get，约 20 分钟。原 walkthrough/Actors 页面本轮访问失败，使用这两份已打开的官方材料。先在纸上跟踪返回值，再修改最小示例。

**接着想一想**：把 Python 返回值与 ObjectRef 画成两种对象，标出真正等待结果的位置。Actor 用于持有状态，不能仅因语法相似就当成普通无状态函数。

**例子与图解：先理解引用，再讨论并发**

~~~text
double(3) 提交 → ObjectRef A ──作为输入依赖──→ add_one(A) 提交 → ObjectRef B
                   实际结果 6                                    结果 7
                                                               ray.get(B)
~~~

ObjectRef 是结果的引用，提交时计算可能尚未完成；顶层任务参数的对象依赖由 Ray 解析。先提交独立任务后统一收集，才能保留并发机会。Actor 是远程的有状态对象，主线只用默认同步 Actor，不讨论异步 Actor 的并发语义。

**暂停题**：同一个同步 Counter Actor 初值 0，依次加 2、加 3，取返回值应是什么？新建第二个 Counter 后读取它会得到什么？

<details>
<summary>核对答案</summary>

同一提交者按顺序调用并核对结果时，应依次得到 2、5；新对象仍为 0。给每个 Actor/Task 保存 ID，避免将不同状态对象混为一谈。先用本地 Python 类和函数生成参考值；远程正确性依赖真实输出，不能仅凭 ObjectRef 存在判定成功。

</details>

**动手练习**：写数值计算 Task 和计数 Actor，提交多个任务后收集返回；将结果与本地函数计算对齐。不要在每提交一个任务后立即等待它，从而意外串行化全部工作。

**检查结果**：能解释异步提交、等待与依赖关系，结果正确。

## 2. 资源声明限制的是什么（50 分钟）

资源定位：[逻辑资源与实际设备](../../resources/README.md#r-ray-resource)。

**先读**：[Resources](../../resources/README.md#r-ray-resource) 的 `Physical Resources and Logical Resources`、`Specifying Node Resources`，再定位 `num_cpus` / `num_gpus` 的任务声明示例。

**接着想一想**：把 W7/W11 的实际 GPU 使用与 Ray 的逻辑令牌分开。申请到 GPU 不等于限制显存占用，也不意味着 GPU 一直忙碌。

**例子与自查：资源令牌只约束调度**

单机声明 2 个逻辑 CPU，三个 Task 各声明 num_cpus=1；在没有其他资源约束且全部 ready 时，资源账本至多同时容纳两个这样的 Task。

**暂停题**：若每个 Task 内部自行开 8 个线程，Ray 的 1 个 CPU 声明是否会把它硬限制成一个线程？num_gpus=1 是否限制显存？

<details>
<summary>核对依据</summary>

不会据此进行硬 CPU 隔离或限制用户代码只能一个线程；库线程配置需单独处理。GPU 资源声明参与调度与设备可见性管理，不是显存配额，也不证明 GPU 正在计算。测并发先用 CPU 主线和显式资源设置；真实设备占用要另取观测数据，不能由逻辑 token 数推断。

</details>

**动手练习**：先用 CPU 任务与显式资源声明验证并发限制，记录开始/结束和可见设备。GPU 可用后再加一个小型计算任务，真实占用另行采样。

**检查结果**：能区分逻辑资源、设备可见性与实际占用；模拟令牌的实验明确标注为模拟。

## 3. 从排队现象得到完整事件记录（50 分钟）

资源定位：[可行性、可用性与节点选择](../../resources/README.md#r-ray-schedule)。

**先读**：[Scheduling](../../resources/README.md#r-ray-schedule) 的 `Resources`，区分 feasible、available、infeasible；再看 `Scheduling Strategies → DEFAULT`，暂不尝试所有放置策略。

**接着想一想**：W10 记录请求等待，这里记录作业等待；虽然都需要时间轴，测量对象和机制不同。Ray 的节点放置也不自动等于自己想要的 FIFO/SJF 队列策略。

**例子与自查：日志能说明什么**

| task_id | submit | start | end | status |
| --- | --- | --- | --- | --- |
| A | 0.0 | 0.2 | 0.7 | success |
| B | 0.0 | 0.3 | 0.6 | failed |

单位均为同一单机时钟的秒。A 的等待和执行时间是多少？B 能否从统计中删去？某任务要求 3 个逻辑 CPU，而所有节点容量最多 2，它是暂时忙还是不可行？

<details>
<summary>核对答案</summary>

A 等待 0.2、执行 0.5 秒；这段等待含调度/启动等开销，不能全部归因资源排队。B 保留失败类型和时间；成功吞吐与失败率分别报。3 CPU 请求在该集群配置下不可行（infeasible）；容量足够但暂被占用才是 feasible 而 unavailable。Ray 的 DEFAULT 节点策略不保证自己的 FIFO/SJF，W16 的待提交队列需单独实现。

</details>

**动手练习**：给每个任务记录 ID、资源、提交/开始/结束、结果或失败。主线单机统一时钟口径，改变资源请求与任务数，解释何时等待；保留失败记录，不能只保存成功样本。

**完成后检查**：从日志可重建等待时间与执行时间，区分资源不足和任务尚未完成；W16 将直接复用事件字段。

## 独立完成与可选 AI 帮助

三段都先遮住答案作答，再核对推导；答错保留原答案，回资源卡指定小节，用不同输入重做。每段“检查结果”连同 [单元完成标准](README.md) 都需要真实笔记或运行记录支持。纸面例子正确只能说明该例的理解，不能替代实验。记录在本单元实验目录的 notes.md，按 W15-S01～S03 分节。

可选提示词：

> 我正在学习 W15 的Task/Actor。我的推导是【粘贴】，我与本段核对说明不同的一步是【填写】。请只用本段的小例子检查这一步，给一个改变单项条件的反例，先让我回答。不要假设我做过实验，也不要用未核验的接口填补解释。

## 整理记录与可选拓展

在 `labs/07-scheduling/ray-basics/` 交付 Task/Actor 示例和事件记录器。CPU sleep 只能验证日志与排队逻辑，不能作为 GPU 利用率结论。

进阶的多 GPU 成组预留后置；本单元不实现集群级调度器。
