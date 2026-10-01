# W8 章节导学：推理阶段、请求路径与测量基线

[本周范围与验收](README.md) · [导学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

资料预算：60 + 45 + 45 = 150 分钟。先单卡、单模型、单请求，再扩大并发。

## 1. prefill 和 decode 为什么资源特征不同（60 分钟）

**先看/读**：[CS336 Lecture 10](https://www.youtube.com/watch?v=EfM546A79aM)，配 [lecture_10.py](https://github.com/stanford-cs336/lectures/blob/main/lecture_10.py) 的 `review_transformer`、`arithmetic_intensity_of_inference`、`throughput_and_latency`。量化、推测解码先跳过。

**接着想一想**：回 W4 的 GEMM 账本，分别写提示词处理和生成一个新 token 时的矩阵形状；用 W6 的 Attention 结构说明 KV Cache 保存的对象。

**卡点补充**：[Scaling Book Part 7](https://jax-ml.github.io/scaling-book/inference/) 的 `The Basics of Transformer Inference` 与 `What do we actually want to optimize?`，替换 20 分钟视频；不进入多加速器部署章节。

**动手练习**：画单请求的发送、首 token、后续 token、结束时间轴；用几个假设时间戳手算 TTFT、TPOT 和端到端延迟，写明不足 2 个输出 token 的处理。

**检查结果**：区分请求延迟、GPU kernel 延迟与输出吞吐，不将“生成更快”当成未定义指标。

## 2. 从模型文件走到一个可追溯请求（45 分钟）

**先读**：[vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/) 的 `Online Serving`，再选其下 Completions 或 Chat Completions API 的一个请求示例。主线只选一种端点；离线批推理不是同一个服务基线。

**接着想一想**：把 endpoint、模型名、tokenizer、chat template 放到第一段的请求路径图上，标出哪些步骤发生在客户端、服务端和 GPU。

**动手练习**：选择能留出缓存余量的小模型，记录 revision、dtype 和完整配置；发一条请求核对返回内容及真实 token 长度。先确认功能，再写压测配置。

**检查结果**：服务可以重复启动，相同请求构造可重建，加载与预热时间有单独记录。

## 3. 给基线限定负载和统计窗口（45 分钟）

**先读**：[vllm bench serve 参数文档](https://docs.vllm.ai/en/latest/cli/bench/serve/) 中 `--num-prompts`、`--request-rate`、`--max-concurrency`、`--save-result`、`--save-detailed` 和输出目录项；长度参数阅读自己选定的数据集对应组，不默认所有组使用相同参数。

**接着想一想**：负载参数控制请求如何进入时间轴，实际发送和完成时间用于核对它们是否真正达到配置值。在线文档与本机版本不一致时，以匹配版本的帮助和文档为准。

**动手练习**：固定一组长度、采样策略和到达率，做少量并发点；保存成功/失败数、真实长度、测量窗口、TTFT/TPOT 和输出 tokens/s。W10 再做系统扫描，本周不扩充大网格。

**完成后检查**：可以从原始记录说明一个图中每个点的来源；小样本分位数标为探索结果。

## 课后整理与选修

在 `labs/05-serving/baseline/` 保存配置、请求构造、数据与报告。W9 复用同一服务做 APC 实验，W10 再统一项目入口。

进阶选择一组更长输入，先用资源模型预测影响；模型更换、量化和多卡推理留到后续，避免同时改变多个因素。
