# 章节导学：把资料串成实验

[总路线](../README.md) · [24 段备课入口](first-eight-weeks.md) · [资源来源与核验](../resources/README.md) · [学习与验收](learning-workflow.md)

开始单元前，先用 [更新流程](weekly-refresh.md) 看当周 `context.md`。之后按 `study-guide.md` 一段段学习：读指定内容，回答问题，再动手验证。README 写本周范围和验收要求；这里的练习由本仓库设计，不算课程官方作业。

## 使用方式

每周拆成 3 个学习段。每段先用 30～60 分钟读指定内容，再立即做对应练习，不必等全部资料看完。默认资料时间共 150 分钟，包含视频、文档和论文；实现与正确性检查 3.5 小时，测量分析 2 小时，开课更新和整理报告各 0.5 小时，总计 9 小时起步，环境补修另计。各段的动手任务共同组成原周项目，不是额外增加三个项目。

- **必读**：完成当段指定范围及暂停练习，再进入下一段。
- **遇到问题再看**：只有回答不了该问题时才读，替换原有复习时间。
- **选修**：通过周验收后自选一个方向，另排时间，不影响基础完成状态。
- **重复资源**：只打开本次指定的小节。例如 CS336 第 6 讲分别服务于 W3 的测量、W5 的 Triton 和 W13 的编译比较。

## 一段怎样助读

详细备课按 [统一模板](../templates/session-preparation.md) 编写。先明确一个问题，再分块读指定起止；每到暂停题先写自己的预测和理由。卡住时依次解释关键词、演示一个更小输入、回原始章节，不直接用完整答案替代作答。

三段作答都在该周唯一实验目录的 `notes.md`，按 `WXX-S01`～`WXX-S03` 分节；保存实际阅读位置、原预测、命令、检查结果与一个未解决问题。通过段内检查再进入下一段，最终合成一个周报告。纸面参考值与概念图均需标明推导/示意，不能当实测。

前八个学习位置的详细入口见 [备课总导航](first-eight-weeks.md)，文件职责见 [管理约定](repository-layout.md)。尚未实际开课的资料预查保留日期，届时重新核对环境和版本。

## 定位规则与核验边界

核验日期：2026-10-01。文档使用“原始 URL + 英文章节标题 / 编号 / 函数名”定位；无章节的短文用示例或代码标识定位。论文采用章节、算法编号；PDF 页码如有标明，指阅读器从 1 开始的页序，不是印刷页码。

视频保留官方英文入口，并配已读取的讲义函数或页面范围。这些函数名是**讲义定位词，不是已确认的视频章节名**。本轮未逐段观看或核对字幕时间轴，因此不编造分钟数；可以先在讲义中搜索定位词，再在视频中找到对应讲解，找不到就先按讲义完成该段。文档和论文的具体定位不依赖视频播放。

在线文档与 GitHub 默认分支会变化。开始一周时记录文档版本、代码 commit 和访问日期；标题找不到时先检查版本，不套用另一版的节号。已核验位置和少数尚未确认的入口见资源索引。前八个学习位置本次已固定主要代码阅读 commit 和论文版本。W1 仅完成工具烟雾检查；没有运行学习练习、外部整份示例或 GPU 实验。

## 按学习顺序打开导学

W13 提前到 W6 后，其余顺序不变；W 编号用于保持文件和引用稳定，具体理由见 [路线设计](curriculum-design.md)。

