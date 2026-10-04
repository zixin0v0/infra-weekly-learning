# 2026-10-04：个人学习正文与图解检查

[维护目录](../README.md) · [当前覆盖表](../coverage.md)

这份记录说明文字与图形实际检查到哪里，不记录个人是否学会。检查了 140 个当前 Markdown 页面：14 个 P/S 内容页、96 个 W 页面、30 个入口/资料/模板等页面；其中 139 页按用途改写、补充或精简，个人进度页只核对、不改动。原有历史记录保持原日期与核验边界。

## 文字怎样改写

先用具体问题引出对象与关系，再用小输入说明原因，最后保留补全、独立实现、变式与排错。术语在首次需要时说明含义；较长核对放在折叠块中，必要解释留在正文。个人记录与材料准备分开，时间仍只用于安排学习。

三个代表入口是 [P1 的函数返回](../../course/foundations/p01.md)、[W1 的 Tensor 布局](../../weeks/week-01-foundations/session-02.md) 和 [W8 的请求时间线](../../weeks/week-08-serving-baseline/session-01.md)。前者先追踪函数返回到变量的值；布局页按 shape/stride 计算位置；请求页区分首 token、末 token 与协议结束。

## 基础与系统衔接逐页记录

每行均检查了正文、术语、示例、练习、核对说明、图片引用及继续学习入口。图片完整文件名可在课页图注打开，下面只列同名 PNG/SVG 的名称。

| 页面 | 讲清的问题 | 原创图 |
| --- | --- | --- |
| [P1](../../course/foundations/p01.md) | 函数调用与返回 | p01-function-call |
| [P2](../../course/foundations/p02.md) | 条件与边界 | p02-branch-boundary |
| [P3](../../course/foundations/p03.md) | 循环与容器访问 | p03-loop-state |
| [P4](../../course/foundations/p04.md) | 异常传播与处理 | p04-exception-path |
| [P5](../../course/foundations/p05.md) | 导入与程序入口 | p05-module-entry |
| [P6](../../course/foundations/p06.md) | 读写文件与进程退出 | p06-file-lifetime |
| [P7](../../course/foundations/p07.md) | 参数、配置、日志与测试 | p07-tool-parts |
| [P8](../../course/foundations/p08.md) | 实例状态与方法调用 | p08-instance-state |
| [S1](../../course/bridges/s01.md) | CPU 进程、线程与 GPU 提交 | s01-process-device |
| [S2](../../course/bridges/s02.md) | 请求路径、端口、带宽与延迟 | s02-request-path、s02-latency-bandwidth |
| [S3](../../course/bridges/s03.md) | 镜像、容器与端口映射 | s03-container-port |
| [S4](../../course/bridges/s04.md) | Dataset、batch、传输与等待 | s04-data-pipeline |
| [S5](../../course/bridges/s05.md) | 持久化卷与恢复 | s05-persistence |
| [S6](../../course/bridges/s06.md) | 任务依赖与 Kubernetes 对象 | s06-task-dependencies、s06-kubernetes-objects |

## W 单元逐页记录

保留学习顺序 W1→W2→W3→W4→W5→W6→W13→W7→W8→W9→W10→W11→W12→W14→W15→W16。每行的六页均已检查；48 个小节使用本节图、跨课引用、必要的表格或保留的简短 Mermaid，不另画重复概念。context 的事实仍对应原有快照日期，不能作为今天的新结论。

