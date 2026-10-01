# AI Infra Learning Lab

这是一个供个人独立学习、练习和复盘的 AI Infra 项目。前 8 个单元学习张量、GPU 编程、性能分析、编译和通信，后 8 个单元学习推理、训练和调度。各单元约 10.5～13.5 小时，完整主线约 178.5 小时；先修补学和首次环境配置另计。按每周 9 小时约需 20 周，再预留 2～4 周返工；实验未完成就顺延。

学习顺序：**必要前置 → CUDA 与性能分析 → Triton 与 Attention → torch.compile → 集合通信 → 推理服务 → 分布式训练 → 调度。**

课程、文档、论文和代码按具体问题放在一起：读完一小段，就做一个对应的练习。所有 16 个单元的目标、前置、阅读、图解与自查已整理；前八个学习位置保留 24 份详细分段文件，后八个在各单元学习指南中展开。W1 已开始学习，学习练习与 GPU 实验尚未开始。

重点是 GPU / LLM 系统性能工程。容器、生产集群和平台运维在后续可选拓展中展开。调整后的顺序、阶段要求和分支选择见 [完整学习设计](docs/curriculum-design.md)，修改理由见 [安排审查](docs/plan-review.md)。

## 从这里开始

1. 先做 [先修检查](docs/prerequisites.md)，再从 [前八个学习位置的 24 段学习指南](docs/first-eight-weeks.md) 打开当前段；首次学习从 [W1 第一段](weeks/week-01-foundations/session-01.md) 开始。全程对应关系和剩余限制见 [16 单元覆盖检查](docs/coverage-review.md)，前八个单元另有 [逐段检查](docs/first-eight-weeks-review.md)。
2. 每次开始新单元，用 [学习前的资料复核](docs/weekly-refresh.md) 核对必读材料的版本和运行条件；实验怎么记录见 [学习方式](docs/learning-workflow.md)。
3. 参照 [环境与硬件安排](docs/environment.md) 选择执行环境；目前尚未安装或验证 GPU 工具链。
4. 在 [进度表](docs/progress.md) 记录开始学习日期、资料更新、实验与报告。

## 16 个单元的学习顺序

W1～W16 是固定单元编号。**W13 的编译实验已移到 W6 后面**，因此编号与实际学习周数不同；按下表和页面底部的“下一单元”推进。

| 建议学习周 | 单元 | 主题 | 要回答的问题 | 完成什么 |
| --- | --- | --- | --- | --- |
| 1 | [W1](weeks/week-01-foundations/README.md) | C++ / Tensor / 资源计算 | 一个 Tensor 和 Linear 层消耗什么资源？ | 资源账本与核对脚本 |
| 2 | [W2](weeks/week-02-cuda-execution/README.md) | GPU 执行与内存 | 线程如何覆盖数据，怎样可靠计时？ | Vector Add 正确性与带宽报告 |
| 3 | [W3](weeks/week-03-reduction-profiling/README.md) | Reduce 与 Profiler | 性能瓶颈的证据在哪里？ | 两种 Reduce 与分析报告 |
| 4 | [W4](weeks/week-04-gemm/README.md) | GEMM 与数据复用 | Tiling 减少了哪些访存？ | 朴素与分块 GEMM 对照 |
| 5 | [W5](weeks/week-05-triton-softmax/README.md) | Triton / Online Softmax | 融合如何减少数据搬运？ | 稳定 Softmax 与性能曲线 |
| 6 | [W6](weeks/week-06-attention/README.md) | Attention / 模型 Profiling | Decoder Block 的资源花在哪里？ | 计算、显存与耗时账本 |
| 7 | [W13](weeks/week-13-systems/README.md) | torch.compile / Systems 综合实验 | 框架优化如何影响模型性能？ | eager/compile 与模型区段对照 |
| 8 | [W7](weeks/week-07-collectives/README.md) | NCCL / 集合通信 | 增加 GPU 为什么不一定更快？ | 2 卡基线，4 卡作为扩展 |
| 9 | [W8](weeks/week-08-serving-baseline/README.md) | vLLM 服务基线 | 怎样定义可信的推理性能？ | 小模型服务与压测报告 |
| 10 | [W9](weeks/week-09-kv-cache/README.md) | KV Cache / PagedAttention | 前缀缓存在什么负载下有效？ | 冷热缓存受控实验 |
| 11 | [W10](weeks/week-10-serving-benchmark/README.md) | 推理负载与调优 | 吞吐增加时牺牲了什么？ | mini-serving-benchmark |
| 12 | [W11](weeks/week-11-ddp/README.md) | DDP / 梯度同步 | 多卡训练比较怎样保持公平？ | 固定全局 batch 的扩展性报告 |
| 13 | [W12](weeks/week-12-fsdp/README.md) | FSDP2 / ZeRO / 恢复 | 省下的显存换来了哪些通信？ | DDP/FSDP2 与恢复对照 |
| 14 | [W14](weeks/week-14-parallelism/README.md) | TP / PP / Megatron | 切分一个层会产生哪些通信？ | 并行切分图与小型验证 |
| 15 | [W15](weeks/week-15-ray/README.md) | Ray Task / Actor / Resource | 资源声明如何影响执行？ | 单机任务执行与排队记录 |
| 16 | [W16](weeks/week-16-scheduling/README.md) | 调度策略与评估 | FIFO 与短作业优先适合什么负载？ | mini-gpu-scheduler |

