# 学习安排审查：2026-10-01

## 2026-10-03 定位修订

当前目标改为完整 AI Infra 基础学习，面向编程基础较弱、数学较好的你。实施内容见 [课程设计](../design.md)、[基础学习](../../course/foundations/README.md)、[系统桥接](../../course/bridges/README.md) 和 [学习地图](../coverage.md)。原性能实验保留并承担实践；增加的数据、存储、网络、Docker、Kubernetes 基础与观测不是可任意跳过的拓展。

完成标准为解释、独立实现、迁移和证据排错四项能力，见 [验收题](../../course/reviews.md)。时间是预计范围，可增加、拆段并记录实际；不以链接数量或固定学习段数衡量完整性。生产运维、大规模容灾和框架内部开发继续后置。

以下为 2026-10-01 的历史审查；当时“平台基础全部后置”的定位已由本节修订，不能继续用来缩减当前基础内容。

## 结论与评估范围

当前路线适合作为 **GPU / LLM 系统性能工程入门**。大部分内容可以保留；W13 编译实验提前到 W6 后，先比较框架优化，再进入通信和推理。需要补齐的是先修、实验比较、当前实现与实际采用条件。

旧版尚未覆盖完整 AI 平台工程：容器交付、集群运维、数据与存储、网络、监控告警、多租户隔离、故障恢复和成本管理仅涉及少量内容。这解释了当时的后置决定；2026-10-03 已把基础部分接回主线，只有生产深度继续后置。

本次检查了 16 个周计划、公共规则、资源索引与项目范围，核对了补充资料的官方页面。结论是设计审查，不是学习效果或机器环境的实测评价。

## 主要发现与处理

| 优先级 | 原安排的缺口 | 影响 | 本次处理 |
| --- | --- | --- | --- |
| 高 | W1 主要检查 C++/Tensor，W6 假设掌握 Decoder，W7 进入 DDP | 缺乏 mask、梯度与训练状态的基础 | 增加按需先修检查，分别在模型和训练单元前补齐 |
| 高 | 每周 9 小时同时承担安装、实现、分析与报告 | W3/6/12/13 容易只跑通示例 | 明确学习单元和缓冲时间，划分必做与扩展 |
| 高 | 有算子表与 Nsight Compute，缺少系统时间线训练 | 将输入等待或启动开销误当 kernel 瓶颈 | W6 补 Nsight Systems，W11 补输入流水线检查 |
| 高 | W9 学 PagedAttention，实测主要改变前缀缓存 | 误将 APC 收益归因于分页管理 | 明确理论学习与实验自变量的边界 |
| 高 | W10 未区分计划到达率和实际发送速率 | 并发上限反压客户端后，真实负载改变 | 记录计划/实际负载、客户端开销与有效吞吐 |
| 中 | 手写 CUDA/Triton 后缺少框架编译优化对照 | 默认性能优化都需要手写 kernel | W13 默认做 eager/torch.compile 对照 |
| 中 | CUDA 数值对照缺少内存与同步错误检查 | 某些越界或 race 未必表现为当前数值错误 | W2～3 补 Compute Sanitizer 的限定检查 |
| 中 | 训练精度、优化器状态与 DataLoader 仅隐含在配置中 | 显存和输入开销解释不完整 | 先修中补训练状态，W11 补 AMP/数据路径材料 |
| 中 | W8 将完成 W7 作为先修 | 暂无多卡时连单卡推理也被阻塞 | 改为模型理解和单卡环境就绪 |
| 中 | W16 的 FIFO/SJF 缺少直接的理论教材 | 会用 Ray 但说不清策略假设 | 用 OSTEP 调度章节替换主线 Ray 架构论文 |

## 进一步调整

| 原安排的问题 | 调整 | 对学习量的影响 |
| --- | --- | --- |
| 编译实验排在训练之后，容易先入为主地手写优化 | W13 移到 W6 后，复用已有小 Block | 不加新单元，保留目录编号 |
| 资料讲了原理，但与当前实现的联系不够明确 | 16 个单元各补一份 context.md，指定一个观察方向和具体阅读位置 | 现作为基础完成后的可选拓展；开始前先核验必读资料 |
| 练习实现缺少现成组件对照 | Reduce / GEMM 明确加入 torch.sum / torch.matmul 参考 | 复用已有正确性参考和测量脚本，不加手写版本 |
| 服务性能报告可能忽略输出变化 | W8 保存少量固定请求输出；W10 检查语义与质量条件 | 并入原单请求检查；完整质量评估按所选优化另排 |
| 新论文、新框架容易被当作下一项必修 | 标明版本、成熟度、硬件要求和未验证部分 | 每单元只观察一个问题，额外实现留作可选拓展 |
| 读完、跑通与可用于真实系统之间缺少区分 | 报告增加选用理由、失败边界、恢复或回退方案 | 用原报告说明，不新建生产系统项目 |

