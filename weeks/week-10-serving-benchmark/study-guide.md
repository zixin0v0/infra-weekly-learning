# W10 分段学习指南：负载、批处理与有效吞吐

[本周范围与验收](README.md) · [自学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

原文选读预算：45 + 60 + 45 = 150 分钟；本地例子与自查另计 60 分钟，动手与正确性检查 270 分钟。含资料复核、分析和报告，本单元约 11 小时，详见 [时间表](../../docs/study-guide.md#time-budget)。

## 学习目标与前置检查

本单元知识点：到达负载、批处理预算、分位数、goodput、观测。学完应当能保存请求明细，做两个单因素扫描，并用指标解释一次配置变化。

**开始前检查**：通过 W8/W9，完成先修 M4。能区分请求率和并发数，知道缓存开关会影响负载条件。 缺项按 [基础补学入口](../../docs/prerequisites.md) 的材料、范围和练习完成；补学时间另计。

<details>
<summary>前置问题核对</summary>

请求率单位 req/s，并发是未完成请求的数量上限；并发限制触顶时实际发送速率可能低于计划。

</details>

资源的难度、语言、前置要求、原始 URL 和停止位置统一保存在 [资源索引](../../resources/README.md)，下文按学习顺序链接。先读必读范围，卡点材料替换复习时间，可选拓展不影响基础完成。

## 1. 计划到达率和真正进入服务的速率（45 分钟）

资源定位：[负载、明细和统计字段](../../resources/README.md#r-bench)。

**先读**：[bench serve](../../resources/README.md#r-bench) 的 `--request-rate`、`--burstiness`、`--max-concurrency`；统计部分看 `--percentile-metrics`、`--metric-percentiles`、`--goodput`。每个参数先核对安装版本，再写入配置。

**接着想一想**：把 W8 时间轴扩成多请求图。预定发送、真实发送与服务完成可能有不同速率；并发上限会使负载发生变化，不能仅凭配置标签称为固定到达率实验。

**例子与图解：负载参数有不同职责**

~~~text
计划到达 → 客户端并发门限 → 实际发出 → 服务端等待 → 执行 → 完成
                ↑                                      ↓
                └─────────── 释放并发名额 ──────────────┘
~~~

**暂停题**：设置每秒 20 个请求、并发上限 2，单请求约 1 秒，能否仅凭配置声称服务器收到 20 req/s？

<details>
<summary>核对依据</summary>

不能。在这个简化稳定例子里，两份名额约每秒只允许完成 2 个请求；客户端可能等待、积压或按工具规则限制发送。保存计划/实际发送时间、并发触顶与失败记录。固定随机种子与轨迹，先改长度分布，再单独改到达强度，避免一起变动后归因。

</details>

**动手练习**：第一组固定上限扫至少 3 个计划到达率；第二组固定计划到达率扫至少 3 个上限。保留实际发送、测量窗口、完成/失败数，检查是否触顶。

**检查结果**：能说清每组实验控制了什么、实际观测又是什么，图例不将二者混写。

## 2. 在什么地方混合 prefill 与 decode（60 分钟）

资源定位：[continuous batching 与 chunked prefill](../../resources/README.md#r-batching)。

**先看/读**：[CS336 Lecture 10](../../resources/README.md#r-inference) 配 [讲义](../../resources/README.md#r-inference) 的 `continuous_batching`，用约 15 分钟画请求加入/退出 batch 的过程。

**立即联读**：[vLLM Optimization](../../resources/README.md#r-batching) 的 `Chunked Prefill` 与 `Performance Tuning with Chunked Prefill`，重点读 token 预算与延迟权衡。不要将 continuous batching 与 chunked prefill 当成同义词。

**例子与图解：token 预算如何分给不同阶段**

假设一轮调度允许处理 8 个 token，已有两个 decode 请求各需一个新位置，剩余一个请求还有 10 个 prefill token。这里只演示预算分配，不是吞吐预测。

| 本轮 | decode token | prefill token | 剩余 prefill |
| --- | --- | --- | --- |
| 第 1 轮 | 2 | 6 | 4 |
| 第 2 轮（仍有两条 decode） | 2 | 4 | 0 |

continuous batching 让完成请求离开、待处理请求加入；chunked prefill 将长输入拆开，与 decode 共同安排。实际规则还受序列数、KV 容量和版本配置约束。

**暂停题**：把 max_num_batched_tokens 增大，是否保证 TTFT 和 TPOT 同时下降？

<details>
<summary>核对依据</summary>

不能保证。更大 prefill 块可能帮助长输入更快完成，同时延长 decode 等待；也可能改变计算效率。先固定负载与缓存条件，只改变一个配置，再对比 TTFT/TPOT、吞吐、失败与时间线。表中的 token 个数是调度工作量，不是相同计算成本。

</details>

**动手练习**：在第一段的一个代表负载点，只改变一个经版本核对的 token batching/prefill 预算参数。先写对 TTFT/TPOT 的预测，再保留默认值和改动值两组结果；不假定任何机制都有独立关闭开关。

**检查结果**：能指出修改影响了调度过程的哪一步；负结果也保留，不只挑最快点。

## 3. 将客户端尾延迟与服务端状态对应（45 分钟）

资源定位：[服务状态与有效吞吐](../../resources/README.md#r-metrics)。

**先读**：[Production Metrics](../../resources/README.md#r-metrics) 的 `General Metrics` 表，定位 `vllm:num_requests_running`、`vllm:num_requests_waiting`，然后查当前版本的缓存与延迟指标。表中存在不代表本机已暴露，运行时保存实际可用字段。

**接着想一想**：等待队列增加可能帮助解释 TTFT，但单个相关曲线不构成因果证明。检查压测端 CPU、tokenization、连接与网络路径；客户端瓶颈也会改变负载。

**例子与自查：有效吞吐和缓存计数**

10 秒窗口有 4 个请求，3 个成功，其中 2 个同时满足预先写下的 TTFT≤0.5 秒、TPOT≤0.1 秒。计算成功吞吐和 goodput。若前后两次采样的 prefix cache hits 为 100/160、queries 为 200/300，窗口命中率是多少？

<details>
<summary>核对答案</summary>

成功吞吐 3/10=0.3 req/s，goodput 2/10=0.2 req/s，失败数 1。阈值应在测量前指定，不能看完结果再挑。当前所选 vLLM 指标以查询/命中的 token 计数，窗口比率为 (160−100)/(300−200)=60%；不是简单用累计 160/300，也不是请求命中率。重启、计数器重置或零分母时单列，不计算无意义比率。对照实际版本的名称与单位。

</details>

**动手练习**：预先选定 TTFT/TPOT 阈值，以“成功且满足全部阈值的请求数 / 测量窗口”定义本实验请求有效吞吐；与 CLI 的 goodput 口径核对，不一致则分开报告。保留样本数和测量区间。

**完成后检查**：p50/p95、输出吞吐、成功率与有效吞吐来自相同可追溯数据；TPOT 与逐 token ITL 不互相替代。

## 独立完成与可选 AI 帮助

三段都先遮住答案作答，再核对推导；答错保留原答案，回资源卡指定小节，用不同输入重做。每段“检查结果”连同 [单元完成标准](README.md) 都需要真实笔记或运行记录支持。纸面例子正确只能说明该例的理解，不能替代实验。记录在本单元实验目录的 notes.md，按 W10-S01～S03 分节。

可选提示词：

> 我正在学习 W10 的到达负载。我的推导是【粘贴】，我与本段核对说明不同的一步是【填写】。请只用本段的小例子检查这一步，给一个改变单项条件的反例，先让我回答。不要假设我做过实验，也不要用未核验的接口填补解释。

## 整理记录与可选拓展

整合 `projects/mini-serving-benchmark/`：配置、请求构造、运行入口、原始数据、汇总图、结论与限制。代码引用 W8/W9 的实现，避免多份脚本漂移。

进阶只选长输入或混合长度负载之一。跨框架比较放在同框架对照完成后，不能用整体速度差直接证明某一个机制的贡献。
