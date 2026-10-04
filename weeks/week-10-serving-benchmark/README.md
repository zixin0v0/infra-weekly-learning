# 单元 W10：推理负载与性能调优

[课程目录](../../course/README.md) · [我的进度](../../course/progress.md) · [环境准备](../../course/environment.md)

预计 10～18 小时用于本单元，变式与排错另留 1～3 小时；桥接只计新发生的时间。按实际掌握推进，记录规则见 [学习方法](../../course/guide.md#time-budget)。

## 这一单元要弄清什么

请求多起来后，吞吐还在上升，为什么有些请求却等得更久？复用 W8/W9 服务，分别改变负载和一个批处理配置，保存每条请求的时间与结果。你会把队列、失败、尾延迟和满足延迟目标的有效吞吐放在一起，判断一次调参是否值得保留。

## 开始前

完成 W8/W9 与 [M4 统计诊断](../../course/prerequisites.md)，扫描前回看 [S2 日志与指标](../../course/bridges/s02.md#s2)。先解释请求率与并发数的区别，并确认缓存条件一致。[S3 Docker 实操](../../course/bridges/s03.md#s3) 要在本阶段检查前完成。

<details>
<summary>先解释，再展开核对</summary>

请求率单位 req/s，并发是未完成请求的数量上限；并发限制触顶时实际发送速率可能低于计划。

</details>

## 按顺序学习

- [复习 S2 日志、指标与请求链](../../course/bridges/s02.md)。
- [W10 第 1 段：配置了 20 req/s，服务就一定收到了吗？](session-01.md)。
- [W10 第 2 段：一轮能处理八个 token，应该怎样分给请求？](session-02.md)。
- [W10 第 3 段：平均值不错，为什么还有请求等得很久？](session-03.md)。
- [核对 S3 的重建记录](../../course/bridges/s03.md)。

- [本单元掌握检查](assessment.md)：实验完成要求、变式与排错题。

## 实践任务

整合项目：projects/mini-serving-benchmark/；复用 labs/05-serving/。

1. 冻结模型、tokenizer、请求集、精度与采样策略。先固定一组输入/输出长度，长输入负载作为扩展。
2. 第一组固定并发上限，扫描至少 3 个计划到达率；第二组固定计划到达率，扫描至少 3 个并发上限。记录实际发送速率与是否触顶，识别限流对负载的影响。
3. 保留W8基线，在一个代表点只改变一个已核对的 token batching/prefill 预算参数。先画出 continuous batching 与 chunked prefill 的概念区别；不假设框架提供任意机制的独立关闭开关。
4. 汇总 TTFT/TPOT 的 p50/p95、输出 tokens/s、请求成功率、显存与实际长度；不要只展示最优点。
5. 写清若干延迟目标下的可用吞吐与局限，整理统一的复现入口和图表。

最小观测协议：保存请求数、测量窗口、发送/完成时间与客户端位置，检查客户端 CPU、tokenization 和连接路径是否限制负载；读取当前版本实际提供的服务端指标，不臆造缺失字段。预先定义 TTFT/TPOT 阈值，用“成功且满足全部阈值的请求数 / 测量窗口”计算本实验的请求有效吞吐。TPOT 是每请求的平均后续 token 时间，不能替代逐 token 的 ITL 分布；只有流式 chunk 时间戳时注明其粒度。

沿用 W8 的固定请求作输出检查，记录模型、模板、采样与停止条件是否变化；若未来引入量化、近似或新 proposer，另设质量对照，不能用吞吐替代质量。记录一个可回退的默认配置；按需估算每成功请求/有效 token 的 GPU 时间，未测电力和费用时不填写金额成本。

## 按需回看

继续查阅 [PagedAttention 论文](../../resources/serving.md#r-paged) 中与实验有关的部分。HF generate 对比可作为后续扩展，不是本周必做项。

需要复习时选看 [CS336 2026 Lecture 10](../../resources/serving.md#r-inference)，不额外增加整讲任务。

完成后做 [阶段复习](../../course/reviews.md#stages)。

[上一单元](../week-09-kv-cache/README.md) · [下一步](../week-11-ddp/README.md)
