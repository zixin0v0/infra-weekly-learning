# W9 章节导学：分页机制与前缀复用实验

[本周范围与验收](README.md) · [导学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

资料预算：60 + 45 + 45 = 150 分钟。理论学习分页，实验测 APC；两个问题分别保留证据。

## 1. 先算容量，再理解为什么分页（60 分钟）

**先读**：[PagedAttention PDF](https://arxiv.org/pdf/2309.06180) §3、§4.1、§4.2。分别定位内存浪费、按块访问以及 KV Cache Manager，不先读全部性能评估。

**接着想一想**：从 W1 的元素字节数与 W8 的 KV 语义出发，按层数、KV 头数、head dimension 和 token 数写容量公式；GQA 使用 KV 头数，不使用 query 头数代替。

**动手练习**：给 2 个不同长度的请求画逻辑块到物理块的表，再画各增加 1 个 token 后的变化。写一个纯计算的小脚本，检查块大小与末块浪费的关系；这是容量模型，不是分配器性能复现。

**检查结果**：能区分分页改变内存管理与改变 Attention 数学定义。

## 2. 共享哪些内容，什么时候需要复制（45 分钟）

**先读**：同一论文 §4.3 的基本解码流程和 §4.4 开头的 parallel sampling / copy-on-write 案例。读到能更新块表和引用计数即可，beam search 的完整执行细节作为进阶。

**配套视频**：[CS336 Lecture 10](https://www.youtube.com/watch?v=EfM546A79aM) 配 [讲义](https://github.com/stanford-cs336/lectures/blob/main/lecture_10.py) 的 `paged_attention`，用于图解仍不清楚时，替换本段部分阅读。

**动手练习**：手工更新“相同前缀、不同续写”的块表，指出共享、分叉和释放各涉及什么。随后拟定共同前缀与独立前缀的两组输入，检查 token IDs，而不是只比较肉眼相似的文本。

**检查结果**：将论文中的共享场景与自己准备测的跨请求 APC 区分，不能直接视为完全相同的当前实现。

## 3. 把机制解释变成可证伪的 APC 对照（45 分钟）

**先读**：[Automatic Prefix Caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/) 的 `Introduction`、`Enabling APC in vLLM`、`Example workloads`。重点判断哪些重复 prefill 有机会被省下；直接作用不在新 token 的 decode 计算。

**接着想一想**：复用 W8 的模型与负载，只改变 APC、前缀复用或冷/热条件中的一个因素。先写实验矩阵，再运行；“已发过请求”不自动等于“已证实命中缓存”。

**动手练习**：分别记录首次与复用请求，确认清理方法，必要时重启服务；寻找匹配版本提供的复用指标或日志。保存实际输入长度、TTFT、TPOT 和失败数。

**完成后检查**：能说明实验支持的是前缀复用效果，不能用 APC 开关隔离 PagedAttention 分配器贡献；无命中证据时，机制归因仍标待验证。

## 课后整理与选修

在 `labs/05-serving/prefix-cache/` 保存容量脚本、块表、请求组与实验报告，交给 W10 作为一种受控场景。

卡点补充：[vLLM 作者博客](https://vllm.ai/blog/2023-06-20-vllm) 中按逻辑块/物理块说明的段落，用于补图解，历史速度数字不作目标。进阶只改变共享前缀比例，观察收益条件。