| 单元 | 已检查页面 | 图文核对重点 |
| --- | --- | --- |
| W1 | [入口](../../weeks/week-01-foundations/README.md) · [第1段](../../weeks/week-01-foundations/session-01.md) · [第2段](../../weeks/week-01-foundations/session-02.md) · [第3段](../../weeks/week-01-foundations/session-03.md) · [掌握检查](../../weeks/week-01-foundations/assessment.md) · [选读背景](../../weeks/week-01-foundations/context.md) | 元素/字节、stride、共享与复制、Linear 形状 |
| W2 | [入口](../../weeks/week-02-cuda-execution/README.md) · [第1段](../../weeks/week-02-cuda-execution/session-01.md) · [第2段](../../weeks/week-02-cuda-execution/session-02.md) · [第3段](../../weeks/week-02-cuda-execution/session-03.md) · [掌握检查](../../weeks/week-02-cuda-execution/assessment.md) · [选读背景](../../weeks/week-02-cuda-execution/context.md) | 线程覆盖、尾部保护与异步计时 |
| W3 | [入口](../../weeks/week-03-reduction-profiling/README.md) · [第1段](../../weeks/week-03-reduction-profiling/session-01.md) · [第2段](../../weeks/week-03-reduction-profiling/session-02.md) · [第3段](../../weeks/week-03-reduction-profiling/session-03.md) · [掌握检查](../../weeks/week-03-reduction-profiling/assessment.md) · [选读背景](../../weeks/week-03-reduction-profiling/context.md) | 局部归约、warp 合并、同步与 CPU 收尾 |
| W4 | [入口](../../weeks/week-04-gemm/README.md) · [第1段](../../weeks/week-04-gemm/session-01.md) · [第2段](../../weeks/week-04-gemm/session-02.md) · [第3段](../../weeks/week-04-gemm/session-03.md) · [掌握检查](../../weeks/week-04-gemm/assessment.md) · [选读背景](../../weeks/week-04-gemm/context.md) | 矩阵地址、tile 复用、理论 Roofline |
| W5 | [入口](../../weeks/week-05-triton-softmax/README.md) · [第1段](../../weeks/week-05-triton-softmax/session-01.md) · [第2段](../../weeks/week-05-triton-softmax/session-02.md) · [第3段](../../weeks/week-05-triton-softmax/session-03.md) · [掌握检查](../../weeks/week-05-triton-softmax/assessment.md) · [选读背景](../../weeks/week-05-triton-softmax/context.md) | 稳定 Softmax 与分块状态重缩放 |
| W6 | [入口](../../weeks/week-06-attention/README.md) · [第1段](../../weeks/week-06-attention/session-01.md) · [第2段](../../weeks/week-06-attention/session-02.md) · [第3段](../../weeks/week-06-attention/session-03.md) · [掌握检查](../../weeks/week-06-attention/assessment.md) · [选读背景](../../weeks/week-06-attention/context.md) | Q/K/V、mask、Attention 与 Block 残差 |
| W13 | [入口](../../weeks/week-13-systems/README.md) · [第1段](../../weeks/week-13-systems/session-01.md) · [第2段](../../weeks/week-13-systems/session-02.md) · [第3段](../../weeks/week-13-systems/session-03.md) · [掌握检查](../../weeks/week-13-systems/assessment.md) · [选读背景](../../weeks/week-13-systems/context.md) | 表达式/图/kernel、首次与稳态、编译回本 |
| W7 | [入口](../../weeks/week-07-collectives/README.md) · [第1段](../../weeks/week-07-collectives/session-01.md) · [第2段](../../weeks/week-07-collectives/session-02.md) · [第3段](../../weeks/week-07-collectives/session-03.md) · [掌握检查](../../weeks/week-07-collectives/assessment.md) · [选读背景](../../weeks/week-07-collectives/context.md) | rank 输出、归约再收集、物理拓扑 |
| W8 | [入口](../../weeks/week-08-serving-baseline/README.md) · [第1段](../../weeks/week-08-serving-baseline/session-01.md) · [第2段](../../weeks/week-08-serving-baseline/session-02.md) · [第3段](../../weeks/week-08-serving-baseline/session-03.md) · [掌握检查](../../weeks/week-08-serving-baseline/assessment.md) · [选读背景](../../weeks/week-08-serving-baseline/context.md) | prefill/decode、首 token、末 token 与结束事件 |
| W9 | [入口](../../weeks/week-09-kv-cache/README.md) · [第1段](../../weeks/week-09-kv-cache/session-01.md) · [第2段](../../weeks/week-09-kv-cache/session-02.md) · [第3段](../../weeks/week-09-kv-cache/session-03.md) · [掌握检查](../../weeks/week-09-kv-cache/assessment.md) · [选读背景](../../weeks/week-09-kv-cache/context.md) | KV 逻辑块、物理块、共享与缓存对照 |
| W10 | [入口](../../weeks/week-10-serving-benchmark/README.md) · [第1段](../../weeks/week-10-serving-benchmark/session-01.md) · [第2段](../../weeks/week-10-serving-benchmark/session-02.md) · [第3段](../../weeks/week-10-serving-benchmark/session-03.md) · [掌握检查](../../weeks/week-10-serving-benchmark/assessment.md) · [选读背景](../../weeks/week-10-serving-benchmark/context.md) | 负载、等待、token 预算、吞吐与尾延迟 |
| W11 | [入口](../../weeks/week-11-ddp/README.md) · [第1段](../../weeks/week-11-ddp/session-01.md) · [第2段](../../weeks/week-11-ddp/session-02.md) · [第3段](../../weeks/week-11-ddp/session-03.md) · [掌握检查](../../weeks/week-11-ddp/assessment.md) · [选读背景](../../weeks/week-11-ddp/context.md) | 样本划分、局部梯度、同步与更新 |
| W12 | [入口](../../weeks/week-12-fsdp/README.md) · [第1段](../../weeks/week-12-fsdp/session-01.md) · [第2段](../../weeks/week-12-fsdp/session-02.md) · [第3段](../../weeks/week-12-fsdp/session-03.md) · [掌握检查](../../weeks/week-12-fsdp/assessment.md) · [选读背景](../../weeks/week-12-fsdp/context.md) | 稳态分片、按需聚合、恢复后的下一步 |
| W14 | [入口](../../weeks/week-14-parallelism/README.md) · [第1段](../../weeks/week-14-parallelism/session-01.md) · [第2段](../../weeks/week-14-parallelism/session-02.md) · [第3段](../../weeks/week-14-parallelism/session-03.md) · [掌握检查](../../weeks/week-14-parallelism/assessment.md) · [选读背景](../../weeks/week-14-parallelism/context.md) | TP 矩阵切分与求和、PP 微批次时间线 |
| W15 | [入口](../../weeks/week-15-ray/README.md) · [第1段](../../weeks/week-15-ray/session-01.md) · [第2段](../../weeks/week-15-ray/session-02.md) · [第3段](../../weeks/week-15-ray/session-03.md) · [掌握检查](../../weeks/week-15-ray/assessment.md) · [选读背景](../../weeks/week-15-ray/context.md) | Task、Actor、ObjectRef、资源等待与失败 |
| W16 | [入口](../../weeks/week-16-scheduling/README.md) · [第1段](../../weeks/week-16-scheduling/session-01.md) · [第2段](../../weeks/week-16-scheduling/session-02.md) · [第3段](../../weeks/week-16-scheduling/session-03.md) · [掌握检查](../../weeks/week-16-scheduling/assessment.md) · [选读背景](../../weeks/week-16-scheduling/context.md) | FIFO/SJF 任务身份、等待、估计误差与公平性 |

