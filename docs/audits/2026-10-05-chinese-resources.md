# 中文视频与图文补充核验 · 2026-10-05

[维护目录](../README.md) · [覆盖表](../coverage.md) · [资料入口](../../resources/README.md)

## 核验范围与记录方式

基线为提交 `4bd7520a413db57a45fdc9768ebed70e02078e54`。P1～P8、单卡训练、S1～S6、全部 50 个 W session 共 65 页逐页添加当前知识点的中文补充或缺项；先修 B 也接入 C++/Tensor 的直接入口。六份资源分类保留原 56 个 P-/R- 锚点，旁边登记对应关系，不建立第二套中文课程目录。

原英文课程、阅读范围、学习顺序、实验与个人进度保持；数学中文页的访问状态按本次结果更新，历史核验文件不改。中文资料默认按需使用：理解同一概念后回原课练习，不增加第二轮必读或重复计时。这里记录资料准备，不能据此填写个人已掌握或实验已运行。

本次通过公开网页实际读取指定文字、代码和可提取公式，结合原课先修与练习选择范围。正文“已预读”只指资源卡限定部分，不代表整页、整站或所有配图均核验。没有执行外部示例、GPU、Docker、多卡或 Ray 集成。原英文预读沿用各自历史核验日期，本次逐卡检查的是中文对应和保留情况。

<a id="source-coverage"></a>

## 原资料逐项对应

“部分”表示已经接入能帮助当前概念的中文资源，但仍有原范围或接口未覆盖；“沿用”表示原卡已有中文，不重复堆来源；“暂缺”表示没有推荐与该卡核心要求匹配且已预读的新增中文内容。统计为 **37 项部分补充、3 项沿用、16 项暂缺**，不解释为 37 项完整中文替代。

