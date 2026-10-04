# 16 个单元的知识覆盖检查

## 2026-10-03：以学习效果为中心的更新

当前完整对应表改为 [学习地图](../coverage.md)，包含基础 P1～P8、系统桥接 S1～S6 和 W1～W16 的能力、先修、材料、练习与核对。新增指定材料的预读范围与发现见 [来源审查](../audits/2026-10-03-sources.md)。

- Python 主教材改用 CS50P 0～6、8；官方教程作为查阅。类在 W6 前，数据管线在 W11 前。
- Docker 实操、Kubernetes 对象/配置/事件、网络、数据、存储和观测纳入基础；生产运维和大规模容灾保留进阶。
- 16 个单元均增加五步练习入口及独立迁移/排错题；四阶段与 W16 综合验收按能力逐项通过。
- 时间仅用于规划，原 178.5 小时是历史实验安排；新增内容可增加时间，不要求等额替换，不限制三段。
- W1 仍为进行中，其余 15 个单元未开始；没有替你登记运行或通过。

本轮交付检查记录在本文末尾。以下保留 2026-10-01 的范围与统计作为历史依据，其中旧时间、平台范围及固定段数不再作为当前约束。

## 2026-10-01 历史检查

[总路线](../../README.md) · [自学方法与预算](../../course/guide.md) · [基础补学](../../course/prerequisites.md) · [资源索引](../../resources/README.md) · [前八单元逐段记录](first-eight-weeks-review-2026-10-01.md)

检查日期：2026-10-01。检查对象是仓库规则、整体路线、16 份单元范围、16 份学习指南、全部补充阅读与资源索引，以及前八个位置的 24 份详细学习段。这里只登记学习材料的覆盖和修订，不登记学习通过；W1 仍为进行中，其余 15 个单元仍未开始。

## 原有缺口与本次处理

| 检查发现 | 本次写回 | 状态与边界 |
| --- | --- | --- |
| Python/C++/Linux/数学/PyTorch 常被概括成“先掌握” | 补学 P/A/B/M1～M4/C/D 给具体范围、用时、小练习和折叠核对 | 入口已补齐；补学不塞入单元预算 |
| 前八位置已有详细段，后八主要是资料和任务清单 | 保留既有结构；后八在 study-guide 中增加 24 组图解/暂停题/答案 | 全部 48 个学习段都有不依赖 AI 的检查路径 |
| W8 默认懂 token、模板、HTTP/JSON | 在推理概念与服务段分别补入门，增加 30 分钟原文 | 前置跳跃已补；模型选择仍按实际设备核对 |
| W11 从推理直接到训练，更新语义不易自行判断 | 单卡训练与恢复补学；本地平均梯度的数值例子 | 材料已补；真实更新尚待学习时验证 |
| W12 状态恢复范围多，原阅读时间偏短 | 修正当前 DCP 已使用 fully_shard 的说明，补状态清单，阅读增至 195 分钟 | 建议分两次，总预算 13.5 小时 |
| 同一讲义/文档被多处重复列成大范围阅读 | 知识卡统一 URL、用途与停止位置；单元链接卡片与本次范围 | 不重复看整讲；遇卡点才复习 |
| context 的进展阅读成为初学者必做门槛 | 全部改为基础通过后的可选拓展 | 核心概念、正确性和复现标准保留 |
| 图例与自查没有独立用时 | 单独安排自查，W16 将已熟悉原文的重复阅读改为字段映射与推演，实践按范围调整 | 总计 178.5 小时；尚无个人实测耗时 |

## 知识点—能力—材料—练习—完成标准

表中材料列按三段顺序列知识卡。难度、语言、先修、原始来源、章节/函数、时间和停止点由卡片维护；具体前置问题与答案在各单元学习指南开头。练习中的数字均为自拟推导，不能登记为运行结果。

