# 按需选读资料

[资料目录](README.md)

完成基础练习后，再按一个具体疑问选读。这里保留额外来源与历史快照，未选读不影响单元完成；接口和设备条件在实际使用前重新核对。

<a id="x-saved"></a>

### X-SAVED · 反向为什么保留中间 Tensor

W12 完成后可选；进阶；英文；autograd、状态账本。

**来源**：[Hooks for autograd saved tensors](https://docs.pytorch.org/tutorials/intermediate/autograd_saved_tensors_hooks_tutorial.html)。

**读到哪里**：从 Saved tensors 到 Hooks for autograd saved tensors 的 pack/unpack 例子，30 分钟；磁盘 offload 和内存优化实现后置。

**带着什么问题读**：用 x*x 的反向依赖画出必须保留的值，解释 hooks 与 checkpoint 重计算不相同；不加到 W12 必做项。 [打开练习与自查](../weeks/week-12-fsdp/README.md)。

<a id="x-allocator"></a>

### X-ALLOCATOR · 流顺序分配与显存生命周期

W13 后可选；进阶；中文官方博客；W2 stream/event 与同步。

**来源**：[NVIDIA 流顺序分配器 Part 1](https://developer.nvidia.cn/blog/using-cuda-stream-ordered-memory-allocator-part-1/)；[Part 2](https://developer.nvidia.com/blog/using-cuda-stream-ordered-memory-allocator-part-2/)。

**读到哪里**：Part 1 的流排序效率、流有序分配语义与图 1，25 分钟；到内存池前停止。Part 2 仅有多 GPU/IPC 卡点时查对应节，另计 20 分钟，基础练习不要求。

**带着什么问题读**：画 allocate → use → free 与跨流事件依赖。用于理解生命周期，不要求重写分配器，也不套用历史速度数字。 [打开练习与自查](../weeks/week-13-systems/README.md)。

<a id="x-activation"></a>

### X-ACTIVATION · 激活重计算与状态分片的区别

W12/W14 后可选；进阶；英文论文；反向与 TP。

**来源**：[Reducing Activation Recomputation](https://arxiv.org/pdf/2205.05198)。

**读到哪里**：先摘要与 Introduction，再用文内 Activation Memory 的标题定位图和变量，30 分钟，停止于重计算/保存对象；不复现大模型实验。

**带着什么问题读**：已预读指定原始范围；列一张参数/优化器分片与激活重计算的对象对照，勿把二者当同一技术。 [打开练习与自查](../weeks/week-12-fsdp/README.md)。

<a id="x-navigation"></a>

### X-NAVIGATION · 课程视频与中文辅助导航

遇到困难时查阅；难度随章节；中/英文；先有具体问题。

**来源**：[CS336 课程表](https://cs336.stanford.edu/)；[官方视频列表](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)；[GPU MODE](https://github.com/gpu-mode/lectures)；[Datawhale diy-llm](https://github.com/datawhalechina/diy-llm)；[AIInfraGuide](https://github.com/caomaolufei/AIInfraGuide)。

**读到哪里**：CS336 L2/L6/L7/L10 对应上面的函数；diy-llm README 只用第 3/4/7/8/10 章导航；AIInfraGuide 只用目录。按具体卡点查找，找到后回原始材料，不把未经逐章核验的目录列为必读。

**带着什么问题读**：Datawhale 中文二手讲解与官方来源分别标明。本卡只保存额外导航；各节视频在当前课页指定，不在这里增加重复观看。 [打开练习与自查](../course/guide.md)。

**其他目录入口**：[AIInfraGuide 网站](https://caomaolufei.github.io/AIInfraGuide/) 仅作中文导航；[CS336 Assignment 2](https://github.com/stanford-cs336/assignment2-systems) 仅核验仓库入口，题面 PDF 未成功读取。两者不承担必读解释，也不宣称全目录资料已核验。完整作业不属于必做练习；后续选题须先检查题面与范围。

<a id="x-cuda"></a>

### X-CUDA · CUDA 映射与转置图解

遇到困难时查阅；中等；英文；W1/W2。

**来源**：[NVIDIA CUDA 入门](https://developer.nvidia.com/blog/even-easier-introduction-cuda/)；[矩阵转置](https://developer.nvidia.com/blog/efficient-matrix-transpose-cuda-cc/)；[GPU MODE CUDA 视频](https://www.youtube.com/watch?v=nOxKexn3iBo)；[lecture_003 代码](https://github.com/gpu-mode/lectures/blob/77a8df418834e5789c12da23e7d2719e0efabef1/lecture_003/pmpp.ipynb)。

**读到哪里**：W2 看 CPU 循环到 kernel 或 rgb_to_grayscale_kernel/grid，替换 20 分钟；W4 看共享 tile 多一列的 padding 例子，替换 15 分钟。视频无已核验时间戳，以代码为准。

**带着什么问题读**：只解释映射/访存，不添加灰度图或转置项目；历史性能不作为目标。 [打开练习与自查](../weeks/week-02-cuda-execution/README.md)。

<a id="x-fa2"></a>

### X-FA2 · FlashAttention-2 工作划分

W6/W13 后可选；进阶；英文作者博客；R-FLASH。

**来源**：[作者机构博客](https://crfm.stanford.edu/2023/07/17/flash2.html)；[论文摘要](https://arxiv.org/abs/2307.08691)。

**读到哪里**：博客的工作划分与非 matmul FLOPs 讨论，30 分钟；停止于设计图，不实现完整反向。论文只保留摘要入口，不填写未核验页码。

**带着什么问题读**：解释 IO 优化后为何还可能有其他开销；不作为 W6 完成前置。 [打开练习与自查](../weeks/week-06-attention/README.md)。

<a id="article-discovery"></a>

## 参考文章的资源取舍

<details><summary>展开历史来源发现记录；这不是另一份必读清单</summary>

已通过浏览器读到 [AI infra学习汇总（持续更新中）](https://zhuanlan.zhihu.com/p/2075514689602187333)，作者“陌丶一叶知秋”，页面显示编辑于 2026-08-27。网页抓取超时后使用页面正文与链接提取；以下只记录与本项目有关的选择，不复制文章路线或推荐结论。

| 文章发现的原始入口 | 历史访问与取舍 | 放置位置 |
| --- | --- | --- |
| PyTorch saved tensors hooks | 已读指定原始教程；前置是反向与保存状态 | [X-SAVED](optional.md#x-saved)，W12 后可选 |
| NVIDIA stream-ordered allocator 两篇 | 原始页面已读；涉及跨流生命周期，超出首个 kernel | [X-ALLOCATOR](optional.md#x-allocator)，W13 后可选 |
| [Triton 中文语义页](https://triton-lang.cn/main/python-api/triton-semantics.html) | 文章中的翻译入口；采用已读上游官方语义页核对接口 | [R-TRITON](gpu.md#r-triton)，W5 增加 10 分钟定点阅读，替代泛看代码 |
| [HF 中文 BPE](https://huggingface.co/learn/llm-course/zh-CN/chapter6/6?fw=pt) | 原链接两次抓取失败；换已读 HF Tokenization algorithms | [R-TOKEN](serving.md#r-token)，W8 只学 token/子词与请求，不训练 tokenizer |
| NCCL Collective Operations | 已打开，和现有核心资料重复 | [R-COLLECTIVE](training.md#r-collective)，W7 继续沿用，阅读不加倍 |
| 激活重计算论文 2205.05198 | PDF 已打开，限定为原理拓展 | [X-ACTIVATION](optional.md#x-activation)，W12/W14 后 |
| Datawhale diy-llm | README/目录已读，未逐章审查中文改编 | [X-NAVIGATION](optional.md#x-navigation)，按需导航 |
| [InfraTech](https://github.com/CalvinXKY/InfraTech)、[ai-infra-hpc](https://github.com/jinbooooom/ai-infra-hpc)、[ml-engineering](https://github.com/stas00/ml-engineering)、[BBuf CUDA 优化](https://github.com/BBuf/how-to-optim-algorithm-in-cuda) | 仅核对仓库入口/README，内容范围较广；未逐例验证 | 保留发现记录，不列必读；分别可在 PyTorch、W7 通信、工程分支、W4 算子完成后自行选题 |
| [Megatron Core MoE 论文](https://arxiv.org/abs/2603.07685)、[TorchTitan 论文](https://arxiv.org/abs/2410.06511) | 摘要页已读，不冒充全文阅读 | W14 后训练系统分支；W11/W12 仍采用小模型官方教程 |
| RL/微调、DualPipe、CP/EP、RDMA 与 MoE 性能合集 | 与当前基础目标不直接对应；未逐篇访问，不作质量排名 | 暂不纳入，先完成现有 16 个单元 |


</details>

## 各单元的补充资料

[课程目录](../course/README.md) · [视频与基础资料](README.md)

核验快照：2026-10-01。以下是与16个单元直接相关的观察对象，不是完整热点榜或通用 SOTA 排名。每个单元的“主流”指代表性官方实践，不声称掌握采用率统计。

该日期的核验读取了下列官方页面或作者仓库的指定部分；没有运行前沿实现、验证 GPU 性能或证明生产可用。Gluon 关联论文仅核验摘要。没有单独列出的发布日期保持未知；访问日不能替代发布日期。前八个学习位置的 [复核记录](../docs/audits/2026-10-03-sources.md) 已固定主要代码阅读 commit、论文版本并登记浮动页面；实际运行仍须选择匹配依赖，W1 最小运行检查不代替学习或前沿复现。

本页是可选拓展索引；基础完成后按具体问题选一项，另排时间。未选读不影响任何单元的完成标准。这里保留原核验日期，不把文字修订当成前沿资料重新核验。

## 如何选读

W1～W6、W13 建立表示与计算能力；W7、W11～W14 跟踪通信与训练；W8～W10 跟踪服务；W15～W16 跟踪执行与调度。推荐学习顺序见总路线，不按此索引的数字顺序推进。

同一个来源再次出现时只读该补充阅读指定范围。例如 CuTe 在 W2 解释编程抽象，在 W4 解释矩阵运算；无需重复阅读整个项目。官方英文视频以当前小节指定范围为准，本页补接口、架构和成熟度，不再添加重复视频任务。

## S01

**W1：Tensor 表示与资源账本** · [补充阅读](../weeks/week-01-foundations/context.md)

来源：[TorchAO 的低精度表示](https://docs.pytorch.org/ao/stable/contributing/quantization_overview.html)；[Inference Workflows](https://docs.pytorch.org/ao/stable/workflows/inference.html)。版本定位：在线文档或默认分支快照，执行前需固定版本。

来源快照中的情况：官方文档已描述量化工作流，但功能成熟度按配置区分；该快照所查 NVFP4 动态激活/权重量化配置仍标 prototype，要求 SM100+。不能把这个限制推广到所有量化方法。

2026-10-01 核验记录：[TorchAO v0.18.0](https://github.com/pytorch/ao/releases/tag/v0.18.0) 增加 dense Linear 的 NVFP4 训练原型，stable 页面仍标 0.17；依赖与硬件条件见 [W1 复核](../docs/audits/2026-10-01-week-01.md)，不增加 W1 实现。

## S02

**W2：执行模型与 kernel 编程入口** · [补充阅读](../weeks/week-02-cuda-execution/context.md)

来源：[CUTLASS Python / CuTe DSL](https://docs.nvidia.com/cutlass/latest/media/docs/pythonDSL/overview.html)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：NVIDIA 官方 DSL，仍在演进；部分接口具有实验性。文档分别列出 Ampere/Ada、Hopper、Blackwell 的不同能力，不能概括成仅支持新一代 GPU。

## S03

**W3：归约、布局与可信性能证据** · [补充阅读](../weeks/week-03-reduction-profiling/context.md)

来源：[Gluon 显式布局与 Linear Layouts](https://triton-lang.org/main/getting-started/tutorials/gluon/layouts.html)；[Linear Layouts 论文摘要](https://arxiv.org/abs/2505.23819)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：官方教程使用 experimental Gluon 命名空间；论文入口只核对摘要，不据此声称精读全文或复现编译器。

## S04

**W4：从分块 GEMM 到架构匹配** · [补充阅读](../weeks/week-04-gemm/context.md)

来源：[CuTe 的分层矩阵运算与流水线](https://docs.nvidia.com/cutlass/latest/media/docs/pythonDSL/overview.html)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：官方实现与文档可供研究，但 Python DSL 的覆盖范围、接口与 C++ 库不完全相同。

## S05

**W5：融合、持久化与资源约束** · [补充阅读](../weeks/week-05-triton-softmax/context.md)

来源：[Triton Persistent Matmul](https://triton-lang.org/main/getting-started/tutorials/09-persistent-matmul.html)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：官方进阶教程，不是本周 softmax 的可直接替换实现；各变体能力要求不同。

## S06

**W6：Attention 后端与模型语义** · [补充阅读](../weeks/week-06-attention/context.md)

来源：[FlashAttention-3 / FlashAttention-4](https://github.com/Dao-AILab/flash-attention)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：README 将 FA3 标为 beta；FA4 使用 CuTe DSL，面向 Hopper/Blackwell 优化。不同代际条目和普通安装入口的支持范围必须分别看。

## S07

**W7：通信接口、重叠与拓扑** · [补充阅读](../weeks/week-07-collectives/context.md)

来源：[NCCL Device API](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/deviceapi.html)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：该快照的 NCCL 文档标 2.32.3，Device API 自 2.28、GIN 自 2.28.7、CFT 自 2.31 引入。CFT 要求 Blackwell+、编译 CUDA 13.3+ 与相应驱动；不同模块的拓扑、网络与版本条件分别核对。详见 [W7 复核](../docs/audits/2026-10-01-week-07.md)，当前 Ada 规划仅观察。

## S08

**W8：单引擎服务与分离式推理** · [补充阅读](../weeks/week-08-serving-baseline/context.md)

来源：[Dynamo 的 Prefill / Decode 分离](https://docs.dynamo.nvidia.com/dynamo/v1.4.1/kubernetes/disaggregated-serving/overview)。版本定位：Dynamo v1.4.1。

核验要点：已发布的官方架构/部署文档，本卡使用 v1.4.1 固定路径；不据此推断任意模型、互联和规模都值得拆分。

## S09

**W9：从前缀复用到分层缓存** · [补充阅读](../weeks/week-09-kv-cache/context.md)

来源：[SGLang HiCache](https://docs.sglang.io/docs/advanced_features/hicache_design)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：官方系统设计文档。L2 是实例私有主机内存；L3 是否跨实例共享取决于后端、命名空间与配置，不能把每台机器的主存视为自动组成共享池。

## S10

**W10：质量约束下的有效吞吐** · [补充阅读](../weeks/week-10-serving-benchmark/context.md)

来源：[vLLM Speculative Decoding](https://docs.vllm.ai/en/latest/features/speculative_decoding/)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：官方文档包含多类方法；成熟度和模型支持需逐项核验，不能把整个功能列表都标成稳定或任意组合可用。

## S11

**W11：训练语义与组合式训练栈** · [补充阅读](../weeks/week-11-ddp/context.md)

来源：[TorchTitan 的组合式训练设计](https://github.com/pytorch/torchtitan)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：PyTorch 官方组织维护的参考平台；README 说明仍在密集开发，最新特性可能要求 nightly。不能将所有示例直接视为当前环境稳定方案。

## S12

**W12：状态分片、恢复与容错** · [补充阅读](../weeks/week-12-fsdp/context.md)

来源：[TorchFT 的故障容忍训练](https://github.com/meta-pytorch/torchft)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：官方作者开源实现，部分路径如 LocalSGD/DiLoCo 明确带 experimental 标记；单个故障演示不能推断所有训练配置可用。

## S13

**W13：先让编译器解决可解决的问题** · [补充阅读](../weeks/week-13-systems/context.md)

来源：[区域编译与冷启动权衡](https://docs.pytorch.org/tutorials/recipes/regional_compilation.html)。教程标注2024年创建/更新，功能不是2026年新发布。

核验要点：官方工程教程，页面标注创建/更新于2024年并要求 PyTorch 2.5+；这是持续有用的成熟设计，不包装成2026年新研究。实际环境仍需核验。

## S14

**W14：稠密并行与 MoE 通信** · [补充阅读](../weeks/week-14-parallelism/context.md)

来源：[DeepEP / DeepEveryParallel](https://github.com/deepseek-ai/DeepEP)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：作者维护的高性能实现；当前要求 Hopper 或更新架构，一些非 EP 扩展仍为 experimental。不要把仓库名称理解成全部并行路径都成熟。

## S15

**W15：任务抽象与固定执行图** · [补充阅读](../weeks/week-15-ray/context.md)

来源：[Ray Compiled Graph](https://docs.ray.io/en/latest/ray-core/compiled-graph/ray-compiled-graph.html)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：官方文档将 Compiled Graph 标为 beta，API 仍可能变化；不能把它当作普通 Task API 的无条件替代。

## S16

**W16：从队列策略到集群准入与放置** · [补充阅读](../weeks/week-16-scheduling/context.md)

来源：[Kueue 与 KAI Scheduler](https://kueue.sigs.k8s.io/docs/overview/)；[NVIDIA Cloud Functions 的 KAI Scheduler 说明](https://docs.nvidia.com/nvcf/compute-plane/kai-scheduler)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：有官方项目文档与具体产品集成说明；NVCF 使用 KAI 的证据不代表行业全部采用，也不是对本机的部署验证。

## 准备实际尝试时

先核对来源版本、设备要求和指定范围。尚未确认的性能、发布日期或项目状态继续记为未知；资料更新方式见 [维护规则](../docs/maintenance.md)。
