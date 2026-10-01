# W8 补充阅读：单引擎服务与分离式推理

[范围与验收](README.md) · [三段导学](study-guide.md) · [更新流程](../../docs/weekly-refresh.md) · [来源登记](../../resources/frontier-watchlist.md#s08)

资料快照：2026-10-01。开课复核：待进行。本地状态：仅阅读，相关实现尚未运行。

开课前用30分钟核对本页资料。这里的练习并入本周报告，额外实现留作选修。

## 现在怎样做

先建立单 GPU、单引擎的 vLLM 服务：模型/tokenizer 固定，单请求输出核对，再做可重复压测。主线先讲清 prefill、decode、TTFT、TPOT 与加载/稳态成本。

## 这一方向还有哪些进展

将 prefill 与 decode 放到不同资源池，靠 KV 传输连接。关注专用资源利用收益与传输、路由、运维成本之间的条件，而不是框架数量。

**读哪里**：[Dynamo 的 Prefill / Decode 分离](https://docs.dynamo.nvidia.com/dynamo/v1.4.1/kubernetes/disaggregated-serving/overview)。Should you disaggregate?、架构说明及 Before production；先读适用/不适用条件，不进入部署清单。

**目前的状态**：已发布的官方架构/部署文档，这里使用 v1.4.1 固定路径；不据此推断任意模型、互联和规模都值得拆分。

**在我们的设备上**：本单元继续单卡基线。规划中的多张 4090 不自动具备合适的跨设备/网络传输能力，不额外部署 Dynamo 或 Kubernetes。

## 真正用起来，还要考虑什么

论文常聚焦吞吐/延迟权衡；工程还要保证模型版本、KV 格式、故障处理、端点行为和可观测性一致。

**写进本周报告**：复用 W8 时间轴，再画一张分离式请求图，标出 KV 传输和新增故障边界。在报告写出拆分收益需超过哪些新增开销；没有测量不代入伪造数值。

## 下次更新时

核对稳定文档版本、后端兼容和 Should you disaggregate?；只有单引擎瓶颈已有证据才把分离式实验加入后续分支。更新写入 [开课记录](../../templates/weekly-refresh.md)，保留旧实验的配置。
