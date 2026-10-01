# W10 章节导学：负载、批处理与有效吞吐

[本周范围与验收](README.md) · [导学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

资料预算：45 + 60 + 45 = 150 分钟。复用 W8/W9，冻结模型、请求集和精度，主线仅一组输入/输出长度。

## 1. 计划到达率和真正进入服务的速率（45 分钟）

**先读**：[bench serve](https://docs.vllm.ai/en/latest/cli/bench/serve/) 的 `--request-rate`、`--burstiness`、`--max-concurrency`；统计部分看 `--percentile-metrics`、`--metric-percentiles`、`--goodput`。每个参数先核对安装版本，再写入配置。

**接着想一想**：把 W8 时间轴扩成多请求图。预定发送、真实发送与服务完成可能有不同速率；并发上限会使负载发生变化，不能仅凭配置标签称为固定到达率实验。

**动手练习**：第一组固定上限扫至少 3 个计划到达率；第二组固定计划到达率扫至少 3 个上限。保留实际发送、测量窗口、完成/失败数，检查是否触顶。

**检查结果**：能说清每组实验控制了什么、实际观测又是什么，图例不将二者混写。

## 2. 在什么地方混合 prefill 与 decode（60 分钟）

**先看/读**：[CS336 Lecture 10](https://www.youtube.com/watch?v=EfM546A79aM) 配 [讲义](https://github.com/stanford-cs336/lectures/blob/main/lecture_10.py) 的 `continuous_batching`，用约 15 分钟画请求加入/退出 batch 的过程。

**立即联读**：[vLLM Optimization](https://docs.vllm.ai/en/latest/configuration/optimization/) 的 `Chunked Prefill` 与 `Performance Tuning with Chunked Prefill`，重点读 token 预算与延迟权衡。不要将 continuous batching 与 chunked prefill 当成同义词。

**动手练习**：在第一段的一个代表负载点，只改变一个经版本核对的 token batching/prefill 预算参数。先写对 TTFT/TPOT 的预测，再保留默认值和改动值两组结果；不假定任何机制都有独立关闭开关。

**检查结果**：能指出修改影响了调度过程的哪一步；负结果也保留，不只挑最快点。

## 3. 将客户端尾延迟与服务端状态对应（45 分钟）

**先读**：[Production Metrics](https://docs.vllm.ai/en/latest/usage/metrics/) 的 `General Metrics` 表，定位 `vllm:num_requests_running`、`vllm:num_requests_waiting`，然后查当前版本的缓存与延迟指标。表中存在不代表本机已暴露，运行时保存实际可用字段。

**接着想一想**：等待队列增加可能帮助解释 TTFT，但单个相关曲线不构成因果证明。检查压测端 CPU、tokenization、连接与网络路径；客户端瓶颈也会改变负载。

**动手练习**：预先选定 TTFT/TPOT 阈值，以“成功且满足全部阈值的请求数 / 测量窗口”定义本实验请求有效吞吐；与 CLI 的 goodput 口径核对，不一致则分开报告。保留样本数和测量区间。

**完成后检查**：p50/p95、输出吞吐、成功率与有效吞吐来自相同可追溯数据；TPOT 与逐 token ITL 不互相替代。

## 课后整理与选修

整合 `projects/mini-serving-benchmark/`：配置、请求构造、运行入口、原始数据、汇总图、结论与限制。代码引用 W8/W9 的实现，避免多份脚本漂移。

进阶只选长输入或混合长度负载之一。跨框架比较放在同框架对照完成后，不能用整体速度差直接证明某一个机制的贡献。
