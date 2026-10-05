# W10 第 2 段：一轮能处理八个 token，应该怎样分给请求？

[本单元](README.md) · [课程目录](../../course/README.md)

长提示词的 prefill 与正在生成的 decode 都需要计算资源。把一轮预算扩大，可能有利于一类请求，却让另一类请求多等一会儿；先弄清预算分给了谁。

## 视频与正文

主要阅读下列正文与图解。视频范围待核验；已看懂的重复内容只需回查。

## 中文补充（按需）

NVIDIA 中文[推理优化](https://developer.nvidia.cn/blog/mastering-llm-techniques-inference-optimization/)只读“动态批处理”，理解一个请求结束后，为什么可以在生成过程中加入另一个请求；指定文字已预读。文中该段讲 continuous/in-flight batching，不应泛化为所有“动态批处理”。chunked prefill 切开的是输入处理，这篇未充分覆盖，仍按原课区分两种动作。[范围与版本](../../resources/serving.md#cn-inference)。

## 开始前

先区分计划与实际负载，再回看 [W8 的 prefill/decode 形状](../week-08-serving-baseline/session-01.md)。

资源定位：[continuous batching 与 chunked prefill](../../resources/serving.md#r-batching)。

**先看/读**：[CS336 Lecture 10](../../resources/serving.md#r-inference) 配 [讲义](../../resources/serving.md#r-inference) 的 `continuous_batching`，用约 15 分钟画请求加入/退出 batch 的过程。

**立即联读**：[vLLM Optimization](../../resources/serving.md#r-batching) 的 `Chunked Prefill` 与 `Performance Tuning with Chunked Prefill`，重点读 token 预算与延迟权衡。不要将 continuous batching 与 chunked prefill 当成同义词。

## 加入 batch 与切开 prefill，是两个动作

**连续批处理（continuous batching）**允许完成的请求退出、新的请求加入，避免整批都等最慢者结束。**分块预填充（chunked prefill）**把长提示词拆成多轮处理，让它有机会与 decode 共同安排。前者改变批次成员，后者改变一个长输入的处理粒度。

一个 token 的调度计数不等于固定计算成本：它属于 prefill 还是 decode，已有 KV 多长，都会影响执行。因此先手推下表的预算，再测 TTFT、TPOT 与吞吐，不能从“每轮 token 更多”直接推出所有请求都更快。

对照[W8 的两阶段形状图](../week-08-serving-baseline/session-01.md)，先确认哪些位置是新 prefill，哪些位置正在 decode。下表只分配位置数，不把两种位置的计算成本画成等长时间块。

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

## 完成后

把代码、预测与实际结果记在同一份笔记中。完成本段检查后，沿下方链接继续。

[上一课](session-01.md) · [下一课](session-03.md)
