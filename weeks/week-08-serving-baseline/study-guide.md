# W8 分段学习指南：推理阶段、请求路径与测量基线

[本周范围与验收](README.md) · [自学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

原文选读预算：75 + 60 + 45 = 180 分钟；本地例子与自查另计 60 分钟，动手与正确性检查 270 分钟。含资料复核、分析和报告，本单元约 11.5 小时，详见 [时间表](../../docs/study-guide.md#time-budget)。

## 学习目标与前置检查

本单元知识点：token 与模板、prefill/decode、HTTP 请求、TTFT/TPOT。学完应当能重建单请求路径，启动一项可复现服务，并解释固定负载下的延迟与吞吐。

**开始前检查**：通过 W6，复用 W4 的资源计算；W7 多卡不是硬依赖。完成先修 P/A；不默认已懂 tokenizer 或 HTTP，本单元前两段补齐。 缺项按 [基础补学入口](../../docs/prerequisites.md) 的材料、范围和练习完成；补学时间另计。

<details>
<summary>前置问题核对</summary>

能写出 Attention 的 KV 对象及脚本 JSON 输入输出即可；网络请求、token 和模板按下方例子学习。

</details>

资源的难度、语言、前置要求、原始 URL 和停止位置统一保存在 [资源索引](../../resources/README.md)，下文按学习顺序链接。先读必读范围，卡点材料替换复习时间，可选拓展不影响基础完成。

## 1. prefill 和 decode 为什么资源特征不同（75 分钟）

资源定位：[prefill、decode 与请求延迟](../../resources/README.md#r-inference) → [token、模板与请求格式](../../resources/README.md#r-token)。

**先看/读**：[CS336 Lecture 10](../../resources/README.md#r-inference)，配 [lecture_10.py](../../resources/README.md#r-inference) 的 `review_transformer`、`arithmetic_intensity_of_inference`、`throughput_and_latency`。量化、推测解码先跳过。

先用 15 分钟读 [token 与模板](../../resources/README.md#r-token) 的 tokenizer 开篇和 BPE 小例子，再用 60 分钟读推理讲义；第二段用 15 分钟阅读请求 JSON 字段，再用 45 分钟读服务教程。

**接着想一想**：回 W4 的 GEMM 账本，分别写提示词处理和生成一个新 token 时的矩阵形状；用 W6 的 Attention 结构说明 KV Cache 保存的对象。

**卡点补充**：[Scaling Book Part 7](../../resources/README.md#r-inference) 的 `The Basics of Transformer Inference` 与 `What do we actually want to optimize?`，替换 20 分钟视频；不进入多加速器部署章节。

**例子与图解：token、推理阶段和时间轴**

token 是 tokenizer 给文本编码后的编号，不等于一个汉字或单词。相同文本使用不同 tokenizer、模板或特殊符号，token 数可能不同。聊天模板把角色和内容组织成模型接收的序列；本单元固定 tokenizer revision 和模板，再核对真实输入长度。

~~~text
文本 → 模板 → tokenizer → 输入 IDs
                           ↓
prefill：一次处理已有 S 个位置 → KV Cache → 首个输出 token
decode：加入一个新位置 → 读取已有 KV → 更新 KV → 下一个 token
~~~

对一个无 batch 合并的请求，prefill 的投影可看作 (S,d)×(d,h)，单步 decode 为 (1,d)×(d,h)；后者仍需访问权重，不能仅凭计算少就认定利用率高。KV 保存各层历史位置的 Key/Value，并非上一轮的整个分数矩阵。

**暂停题**：请求在 0 秒发出，三个输出 token 分别在 0.20、0.25、0.30 秒到达。TTFT、平均 TPOT、末 token 延迟各是多少？只输出一个 token 时呢？

<details>
<summary>先写答案，再核对</summary>

TTFT=0.20 秒；平均 TPOT=(0.30−0.20)/(3−1)=0.05 秒；发出到末 token 是 0.30 秒。若协议结束消息更晚到达，完整请求 E2E 还应计至结束事件，不能用末 token 偷换。只有一个 token 时 TPOT 分母为零，记录不适用，不能填 0。这个例子假设逐 token 到达；真实 streaming chunk 可能含多个 token，客户端接收时间也不等于 GPU 生成时间。

</details>

**动手练习**：画单请求的发送、首 token、后续 token、结束时间轴；用几个假设时间戳手算 TTFT、TPOT 和端到端延迟，写明不足 2 个输出 token 的处理。

**检查结果**：区分请求延迟、GPU kernel 延迟与输出吞吐，不将“生成更快”当成未定义指标。

## 2. 从模型文件走到一个可追溯请求（60 分钟）

资源定位：[token、模板与请求格式](../../resources/README.md#r-token) → [单卡在线服务](../../resources/README.md#r-serving)。

**先读**：[vLLM Quickstart](../../resources/README.md#r-token) 的 `Online Serving`，再选其下 Completions 或 Chat Completions API 的一个请求示例。主线只选一种端点；离线批推理不是同一个服务基线。

**接着想一想**：把 endpoint、模型名、tokenizer、chat template 放到第一段的请求路径图上，标出哪些步骤发生在客户端、服务端和 GPU。

**例子与图解：一个请求经过哪里**

HTTP 是客户端与服务器交换请求和响应的协议；URL 指定服务器地址与路径，POST 发送内容，JSON 用字段表达请求。以所选端点的官方示例为准：Completions 常用 prompt，Chat Completions 使用 messages；两种模板语义不要混用。模型名标识服务中可访问的模型，不自动等同本地目录名。

~~~text
客户端：JSON + POST
   → 服务：检查字段/模型 → 模板与分词 → 排队 → GPU 推理
   ← 响应：状态码 + JSON 或 streaming 事件
~~~

**暂停题**：返回了状态码，但响应缺少生成结果，是否能开始压测？手写的“10 个字”能否作为 10-token 输入？

<details>
<summary>核对依据</summary>

不能。先查状态码、错误字段、服务日志和端点格式，再用官方最小请求确认真实结果。token 数由固定 tokenizer 与模板确定，字符数不能替代；服务返回 usage 时也需说明是否包含模板 token。记录 revision、dtype、tokenizer、模板、端点、采样与停止条件，才能重建请求。先保留 3～5 条功能请求；模型下载与许可要求按选定模型页面核对，当前指南不宣称任意模型都能装进单卡。

</details>

**动手练习**：选择能留出缓存余量的小模型，记录 revision、dtype 和完整配置；发一条请求核对返回内容及真实 token 长度。先确认功能，再写压测配置。

**检查结果**：服务可以重复启动，相同请求构造可重建，加载与预热时间有单独记录。

## 3. 给基线限定负载和统计窗口（45 分钟）

资源定位：[负载、明细和统计字段](../../resources/README.md#r-bench)。

**先读**：[vllm bench serve 参数文档](../../resources/README.md#r-bench) 中 `--num-prompts`、`--request-rate`、`--max-concurrency`、`--save-result`、`--save-detailed` 和输出目录项；长度参数阅读自己选定的数据集对应组，不默认所有组使用相同参数。

**接着想一想**：负载参数控制请求如何进入时间轴，实际发送和完成时间用于核对它们是否真正达到配置值。在线文档与本机版本不一致时，以匹配版本的帮助和文档为准。

**暂停题与结果核对**

10 秒窗口内完成 4 个成功请求，分别生成 2、3、4、1 个 token。请求吞吐与输出吞吐是多少？是否能由平均延迟反推出 p95？

<details>
<summary>核对答案</summary>

成功请求吞吐为 4/10=0.4 req/s；输出吞吐为 10/10=1 token/s。失败请求另计；记录窗口按发送批次还是完成事件划分，不能混用分母。平均值不能确定 p95，需要每个请求的记录及分位数规则。4 个样本只能作流程核对，尾延迟结论需更多请求与重复运行。W10 再引入有效吞吐。

</details>

**动手练习**：固定一组长度、采样策略和到达率，做少量并发点；保存成功/失败数、真实长度、测量窗口、TTFT/TPOT 和输出 tokens/s。W10 再做系统扫描，本周不扩充大网格。

**完成后检查**：可以从原始记录说明一个图中每个点的来源；小样本分位数标为探索结果。

## 独立完成与可选 AI 帮助

三段都先遮住答案作答，再核对推导；答错保留原答案，回资源卡指定小节，用不同输入重做。每段“检查结果”连同 [单元完成标准](README.md) 都需要真实笔记或运行记录支持。纸面例子正确只能说明该例的理解，不能替代实验。记录在本单元实验目录的 notes.md，按 W8-S01～S03 分节。

可选提示词：

> 我正在学习 W8 的token 与模板。我的推导是【粘贴】，我与本段核对说明不同的一步是【填写】。请只用本段的小例子检查这一步，给一个改变单项条件的反例，先让我回答。不要假设我做过实验，也不要用未核验的接口填补解释。

## 整理记录与可选拓展

在 `labs/05-serving/baseline/` 保存配置、请求构造、数据与报告。W9 复用同一服务做 APC 实验，W10 再统一项目入口。

进阶选择一组更长输入，先用资源模型预测影响；模型更换、量化和多卡推理留到后续，避免同时改变多个因素。
