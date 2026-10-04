# 文件迁移记录：2026-10-04

迁移以本轮开始时的工作区为基准，保留上轮未提交修改。原有 108 份 Markdown；docs 根目录 18 份。W1 进行中，其余十五单元未开始，未创建学习实验。没有提交或推送。

旧正文确认迁移后移除。下表使用代码路径记录旧地址，避免把已删除文件做成失效链接；锚点映射在迁移完成时补入。


## 文件与分段去向

| 旧文件 | 新位置 | 定位 |
| --- | --- | --- |
| `docs/coverage-review.md` | [docs/archive/coverage-review-2026-10-03.md](coverage-review-2026-10-03.md) | 标题锚点保留或随正文迁移 |
| `docs/coverage-review.md` | [docs/coverage.md](../coverage.md) | 内容合并；见对应页面 |
| `docs/curriculum-design.md` | [docs/design.md](../design.md) | 内容合并；见对应页面 |
| `docs/environment.md` | [course/environment.md](../../course/environment.md) | 内容合并；见对应页面 |
| `docs/first-eight-weeks-review.md` | [docs/archive/first-eight-weeks-review-2026-10-01.md](first-eight-weeks-review-2026-10-01.md) | 内容合并；见对应页面 |
| `docs/first-eight-weeks.md` | [course/README.md](../../course/README.md) | 内容合并；见对应页面 |
| `docs/foundations.md` | [course/foundations/p01.md](../../course/foundations/p01.md) | `#p1`、`#p1把数学计算写成有输入和返回值的函数` |
| `docs/foundations.md` | [course/foundations/p02.md](../../course/foundations/p02.md) | `#p2`、`#p2让每种输入都有明确去处` |
| `docs/foundations.md` | [course/foundations/p03.md](../../course/foundations/p03.md) | `#p3`、`#p3遍历容器并追踪每次循环的状态` |
| `docs/foundations.md` | [course/foundations/p04.md](../../course/foundations/p04.md) | `#p4`、`#p4读懂报错区分输入问题与程序错误` |
| `docs/foundations.md` | [course/foundations/p05.md](../../course/foundations/p05.md) | `#p5`、`#p5拆分模块理解运行入口和命令行` |
| `docs/foundations.md` | [course/foundations/p06.md](../../course/foundations/p06.md) | `#p6`、`#p6把结果保存在进程之外` |
| `docs/foundations.md` | [course/foundations/p07.md](../../course/foundations/p07.md) | `#p7`、`#p7测试排错和独立小工具` |
| `docs/foundations.md` | [course/foundations/p08.md](../../course/foundations/p08.md) | `#p8`、`#p8对象状态和模型模块w6-前` |
| `docs/foundations.md` | [course/foundations/README.md](../../course/foundations/README.md) | 内容合并；见对应页面 |
| `docs/github-publishing.md` | [docs/maintenance.md](../maintenance.md) | 内容合并；见对应页面 |
| `docs/learning-map.md` | [docs/coverage.md](../coverage.md) | 内容合并；见对应页面 |
| `docs/learning-workflow.md` | [course/guide.md](../../course/guide.md) | 内容合并；见对应页面 |
| `docs/mastery-checks.md` | [course/foundations/README.md](../../course/foundations/README.md) | 标题锚点保留或随正文迁移 |
| `docs/mastery-checks.md` | [weeks/week-01-foundations/assessment.md](../../weeks/week-01-foundations/assessment.md) | `#w1`、`#w1内存布局与资源账本` |
| `docs/mastery-checks.md` | [weeks/week-02-cuda-execution/assessment.md](../../weeks/week-02-cuda-execution/assessment.md) | `#w2`、`#w2线程搬运与同步` |
| `docs/mastery-checks.md` | [weeks/week-03-reduction-profiling/assessment.md](../../weeks/week-03-reduction-profiling/assessment.md) | `#w3`、`#w3归约与证据` |
| `docs/mastery-checks.md` | [weeks/week-04-gemm/assessment.md](../../weeks/week-04-gemm/assessment.md) | `#w4`、`#w4计算量不等于耗时` |
| `docs/mastery-checks.md` | [weeks/week-05-triton-softmax/assessment.md](../../weeks/week-05-triton-softmax/assessment.md) | `#w5`、`#w5表达式融合与数值` |
| `docs/mastery-checks.md` | [weeks/week-06-attention/assessment.md](../../weeks/week-06-attention/assessment.md) | `#w6`、`#w6模型形状与整体成本` |
| `docs/mastery-checks.md` | [weeks/week-13-systems/assessment.md](../../weeks/week-13-systems/assessment.md) | `#w13`、`#w13图kernel-与编译成本` |
| `docs/mastery-checks.md` | [weeks/week-07-collectives/assessment.md](../../weeks/week-07-collectives/assessment.md) | `#w7`、`#w7通信语义与网络成本` |
| `docs/mastery-checks.md` | [weeks/week-08-serving-baseline/assessment.md](../../weeks/week-08-serving-baseline/assessment.md) | `#w8`、`#w8服务与请求生命周期` |
| `docs/mastery-checks.md` | [weeks/week-09-kv-cache/assessment.md](../../weeks/week-09-kv-cache/assessment.md) | `#w9`、`#w9kv-容量与共享` |
| `docs/mastery-checks.md` | [weeks/week-10-serving-benchmark/assessment.md](../../weeks/week-10-serving-benchmark/assessment.md) | `#w10`、`#w10观测与负载解释` |
| `docs/mastery-checks.md` | [weeks/week-11-ddp/assessment.md](../../weeks/week-11-ddp/assessment.md) | `#w11`、`#w11数据更新与通信` |
| `docs/mastery-checks.md` | [weeks/week-12-fsdp/assessment.md](../../weeks/week-12-fsdp/assessment.md) | `#w12`、`#w12分片持久化与下一步` |
| `docs/mastery-checks.md` | [weeks/week-14-parallelism/assessment.md](../../weeks/week-14-parallelism/assessment.md) | `#w14`、`#w14并行切分与依赖` |
| `docs/mastery-checks.md` | [weeks/week-15-ray/assessment.md](../../weeks/week-15-ray/assessment.md) | `#w15`、`#w15任务状态与重试` |
| `docs/mastery-checks.md` | [weeks/week-16-scheduling/assessment.md](../../weeks/week-16-scheduling/assessment.md) | `#w16`、`#w16调度与公平性` |
| `docs/mastery-checks.md` | [course/reviews.md](../../course/reviews.md) | 内容合并；见对应页面 |
| `docs/plan-review.md` | [docs/archive/plan-review-2026-10-03.md](plan-review-2026-10-03.md) | 内容合并；见对应页面 |
| `docs/prerequisites.md` | [course/prerequisites.md](../../course/prerequisites.md) | 内容合并；见对应页面 |
| `docs/progress.md` | [course/progress.md](../../course/progress.md) | 内容合并；见对应页面 |
| `docs/repository-layout.md` | [docs/maintenance.md](../maintenance.md) | 内容合并；见对应页面 |
| `docs/source-audit-2026-10-03.md` | [docs/audits/2026-10-03-sources.md](../audits/2026-10-03-sources.md) | 内容合并；见对应页面 |
| `docs/study-guide.md` | [course/guide.md](../../course/guide.md) | 内容合并；见对应页面 |
| `docs/systems-bridges.md` | [course/bridges/s01.md](../../course/bridges/s01.md) | `#s1`、`#s1程序如何运行在机器上` |
| `docs/systems-bridges.md` | [course/bridges/s02.md](../../course/bridges/s02.md) | `#s2`、`#s2一次搬运和一次请求` |
| `docs/systems-bridges.md` | [course/bridges/s03.md](../../course/bridges/s03.md) | `#s3`、`#s3把一个服务装进容器` |
| `docs/systems-bridges.md` | [course/bridges/s04.md](../../course/bridges/s04.md) | `#s4`、`#s4gpu-在等什么数据` |
| `docs/systems-bridges.md` | [course/bridges/s05.md](../../course/bridges/s05.md) | `#s5`、`#s5保存下来与恢复正确` |
| `docs/systems-bridges.md` | [course/bridges/s06.md](../../course/bridges/s06.md) | `#s6`、`#s6任务依赖资源准入与-kubernetes` |
| `docs/systems-bridges.md` | [course/bridges/README.md](../../course/bridges/README.md) | 内容合并；见对应页面 |
| `docs/weekly-refresh.md` | [docs/maintenance.md](../maintenance.md) | 内容合并；见对应页面 |
| `resources/frontier-watchlist.md` | [resources/optional.md](../../resources/optional.md) | 内容合并；见对应页面 |
| `resources/README.md` | [resources/foundations.md](../../resources/foundations.md) | `#r-views`、`#r-views--tensor-的视图转置与复制` |
| `resources/README.md` | [resources/gpu.md](../../resources/gpu.md) | `#r-online`、`#r-online--分块-softmax-的状态合并` |
| `resources/README.md` | [resources/models.md](../../resources/models.md) | `#r-compile`、`#r-compile--eager编译和变化输入` |
| `resources/README.md` | [resources/training.md](../../resources/training.md) | `#r-parallel`、`#r-parallel--tp-通信与-pp-流水线` |
| `resources/README.md` | [resources/serving.md](../../resources/serving.md) | `#r-metrics`、`#r-metrics--服务状态与有效吞吐` |
| `resources/README.md` | [resources/scheduling.md](../../resources/scheduling.md) | `#r-ostep`、`#r-ostep--排队指标fifo-与-sjf` |
| `resources/README.md` | [resources/optional.md](../../resources/optional.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-01-foundations/refresh-2026-10-01.md` | [docs/audits/2026-10-01-week-01.md](../audits/2026-10-01-week-01.md) | 内容合并；见对应页面 |
| `weeks/week-01-foundations/study-guide.md` | [weeks/week-01-foundations/README.md](../../weeks/week-01-foundations/README.md) | 内容合并；见对应页面 |
| `weeks/week-02-cuda-execution/refresh-2026-10-01.md` | [docs/audits/2026-10-01-week-02.md](../audits/2026-10-01-week-02.md) | 内容合并；见对应页面 |
| `weeks/week-02-cuda-execution/study-guide.md` | [weeks/week-02-cuda-execution/README.md](../../weeks/week-02-cuda-execution/README.md) | 内容合并；见对应页面 |
| `weeks/week-03-reduction-profiling/refresh-2026-10-01.md` | [docs/audits/2026-10-01-week-03.md](../audits/2026-10-01-week-03.md) | 内容合并；见对应页面 |
| `weeks/week-03-reduction-profiling/study-guide.md` | [weeks/week-03-reduction-profiling/README.md](../../weeks/week-03-reduction-profiling/README.md) | 内容合并；见对应页面 |
| `weeks/week-04-gemm/refresh-2026-10-01.md` | [docs/audits/2026-10-01-week-04.md](../audits/2026-10-01-week-04.md) | 内容合并；见对应页面 |
| `weeks/week-04-gemm/study-guide.md` | [weeks/week-04-gemm/README.md](../../weeks/week-04-gemm/README.md) | 内容合并；见对应页面 |
| `weeks/week-05-triton-softmax/refresh-2026-10-01.md` | [docs/audits/2026-10-01-week-05.md](../audits/2026-10-01-week-05.md) | 内容合并；见对应页面 |
| `weeks/week-05-triton-softmax/study-guide.md` | [weeks/week-05-triton-softmax/README.md](../../weeks/week-05-triton-softmax/README.md) | 内容合并；见对应页面 |
| `weeks/week-06-attention/refresh-2026-10-01.md` | [docs/audits/2026-10-01-week-06.md](../audits/2026-10-01-week-06.md) | 内容合并；见对应页面 |
| `weeks/week-06-attention/study-guide.md` | [weeks/week-06-attention/README.md](../../weeks/week-06-attention/README.md) | 内容合并；见对应页面 |
| `weeks/week-07-collectives/refresh-2026-10-01.md` | [docs/audits/2026-10-01-week-07.md](../audits/2026-10-01-week-07.md) | 内容合并；见对应页面 |
| `weeks/week-07-collectives/study-guide.md` | [weeks/week-07-collectives/README.md](../../weeks/week-07-collectives/README.md) | 内容合并；见对应页面 |
| `weeks/week-08-serving-baseline/study-guide.md` | [weeks/week-08-serving-baseline/session-01.md](../../weeks/week-08-serving-baseline/session-01.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-08-serving-baseline/study-guide.md` | [weeks/week-08-serving-baseline/session-02.md](../../weeks/week-08-serving-baseline/session-02.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-08-serving-baseline/study-guide.md` | [weeks/week-08-serving-baseline/session-03.md](../../weeks/week-08-serving-baseline/session-03.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-08-serving-baseline/study-guide.md` | [weeks/week-08-serving-baseline/README.md](../../weeks/week-08-serving-baseline/README.md) | 内容合并；见对应页面 |
| `weeks/week-09-kv-cache/study-guide.md` | [weeks/week-09-kv-cache/session-01.md](../../weeks/week-09-kv-cache/session-01.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-09-kv-cache/study-guide.md` | [weeks/week-09-kv-cache/session-02.md](../../weeks/week-09-kv-cache/session-02.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-09-kv-cache/study-guide.md` | [weeks/week-09-kv-cache/session-03.md](../../weeks/week-09-kv-cache/session-03.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-09-kv-cache/study-guide.md` | [weeks/week-09-kv-cache/README.md](../../weeks/week-09-kv-cache/README.md) | 内容合并；见对应页面 |
| `weeks/week-10-serving-benchmark/study-guide.md` | [weeks/week-10-serving-benchmark/session-01.md](../../weeks/week-10-serving-benchmark/session-01.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-10-serving-benchmark/study-guide.md` | [weeks/week-10-serving-benchmark/session-02.md](../../weeks/week-10-serving-benchmark/session-02.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-10-serving-benchmark/study-guide.md` | [weeks/week-10-serving-benchmark/session-03.md](../../weeks/week-10-serving-benchmark/session-03.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-10-serving-benchmark/study-guide.md` | [weeks/week-10-serving-benchmark/README.md](../../weeks/week-10-serving-benchmark/README.md) | 内容合并；见对应页面 |
| `weeks/week-11-ddp/study-guide.md` | [weeks/week-11-ddp/session-01.md](../../weeks/week-11-ddp/session-01.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-11-ddp/study-guide.md` | [weeks/week-11-ddp/session-02.md](../../weeks/week-11-ddp/session-02.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-11-ddp/study-guide.md` | [weeks/week-11-ddp/session-03.md](../../weeks/week-11-ddp/session-03.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-11-ddp/study-guide.md` | [weeks/week-11-ddp/README.md](../../weeks/week-11-ddp/README.md) | 内容合并；见对应页面 |
| `weeks/week-12-fsdp/study-guide.md` | [weeks/week-12-fsdp/session-01.md](../../weeks/week-12-fsdp/session-01.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-12-fsdp/study-guide.md` | [weeks/week-12-fsdp/session-02.md](../../weeks/week-12-fsdp/session-02.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-12-fsdp/study-guide.md` | [weeks/week-12-fsdp/session-03.md](../../weeks/week-12-fsdp/session-03.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-12-fsdp/study-guide.md` | [weeks/week-12-fsdp/README.md](../../weeks/week-12-fsdp/README.md) | 内容合并；见对应页面 |
| `weeks/week-13-systems/refresh-2026-10-01.md` | [docs/audits/2026-10-01-week-13.md](../audits/2026-10-01-week-13.md) | 内容合并；见对应页面 |
| `weeks/week-13-systems/study-guide.md` | [weeks/week-13-systems/README.md](../../weeks/week-13-systems/README.md) | 内容合并；见对应页面 |
| `weeks/week-14-parallelism/study-guide.md` | [weeks/week-14-parallelism/session-01.md](../../weeks/week-14-parallelism/session-01.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-14-parallelism/study-guide.md` | [weeks/week-14-parallelism/session-02.md](../../weeks/week-14-parallelism/session-02.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-14-parallelism/study-guide.md` | [weeks/week-14-parallelism/session-03.md](../../weeks/week-14-parallelism/session-03.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-14-parallelism/study-guide.md` | [weeks/week-14-parallelism/README.md](../../weeks/week-14-parallelism/README.md) | 内容合并；见对应页面 |
| `weeks/week-15-ray/study-guide.md` | [weeks/week-15-ray/session-01.md](../../weeks/week-15-ray/session-01.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-15-ray/study-guide.md` | [weeks/week-15-ray/session-02.md](../../weeks/week-15-ray/session-02.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-15-ray/study-guide.md` | [weeks/week-15-ray/session-03.md](../../weeks/week-15-ray/session-03.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-15-ray/study-guide.md` | [weeks/week-15-ray/README.md](../../weeks/week-15-ray/README.md) | 内容合并；见对应页面 |
| `weeks/week-16-scheduling/study-guide.md` | [weeks/week-16-scheduling/session-01.md](../../weeks/week-16-scheduling/session-01.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-16-scheduling/study-guide.md` | [weeks/week-16-scheduling/session-02.md](../../weeks/week-16-scheduling/session-02.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-16-scheduling/study-guide.md` | [weeks/week-16-scheduling/session-03.md](../../weeks/week-16-scheduling/session-03.md) | 标题锚点保留或随正文迁移 |
| `weeks/week-16-scheduling/study-guide.md` | [weeks/week-16-scheduling/README.md](../../weeks/week-16-scheduling/README.md) | 内容合并；见对应页面 |

## 内容保留核对

P1～P8、S1～S6 按原段拆分；48 个 W session 保留原有解释、图解、暂停题和答案，后八单元由导学正文拆出。各单元的原实践任务和完成要求分别进入 README 与 assessment，新增迁移/排错按原 W 锚点迁移。阶段和综合题进入 reviews。旧时间表与历史审查不参与当前日常规划。

迁移不改变 W1 进行中及其余单元未开始状态；保留历史预读日期，不声称重跑实验。旧外部书签使用本表查找；仓库内链接更新到新位置。

## 历史预算与定位

旧 `docs/study-guide.md#原实验时间拆分历史参考` 的表格保存在 [历史时间估计](time-budget-2026-10-03.md)，不参与当前规划。P1～P8 对应各 pXX 文件的同名 `#pN`；S1～S6 对应 sXX 的 `#sN`；原掌握检查的 `#wN` 对应各单元 assessment，`#stages` 与 `#final` 对应 reviews。

前八单元已有 session 文件名不变；后八单元原 guide 的第 1、2、3 段分别对应 session-01、02、03。通用作答方式并入 course/guide，整理记录与拓展保留在各单元最后一段。
