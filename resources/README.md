# 资源索引与核验记录

日常从 [章节导学导航](../docs/study-guide.md) 进入，不按这个索引从头到尾刷完资料。这里维护来源与核验状态；各周 `study-guide.md` 指定章节、联读关系、暂停练习和阅读预算，周 README 保留最终验收。

前八个学习位置已准备 [24 段详细备课与 8 份资料复核](../docs/first-eight-weeks.md)。代码阅读提交、论文版本、网页版本、访问日与设备限制以各周复核记录为准；实际开课仍须重查，资料版本不代替已安装版本。

资源选择：**官方英文视频为主，配中文阅读指引；官方文档核对实现；作者博客与论文解释机制；GitHub 项目辅助实践。**

涉及当前工程做法、新实现和硬件限制的资料放在 [进展索引](frontier-watchlist.md)。开课时按 [更新流程](../docs/weekly-refresh.md) 重查；原课程继续用于学习原理，不因版本变新就整套重学。

## 核验范围

核验日期：2026-10-01。

- “页面已读”：本轮读取了官方页面、项目 README、目录或论文摘要页，确认标题与主题；不表示完整教程已运行。
- “视频元数据已核对”：官方视频标题和发布者/关联课程能从页面或搜索结果核对；未在本机验证播放、字幕或完整观看。
- “官方入口已核对”：官方课程或仓库链接到该频道/播放列表，讲次由官方课程表确认；未逐集验证播放。
- 本轮进一步读取了 Online normalizer、FlashAttention、PagedAttention、ZeRO、Megatron 的 PDF 指定部分，核对章节/算法位置；不宣称精读全文。FlashAttention-2 与 Ray 论文仍主要核验摘要入口。
- 本轮没有执行外部整份项目、安装依赖或运行学习实验。W1 另做了 C++/PyTorch CPU 最小烟雾检查，证据见 [开课记录](../weeks/week-01-foundations/refresh-2026-10-01.md)。所有主线文档与论文链接均来自实际读取的来源；资源可访问性仍可能受网络和上游修改影响。

## 课程与视频

时间预算见周页面，和视频完整时长不同。无需先学完整门课程再动手。