前 8 个学习位置对应 W1～W6、W13、W7；后 8 个对应其余单元。W6 不要求完整实现 FlashAttention2；W13 使用本仓库的编译对照练习，CS336 子题留作可选拓展。每个单元是否能开始，以 [先修条件](docs/prerequisites.md) 为准。

## 每个单元怎样学习

| 文件 | 什么时候看 | 里面有什么 |
| --- | --- | --- |
| `README.md` | 开始前和验收时 | 问题、范围、练习和完成要求 |
| `context.md` | 基础通过后按需选读 | 当前常用做法、一个值得关注的进展、硬件条件，以及从论文到实际使用还缺什么 |
| `study-guide.md` | 每次学习时 | 目标与前置检查；前八单元为三段导航，后八单元直接展开图解、自查与练习 |
| `session-01.md`～`session-03.md`（前八单元） | 每段学习时 | 阅读起止、概念与图例、预测题和核对、动手与完成要求、可选 AI 提示词 |
| `refresh-YYYY-MM-DD.md` | 开始学习核验后创建 | 这次更新了什么、为什么保留或替换资料 |

每个单元仍是 3 段。原文选读多数为 150 分钟，W8 为 180、W12 为 195、W16 为 90；图解与自查另计，详见 [完整时间表](docs/study-guide.md#time-budget)。所有资源按知识点登记 [难度、语言、阅读范围和停止位置](resources/README.md)；未经核对的视频时间戳不填写。

全部学习单元按独立自学设计：先读指定材料，写下预测，再展开核对说明并运行练习。图解帮助追踪地址、形状、数据流或执行顺序；每段的 AI 理解提示词可全部跳过。对照段内要求自查后继续，具体方法见 [自学说明](docs/study-guide.md)。

基础概念先用小例子与官方教程理解，再读论文中的机制。context 的相关进展属于可选拓展，不作为刚入门时的必读或完成门槛。

## 目录

```text
infra-learning/
├── README.md
├── docs/                 路线设计、学习方法、环境、进度与更新流程
├── weeks/
│   ├── week-01-foundations/
│   │   ├── README.md
│   │   ├── context.md
│   │   ├── study-guide.md
│   │   ├── session-01.md～session-03.md
│   │   └── refresh-YYYY-MM-DD.md
│   └── ...
├── resources/            基础课程与前沿来源索引
├── labs/                 开始实验时创建实现目录
├── projects/             复用实验，整理跨单元成果
└── templates/            实验、论文与资料更新记录
```

[分段学习指南导航](docs/study-guide.md) 按推荐顺序列出所有练习。[基础资源](resources/README.md) 保存课程入口，[进展索引](resources/frontier-watchlist.md) 保存当前观察对象。代码只保留一份，各单元通过链接引用；目录、段号和运行归档约定见 [项目结构与文件管理](docs/repository-layout.md)；实验与复用入口见 [labs](labs/README.md) 和 [projects](projects/README.md)。

## 发布到 GitHub

远程仓库为 [zixin0v0/infra-weekly-learning](https://github.com/zixin0v0/infra-weekly-learning)，默认分支为 `main`。学习指南、来源版本、原创示意图和真实小型实验记录纳入版本管理；推送与忽略约定见 [发布说明](docs/github-publishing.md)。
