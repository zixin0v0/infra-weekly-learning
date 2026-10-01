# 学习进度

完成计划编写不代表完成学习。所有单元初始状态均为“未开始”；开课后按实际状态更新，通过验收后才记为“已通过”。下表按学习顺序排列，W 编号保持不变。

状态取值：未开始 / 进行中 / 待验收 / 已通过 / 需补做。

| 单元 | 主题 | 状态 | 实验或报告链接 | 自评分与验收日期 | 阻塞问题 |
| --- | --- | --- | --- | --- | --- |
| [W1](../weeks/week-01-foundations/README.md) | Tensor、内存与资源账本 | 进行中 | [第一段备课](../weeks/week-01-foundations/session-01.md)；实验尚未创建 | 待验收 | 诊断待答；第一段学习练习待做 |
| [W2](../weeks/week-02-cuda-execution/README.md) | GPU 执行与内存 | 未开始 | 尚未创建 | 待验收 | 待诊断 |
| [W3](../weeks/week-03-reduction-profiling/README.md) | Reduce 与性能分析 | 未开始 | 尚未创建 | 待验收 | 待诊断 |
| [W4](../weeks/week-04-gemm/README.md) | GEMM 与数据复用 | 未开始 | 尚未创建 | 待验收 | 待诊断 |
| [W5](../weeks/week-05-triton-softmax/README.md) | Triton 与 Online Softmax | 未开始 | 尚未创建 | 待验收 | 待诊断 |
| [W6](../weeks/week-06-attention/README.md) | Attention 资源账本 | 未开始 | 尚未创建 | 待验收 | 待诊断 |
| [W13](../weeks/week-13-systems/README.md) | torch.compile 与 Systems 综合实验 | 未开始 | 尚未创建 | 待验收 | 待诊断 |
| [W7](../weeks/week-07-collectives/README.md) | 集合通信与 NCCL | 未开始 | 尚未创建 | 待验收 | 待诊断 |
| [W8](../weeks/week-08-serving-baseline/README.md) | 小型推理服务基线 | 未开始 | 尚未创建 | 待验收 | 待诊断 |
| [W9](../weeks/week-09-kv-cache/README.md) | KV Cache 与 PagedAttention | 未开始 | 尚未创建 | 待验收 | 待诊断 |
| [W10](../weeks/week-10-serving-benchmark/README.md) | 推理负载与性能调优 | 未开始 | 尚未创建 | 待验收 | 待诊断 |
| [W11](../weeks/week-11-ddp/README.md) | DDP 与训练扩展性 | 未开始 | 尚未创建 | 待验收 | 待诊断 |
| [W12](../weeks/week-12-fsdp/README.md) | FSDP2、ZeRO 与恢复 | 未开始 | 尚未创建 | 待验收 | 待诊断 |
| [W14](../weeks/week-14-parallelism/README.md) | TP、PP 与 Megatron | 未开始 | 尚未创建 | 待验收 | 待诊断 |
| [W15](../weeks/week-15-ray/README.md) | Ray 任务与资源 | 未开始 | 尚未创建 | 待验收 | 待诊断 |
| [W16](../weeks/week-16-scheduling/README.md) | 调度策略与评估 | 未开始 | 尚未创建 | 待验收 | 待诊断 |

按 [学习方式](learning-workflow.md) 评分。每次只维护当前周；需要顺延就调整实际日期，不以日历周数代替验收。

按 [先修检查](prerequisites.md) 记录需要补课的项目。基础通过和扩展完成分别注明；例如 W7 的 2 卡基线已通过时，4 卡扩展仍可保持未完成。

## 备课进度

2026-10-01 已准备前八个学习位置的 24 段备课和 8 份资料更新，统一入口见 [备课导航](first-eight-weeks.md)。W1 的实际开课更新已完成；其余七份是带日期的备课复核，实际开课时仍须重查。学习状态继续以上表为准，备课、手算参考和工具检查不代替验收。

## 当前单元的开课记录

实际开课日期：2026-10-01。单元：W1。资料更新记录：[2026-10-01 开课更新](../weeks/week-01-foundations/refresh-2026-10-01.md)。

当前完成：来源与版本核验、C++ / CPU 张量最小运行检查、W1 三段备课。当前未完成：学习者先修诊断、指定阅读、学习练习与验收；备课和工具检查不能代替学习成果。

按 [开课更新](weekly-refresh.md) 核验后，在这里链接当前单元的 `refresh-YYYY-MM-DD.md`。历史记录留在各单元目录；资料查过不等于实验做过。