| 单元 / 知识点 | 能力目标 | 材料（按顺序） | 练习 | 完成标准 | 已补齐 |
| --- | --- | --- | --- | --- | --- |
| [W1](../../weeks/week-01-foundations/README.md)：类型、字节、shape/stride、Linear 参数与 FLOPs | 能从索引算地址，区分共享视图和复制，并实现可手算核对的资源计算器。 | [类型、地址与生命周期](../../resources/foundations.md#r-cpp) → [Tensor 存储、FLOPs 与 Roofline 讲义](../../resources/foundations.md#r-l2) → [Tensor 的视图、转置与复制](../../resources/foundations.md#r-views) | 数组地址/Tensor 视图/Linear 计算器 | 手算与代码逐项一致，含非连续视图、dtype 与 bias 口径 | P/B/M1 入口、单位与地址核对 |
| [W2](../../weeks/week-02-cuda-execution/README.md)：线程覆盖、host/device 内存、异步计时、带宽 | 能实现有尾部保护的 Vector Add，定位访存错误，并解释 kernel 与端到端时间。 | [CUDA 线程与 host/device 数据路径](../../resources/gpu.md#r-cuda) → [内存与共享同步检查](../../resources/gpu.md#r-sanitizer) → [计时、有效带宽与 GEMM 数据复用](../../resources/gpu.md#r-best) | 尾部索引、Vector Add、两种计时边界 | 边界输出与 sanitizer 记录；计时范围明确 | 内存前置与运行顺序已拆开 |
| [W3](../../weeks/week-03-reduction-profiling/README.md)：树形归约、barrier、warp mask、性能证据 | 能比较共享内存与 warp 归约，在一致计时范围内用数据说明瓶颈。 | [共享内存归约代码](../../resources/gpu.md#r-reduce) → [warp 交换、mask 与同步](../../resources/gpu.md#r-warp) → [内存与共享同步检查](../../resources/gpu.md#r-sanitizer) → [测量、Triton 与编译的讲义例子](../../resources/gpu.md#r-l6) → [kernel 内部的性能证据](../../resources/gpu.md#r-ncu) | 共享/warp 两版归约、同一 CPU 收尾 | 部分和与最终和分别核对；第一阶段性能比较范围相同 | 统一第二阶段和完整归约的区别 |
| [W4](../../weeks/week-04-gemm/README.md)：访存连续性、共享 tile、算术强度、Roofline | 能实现朴素/分块 GEMM，说明复用、边界和性能上限的关系。 | [计时、有效带宽与 GEMM 数据复用](../../resources/gpu.md#r-best) → [用 Roofline 连接 FLOPs 与搬运](../../resources/gpu.md#r-roofline) → [Tensor 存储、FLOPs 与 Roofline 讲义](../../resources/foundations.md#r-l2) | 朴素/tile GEMM、地址图、Roofline | 尾部 shape 与参考对齐；理论搬运和实测分开 | tile 同步与性能模型图解 |
| [W5](../../weeks/week-05-triton-softmax/README.md)：program/mask、广播与类型、稳定 Softmax、在线状态 | 能写稳定的行 Softmax，解释融合减少的搬运，并核对分块状态合并。 | [测量、Triton 与编译的讲义例子](../../resources/gpu.md#r-l6) → [Triton program、mask 与类型](../../resources/gpu.md#r-triton) → [稳定 Softmax 与融合](../../resources/gpu.md#r-softmax) → [分块 Softmax 的状态合并](../../resources/gpu.md#r-online) | 广播类型题、稳定 Softmax、在线状态合并 | 非二次幂/大幅值与参考一致；会解释重缩放 | Triton 语义入口、在线递推答案 |
| [W6](../../weeks/week-06-attention/README.md)：Attention 语义、因果 mask、在线 IO、Block 时间线 | 能对齐显式 Attention 与 SDPA，完成小 Block 的形状、资源和耗时分析。 | [Attention 语义和后端](../../resources/models.md#r-sdpa) → [Attention 的 IO 与在线分块](../../resources/models.md#r-flash) → [模型区段与 CPU/GPU 时间线](../../resources/models.md#r-trace) | 显式/SDPA Attention、小 Block 时间线 | shape/mask/dropout/精度对齐；资源与实际区段对应 | 模型补学 C、固定 Block 定义 |
| [W13](../../weeks/week-13-systems/README.md)：eager/compile、首次成本、稳态、graph break | 能对齐编译前后结果，估算成本回收，并用模型区段解释整体收益。 | [eager、编译和变化输入](../../resources/models.md#r-compile) → [测量、Triton 与编译的讲义例子](../../resources/gpu.md#r-l6) | eager/compile、首次/稳态、变化输入 | 结果一致；回本与整体收益有计算和日志依据 | 成本回收例子、graph break 核对 |
| [W7](../../weeks/week-07-collectives/README.md)：rank、collective 语义、algbw/busbw、拓扑 | 能验证 2 卡 collective，解释随消息大小变化的延迟与带宽。 | [各 rank 的输入输出](../../resources/training.md#r-collective) → [通信、TP 和 PP 讲义](../../resources/training.md#r-l7) → [通信计时与两种带宽](../../resources/training.md#r-nccl-tests) | rank 输入输出表、2 卡 nccl-tests 曲线 | 语义正确，algbw/busbw 可重算；记录真实拓扑 | 通信图、计量定义与硬件边界 |
| [W8](../../weeks/week-08-serving-baseline/README.md)：token 与模板、prefill/decode、HTTP 请求、TTFT/TPOT | 能重建单请求路径，启动一项可复现服务，并解释固定负载下的延迟与吞吐。 | [prefill、decode 与请求延迟](../../resources/serving.md#r-inference) → [token、模板与请求格式](../../resources/serving.md#r-token) → [单卡在线服务](../../resources/serving.md#r-serving) → [负载、明细和统计字段](../../resources/serving.md#r-bench) | 请求 JSON、token 核对、时间轴和基线 | 服务可重建；真实长度、成功失败与指标明细齐全 | token/模板/HTTP 入门与时间轴答案 |
| [W9](../../weeks/week-09-kv-cache/README.md)：KV 字节、逻辑/物理块、碎片、共享与 APC | 能手算 KV 容量、追踪块表，并设计冷/热缓存对照而不混淆生成质量。 | [KV 容量、分页和共享](../../resources/serving.md#r-paged) → [前缀复用的条件与限制](../../resources/serving.md#r-apc) | KV 字节脚本、共享块表、冷/热 APC | 区分容量与进程显存；控制输入前缀并保留命中证据 | 块号/偏移与 copy-on-write 图 |
| [W10](../../weeks/week-10-serving-benchmark/README.md)：到达负载、批处理预算、分位数、goodput、观测 | 能保存请求明细，做两个单因素扫描，并用指标解释一次配置变化。 | [负载、明细和统计字段](../../resources/serving.md#r-bench) → [continuous batching 与 chunked prefill](../../resources/serving.md#r-batching) → [服务状态与有效吞吐](../../resources/serving.md#r-metrics) | 两条单因素扫描、一个调优变量 | 明细重算分位数/goodput；计划与实际发送分开 | batching token 表、指标单位与反例 |
| [W11](../../weeks/week-11-ddp/README.md)：样本划分、平均梯度、全局 batch、精度、输入等待 | 能核对 1/2 卡一次更新，保持更新语义一致，并解释扩展性和状态大小。 | [rank、模型副本与样本归属](../../resources/training.md#r-ddp-start) → [梯度同步和公平更新](../../resources/training.md#r-ddp) → [精度与输入路径的分离](../../resources/training.md#r-amp) | 样本 ID、单步参数对齐、1/2 卡 FP32 | 全局 batch/loss 约定一致；真实更新和同步证据 | 训练补学 D、标量梯度推导与状态表 |
| [W12](../../weeks/week-12-fsdp/README.md)：状态分片、参数聚合、峰值显存、完整恢复 | 能对照 DDP/FSDP2 状态与通信，并用下一步结果验证同 world size 恢复。 | [训练状态分片的对象](../../resources/training.md#r-zero) → [FSDP2 参数聚合与分片](../../resources/training.md#r-fsdp) → [模型、优化器与应用状态恢复](../../resources/training.md#r-dcp) | DDP/FSDP2 状态表、连续 3 步 vs 2+恢复+1 | 模型/优化器/进度恢复；下一步样本、loss、参数可比较 | 聚合时序、完整恢复清单与拆分预算 |
| [W14](../../weeks/week-14-parallelism/README.md)：TP 代数、非线性与合并、PP 气泡、DP/TP/PP | 能验证两层 MLP 切分等价，标明通信并手算前向流水线。 | [TP 的两层 MLP 代数](../../resources/training.md#r-megatron) → [通信、TP 和 PP 讲义](../../resources/training.md#r-l7) → [TP 通信与 PP 流水线](../../resources/training.md#r-parallel) | 两层 MLP 切分、非线性反例、PP 时间线 | 数值一致、合并位置正确；模拟和实测区分 | 局部求和/bias 核对与气泡手算 |
| [W15](../../weeks/week-15-ray/README.md)：Task/Actor、ObjectRef、资源声明、排队日志 | 能写可核对结果的任务与状态对象，区分逻辑资源和实际占用，重建执行事件。 | [Task、Actor 与 ObjectRef](../../resources/scheduling.md#r-ray-task) → [逻辑资源与实际设备](../../resources/scheduling.md#r-ray-resource) → [可行性、可用性与节点选择](../../resources/scheduling.md#r-ray-schedule) | Task/Actor、本地参考、资源与事件日志 | 结果正确，等待可重算；逻辑令牌不冒充占用 | 可访问官方替代材料、依赖图与日志答案 |
| [W16](../../weeks/week-16-scheduling/README.md)：事件仿真、FIFO/SJF、估计时长、等待与周转 | 能实现非抢占策略，按同一轨迹核对资源约束和统计，限定结论范围。 | [排队指标、FIFO 与 SJF](../../resources/scheduling.md#r-ostep) → [可行性、可用性与节点选择](../../resources/scheduling.md#r-ray-schedule) | 同轨迹 FIFO/理想 SJF/估计 SJF 仿真 | 不丢任务不超分配；手算对齐、有限假设下比较 | 完整小轨迹、事件次序和两层等待 |

## 顺序与依赖检查

主线保持 W1 → W2 → W3 → W4 → W5 → W6 → W13 → W7 → W8 → W9 → W10 → W11 → W12 → W14 → W15 → W16。各单元底部导航与此一致。W13 只复用 W6 Block，不要求后面的训练基础；W7 通信概念只需前面的张量与计时，2 卡实验是 W11 的前置。

推荐位置不等于所有早期单元都是技术依赖：缺少 2 卡可先做 W8～W10，W7 留待完成；W14 CPU 代数能验证切分但不能证明多卡性能；W15 CPU Task 需要 Python 与日志能力，W16 主线是仿真。任何环境例外都不能自动勾选未做的 GPU 项。

先修 C 在 W6 前引入 Attention/模型结构；先修 D 和 M3 在 W11 前引入梯度、优化器与单卡恢复。避免为了 W1 先读完整深度学习教材。资料卡和各段只使用当前已引入的概念；后续主题明确标扩展。

## 来源核验记录

参考文章已通过浏览器读取，并提取与主线有关的外链继续访问原始来源。Triton 语义进入 W5，tokenizer 的官方替代进入 W8；saved tensor hooks、流顺序分配、激活重计算放到具备基础后的选读。综合目录只作导航，MoE/完整生产训练路线不替换本项目。逐项 URL 与采用/后置理由见[资源取舍记录](../../resources/optional.md#article-discovery)。

新增必读页面实际打开核对；已有前八单元来源沿用本会话同日的页面、PDF 与代码检查。D2L 中文线性代数、HF 中文 BPE、Ray walkthrough/Actors 未成功访问，已使用可访问的英文教材或官方 Tasks/API 替代。未核验的视频分钟数不填写；题面未读到的完整作业不指定题号。前沿索引保留日期快照，本次不宣称重新验证全部前沿发布。

## 尚存限制

- 材料与推导已补齐，独立学习效果还要由实际作答、边界检查和复现报告验证。不能把资料整理完成当作学习完成。
- CUDA/Triton/compile、profiler 权限、2 卡互连和服务环境未在本次运行；具体安装版本、模型 revision 与显存余量在开始实验时记录。
- 原文多数为英文，已配中文概念图和答案；若语言阅读耗时明显增加，按实际顺延，不跳过关键接口约定。
- 基础补学、下载和配置不含在 178.5 小时内；个人实际时长未知，先用一个单元校准。各段完成标准不因预算到点降低。
- 当时将平台主题整体后置；2026-10-03 已补容器、对象/配置/事件诊断等基础，只有生产部署、CP/EP/MoE 等深度主题继续后置。

## 本地验证

已检查 103 份 Markdown、1256 个本地链接（其中 381 个带本地锚点）、72 个折叠区及代码块闭合，未发现断链或未闭合。检查全部 16 个单元、48 个学习段、58 张资源卡，README 与学习指南的三段阅读时间一致，合计 178.5 小时；前后导航、W1 进行中/其余未开始的状态均一致。

静态复算 45 项数值关系，包括基础矩阵、梯度、资源字节、TTFT/TPOT、KV 分页、goodput、DDP 更新、TP/PP 和 FIFO/SJF，全部通过。Git 差异格式检查通过。以上仅检查文档结构、手算和规划一致性，没有运行 CUDA、Triton、模型、训练、服务或 Ray 学习实验。

## 2026-10-03 交付检查

- 对当前 108 份 Markdown 检查本地文件链接、显式/标题锚点、代码围栏及折叠块闭合；未发现断链或未闭合。16 份 README 和 16 份 study-guide 均有对应能力关卡入口。
- 检查 P1～P7→W1、C++/系统→W2、P8/C→W6、D/S4/W7→W11、S5→W12、S6→W15/W16 的先修顺序；W 编号与主线导航保持原顺序。
- 检查所有 16 个单元新增迁移/排错题均有折叠核对、回看位置与原实验入口；四阶段和综合验收使用同一批实验，核心能力逐项通过。
- W1 的量化背景移回选读；W11 原先把输入对照列为扩展的残留说明已同步修正。Docker 操作必做、Kubernetes 配置/事件必做、集群操作后续选做的边界一致。
- 新增文档中 7 段 Python 示例通过语法解析；32 项纯函数、学习数值和 YAML 字段检查通过。实际执行只涉及无依赖的字节函数/Counter 小例及核对算术；统计工具、训练循环、DataLoader、GPU 和 Docker 实验未代替你运行。YAML 解析不代表 Kubernetes 集群验证。
- 时间检查区分旧实验起步数字、新版范围与新增段；A/S1、复用数据/代码、原文与视频重复部分不重复计时。实际学习耗时仍待填写。
- `git diff --check` 通过；学习状态仍是 W1 进行中、其余 15 单元未开始，没有新增学习验收通过记录。

本轮未提交或推送。材料可作为学习入口；真正掌握需后续独立作答、变化条件和真实运行证据。
