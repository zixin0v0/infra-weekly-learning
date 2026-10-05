# W8 第 2 段：请求已经发出，为什么还没有生成结果？

[本单元](README.md) · [课程目录](../../course/README.md)

有 HTTP 响应，不等于有正确的模型输出。先确认端点、模型和请求字段确实匹配，再保留几个可重复的功能请求，最后才开始施加负载。

## 视频与正文

主要阅读下列正文与图解。视频范围待核验；已看懂的重复内容只需回查。

## 中文补充（按需）

MDN 中文[HTTP 概述](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Overview)只看系统组成、HTTP 流与请求/响应消息，用本课请求逐项找 method、路径、状态码和 body。它是官方站社区译文，指定正文已预读；不包含 vLLM 当前启动参数、ready 语义或流式 token 事件。卡在容器端口时回 S3，不另学一套服务框架。[范围与版本](../../resources/serving.md#cn-http)。

## 开始前

上一段能区分 token 与字符，并能画 TTFT/TPOT 时间线；HTTP 或容器还不熟时，先做 [S2](../../course/bridges/s02.md) 与 [S3](../../course/bridges/s03.md)。

资源定位：[token、模板与请求格式](../../resources/serving.md#r-token) → [单卡在线服务](../../resources/serving.md#r-serving)。

**先读**：[vLLM Quickstart](../../resources/serving.md#r-token) 的 `Online Serving`，再选其下 Completions 或 Chat Completions API 的一个请求示例。这里先选一种端点；离线批推理不是同一个服务基线。

**接着想一想**：把 endpoint、模型名、tokenizer、chat template 放到第一段的请求路径图上，标出哪些步骤发生在客户端、服务端和 GPU。

## 从请求字段追到输出内容

一次请求至少有两层约定：网络层面要到达正确地址和端口，应用层面要使用正确路径与 JSON 字段。端口未监听时，应用根本没有机会校验 prompt；收到应用错误响应后，则要回到字段、模型名和端点语义。

复用 [S2 的请求路径图](../../course/bridges/s02.md)，在自己的请求上圈出 host、port、path、method、headers 与 body。然后检查返回的生成内容、实际 token 长度和停止原因。模型加载与预热要单独记录，因为它们不是每条稳态请求都会重新支付的成本。

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

## 完成后

把代码、预测与实际结果记在同一份笔记中。完成本段检查后，沿下方链接继续。

[上一课](session-01.md) · [下一课](session-03.md)
