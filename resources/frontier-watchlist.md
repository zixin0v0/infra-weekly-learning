# 各单元的进展与补充资料

[课程设计](../docs/curriculum-design.md) · [开课更新](../docs/weekly-refresh.md) · [基础课程来源](README.md)

核验快照：2026-10-01。以下是与16个单元直接相关的观察对象，不是完整热点榜或通用 SOTA 排名。每个单元的“主流”指代表性官方实践，不声称掌握采用率统计。

本轮读取了下列官方页面/作者仓库对应部分；没有运行代码、验证 GPU 性能或证明生产可用。Gluon 关联论文仅核验摘要。没有单独列出的发布日期保持未知；访问日不能替代发布日期。浮动页面尚未固定 commit，开课须选择与本地依赖匹配的版本并保存记录。

## 如何选读

W1～W6、W13 建立表示与计算能力；W7、W11～W14 跟踪通信与训练；W8～W10 跟踪服务；W15～W16 跟踪执行与调度。推荐学习顺序见总路线，不按此索引的数字顺序推进。

同一个来源再次出现时只读该补充阅读指定范围。例如 CuTe 在 W2 解释编程抽象，在 W4 解释矩阵运算；无需重复阅读整个项目。官方英文视频仍以原章节导学为主，本页补接口、架构和成熟度，不再添加重复视频任务。

## S01

**W1：Tensor 表示与资源账本** · [补充阅读](../weeks/week-01-foundations/context.md)

来源：[TorchAO 的低精度表示](https://docs.pytorch.org/ao/stable/contributing/quantization_overview.html)；[Inference Workflows](https://docs.pytorch.org/ao/stable/workflows/inference.html)。版本定位：在线文档或默认分支快照，执行前需固定版本。

目前查到的情况：官方文档已描述量化工作流，但功能成熟度按配置区分；本次所查 NVFP4 动态激活/权重量化配置仍标 prototype，要求 SM100+。不能把这个限制推广到所有量化方法。

## S02

**W2：执行模型与 kernel 编程入口** · [补充阅读](../weeks/week-02-cuda-execution/context.md)

来源：[CUTLASS Python / CuTe DSL](https://docs.nvidia.com/cutlass/latest/media/docs/pythonDSL/overview.html)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：NVIDIA 官方 DSL，仍在演进；部分接口具有实验性。文档分别列出 Ampere/Ada、Hopper、Blackwell 的不同能力，不能概括成仅支持新一代 GPU。

## S03

**W3：归约、布局与可信性能证据** · [补充阅读](../weeks/week-03-reduction-profiling/context.md)

来源：[Gluon 显式布局与 Linear Layouts](https://triton-lang.org/main/getting-started/tutorials/gluon/layouts.html)；[Linear Layouts 论文摘要](https://arxiv.org/abs/2505.23819)。版本定位：在线文档或默认分支快照，执行前需固定版本。

核验要点：官方教程使用 experimental Gluon 命名空间；论文入口本轮核对摘要，不据此声称精读全文或复现编译器。

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

核验要点：官方文档说明 Device API 自 NCCL 2.28 引入，GIN 自 2.28.7 引入；不同能力有不同拓扑与传输要求。

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

## 以后怎样更新

来源出现变化时，先更新当前单元补充阅读和开课记录。只有先修、接口、硬件可用性或核心实验解释发生变化才修订主线。未确认性能、发布日期或项目状态时保留“未知”，不使用项目宣传词替代复现实验。