| 周 | 三段内容 | 课后完成 |
| --- | --- | --- |
| [W1](../weeks/week-01-foundations/study-guide.md) | 地址与类型 → Tensor 视图 → 资源账本 | 布局检查与资源计算器 |
| [W2](../weeks/week-02-cuda-execution/study-guide.md) | 线程映射 → 内存与错误 → 计时与带宽 | Vector Add 实验 |
| [W3](../weeks/week-03-reduction-profiling/study-guide.md) | 树形归约 → warp 归约 → profiler 证据 | 两种 Reduce 对照 |
| [W4](../weeks/week-04-gemm/study-guide.md) | 访存地址 → tile 复用 → Roofline 预测 | 朴素/分块 GEMM |
| [W5](../weeks/week-05-triton-softmax/study-guide.md) | Triton 映射 → 稳定融合 → 在线递推 | Softmax 与状态合并 |
| [W6](../weeks/week-06-attention/study-guide.md) | Attention 语义 → IO 算法 → 模型时间线 | Decoder Block 报告 |
| [W13](../weeks/week-13-systems/study-guide.md) | eager/compile → 首次/稳态 → graph break | 编译与模型区段对照 |
| [W7](../weeks/week-07-collectives/study-guide.md) | rank 数据语义 → 通信计量 → 拓扑解释 | AllReduce 曲线 |
| [W8](../weeks/week-08-serving-baseline/study-guide.md) | 推理阶段 → 服务请求 → 基线测量 | 可复现推理服务 |
| [W9](../weeks/week-09-kv-cache/study-guide.md) | 容量与分页 → 共享机制 → APC 对照 | 冷/热前缀缓存实验 |
| [W10](../weeks/week-10-serving-benchmark/study-guide.md) | 负载控制 → 批处理预算 → 服务观测 | mini-serving-benchmark |
| [W11](../weeks/week-11-ddp/study-guide.md) | 进程与数据 → 更新与同步 → 精度和输入路径 | DDP 扩展性报告 |
| [W12](../weeks/week-12-fsdp/study-guide.md) | 状态账本 → fully_shard → 状态恢复 | FSDP2 对照与恢复 |
| [W14](../weeks/week-14-parallelism/study-guide.md) | TP 代数 → 通信与形状 → PP 时间线 | 两层 MLP 切分验证 |
| [W15](../weeks/week-15-ray/study-guide.md) | Task/Actor → 逻辑资源 → 执行日志 | Ray 任务记录器 |
| [W16](../weeks/week-16-scheduling/study-guide.md) | 假设和指标 → FIFO/SJF → 执行层映射 | 调度仿真与评估 |

## 为什么选这些资料

| 调整 | 理由 | 控制范围 |
| --- | --- | --- |
| W3 用 CS336 第 6 讲的测量函数作视频入口 | 与 W5/W13 共用讲义，能精确定位代码；GPU MODE 第 1 讲保留为补充 | 不重复观看整讲 |
| W3 补 NVIDIA warp primitives 博客 | 补齐 shuffle 的参与线程与同步语义 | 只读指定三节；旧 reduction 幻灯片仅帮助理解树形过程 |
| W4 补 Scaling Book 的 Roofline 章节 | 将 FLOPs、搬运量、吞吐预测接到同一个 GEMM 实验 | 只用通用计算模型；不照搬 TPU/其他 GPU 的硬件数字 |
| W7 从仓库首页下沉到 nccl-tests 的 PERFORMANCE.md | 明确实际报表各列的定义 | 只读 Time、两种 bandwidth 与 AllReduce |
| W8 补 Scaling Book 的推理开篇 | 用 W4 的算术强度解释 prefill/decode | 仅作为卡点替换，不要求完整读书 |
| W11 指定 PyTorch 单机多卡视频页 | 直接对照进程组、模型和数据划分三个章节 | 多机和容错扩展后置 |
| W12 联读 FSDP2 的 State Dict 与 DCP 教程 | 避免混用 FSDP1/FSDP2 示例，恢复验证有明确对象 | 同 world size，小型确定性实验 |
| W13 将官方大作业降为进阶 | 当前目标是可完成的编译实验；本轮题面 PDF 章节未成功核验 | 不编造官方题号，不增加大作业要求 |
| W14 用 CS336 第 7 讲可执行函数辅助 TP/PP | 可把切分图对应到张量和 collective | 第 8 讲作为后续深入 |

## 学完一段，记下这几件事

记录：实际读到的标题/函数、自己的一个预测、练习代码入口、检查结果、解释不通的一个问题。读完不等于过关；预测与结果不一致时先解释差异，再增加资料。最后把三段记录合并到 [实验报告](../templates/experiment-report.md)，说明当前做法适合什么条件、还不能得出什么结论，再更新 [进度](progress.md)。