| 原资源 | 中文对应状态 | 指定补充或未覆盖部分 |
| --- | --- | --- |
| [P-PY](../../resources/foundations.md#p-py) | 部分 | [对应资料](../../resources/foundations.md#cn-python)；P1～P8 有逐段中文正文；中文原创视频分集仍缺。 |
| [P-SHELL](../../resources/foundations.md#p-shell) | 部分 | [对应资料](../../resources/foundations.md#cn-shell)；2026 Shell 社区译文；视频字幕与画面未核验。 |
| [P-ENV](../../resources/foundations.md#p-env) | 部分 | [对应资料](../../resources/foundations.md#cn-shell)；venv 沿用原有官方中文；Git 补 2020 社区译文，与 2026 讲次区分。 |
| [P-CPP](../../resources/foundations.md#p-cpp) | 部分 | [对应资料](../../resources/foundations.md#cn-cpp)；地址、固定数组与边界；完整类型、引用和生命周期仍读原文。 |
| [P-TENSOR](../../resources/foundations.md#p-tensor) | 部分 | [对应资料](../../resources/foundations.md#cn-tensor)；李沐中文视频与数据操作；拼接等接口仍查原文。 |
| [P-MATH](../../resources/foundations.md#p-math) | 沿用 | 已有作者中文对应页；2026-10-05 已可访问，整段预读仍未重做，英文指定范围保持。 |
| [P-SOFTMAX](../../resources/foundations.md#p-softmax) | 沿用 | 已有作者中文 §3.4.2～3.4.3，保持原范围，不重复加来源。 |
| [P-CALCULUS](../../resources/foundations.md#p-calculus) | 沿用 | 已有作者中文指定小节，保持原范围；未新增视频要求。 |
| [P-STATS](../../resources/foundations.md#p-stats) | 暂缺 | 已找到中文版，但与英文节号不同；尚未完成随机变量、期望/方差对应范围预读，暂不推荐新范围。 |
| [P-MODEL](../../resources/foundations.md#p-model) | 部分 | [对应资料](../../resources/models.md#cn-attention)；原有作者中文正文保留；补注意力分数视频，字幕与画面待核验。 |
| [P-TRAIN](../../resources/foundations.md#p-train) | 部分 | [对应资料](../../resources/foundations.md#cn-training)；自动求导、训练循环与权重读回；完整恢复继续读原文。 |
| [R-NUMERICS](../../resources/foundations.md#r-numerics) | 暂缺 | 浮点范围、舍入、累加顺序和容差的完整中文对应待补。 |
| [R-CPP](../../resources/foundations.md#r-cpp) | 部分 | [对应资料](../../resources/foundations.md#cn-cpp)；微软中文指针/数组小例子；不替代 CS106L 类型与寿命范围。 |
| [R-L2](../../resources/foundations.md#r-l2) | 部分 | [对应资料](../../resources/foundations.md#cn-tensor)；形状和基础运算有中文补充；FLOPs/显存账本/Roofline 未完整覆盖。 |
| [R-VIEWS](../../resources/foundations.md#r-views) | 部分 | [对应资料](../../resources/foundations.md#cn-tensor)；先补 shape/广播；stride、共享、复制语义仍以原文为准。 |
| [R-CUDA](../../resources/gpu.md#r-cuda) | 部分 | [对应资料](../../resources/gpu.md#cn-cuda)；中文入门视频与限定索引例子；保留显式搬运和同步实验。 |
| [R-SANITIZER](../../resources/gpu.md#r-sanitizer) | 暂缺 | 现代 Compute Sanitizer 运行与判读缺合适中文对应。 |
| [R-BEST](../../resources/gpu.md#r-best) | 部分 | [对应资料](../../resources/gpu.md#cn-triton)；分块伪代码补复用直觉；合并访存、shared 同步等仍查原指南。 |
| [R-REDUCE](../../resources/gpu.md#r-reduce) | 部分 | [对应资料](../../resources/gpu.md#cn-reduce)；中文树形合并解释；旧 kernel 不作为正确性参考。 |
| [R-WARP](../../resources/gpu.md#r-warp) | 暂缺 | 现代 warp 的参与 mask/同步语义缺准确中文对应。 |
| [R-L6](../../resources/gpu.md#r-l6) | 部分 | [对应资料](../../resources/gpu.md#cn-triton)；Triton 和融合有社区译文；计量、剖析与完整讲义未覆盖。 |
| [R-NCU](../../resources/gpu.md#r-ncu) | 暂缺 | 当前 Nsight Compute 指标及 profiler 开销缺匹配中文章节。 |
| [R-ROOFLINE](../../resources/gpu.md#r-roofline) | 暂缺 | 逻辑字节、实际流量、算术强度与上限的完整中文对应待补。 |
| [R-TRITON](../../resources/gpu.md#r-triton) | 部分 | [对应资料](../../resources/gpu.md#cn-triton)；向量相加的社区译文；类型提升继续查原文。 |
| [R-SOFTMAX](../../resources/gpu.md#r-softmax) | 部分 | [对应资料](../../resources/gpu.md#cn-triton)；中文 kernel 与动机；运行、测试/benchmark 仍用固定上游版本。 |
| [R-ONLINE](../../resources/gpu.md#r-online) | 部分 | [对应资料](../../resources/models.md#cn-flash)；中文分块 max/sum 公式，先不读 Attention 扩展。 |
| [R-GPU-HARDWARE](../../resources/gpu.md#r-gpu-hardware) | 部分 | [对应资料](../../resources/gpu.md#cn-hardware)；CPU/GPU 与互连关系；SM/warp/occupancy 精确约束仍查原文。 |
| [R-SDPA](../../resources/models.md#r-sdpa) | 部分 | [对应资料](../../resources/models.md#cn-attention)；中文缩放点积/mask；SDPA 参数与后端控制仍查原文。 |
| [R-FLASH](../../resources/models.md#r-flash) | 部分 | [对应资料](../../resources/models.md#cn-flash)；中文分块公式；动画、复杂度与后端实现未核验。 |
| [R-TRACE](../../resources/models.md#r-trace) | 暂缺 | Profiler 的 CPU/kernel/等待时间线缺匹配中文正文。 |
| [R-COMPILE](../../resources/models.md#r-compile) | 部分 | [对应资料](../../resources/models.md#cn-compile)；sum/abs 融合例子；graph break、重编译和回本分析仍缺。 |
| [R-MEMORY-LIFETIME](../../resources/models.md#r-memory-lifetime) | 部分 | [对应资料](../../resources/models.md#cn-memory)；中文 detach 例子；allocated/reserved/peak 等未覆盖。 |
| [R-INFERENCE](../../resources/serving.md#r-inference) | 部分 | [对应资料](../../resources/serving.md#cn-inference)；中文 prefill/decode 与缓存；算术强度仍按原讲义。 |
| [R-TOKEN](../../resources/serving.md#r-token) | 暂缺 | [对应资料](../../resources/serving.md#cn-serving-gaps)；BPE 合并、聊天模板与当前请求字段没有完整中文对应。 |
| [R-SERVING](../../resources/serving.md#r-serving) | 部分 | [对应资料](../../resources/serving.md#cn-http)；中文 HTTP 解释请求路径；vLLM 当前启动与服务接口仍查原文。 |
| [R-BENCH](../../resources/serving.md#r-bench) | 部分 | [对应资料](../../resources/serving.md#cn-metrics)；中文 TTFT/吞吐/ITL 定义；当前 bench 参数未覆盖。 |
| [R-PAGED](../../resources/serving.md#r-paged) | 部分 | [对应资料](../../resources/serving.md#cn-inference)；中文 KV/分页动机；块表共享、写时复制仍按原论文。 |
| [R-APC](../../resources/serving.md#r-apc) | 暂缺 | [对应资料](../../resources/serving.md#cn-serving-gaps)；当前 APC 接口、缓存键与命中计数缺匹配中文材料。 |
| [R-BATCHING](../../resources/serving.md#r-batching) | 部分 | [对应资料](../../resources/serving.md#cn-inference)；中文 continuous batching 动机；chunked prefill 预算仍查原文。 |
| [R-METRICS](../../resources/serving.md#r-metrics) | 部分 | [对应资料](../../resources/serving.md#cn-metrics)；概念指标有中文解释；当前字段、缓存单位及 goodput 不在补充范围。 |
| [R-COLLECTIVE](../../resources/training.md#r-collective) | 部分 | [对应资料](../../resources/training.md#cn-data-parallel)；中文手动 allreduce 小函数；其余 collective 与 torchrun 仍查原文。 |
| [R-L7](../../resources/training.md#r-l7) | 部分 | [对应资料](../../resources/training.md#cn-parallel)；中文 TP MLP 与 PP 概念；固定讲义代码/计量仍按原范围。 |
| [R-NCCL-TESTS](../../resources/training.md#r-nccl-tests) | 暂缺 | [对应资料](../../resources/training.md#cn-training-gaps)；algbw/busbw、构建与测量缺准确中文对应。 |
| [R-DDP-START](../../resources/training.md#r-ddp-start) | 部分 | [对应资料](../../resources/training.md#cn-data-parallel)；中文数据并行步骤；不是 DDP/DistributedSampler 接口教程。 |
| [R-DDP](../../resources/training.md#r-ddp) | 部分 | [对应资料](../../resources/training.md#cn-data-parallel)；中文梯度求和直觉；DDP 平均、不同步与恢复仍查原文。 |
| [R-AMP](../../resources/training.md#r-amp) | 暂缺 | [对应资料](../../resources/training.md#cn-training-gaps)；autocast/GradScaler 与异步加载调优缺合适中文对应。 |
| [R-ZERO](../../resources/training.md#r-zero) | 部分 | [对应资料](../../resources/training.md#cn-sharding)；中文三阶段分片分类；账本假设、其余状态仍按原论文。 |
| [R-FSDP](../../resources/training.md#r-fsdp) | 暂缺 | [对应资料](../../resources/training.md#cn-training-gaps)；已核验的 FSDP2 fully_shard/DTensor 中文教程待补，不能用 FSDP1。 |
| [R-DCP](../../resources/training.md#r-dcp) | 暂缺 | [对应资料](../../resources/training.md#cn-training-gaps)；DCP + FSDP2 完整状态恢复缺匹配中文材料。 |
| [R-MEGATRON](../../resources/training.md#r-megatron) | 部分 | [对应资料](../../resources/training.md#cn-parallel)；中文两层 MLP/f/g；bias、Attention 切分仍查原文。 |
| [R-PARALLEL](../../resources/training.md#r-parallel) | 部分 | [对应资料](../../resources/training.md#cn-parallel)；中文 TP/PP 概念；Interleaved 调度与配置字段仍查原文。 |
| [R-RAY-TASK](../../resources/scheduling.md#r-ray-task) | 暂缺 | [对应资料](../../resources/scheduling.md#cn-ray-gap)；Task/Actor/ObjectRef 的合适外部中文材料待补。 |
| [R-RAY-RESOURCE](../../resources/scheduling.md#r-ray-resource) | 暂缺 | [对应资料](../../resources/scheduling.md#cn-ray-gap)；逻辑资源与实际隔离的准确中文对应待补。 |
| [R-RAY-SCHEDULE](../../resources/scheduling.md#r-ray-schedule) | 暂缺 | [对应资料](../../resources/scheduling.md#cn-ray-gap)；Ray 可行性/可用性及 DEFAULT 策略缺匹配中文对应。 |
| [R-OSTEP](../../resources/scheduling.md#r-ostep) | 部分 | [对应资料](../../resources/scheduling.md#cn-scheduling)；中文 FCFS/SJF；STCF 区分和本课事件轨迹仍读原文。 |
| [R-RETRY](../../resources/scheduling.md#r-retry) | 部分 | [对应资料](../../resources/scheduling.md#cn-retry)；AWS 同范围官方中文译文；ray.get timeout 仍查原接口。 |

## 实际预读的中文范围与版本

准确章节、起止点、直接链接和读时注意事项统一在以下来源卡维护。表中“已预读”指文字/代码/公式范围；外部插图、动画没有逐张视觉检查，正文仍使用仓库已有图解推演。

| 作者或维护方 | 本次读取的范围与用途 | 版本与核验边界 |
| --- | --- | --- |
| 廖雪峰 / Python 官方 | [CN-Python](../../resources/foundations.md#cn-python)：函数、条件、循环/list、异常、模块、文件/JSON、选测试输入、类实例 | 作者当前 Python 3 正文；官方 zh-cn/3 随版本更新。指定段落已预读；P7 止于 Dict 类前，不引入未学继承 |
| Missing Semester 中文社区 | [CN-Shell](../../resources/foundations.md#cn-shell)：导航/PATH/标准流；任务控制；Git 快照/暂存/status/diff/log | Shell 明确 2026，Job Control/Git 明确 2020；文字已预读，不把不同年份当同一视频 |
| Microsoft Learn | [CN-CPP](../../resources/foundations.md#cn-cpp)：取地址、解引用、已初始化固定数组与边界 | MSVC 170 文档视图；文字/首个小例子已预读，编译器不随资料更换 |
| 李沐等 D2L 作者团队 | [Tensor](../../resources/foundations.md#cn-tensor)、[自动微分](../../resources/foundations.md#cn-autograd)、[线性回归训练](../../resources/foundations.md#cn-training)、[保存加载](../../resources/foundations.md#cn-save) | 中文 v2 教材，核对 PyTorch 页签；指定正文与代码已预读，旧代码不作为安装版本 |
| D2L 作者团队 | [硬件](../../resources/gpu.md#cn-hardware)、[Attention](../../resources/models.md#cn-attention)、[数据并行](../../resources/training.md#cn-data-parallel) | 只用组件/公式/限定小函数；不套旧硬件数字、valid_lens 或单进程手动 allreduce 接口 |
| coderonion / codingonion | [CN-CUDA](../../resources/gpu.md#cn-cuda)：作者仓库中第 3、4 集与配套说明 | 仓库题为 CUDA 12.x；当前 README 只列 4 集，不能标为完整优化课程；录制年份未确认 |
| NVIDIA / Mark Harris | [CN-CUDA](../../resources/gpu.md#cn-cuda)：CPU 与完整三参数 CUDA 例子、线程和 grid-stride | 中文页更新 2025-05-02，原文起于 2017；预读发现局部 sum 参数混用、取整译词和 tg_ 残留，已在卡片提示；性能/工具段不指定 |
| 谭升 | [线程索引](../../resources/gpu.md#cn-cuda)、[计时](../../resources/gpu.md#cn-timing)、[归约树](../../resources/gpu.md#cn-reduce) | 2018 系列；只指定索引、五个时间事件和配对文字，代码同步规则回查当前英文 |
| HyperAI 超神经 | [CN-Triton](../../resources/gpu.md#cn-triton)：向量相加、Softmax kernel、GEMM 伪代码/指针 | 社区译文，未固定到本仓库上游 commit；文字/限定代码已预读，MN 元素与 num_warps 译法已纠正 |
| Bowen Zhou | [CN-Flash](../../resources/models.md#cn-flash)：Softmax Tiling 与 Attention 分块状态公式 | 2024 作者文章；文字/公式已预读，动画未检查。用完整公式补上旧状态的指数重缩放，不采用不一致的维度名称 |
| NVIDIA / Daniel Rodriguez | [CN-Compile](../../resources/models.md#cn-compile)：隐式融合的 sum/abs 与两个生成 kernel | 2026-07-10 中文文章；只读 torch.compile 例子，不引入 CUDA 13.2 C++、性能表或新依赖 |
| NVIDIA / Shashank Verma、Neal Vaidya | [CN-Inference](../../resources/serving.md#cn-inference)：prefill/decode、KV、分页、continuous batching；[PP 概念](../../resources/training.md#cn-parallel) | 2023-11-17；指定文字已预读，不据此配置当前 vLLM 或完整训练流水线 |
| NVIDIA / David Yastremsky 等 | [CN-Metrics](../../resources/serving.md#cn-metrics)：TTFT、输出吞吐、ITL | 2024-08-01；读到介绍 GenAI-Perf 前，不加入另一套压测；明确响应块 ITL 与请求 TPOT 的差别 |
| MDN 中文社区 | [CN-HTTP](../../resources/serving.md#cn-http)：组成、flow、HTTP/1.1 消息 | 官方站中文译文；指定正文已预读，不采用页面中旧 QUIC 背景 |
| 杨保华、戴王剑等 | [CN-Docker](../../resources/serving.md#cn-docker)、[CN-Storage](../../resources/training.md#cn-storage)：概念 2.2.1～6、卷生命周期及 source/target | 社区中文教程当前 GitBook；正文概念已预读，动态命令块未核验，实操沿用 S3/S5 |
| AWS | [S3 术语](../../resources/training.md#cn-storage)、[退避重试](../../resources/scheduling.md#cn-retry) | 官方中文译文；限定文字已预读，object key 译作“密钥”时不理解为凭据；不创建云资源 |
| Kubernetes | [CN-Kubernetes](../../resources/scheduling.md#cn-kubernetes)：对象、spec/status、资源/单位、调度与 Events | 官方当前中文；指定文字已预读，跳过新特性扩展。Pending 必须结合事件/容器状态，阅读不等于集群验证 |
| Datawhale DIY-LLM | [ZeRO 分类](../../resources/training.md#cn-sharding)、[TP 两层 MLP](../../resources/training.md#cn-parallel) | 当前社区讲义，仅限定文字/代数已预读；不是 CS336 2026 的逐段译文。FSDP2 接口、其他通信/性能概括不纳入 |
| 小林 x | [CN-Scheduling](../../resources/scheduling.md#cn-scheduling)：FCFS/SJF | 作者原站当前文字，指定范围已预读；操作系统例子用于排队直觉，不冒充 Ray 策略或吞吐结论 |

上述推荐的正文页均已成功取得页面内容；网页内容可能后续更新。D2L 数学/统计页本次可访问，但没有完成整段中文对应预读，不能把 HTTP 成功登记成预读完成。Docker 的动态命令与网页动画同理。

<a id="video-status"></a>

## 视频证据分别记录

以下均为中文讲解来源。作者课表/仓库中的标题、链接和分集位置已确认，不是仅打开课程首页。B 站页面/API 直接读取返回访问限制（412），因此没有把搜索片段或播放地址当作字幕、画面证据；不提供分钟时间戳。

| 来源与讲次 | 作者处标题/分集对应 | 直接播放核验 | 字幕 | 画面/分钟范围 | 独立文字路径 |
| --- | --- | --- | --- | --- | --- |
| 李沐 2021 数据操作 | 已确认 BV1CV411Y7i4 | 未完成 | 未检查 | 未检查 | CN-Tensor |
| 李沐 2021 自动求导 | 已确认 BV1KA411N7Px | 未完成 | 未检查 | 未检查 | CN-Autograd |
| 李沐 2021 线性回归：从零实现 | 已确认 BV1PX4y1g7KC，P3 | 未完成 | 未检查 | 未检查 | CN-Train |
| 李沐 2021 模型构造：读写文件 | 已确认 BV1AK4y1P7vs，P4 | 未完成 | 未检查 | 未检查 | CN-Save |
| 李沐 2021 硬件：CPU 和 GPU | 已确认 BV1TU4y1j7Wd | 未完成 | 未检查 | 未检查 | CN-Hardware |
| 李沐 2021 多 GPU 训练 | 已确认 BV1vU4y1V7rd | 未完成 | 未检查 | 未检查 | CN-DP |
| 李沐 2021 注意力分数 | 已确认 BV1Tb4y167rb | 未完成 | 未检查 | 未检查 | CN-Attention |
| coderonion CUDA 第 3 集 | 已确认 BV1oc411x7Gt，运行第一个 CUDA 程序 | 未完成 | 未检查 | 未检查 | CN-CUDA |
| coderonion CUDA 第 4 集 | 已确认 BV1jueweLEQ1，你好 CUDA | 未完成 | 未检查 | 未检查 | CN-CUDA |

证据入口：[李沐 2021 中文课表](https://c.d2l.ai/zh-v2/)与 [CUDA 12.x 作者仓库](https://github.com/coderonion/cuda-beginner-course-cpp-version)。直接视频链接放在[资料入口](../../resources/README.md)和对应课页，不在这里另立观看顺序。Missing Semester 中文站作为社区译文登记，不自动称为中文原创视频或已核验中文字幕。

## 没有采用或只选有限范围的候选

筛选结论仅针对本课的用途和当前检索版本，不评价整套资源。

| 候选 | 本次发现与处理 |
| --- | --- |
| 廖雪峰字典/文件小节 | “字典顺序无关”不适合当前 Python 3；文本 read(size) 不能一概解释成字节。改用官方中文对应范围，作者其余合适小节保留 |
| DIY-LLM PyTorch/资源章节 | Tensor 总是连续、contiguous 总是新存储等概括不可靠；精度段也不足以解释本课数值边界。不作为 R-VIEWS/R-NUMERICS 补充 |
| DIY-LLM GPU/编译章节 | GEMM 尾部 mask、shared 数据移动的描述及 JIT/compile 区分需额外修正。选择上游社区译文和 NVIDIA 限定融合例子 |
| DIY-LLM 分布式训练章节 | ReduceScatter 描述存在输出归属混淆，PP 效率公式不适合直接使用。只保留 ZeRO 三阶段分类和 TP MLP/f/g 限定段，避开后续泛化通信量/性能百分比 |
| DIY-LLM 推理章节 | 简化 cache/伪造 logits 示例及时间口径不足以支撑本课真实 KV/TTFT 检查。改用 NVIDIA 概念说明，APC 仍缺 |
| 谭升旧内存优化/归约代码 | 事务大小、对齐、warp 锁步或提前 return 的条件不能直接用于当前设备/任意长度。不指定这些实现，只保留配对、索引和计时文字 |
| [AiFly 的 Ray 博客](https://www.cnblogs.com/softlin/p/17976571) | 示例有未定义调用/缺装饰器；多 CPU 资源申请不代表自动多线程。未接入课页 |
| [peacemaple 的 Ray 博客](https://www.cnblogs.com/peacemaple/p/18916378) | ray.wait 被概括为不带条件的非阻塞、取消后 get 的说明和示例存在问题。未接入课页 |
| Ray 中文镜像与视频候选 | 部分镜像维护者/版本关系不清；视频候选未核验或配套代码访问受限。未标官方，也未推荐为完整 Ray 基础 |
| Hugging Face 旧中文 parallelism 路径 | HTTP 200 实际是文档不存在提示，属于软 404；没有加入资源卡 |
| Python 中文视频合集候选 | 页面访问受限，未确认与 P1～P8 匹配的分集/先修。保留中文正文和原 CS50P，不用大合集充当逐段对应 |

<a id="pending"></a>

## 仍待补的具体内容

- Python 与 C++ 的合适中文原创视频分集；C++ 完整类型、引用与生命周期对应。
- 浮点数值、现代 warp/同步、Compute Sanitizer、Nsight、Roofline 与真实流量计量。
- Triton 类型提升；torch.compile 的 graph break、guard/重编译、首次成本与回本；显存 allocated/reserved/peak。
- token/BPE/聊天模板、当前 vLLM 服务与 bench 字段、APC 命中证据、chunked prefill、goodput 与 trace。
- NCCL tests 的 algbw/busbw、AMP、多 worker 输入等待与通信重叠；FSDP2/DTensor/DCP 完整恢复。
- Ray Task/Actor/ObjectRef、逻辑资源/隔离与调度策略的可靠中文对应；PP 完整训练调度。
- 已接入视频的直接播放、字幕、画面和时间轴。暂未找到合适中文视频的 Docker、存储、Kubernetes 等主题保留指定中文正文。

暂缺不等于相关知识被省略：本地中文解释、原英文来源、实验与掌握检查都继续有效。不用 FSDP1、单进程 DataParallel、旧工具或未经核验的镜像填这些空位。

## 交付检查

- `python scripts/check_docs.py`：162 份 Markdown、2127 条本地链接、16 个单元、52 处图片引用/52 组 PNG-SVG，通过，0 错误。覆盖相对路径、锚点、代码围栏、折叠块和课程导航。
- `git diff --check`：通过，无空白差异错误。新增段落与资源登记之外，只更新 P-MATH 的中文页可访问状态，没有修改英文指定范围。
- 对基线逐行比对：除上述访问状态句外，所有旧 Markdown 非空行按原顺序保留；395 次原外部 URL 引用没有减少。65/65 课页各有一个中文补充段，56/56 原资源锚点均有对应或缺项说明。
- `course/progress.md`、课程顺序、单元 README/assessment、labs、exercises、projects、assets、scripts 和旧核验/归档文件没有修改；docs 根目录仍只有四份维护文档。
- 新增引用的正文 URL 与本次缓存的成功读取记录对应；视频例外单独列在上表，不用作者索引确认代替播放验证。页面片段锚点按正文标题/HTML 核对，未声称外部站点长期可用。
- 人工核对 P1→W1、P8→W6、S2/S3→W8、训练/S4→W11、S5→W12、S6→W15/W16 的新增段落：没有加入新的必读次数或操作前提；W14 仍只要求原有 2 stage 前向时间线。

检查脚本和公开网页读取缓存放在仓库外临时目录，不作为课程正文或学习结果提交。没有新增依赖，也没有执行课程实验；后续个人作答、实际耗时与硬件运行继续各自记录。
