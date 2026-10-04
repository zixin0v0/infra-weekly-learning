# 完整课程目录

[首页](../README.md) · [我的进度](progress.md) · [环境准备](environment.md)

先从 [基础自测](prerequisites.md) 确定起点。编程基础不足时按 [P1～P7](foundations/README.md) 学习；P8 与 [单卡训练、验证和权重重载](foundations/training.md) 在 W6 前完成；训练课的 Adam 恢复部分在 W11 前接回。数学已会的部分，换一组数仍能算清楚，就跳过重复讲解。

W 是固定单元编号，不是必须完成的日历周。按下面顺序推进，W13 位于 W6 后。基础检查、系统衔接和阶段复习已经接入各单元课表。

| 学习位置 | 单元 | 主题 | 要回答的问题 | 完成什么 |
| --- | --- | --- | --- | --- |
| 1 | [W1](../weeks/week-01-foundations/README.md) | C++ / Tensor / 资源与数值精度 | 一个 Tensor 和 Linear 层消耗什么资源？ | 资源账本与核对脚本 |
| 2 | [W2](../weeks/week-02-cuda-execution/README.md) | GPU 执行与内存 | 线程如何覆盖数据，怎样可靠计时？ | Vector Add 正确性与带宽报告 |
| 3 | [W3](../weeks/week-03-reduction-profiling/README.md) | Reduce 与 Profiler | 哪些测量能解释快慢差异？ | 两种 Reduce 与分析报告 |
| 4 | [W4](../weeks/week-04-gemm/README.md) | GEMM 与数据复用 | Tiling 减少了哪些访存？ | 朴素与分块 GEMM 对照 |
| 5 | [W5](../weeks/week-05-triton-softmax/README.md) | Triton / Online Softmax | 融合如何减少数据搬运？ | 稳定 Softmax 与性能曲线 |
| 6 | [W6](../weeks/week-06-attention/README.md) | Attention / 模型 Profiling | Decoder Block 的资源花在哪里？ | 计算、显存与耗时账本 |
| 7 | [W13](../weeks/week-13-systems/README.md) | torch.compile / Systems 综合实验 | 框架优化如何影响模型性能？ | eager/compile 与模型区段对照 |
| 8 | [W7](../weeks/week-07-collectives/README.md) | NCCL / 集合通信 | 增加 GPU 为什么不一定更快？ | 2 卡基线，4 卡作为扩展 |
| 9 | [W8](../weeks/week-08-serving-baseline/README.md) | vLLM 服务基线 | 怎样定义可信的推理性能？ | 小模型服务与压测报告 |
| 10 | [W9](../weeks/week-09-kv-cache/README.md) | KV Cache / PagedAttention | 前缀缓存在什么负载下有效？ | 冷热缓存受控实验 |
| 11 | [W10](../weeks/week-10-serving-benchmark/README.md) | 推理负载与调优 | 吞吐增加时牺牲了什么？ | mini-serving-benchmark |
| 12 | [W11](../weeks/week-11-ddp/README.md) | DDP / 梯度同步 | 多卡训练比较怎样保持公平？ | 固定全局 batch 的扩展性报告 |
| 13 | [W12](../weeks/week-12-fsdp/README.md) | FSDP2 / ZeRO / 恢复 | 省下的显存换来了哪些通信？ | DDP/FSDP2 与恢复对照 |
| 14 | [W14](../weeks/week-14-parallelism/README.md) | TP / PP / Megatron | 切分一个层会产生哪些通信？ | 并行切分图与小型验证 |
| 15 | [W15](../weeks/week-15-ray/README.md) | Ray Task / Actor / Resource | 资源声明和失败重试如何影响执行？ | 单机任务执行与排队记录 |
| 16 | [W16](../weeks/week-16-scheduling/README.md) | 调度策略与评估 | FIFO 与短作业优先适合什么负载？ | mini-gpu-scheduler |

点开单元后，按课表进入具体小节。视频链接、中文解释、图和暂停题都在当页；先作答，再展开核对。完成各节练习后做单元检查，相关进展可以之后选读。

[基础阶段](foundations/README.md) · [系统衔接](bridges/README.md) · [阶段复习](reviews.md) · [视频与资料](../resources/README.md)
