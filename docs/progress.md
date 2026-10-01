# 学习进度

完成计划编写不代表完成学习。所有单元初始状态均为“未开始”；开始学习后按实际状态更新，通过验收后才记为“已通过”。下表按学习顺序排列，W 编号保持不变。

状态取值：未开始 / 进行中 / 待验收 / 已通过 / 需补做。

| 单元 | 主题 | 状态 | 实验或报告链接 | 自评分与验收日期 | 阻塞问题 |
| --- | --- | --- | --- | --- | --- |
| [W1](../weeks/week-01-foundations/README.md) | Tensor、内存与资源账本 | 进行中 | [第一段学习指南](../weeks/week-01-foundations/session-01.md)；实验尚未创建 | 待验收 | 基础自测待完成；第一段学习练习待做 |
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

按 [先修检查](prerequisites.md) 记录需要补学的项目。基础通过和扩展完成分别注明；例如 W7 的 2 卡基线已通过时，4 卡扩展仍可保持未完成。

## 学习指南整理进度

2026-10-01 已准备前八个学习位置的 24 段学习指南和 8 份资料更新，统一入口见 [自学导航](first-eight-weeks.md)。W1 的实际学习前资料复核已完成；其余七份是带日期的提前资料复核，实际开始学习时仍须重查。学习状态继续以上表为准，学习指南、手算参考和工具检查不代替验收。

同日完成 [逐周自学指南检查](first-eight-weeks-review.md)：八个单元均按统一规则核对；24 段补齐读图说明、暂停题核对与可选 AI 理解提示词。另修订 W2 的运行顺序、W3 的归约收尾与计时范围、W6 的 Block 结构和 W13 的回本计算。本次为教材修订，未增加学习完成项。

同日扩展到 [全部 16 单元覆盖检查](coverage-review.md)：补齐基础入口，按知识点整理原始资源；后八单元在 study-guide 内加入 24 组图解/暂停核对。全部 48 段的前置、材料、练习与标准已对应，预算按实际阅读范围重新估计。这里只登记材料整理，不新增学习完成或实验结果。

## 当前单元的学习资料复核记录

实际开始学习日期：2026-10-01。单元：W1。资料更新记录：[2026-10-01 学习前资料复核](../weeks/week-01-foundations/refresh-2026-10-01.md)。

当前完成：来源与版本核验、C++ / CPU 张量最小运行检查、W1 三段学习指南。当前未完成：前置基础诊断、指定阅读、学习练习与验收；学习指南和工具检查不能代替学习成果。

按 [学习前资料复核](weekly-refresh.md) 核验后，在这里链接当前单元的 `refresh-YYYY-MM-DD.md`。历史记录留在各单元目录；资料查过不等于实验做过。