当前方案见 [完整设计](../design.md)，新资料与更新办法见 [进展索引](../../resources/optional.md) 和 [学习前资料复核](../maintenance.md)。

## 容易偏离目标的地方

C++ 与 kernel 学习应服务于理解程序和性能。CS106L 用于选题补学，不承担完整 C++ 入门；模板元编程、复杂构建系统和大量算子刷题不作为当前前置。W6 和 W13 应回到模型区段，验证优化对整体执行的影响。

算子表定位热点，系统时间线观察 CPU、传输、GPU 和等待，kernel 指标解释算子内部行为。有效带宽、理论访存量与实测 DRAM 流量要分开；理论性能上界不是必须达到的成绩线。[Nsight Systems CUDA Trace](https://docs.nvidia.com/nsight-systems/UserGuide/index.html#cuda-trace) 可支持时间线这一环。

PagedAttention 分页管理与 APC 计算复用不是同一个自变量。W9 可以学两者，但 APC 开关实验只能直接说明前缀复用的影响。[vLLM APC 文档](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/) 将直接收益解释为减少重复 prefill，不能据此断言 decode kernel 变快。

Ray 单机 FIFO/SJF 有助于学习排队与资源准入，但不能代表多节点放置、抢占、弹性伸缩或多租户隔离。先验证同资源任务的两策略，再扩展多 GPU 作业。

## 资料补充的取舍

| 缺口 | 优先来源 | 使用方式 |
| --- | --- | --- |
| 工具基础 | [Missing Semester 2026](https://missing.csail.mit.edu/) | 诊断不过再选 Shell/Git |
| 训练先修 | [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | 自动求导与单卡优化循环 |
| 模型先修 | [CS336 2026 课程表](https://cs336.stanford.edu/) 中 Lecture 3 与已有 SDPA 教程 | 画 shape、mask、残差和 MLP |
| GPU 正确性 | [Compute Sanitizer](https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html) | W2 memcheck，W3 共享内存与同步检查 |
| 框架优化 | [torch.compile 入门](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html) | W13 正确性、首次编译、稳态与 graph break |
| 训练性能 | [AMP](https://docs.pytorch.org/tutorials/recipes/recipes/amp_recipe.html)、[Performance Tuning Guide](https://docs.pytorch.org/tutorials/recipes/recipes/tuning_guide.html) | 分别检查精度与输入流水线，避免混入卡数对照 |
| 服务观测 | [vLLM Production Metrics](https://docs.vllm.ai/en/latest/usage/metrics/) | 将客户端结果连接到服务端状态 |
| 调度假设 | [OSTEP：Scheduling Introduction](https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf) | 先读 FIFO/SJF 与指标，再讨论 GPU 作业差异 |

补充时间通过替换重复观看、精简扩展和按需补学安排。新增必读已计入 [逐单元预算](../../course/guide.md#time-budget)，原 9 小时统一预算不再沿用。

## 节奏与成果范围

保留 W1～W16 编号，视为 16 个学习单元。基础已满足时仍可按每单元约一周推进；日历建议预留 2～4 周用于环境和返工，这是规划余量，不是保证完成时间。单卡训练或模型基础不足时，补学时间另计。

先整理 GPU 性能实验集与 mini-serving-benchmark；训练和调度先完成小实验报告。四个项目目录表示长期归档方向，不要求 16 个单元内产出四套成熟系统。

仍待开始学习时确认：实际先修水平、工具链、服务器配额、具体模型、依赖版本及视频选看位置。链接核验不能代替这些检查。

## 后续分支，不立即加为必修

| 方向 | 何时加入 | 当前取舍 |
| --- | --- | --- |
| Tensor Core/CUTLASS、更多 Triton 算子、编译器内部实现 | W13 后确定偏底层优化时 | 避免扩大初期实现量 |
| Activation checkpointing、CPU offload、复杂并行组合 | DDP/FSDP2 基线可信后 | 先分清显存与通信代价 |
| 量化、CUDA Graph、投机解码、多卡推理 | 单卡服务与质量检查可靠后 | 每项需独立对照，有些涉及质量变化 |
| 平台进阶：生产集群运维、Slurm、多租户治理、大规模容灾 | 基础 Docker/Kubernetes/网络/数据/存储通过后 | 基础部分已纳入 S1～S6，进阶另定范围 |

这些是后续方向，不是必须立即补齐的所有“缺课”。
