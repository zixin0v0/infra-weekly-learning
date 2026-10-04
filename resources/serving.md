# 推理服务资料

[资料目录](README.md)

先弄清一条请求怎样完成，再比较更多请求一起到达时的表现。这里登记 token、服务、缓存与指标的来源，具体观看和操作顺序在对应 W 小节。

<a id="r-inference"></a>

### R-INFERENCE · prefill、decode 与请求延迟

W8-S01 必读；中等；英文；W4 Roofline、W6 Attention。

**来源**：[CS336 lecture_10.py](https://github.com/stanford-cs336/lectures/blob/main/lecture_10.py)；[Scaling Book Inference](https://jax-ml.github.io/scaling-book/inference/)。

**读到哪里**：讲义 review_transformer、arithmetic_intensity_of_inference、throughput_and_latency，60 分钟。书的 The Basics of Transformer Inference、What do we actually want to optimize? 仅卡点替换 20 分钟；量化、投机、多加速器后置。

**带着什么问题读**：复用算术强度解释两个阶段；从本地假设时间戳算 TTFT/TPOT，不能拿 GPU 延迟当请求延迟。 [打开练习与自查](../weeks/week-08-serving-baseline/README.md)。

**视频入口**：[CS336 Lecture 10](https://www.youtube.com/watch?v=EfM546A79aM)。用对应讲义函数定位并替换相同主题的阅读时间，分钟位置未核验。W9 共享机制图解卡住时，可查同讲义 paged_attention，替换 15 分钟复习，不重复 W8 推理开篇。

<a id="r-token"></a>

### R-TOKEN · token、模板与请求格式

W8-S01/S02 必读；入门；英文；Python 字典与字符串。

**来源**：[HF Tokenization algorithms](https://huggingface.co/docs/transformers/main/en/tokenizer_summary)；[vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)。

**读到哪里**：HF 页开头的 subword 例子及 BPE 最初合并示例，15 分钟；Quickstart 的请求 JSON 中 model/prompt 或 messages、max_tokens 字段，15 分钟，合计 30 分钟，已含在对应小节阅读安排里。不训练 tokenizer；其他算法后置。

**带着什么问题读**：补齐“字符数不等于 token 数”；结合服务请求路径核对模板、返回状态与实际生成长度。 [打开练习与自查](../weeks/week-08-serving-baseline/README.md)。

<a id="r-serving"></a>

### R-SERVING · 单卡在线服务

W8-S02 必读；中等；英文；R-TOKEN、Linux 环境。

**来源**：[vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)。

**读到哪里**：Online Serving → Completions 或 Chat Completions 二选一，45 分钟；停止于一条可追溯请求，不把 Offline Batched Inference 算作在线基线。启动模型名是示例，实际选择与 revision 要自己记录。

**带着什么问题读**：先 3～5 条固定请求检查输出再压测，实际启动结果记录在自己的实验目录。 [打开练习与自查](../weeks/week-08-serving-baseline/README.md)。

<a id="r-bench"></a>

### R-BENCH · 负载、明细和统计字段

W8-S03/W10-S01 必读；中等；英文；已理解请求路径。

**来源**：[vllm bench serve](https://docs.vllm.ai/en/latest/cli/bench/serve/)。

**读到哪里**：W8 45 分钟：num-prompts、request-rate、max-concurrency、num-warmups、save-result、save-detailed、result-dir；长度只查所选 dataset 参数组。W10 45 分钟：burstiness、percentile-metrics、metric-percentiles、goodput；旧字段回查不重读。

**带着什么问题读**：固定工作负载并保存失败；W10 做两个单因素扫描。CLI goodput 与本地定义先核对再比较。 [打开练习与自查](../weeks/week-10-serving-benchmark/README.md)。

<a id="r-paged"></a>

### R-PAGED · KV 容量、分页和共享

W9-S01/S02 必读；进阶起步；英文论文；W8 与字节账本。

**来源**：[PagedAttention PDF](https://arxiv.org/pdf/2309.06180)；[作者博客图解](https://vllm.ai/blog/2023-06-20-vllm)。

**读到哪里**：S01：论文 §3、§4.1～4.2，60 分钟；S02：§4.3、§4.4 开头 parallel sampling/copy-on-write，45 分钟。博客块映射图只作卡点替换 15 分钟；停在基本共享，不读完整 beam search 或性能评估。

**带着什么问题读**：先本地两请求块表，再追论文；APC 开关实验不能隔离分页分配器贡献。 [打开练习与自查](../weeks/week-09-kv-cache/README.md)。

<a id="r-apc"></a>

### R-APC · 前缀复用的条件与限制

W9-S03 必读；中等；英文；KV 块表、W8 基线。

**来源**：[Automatic Prefix Caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/)。

**读到哪里**：Introduction、Enabling APC in vLLM、Example workloads、Limits，45 分钟；跳过 Hybrid Mamba 专项。当前接口在实际开始学习时按安装版本核对。

**带着什么问题读**：构造 token 前缀一致/不同、冷/热、开/关对照；把重复 prefill 的直接作用与其他指标变化分开。 [打开练习与自查](../weeks/week-09-kv-cache/README.md)。

<a id="r-batching"></a>

### R-BATCHING · continuous batching 与 chunked prefill

W10-S02 必读；中等；英文；W8/W9。

**来源**：[CS336 lecture_10.py](https://github.com/stanford-cs336/lectures/blob/main/lecture_10.py)；[vLLM Optimization](https://docs.vllm.ai/en/latest/configuration/optimization/)。

**读到哪里**：讲义 continuous_batching 15 分钟；文档 Chunked Prefill、Performance Tuning with Chunked Prefill 45 分钟。停在 max_num_batched_tokens 的含义，不加入量化/多卡配置。

**带着什么问题读**：一张逐轮调度表区分请求集合变化与长 prefill 拆分；选一个预算变量对照默认值。 [打开练习与自查](../weeks/week-10-serving-benchmark/README.md)。

<a id="r-metrics"></a>

### R-METRICS · 服务状态与有效吞吐

W10-S03 必读，W9 命中证据查阅；中等；英文；M4、R-BENCH。

**来源**：[Production Metrics](https://docs.vllm.ai/en/latest/usage/metrics/)。

**读到哪里**：General Metrics：num_requests_running、num_requests_waiting、prefix_cache_hits/queries 及延迟项，45 分钟。停止于本机实际存在的字段；不要求部署 Prometheus。缓存计数当前按 token，不直接当请求命中率。

**带着什么问题读**：从成功且满足阈值的请求重算 goodput；累计计数用同窗口增量，未暴露字段记缺失。 [打开练习与自查](../weeks/week-10-serving-benchmark/README.md)。
