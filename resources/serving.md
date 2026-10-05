# 推理服务资料

[资料目录](README.md)

先弄清一条请求怎样完成，再比较更多请求一起到达时的表现。这里登记 token、服务、缓存与指标的来源，具体观看和操作顺序在对应 W 小节。

<a id="r-inference"></a>

### R-INFERENCE · prefill、decode 与请求延迟

**中文补充（按需，部分）：** 中文 prefill/decode 与缓存；算术强度仍按原讲义。 [对应范围](#cn-inference)。

W8-S01 必读；中等；英文；W4 Roofline、W6 Attention。

**来源**：[CS336 lecture_10.py](https://github.com/stanford-cs336/lectures/blob/main/lecture_10.py)；[Scaling Book Inference](https://jax-ml.github.io/scaling-book/inference/)。

**读到哪里**：讲义 review_transformer、arithmetic_intensity_of_inference、throughput_and_latency，60 分钟。书的 The Basics of Transformer Inference、What do we actually want to optimize? 仅卡点替换 20 分钟；量化、投机、多加速器后置。

**带着什么问题读**：复用算术强度解释两个阶段；从本地假设时间戳算 TTFT/TPOT，不能拿 GPU 延迟当请求延迟。 [打开练习与自查](../weeks/week-08-serving-baseline/README.md)。

**视频入口**：[CS336 Lecture 10](https://www.youtube.com/watch?v=EfM546A79aM)。用对应讲义函数定位并替换相同主题的阅读时间，分钟位置未核验。W9 共享机制图解卡住时，可查同讲义 paged_attention，替换 15 分钟复习，不重复 W8 推理开篇。

<a id="r-token"></a>

### R-TOKEN · token、模板与请求格式

**中文补充（按需，暂缺）：** BPE 合并、聊天模板与当前请求字段没有完整中文对应。 [对应范围](#cn-serving-gaps)。

W8-S01/S02 必读；入门；英文；Python 字典与字符串。

**来源**：[HF Tokenization algorithms](https://huggingface.co/docs/transformers/main/en/tokenizer_summary)；[vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)。

**读到哪里**：HF 页开头的 subword 例子及 BPE 最初合并示例，15 分钟；Quickstart 的请求 JSON 中 model/prompt 或 messages、max_tokens 字段，15 分钟，合计 30 分钟，已含在对应小节阅读安排里。不训练 tokenizer；其他算法后置。

**带着什么问题读**：补齐“字符数不等于 token 数”；结合服务请求路径核对模板、返回状态与实际生成长度。 [打开练习与自查](../weeks/week-08-serving-baseline/README.md)。

<a id="r-serving"></a>

### R-SERVING · 单卡在线服务

**中文补充（按需，部分）：** 中文 HTTP 解释请求路径；vLLM 当前启动与服务接口仍查原文。 [对应范围](#cn-http)。

W8-S02 必读；中等；英文；R-TOKEN、Linux 环境。

**来源**：[vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)。

**读到哪里**：Online Serving → Completions 或 Chat Completions 二选一，45 分钟；停止于一条可追溯请求，不把 Offline Batched Inference 算作在线基线。启动模型名是示例，实际选择与 revision 要自己记录。

**带着什么问题读**：先 3～5 条固定请求检查输出再压测，实际启动结果记录在自己的实验目录。 [打开练习与自查](../weeks/week-08-serving-baseline/README.md)。

<a id="r-bench"></a>

### R-BENCH · 负载、明细和统计字段

**中文补充（按需，部分）：** 中文 TTFT/吞吐/ITL 定义；当前 bench 参数未覆盖。 [对应范围](#cn-metrics)。

W8-S03/W10-S01 必读；中等；英文；已理解请求路径。

**来源**：[vllm bench serve](https://docs.vllm.ai/en/latest/cli/bench/serve/)。

**读到哪里**：W8 45 分钟：num-prompts、request-rate、max-concurrency、num-warmups、save-result、save-detailed、result-dir；长度只查所选 dataset 参数组。W10 45 分钟：burstiness、percentile-metrics、metric-percentiles、goodput；旧字段回查不重读。

**带着什么问题读**：固定工作负载并保存失败；W10 做两个单因素扫描。CLI goodput 与本地定义先核对再比较。 [打开练习与自查](../weeks/week-10-serving-benchmark/README.md)。

<a id="r-paged"></a>

### R-PAGED · KV 容量、分页和共享

**中文补充（按需，部分）：** 中文 KV/分页动机；块表共享、写时复制仍按原论文。 [对应范围](#cn-inference)。

W9-S01/S02 必读；进阶起步；英文论文；W8 与字节账本。

**来源**：[PagedAttention PDF](https://arxiv.org/pdf/2309.06180)；[作者博客图解](https://vllm.ai/blog/2023-06-20-vllm)。

**读到哪里**：S01：论文 §3、§4.1～4.2，60 分钟；S02：§4.3、§4.4 开头 parallel sampling/copy-on-write，45 分钟。博客块映射图只作卡点替换 15 分钟；停在基本共享，不读完整 beam search 或性能评估。

**带着什么问题读**：先本地两请求块表，再追论文；APC 开关实验不能隔离分页分配器贡献。 [打开练习与自查](../weeks/week-09-kv-cache/README.md)。

<a id="r-apc"></a>

### R-APC · 前缀复用的条件与限制

**中文补充（按需，暂缺）：** 当前 APC 接口、缓存键与命中计数缺匹配中文材料。 [对应范围](#cn-serving-gaps)。

W9-S03 必读；中等；英文；KV 块表、W8 基线。

**来源**：[Automatic Prefix Caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/)。

**读到哪里**：Introduction、Enabling APC in vLLM、Example workloads、Limits，45 分钟；跳过 Hybrid Mamba 专项。当前接口在实际开始学习时按安装版本核对。

**带着什么问题读**：构造 token 前缀一致/不同、冷/热、开/关对照；把重复 prefill 的直接作用与其他指标变化分开。 [打开练习与自查](../weeks/week-09-kv-cache/README.md)。

<a id="r-batching"></a>

### R-BATCHING · continuous batching 与 chunked prefill

**中文补充（按需，部分）：** 中文 continuous batching 动机；chunked prefill 预算仍查原文。 [对应范围](#cn-inference)。

W10-S02 必读；中等；英文；W8/W9。

**来源**：[CS336 lecture_10.py](https://github.com/stanford-cs336/lectures/blob/main/lecture_10.py)；[vLLM Optimization](https://docs.vllm.ai/en/latest/configuration/optimization/)。

**读到哪里**：讲义 continuous_batching 15 分钟；文档 Chunked Prefill、Performance Tuning with Chunked Prefill 45 分钟。停在 max_num_batched_tokens 的含义，不加入量化/多卡配置。

**带着什么问题读**：一张逐轮调度表区分请求集合变化与长 prefill 拆分；选一个预算变量对照默认值。 [打开练习与自查](../weeks/week-10-serving-benchmark/README.md)。

<a id="r-metrics"></a>

### R-METRICS · 服务状态与有效吞吐

**中文补充（按需，部分）：** 概念指标有中文解释；当前字段、缓存单位及 goodput 不在补充范围。 [对应范围](#cn-metrics)。

W10-S03 必读，W9 命中证据查阅；中等；英文；M4、R-BENCH。

**来源**：[Production Metrics](https://docs.vllm.ai/en/latest/usage/metrics/)。

**读到哪里**：General Metrics：num_requests_running、num_requests_waiting、prefix_cache_hits/queries 及延迟项，45 分钟。停止于本机实际存在的字段；不要求部署 Prometheus。缓存计数当前按 token，不直接当请求命中率。

**带着什么问题读**：从成功且满足阈值的请求重算 goodput；累计计数用同窗口增量，未暴露字段记缺失。 [打开练习与自查](../weeks/week-10-serving-benchmark/README.md)。

## 中文补充：沿着请求、缓存和排队阅读

<a id="cn-inference"></a>

### CN-Inference：同一篇文章分三次用

**来源与关系：** NVIDIA / Shashank Verma、Neal Vaidya，2023-11-17 [掌握 LLM 技术：推理优化](https://developer.nvidia.cn/blog/mastering-llm-techniques-inference-optimization/)，NVIDIA 发布的中文版本，作为 CS336 推理内容的同主题补充。

| 当前内容 | 只看这些小节 | 看完回原课做什么 |
| --- | --- | --- |
| W8 第一段 | “了解 LLM 推理”至“键值缓存” | 画 prefill/decode 输入形状和请求时间线 |
| W9 第一/二段 | “键值缓存”“LLM 内存需求”“通过分页有效管理 KV 缓存” | 算 KV 字节与末块浪费，追踪块表 |
| W10 第二段 | “批处理”和“模型服务技术 → 动态批处理” | 对照固定 batch 与按迭代加入/退出的请求 |

**准备状态与边界：** 指定文字已预读，图只用于辅助定位，未复现作者结果。“一个 token 约四个英文字符”不是中文文本计数规则；prefill 是否算力受限也取决于形状。KV 公式里的 heads 在 GQA 中必须用 KV head 数。文中“动态批处理”这一节描述的是 continuous/in-flight batching，不是等待凑批的通用定义。文章没有覆盖 copy-on-write 全过程、APC 命中实验或 chunked prefill，相关英文范围保留。量化、蒸馏与推测解码跳过。

<a id="cn-http"></a>

### CN-HTTP：看懂请求和响应各有哪些字段

**中文正文：** MDN 社区译文 [HTTP 概述](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Overview)的“基于 HTTP 的系统的组成”“HTTP 流”“HTTP 报文”，到响应字段结束。与 S2 的英文页面直接对应；先读客户端/服务端，再把本课请求里的方法、路径、头和 JSON 标出来。

指定正文已预读。只用 HTTP/1.1 示例，译文将 QUIC 描述为实验的旧背景不适用于现在。MDN 不解释模型名、聊天模板、token 或 vLLM 启动选项，这些仍按 R-TOKEN/R-SERVING。

<a id="cn-docker"></a>

### CN-Docker：镜像跑起来以后，什么会留下来

**中文图文：** 杨保华、戴王剑及社区维护的《Docker — 从入门到实践》[2.2 容器](https://yeasy.gitbook.io/docker_practice/di-yi-bu-fen-ru-men-pian/02_basic_concept/2.2_container)，看 2.2.1～2.2.6 的镜像/实例、进程、可写层和生命周期；需要持久化时接[8.1 数据卷](training.md#cn-storage)。

这是中文社区教程，不是 Docker Get Started 逐字译文。上述概念文字已预读；站点部分命令块依赖网页渲染，本次未将其作为已核验命令。S3 继续使用本仓库已有 Docker 操作。容器隔离不是绝对互不影响，端口映射与健康检查也不能从“运行中”推断。暂缺已核验到具体分集的中文视频。

<a id="cn-metrics"></a>

### CN-Metrics：先说明时间从哪里开始

**中文正文：** NVIDIA / David Yastremsky 等，2024-08-01 [使用 NVIDIA GenAI-Perf 和 OpenAI 兼容 API 测量生成式 AI 模型性能](https://developer.nvidia.cn/blog/measuring-generative-ai-model-performance-using-nvidia-genai-perf-and-an-openai-compatible-api/)，只读开头的 TTFT、输出 token 吞吐与 token 间延迟，到“介绍 GenAI-Perf”前。适合 W8 第三段、W10 第一/三段作为术语对照。

这是 NVIDIA 发布的中文版本，指定正文已预读，不要求安装另一套压测工具。文章的响应间隔可能按一次响应包含的 token 数归一化；本课平均 TPOT 与逐 token ITL 必须按原始事件分别计算。p95、失败请求分母、goodput、Prometheus 字段与 vLLM 命令仍以原课约定和当前英文接口为准。

<a id="cn-serving-gaps"></a>

### 仍缺哪些中文对应

尚未选到能准确对应当前版本的 **APC 开关/计数、聊天模板/BPE、vLLM bench serve 全部选项、chunked prefill、日志与 trace 关联** 的中文视频或正文。W9 第三段不要拿分页概念文替代 APC 操作；遇到这些卡点，继续用当前课页的中文算例与原英文来源。中文文档镜像的域名不能证明其为 vLLM 官方译文，未确认来源和版本的镜像未纳入推荐。
