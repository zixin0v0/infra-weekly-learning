# W9 第 1 段：每增加一个 token，KV 要多占多少空间？

[本单元](README.md) · [课程目录](../../course/README.md)

模型权重在请求之间通常不变，KV 却随着每条序列增长。先数清到底存了多少 Key 和 Value，再理解按块分配为何能减少预留浪费。

## 视频与正文

先看 [CS336 2026 Lecture 10 · Inference](https://www.youtube.com/watch?v=EfM546A79aM)：KV Cache 与 paged attention；暂停按层数、token 数、KV heads 和 dtype 计算容量。

视频分钟位置待核验；下列章节或函数用于正文定位，也可以直接按正文完成练习。

## 中文补充（按需）

NVIDIA 中文[推理优化](https://developer.nvidia.cn/blog/mastering-llm-techniques-inference-optimization/)看 KV cache 与“LLM 内存要求”的说明，把层数、序列长度和缓存元素联系起来；指定文字已预读。文章偏标准多头注意力，GQA/MQA 要按本课实际 KV head 数计算，不能机械用 query head 数。它补概念，不替代本页容量账本。[范围与版本](../../resources/serving.md#cn-inference)。

## 开始前

完成 W8 的 token 与 KV 解释，能用 W1 的元素数乘字节数计量；query heads 与 KV heads 必须分清。

资源定位：[KV 容量、分页和共享](../../resources/serving.md#r-paged)。

**先读**：[PagedAttention PDF](../../resources/serving.md#r-paged) §3、§4.1、§4.2。分别定位内存浪费、按块访问以及 KV Cache Manager，不先读全部性能评估。

**接着想一想**：从 W1 的元素字节数与 W8 的 KV 语义出发，按层数、KV 头数、head dimension 和 token 数写容量公式；GQA 使用 KV 头数，不使用 query 头数代替。

## 从一个位置数到所有层

每个缓存位置在每层都要保存 Key 和 Value。先乘 KV 头数和每头维度，得到一份 K 的元素数；乘 2 加上 V，再乘层数、缓存长度和 dtype 字节数。分组查询注意力（GQA）可以让多个 query heads 使用较少的 KV heads，因此不能直接用 query 头数代替。

分页把序列切成固定容量的逻辑块，再用块表定位物理块。逻辑上的相邻 token 不必占据一整段预留到最大长度的空间；但最后一块可能没填满，块表本身也需要元数据。下一段的[块表图](session-02.md)会追踪两条请求怎样共享前缀。

**例子与图解：先算容量，再读分页论文**

单请求 KV 数据字节为 2×层数 L×KV heads×head_dim×缓存 token 数 S×每元素字节；2 对应 K 与 V。暂不计元数据、padding、量化 scale 或其他缓冲。这个公式描述存储对象，不是服务进程全部显存。

| 手算项 | 值 |
| --- | --- |
| L、KV heads、head_dim | 2、2、4 |
| S、dtype | 5、FP16（2 字节） |
| 有效 KV 字节 | 2×2×2×4×5×2 = 320 |
| 每块 4 token，需 2 块 | 容量 8 token，共 512 字节 |
| 尾块暂未用容量 | 3 token，共 192 字节 |

**暂停题**：若 query heads 从 2 改成 4，但 KV heads 仍为 2，上表有效 KV 是否翻倍？为什么不用申请一个最大序列的连续大区域？

<details>
<summary>核对依据</summary>

不会因 query heads 单独改变而翻倍；公式使用 KV heads。分页让逻辑连续序列映射到可分散的物理块，按增长分配并减少大区域预留浪费；不能因此声称没有尾块碎片或任何元数据成本。

</details>

**动手练习**：给 2 个不同长度的请求画逻辑块到物理块的表，再画各增加 1 个 token 后的变化。写一个纯计算的小脚本，检查块大小与末块浪费的关系；这是容量模型，不是分配器性能复现。

**检查结果**：能区分分页改变内存管理与改变 Attention 数学定义。

## 完成后

把代码、预测与实际结果记在同一份笔记中。完成本段检查后，沿下方链接继续。

[上一课](README.md) · [下一课](session-02.md)