| 资源与入口 | 版本/语言 | 对应周与使用方式 | 核验状态 |
| --- | --- | --- | --- |
| [CS106L Spring 2026 归档](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/) | 2026 春季，英文讲义 | W1：类型、引用、指针；按需查 RAII | 页面已读；主站已切到 Fall 2026，使用归档 |
| [CS336 课程主页](https://cs336.stanford.edu/) · [2026 官方播放列表](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV) | Spring 2026，英文 | 全程按指定讲次使用 | 官方课程表与列表入口已核对 |
| [CS336 Lecture 2: PyTorch (einops)](https://www.youtube.com/watch?v=kuYAsz7zspQ) | Spring 2026，英文 | W1：Tensor 与资源估算；W4：算术强度与 Roofline | 视频元数据已核对，讲义函数已读 |
| [CS336 Lecture 5: GPUs, TPUs](https://www.youtube.com/watch?v=izZba4UA7iY) | Spring 2026，英文 | W4 硬件概念补充；主线优先精读 L2 的相关函数 | 视频元数据已核对 |
| [CS336 Lecture 6: Kernels, Triton, XLA](https://www.youtube.com/watch?v=xnDHaNUvHBg) | Spring 2026，英文 | W3 测量、W5 Triton、W13 编译；W6 按需复习 | 视频元数据已核对，讲义函数已读；不另加 XLA 专题 |
| [CS336 Lecture 7 讲义代码](https://github.com/stanford-cs336/lectures/blob/main/lecture_07.py) · [Lecture 8 讲义](https://github.com/stanford-cs336/lectures/blob/main/lecture_08.pdf) | Spring 2026，英文 | W7 collective、W14 TP/PP 以 L7 函数定位；L8 进阶 | L7 指定函数已读；L8 入口已核对；未逐段核验视频 |
| [CS336 Lecture 10: Inference](https://www.youtube.com/watch?v=EfM546A79aM) | Spring 2026，英文 | W8～10：推理机制与开销 | 视频标题页已核对 |
| [GPU MODE 官方频道](https://www.youtube.com/@GPUMODE) · [讲义仓库](https://github.com/gpu-mode/lectures) | 英文；各讲按原发布版本 | W2、3、7：CUDA、profiling、collective | 官方入口与讲义目录已核对 |
| [Jeremy Howard: Getting Started With CUDA for Python Programmers](https://www.youtube.com/watch?v=nOxKexn3iBo) | 2024，英文 | W2：GPU MODE 第 3 讲相关入门视频 | 视频元数据已核对 |
| [PyTorch DDP 官方视频教程入口](https://docs.pytorch.org/tutorials/beginner/ddp_series_intro.html) | 英文，在线教程 | W11：按卡点选单机多卡和数据划分 | 页面已读；未逐集播放 |

GPU MODE 第 1 讲的标题在仓库中是 Profiling and Integrating CUDA kernels in PyTorch，也可按 How to profile CUDA kernels in PyTorch 查找。这里使用官方频道与讲义入口，不将本轮抓取失败的单集页面标为已确认可播放。

## 官方教程与参考文档

除 Tensor Views 固定到本次读取的 2.14 页面外，以下多数是可变的在线文档。核验状态为“页面已读”；真正实现时要与安装版本匹配，不把本次页面版本当作已安装环境。

| 文档 | 周次 | 用来解决的问题 |
| --- | --- | --- |
| [PyTorch Tensor Views](https://docs.pytorch.org/docs/2.14/tensor_view.html) | W1 | 布局、视图和复制语义 |
| [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/) | W2 | 执行模型、内存与同步 |
| [CUDA Best Practices Guide](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html) | W4 | 合并访存、共享内存与数据复用 |
| [Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html) | W3 | 指标含义与性能证据 |
| [Triton Vector Addition](https://triton-lang.org/main/getting-started/tutorials/01-vector-add.html) | W5 | program、数据块与 mask |
| [Triton Fused Softmax](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html) | W5 | 逐行归约与融合基线 |
| [PyTorch Profiler](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html) | W3、6 | 模型区段、算子与 trace |
| [PyTorch SDPA 教程](https://docs.pytorch.org/tutorials/intermediate/scaled_dot_product_attention_tutorial.html) | W6 | Attention 接口与后端行为 |
| [NCCL Collective Operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html) | W7 | 各 rank 的输入输出语义 |
| [PyTorch DDP 入门](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html) | W7、11 | 进程组与梯度同步 |
| [vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/) | W8 | 服务启动与请求路径 |
| [vllm bench serve](https://docs.vllm.ai/en/latest/cli/bench/serve/) | W8、10 | 负载控制与指标定义 |
| [vLLM Automatic Prefix Caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/) | W9 | 前缀复用与缓存实验 |
| [vLLM Optimization and Tuning](https://docs.vllm.ai/en/latest/configuration/optimization/) | W10 | 选择一个可解释的调优变量 |
| [PyTorch FSDP2](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) | W12 | fully_shard 与分片训练 |
| [PyTorch Distributed Checkpoint](https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html) | W12 | 分布式状态保存与恢复 |
| [Megatron Bridge Parallelisms Guide](https://docs.nvidia.com/nemo/megatron-bridge/latest/parallelisms.html) | W14 | 理解并行维度与组合方式 |
| [What's Ray Core?](https://docs.ray.io/en/latest/ray-core/walkthrough.html) | W15 | Task、Actor 与依赖关系 |
| [Ray Resources](https://docs.ray.io/en/latest/ray-core/scheduling/resources.html) | W15 | 逻辑资源与执行约束 |
| [Ray Scheduling](https://docs.ray.io/en/latest/ray-core/scheduling/index.html) | W15～16 | 调度可行性与放置策略 |
| [Ray Placement Groups](https://docs.ray.io/en/latest/ray-core/scheduling/placement-group.html) | W16 | 资源 bundle 与成组预留 |

环境资料另见 [环境安排](../docs/environment.md)，其中包括 CUDA on WSL、Triton 兼容说明与 vLLM GPU 安装要求。

## 博客：有具体疑问时再读

每两周最多额外选一篇；可以复用同一篇，不另行叠加阅读预算。四篇均已读取作者/项目原始页面。

| 博客 | 来源与年份 | 周次与作用 |
| --- | --- | --- |
| [An Even Easier Introduction to CUDA](https://developer.nvidia.com/blog/even-easier-introduction-cuda/) | NVIDIA，带更新的文章 | W2：形成 CPU/GPU 工作分工直觉 |
| [An Efficient Matrix Transpose in CUDA C/C++](https://developer.nvidia.com/blog/efficient-matrix-transpose-cuda-cc/) | NVIDIA，2013 | W4：看懂访存方式与 shared memory padding；性能数字是历史案例 |
| [FlashAttention-2](https://crfm.stanford.edu/2023/07/17/flash2.html) | Stanford CRFM / Tri Dao，2023 | W6、13：理解工作划分带来的影响 |
| [vLLM 与 PagedAttention](https://vllm.ai/blog/2023-06-20-vllm) | vLLM 项目，2023 | W8～9：理解 KV Cache 管理；旧博客不充当当前安装手册 |

## 论文：带着实验问题读

年份采用首次预印本年份；期刊/会议发表年份可能不同。下表保留摘要入口，章节导学直达 PDF 并指定阅读位置。节号按本轮 PDF 核对，版本变化时以标题与算法名复核。阅读记录使用 [论文模板](../templates/paper-note.md)。

| 论文 | 年份 | 周次与限定范围 |
| --- | --- | --- |
| [Online normalizer calculation for softmax](https://arxiv.org/abs/1805.02867) | 2018 | W5：在线更新递推，手算小例子 |
| [FlashAttention](https://arxiv.org/abs/2205.14135) | 2022 | W6：IO 问题与分块算法 |
| [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180) | 2023 | W9：内存管理、分页与共享 |
| [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054) | 2019 | W12：模型状态与分片阶段 |
| [FlashAttention-2](https://arxiv.org/abs/2307.08691) | 2023 | W13 选读：并行与工作划分 |
| [Megatron-LM](https://arxiv.org/abs/1909.08053) | 2019 | W14：单层模型并行切分 |
| [Ray: A Distributed Framework for Emerging AI Applications](https://arxiv.org/abs/1712.05889) | 2017 | W16 选读：历史系统架构，和当前 API 分开理解 |

## GitHub 项目与中文导航

已读取项目 README 或官方目录；没有下载和运行项目。开始复现实验时记录 tag/commit。

| 项目 | 周次 | 使用边界 |
| --- | --- | --- |
| [AIInfraGuide](https://github.com/caomaolufei/AIInfraGuide) · [中文站](https://caomaolufei.github.io/AIInfraGuide/) | 全程按需 | 中文主题导航；本轮只核对主页/仓库目录，不宣称所有章节都有完整正文 |
| [GPU MODE lectures](https://github.com/gpu-mode/lectures) | W2、3、7 | 重点定位 lecture_003、lecture_001、lecture_009、lecture_017 |
| [NVIDIA cuda-samples](https://github.com/NVIDIA/cuda-samples) | W2、4 | 对照入门与矩阵乘法样例，按仓库构建说明操作 |
| [triton-lang/triton](https://github.com/triton-lang/triton) | W5、13 | 教程与兼容信息；不把读编译器源码设为前置 |
| [NVIDIA nccl-tests](https://github.com/NVIDIA/nccl-tests) | W7 | 使用已有通信测量与正确性检查 |
| [CS336 Assignment 2 Systems](https://github.com/stanford-cs336/assignment2-systems/tree/main) | W13 进阶 | 2026 仓库与题面文件入口已核验；本轮 PDF 内容抓取失败，不指定未经核验题号。默认做本仓库 eager/compile 对照 |
| [ray-project/ray](https://github.com/ray-project/ray) | W15～16 | Task/Actor 与调度示例，先通过公开 API 理解行为 |

## 设计审查后的定向补充

补充核验日期：2026-10-01。下列官方教程/作者教材的页面内容已读取，尚未执行代码。它们按对应阶段替换部分重复观看或作为先修补修，不要求额外学完整套课程。单项预算用于选读参考；实际顺序与分配以最新 [章节导学](../docs/study-guide.md) 为准，不与该表累加。先修补修见 [先修检查](../docs/prerequisites.md)。

| 资源 | 类型与语言 | 对应缺口与范围 | 选读预算 |
| --- | --- | --- | --- |
| [Missing Semester 2026 Shell](https://missing.csail.mit.edu/2026/course-shell/) · [Git](https://missing.csail.mit.edu/2026/version-control/) | MIT 课程，英文 | 先修 A：命令环境、版本管理；仅补卡点 | 初次合计 1～2 小时，实践不足时另排 |
| [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | 官方教程，英文，在线版 | 先修 D：建立单卡训练流程 | 先做诊断，零基础单列补修单元 |
| [Autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) · [Optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) | 官方教程，英文，在线版 | 先修 D：梯度、清梯度、参数更新，配小型 MLP | 计入补修单元 |
| [CS336 2026 课程表](https://cs336.stanford.edu/) | 官方课程入口，英文 | 先修 C：Lecture 3 架构，配已有 SDPA 教程；当前仅核验课表入口 | 图与形状推导约 1～2 小时，实践另计 |
| [Compute Sanitizer](https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html) | NVIDIA 工具文档，英文，在线版 | W2 memcheck；W3 共享内存 racecheck 与 synccheck，按平台支持使用 | 每单元约 15 分钟查用法 |
| [Nsight Systems CUDA Trace](https://docs.nvidia.com/nsight-systems/UserGuide/index.html#cuda-trace) | NVIDIA 工具文档，英文，在线版 | W6：CPU 启动、传输、GPU kernel 与等待的时间线 | 30 分钟 |
| [Automatic Mixed Precision](https://docs.pytorch.org/tutorials/recipes/recipes/amp_recipe.html) | PyTorch 教程，英文，在线版 | W11：autocast、梯度缩放与 dtype；FP32 参考保持不变 | 30 分钟 |
| [Performance Tuning Guide](https://docs.pytorch.org/tutorials/recipes/recipes/tuning_guide.html) | PyTorch 指南，英文，在线版 | W11：DataLoader、num_workers、pin_memory；出现等待再做对照 | 15 分钟 |
| [Introduction to torch.compile](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html) | PyTorch 教程，英文，在线版 | W13：编译入口、首次/稳态与 graph break | 按 W13 三段分配 |
| [vLLM Production Metrics](https://docs.vllm.ai/en/latest/usage/metrics/) | 官方文档，英文，在线版 | W10：对照实际版本的服务端指标，配客户端测量 | 45 分钟 |
| [OSTEP — Scheduling Introduction](https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf) | 作者公开教材，英文；不依赖软件版本 | W16：FIFO/SJF、周转时间与假设；再分析 GPU 作业差异 | 60 分钟 |

此前复核时 `vllm bench serve` 曾抓取失败；本轮章节细化已成功读取参数页，核对了到达率、并发上限、结果保存与统计参数。真正开始 W8/W10 时仍以安装版本的 CLI 帮助及对应文档确认；没有生成已运行压测的结论。

## 章节细化后的定向资源

以下材料于 2026-10-01 读取指定内容。加入原因是补齐某一段的解释或定位，不增加每周 150 分钟的主线资料预算。

| 资源 | 使用位置 | 选择理由与范围 |
| --- | --- | --- |
| [CS106L 第 2 讲 PDF](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-02-TypesAndStructs.pdf) · [第 6 讲 PDF](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-06-Iterators.pdf) | W1 第 1 段 | 直接定位类型页与指针页；第 3 讲 PDF 未成功抓取，仅保留课表入口 |
| [CS336 lecture_02.py](https://github.com/stanford-cs336/lectures/blob/main/lecture_02.py) · [lecture_06.py](https://github.com/stanford-cs336/lectures/blob/main/lecture_06.py) · [lecture_10.py](https://github.com/stanford-cs336/lectures/blob/main/lecture_10.py) | W1、3～5、8～10、13 | 函数名使视频与代码可以相互定位；不是已确认的视频章节或时间戳 |
| [NVIDIA Warp-Level Primitives](https://developer.nvidia.com/blog/using-cuda-warp-level-primitives/) | W3 第 2 段 | 寄存器交换、参与 mask 与同步，补齐 warp 归约语义 |
| [NVIDIA Reduction 幻灯片](https://developer.download.nvidia.com/assets/cuda/files/reduction.pdf) | W3 卡点补充 | 仅 Reduction #3 的树形图解；历史性能与隐式 warp 同步写法不照搬 |
| [Scaling Book Part 1: Rooflines](https://jax-ml.github.io/scaling-book/roofline/) | W4 第 3 段 | 只读图解与矩阵乘法小节；连接账本与预测 |
| [Scaling Book Part 7: Inference](https://jax-ml.github.io/scaling-book/inference/) | W8 卡点补充 | 只读推理开篇和优化目标，后续 TPU/多机细节暂缓 |
| [nccl-tests PERFORMANCE.md](https://github.com/NVIDIA/nccl-tests/blob/master/doc/PERFORMANCE.md) | W7 第 2 段 | 直接解释输出列，避免只会运行命令 |
| [PyTorch 单机多卡视频页](https://docs.pytorch.org/tutorials/beginner/ddp_series_multigpu.html) | W11 第 1 段 | 进程组、模型包装、数据划分三个文本章节配官方视频 |

论文位置核对：Online normalizer v2 的 §2/§3/§3.1、FlashAttention 的 §2/§3 与 Algorithm 1、PagedAttention 的 §3/§4.1～4.4、ZeRO v3 的 §3.1～3.2 与 §5.1～5.3、Megatron v4 的 §3；OSTEP 第 7 章 §7.1～7.6 已核对。导学只安排其中与实验相关的范围。

课程代码为本次读取的默认分支，尚未固定 commit；在线 PyTorch、CUDA、vLLM、Ray 文档不代表本地已安装的版本。开始实践时记录版本和 commit，核对 API 后再运行。主线资源以作者/项目官方来源为依据；中文导航仍是按需辅助，不用于替代版本核对。

## 如何补充新资源

每条新资料至少记录：标题、原始链接、类型、语言、年份/版本、对应 Topic、推荐章节、解决的具体问题、预计选读时间与核验日期。

优先替换已有薄弱资料。视频版本变化时核对年份、讲次与配套代码；失效链接先回原作者或官方项目寻找替代入口。后续如加入 B 站译制版，注明原版对应关系与译制身份，不替换官方出处。