## 其他当前页面

| 文件组 | 已检查页面 | 处理 |
| --- | --- | --- |
| 首页 | [README.md](../../README.md) | 直接进入当前学习位置 |
| 课程入口 | [course/reviews.md](../../course/reviews.md) · [course/prerequisites.md](../../course/prerequisites.md) · [course/README.md](../../course/README.md) · [course/guide.md](../../course/guide.md) · [course/foundations/README.md](../../course/foundations/README.md) · [course/environment.md](../../course/environment.md) · [course/bridges/README.md](../../course/bridges/README.md) | 合并共用说明；先修训练与综合复习接入图解 |
| 个人进度 | [course/progress.md](../../course/progress.md) | 只读核对；W1 进行中，其余未开始；内容保持不变 |
| 来源索引 | [resources/training.md](../../resources/training.md) · [resources/optional.md](../../resources/optional.md) · [resources/scheduling.md](../../resources/scheduling.md) · [resources/serving.md](../../resources/serving.md) · [resources/README.md](../../resources/README.md) · [resources/gpu.md](../../resources/gpu.md) · [resources/models.md](../../resources/models.md) · [resources/foundations.md](../../resources/foundations.md) | 保留资源 ID、原始链接和指定范围，中文说明改为具体阅读问题 |
| 维护 | [docs/README.md](../../docs/README.md) · [docs/maintenance.md](../../docs/maintenance.md) · [docs/coverage.md](../../docs/coverage.md) · [docs/design.md](../../docs/design.md) | 四份根文档维持职责；图形规则与准备状态写回现有文件 |
| 模板 | [templates/weekly-refresh.md](../../templates/weekly-refresh.md) · [templates/week-plan.md](../../templates/week-plan.md) · [templates/experiment-report.md](../../templates/experiment-report.md) · [templates/paper-note.md](../../templates/paper-note.md) · [templates/study-session.md](../../templates/study-session.md) | 以后新增的小节与记录沿用个人表达和图文规则 |
| 练习与成果 | [projects/README.md](../../projects/README.md) · [labs/README.md](../../labs/README.md) · [exercises/README.md](../../exercises/README.md) · [exercises/foundations/independent-tool.md](../../exercises/foundations/independent-tool.md) | 区分待补全输入、独立实现与真实记录；P6 字典输入和 P7 顶层列表分别说明 |

