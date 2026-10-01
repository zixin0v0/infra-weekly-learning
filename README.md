# AI Infra Learning Lab

这是一份边学边做的 AI Infra 学习计划。前 8 个单元学习张量、GPU 编程、性能分析、编译和通信，后 8 个单元学习推理、训练和调度。每单元先按 9 小时安排，没有完成实验就顺延；日历预留 2～4 周用于配置环境和返工，先修补课另计。

学习顺序：**必要前置 → CUDA 与性能分析 → Triton 与 Attention → torch.compile → 集合通信 → 推理服务 → 分布式训练 → 调度。**

课程、文档、论文和代码按具体问题放在一起：读完一小段，就做一个对应的练习。前八个学习位置的 24 段备课与 2026-10-01 资料复核已准备；W1 已开课，学习练习与 GPU 实验尚未开始。

重点是 GPU / LLM 系统性能工程。容器、生产集群和平台运维在后续选修中展开。调整后的顺序、阶段要求和分支选择见 [完整学习设计](docs/curriculum-design.md)，修改理由见 [安排审查](docs/plan-review.md)。

## 从这里开始

1. 先做 [先修检查](docs/prerequisites.md)，再从 [前八个学习位置的 24 段备课](docs/first-eight-weeks.md) 打开当前段；今天从 [W1 第一段](weeks/week-01-foundations/session-01.md) 开始。
2. 每次开始新单元，用 [开课前的资料更新](docs/weekly-refresh.md) 核对版本与新进展；实验怎么记录见 [学习方式](docs/learning-workflow.md)。
3. 参照 [环境与硬件安排](docs/environment.md) 选择执行环境；目前尚未安装或验证 GPU 工具链。
4. 在 [进度表](docs/progress.md) 记录开课日期、资料更新、实验与报告。

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

前 8 个学习位置对应 W1～W6、W13、W7；后 8 个对应其余单元。W6 不要求完整实现 FlashAttention2；W13 使用本仓库的编译对照练习，CS336 子题留作选修。每个单元是否能开始，以 [先修条件](docs/prerequisites.md) 为准。

## 每个单元怎样学习

| 文件 | 什么时候看 | 里面有什么 |
| --- | --- | --- |
| `README.md` | 开始前和验收时 | 问题、范围、练习和完成要求 |
| `context.md` | 开始前的 30 分钟 | 当前常用做法、一个值得关注的进展、硬件条件，以及从论文到实际使用还缺什么 |
| `study-guide.md` | 每次学习时 | 三段概览、衔接与详细备课入口 |
| `session-01.md`～`session-03.md` | 每段开始时 | 精确起止、中文助读、预测题、练习边界与检查条件 |
| `refresh-YYYY-MM-DD.md` | 开课核验后创建 | 这次更新了什么、为什么保留或替换资料 |

每个单元仍是 3 段，视频、文档和论文的阅读预算合计 150 分钟。官方英文视频配中文说明；文档定位到标题，论文定位到小节或算法。未经核对的视频时间戳不填写。

例如 W1 先学 Tensor 的类型、视图和字节计算，再用一个低位宽存储算例了解打包和 scale 的额外开销；不会在第一周加入完整量化项目。前沿内容帮助理解当前问题，每周只选一个，随开课日期重新核验。

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

[章节导学导航](docs/study-guide.md) 按推荐顺序列出所有练习。[基础资源](resources/README.md) 保存课程入口，[进展索引](resources/frontier-watchlist.md) 保存当前观察对象。代码只保留一份，各单元通过链接引用；目录、段号和运行归档约定见 [项目结构与文件管理](docs/repository-layout.md)；实验与复用入口见 [labs](labs/README.md) 和 [projects](projects/README.md)。

## 发布到 GitHub

远程仓库为 [zixin0v0/infra-weekly-learning](https://github.com/zixin0v0/infra-weekly-learning)，默认分支为 `main`。备课、来源版本、原创示意图和真实小型实验记录纳入版本管理；推送与忽略约定见 [发布说明](docs/github-publishing.md)。