## 图形导出与实际视觉检查

48 张原创图各保存一份 PNG 与同名 SVG，共 96 个导出文件；布局和文字由 [render_figures.py](../../scripts/render_figures.py) 维护。使用本机微软雅黑 `C:/Windows/Fonts/msyh.ttc`，无外部截图或课件搬运。PNG 宽度 1400 px；SVG 可放大查看。

全部 48 张已查看正常尺寸导出，并查看约 600 px 宽缩放预览；检查中文、数字、上下标写法、箭头、边框、裁切和间距。改过的图片重新导出再看。缺字形和文字超出画布会使导出中止；这些自动检查不代替人工看图。临时缩放图与联系表放在仓库外，未加入第二套图片。

图中所有性能数字明确标为理论或假设例子，没有生成真实测量曲线。固定配色之外仍保留对象名、箭头与线型。每张图有替代文本、图注、读图方向、暂停题，公式和关键数字也保留在正文。

核对中修正了以下容易误解之处：

- 异常沿调用栈传播，不能用函数返回值的说法解释；Linear 矩阵乘积之后还要逐行加 bias。
- Kubernetes 的 Job 与 Deployment 对应两个不同例子的 Pod，避免暗示两者共同拥有同一个 Pod。
- Attention 的 Q 与 K 是两个输入，乘号不画成 Q 生成 K 的箭头；Block 的两条残差分别回到正确加法位置。
- AllReduce 的归约分片再收集只是概念分解，没有标成某次 NCCL 的实际算法轨迹。
- W8 检查题区分末 token 的 180 ms 与协议结束的 200 ms；TPOT 使用四个 token 间隔，端到端时间单列。
- W13 区分“首次调用比原来多花的时间”与“另计的编译开销”：前者只由后续 N−1 次节省摊平，后者由 N 次稳态执行节省摊平。
- TP 的第一层按列切、第二层按行切；PP 图的微批次编号与正文一致，前向示意不当完整训练时间线。
- FIFO/SJF 的等待数组按 A/B/C 身份列出，不按执行顺序混写；有限轨迹不证明无饥饿。
- 标量训练图与代码统一为 weight=1、梯度 −16、学习率 0.1、一步更新到 2.6。

## 已做的检查与保留边界

- `python scripts/check_docs.py`：157 份 Markdown、1760 个本地链接、16 个单元、48 处图片引用、48 组 PNG/SVG，0 个错误。覆盖链接/锚点/大小写、围栏、折叠块、课间导航、替代文本和图片配对；外部链接不在这个离线检查的可访问性结论内。
- `git -c core.autocrlf=false diff --check` 通过；仓库保持未提交状态，没有创建分支或推送。
- 全量图形导出成功：48 组；缺字形与文字越界检查通过。
- 两个 Python 工具用 AST 做语法检查，通过；未执行待补全练习作为个人解答。
- 用 Python 标准库重算了 19 项示意计算，包括字节/stride、三组线程覆盖、归约、tile 字节、Softmax 状态合并、集合通信、时间戳、梯度、两种回本口径、TP 数值等价、PP 占用与 FIFO/SJF 等待，全部通过。这不是硬件性能实验。
- 对保存的正文快照核对，原有 HTTP(S) 来源链接没有丢失，可执行代码块没有删改；图文增加使用独立示例，原有实验要求继续保留。
- 当前正文检索未发现角色化管理词语或“练习梯度、能力关卡、证据位置”等表达。
- 个人进度与此次改写前的内容一致；历史核验记录和原始运行记录未改动。未创建空实验或占位结果。

原始材料的预读状态沿用各自日期记录；本记录没有重新声称所有外部论文、视频或网页都已预读。视频画面与分钟轴仍待核验；GPU、CUDA、Triton、NCCL、多卡、Docker 和集群操作未在这次图文检查中运行。源码语法与文档检查不代表这些实验已通过，也不代表个人已经掌握。
