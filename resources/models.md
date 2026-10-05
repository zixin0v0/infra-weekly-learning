# 模型与编译资料

[资料目录](README.md)

沿着“Tensor 怎样组成模型、模型怎样成为设备上的工作”回查。Attention 的语义、资源开销与编译成本分别有对应练习，不以读完论文替代数值和计时检查。

<a id="r-sdpa"></a>

### R-SDPA · Attention 语义和后端

**中文补充（按需，部分）：** 中文缩放点积/mask；SDPA 参数与后端控制仍查原文。 [对应范围](#cn-attention)。

W6-S01 必读；中等；英文；先修 C、W5。

**来源**：[SDPA 教程](https://docs.pytorch.org/tutorials/intermediate/scaled_dot_product_attention_tutorial.html)；[SDPA API 2.14](https://docs.pytorch.org/docs/2.14/generated/torch.nn.functional.scaled_dot_product_attention.html)。

**读到哪里**：教程开头接口与 Explicit Dispatcher Control；API 只核对 mask、is_causal、dropout_p，40 分钟；停在前向对照。

**带着什么问题读**：显式 Attention 与 SDPA 统一语义；函数式 dropout 显式设 0，布尔 True 表示可参与；后端需证据。 [打开练习与自查](../weeks/week-06-attention/session-01.md)。

<a id="r-flash"></a>

### R-FLASH · Attention 的 IO 与在线分块

**中文补充（按需，部分）：** 中文分块公式；动画、复杂度与后端实现未核验。 [对应范围](#cn-flash)。

W6-S02 必读；进阶起步；英文论文；W4、W5、W6-S01。

**来源**：[FlashAttention 原论文 arXiv v2](https://arxiv.org/pdf/2205.14135v2)。

**读到哪里**：§2.1～2.2 → §3.1 Algorithm 1 → §3.2 IO 结论，50 分钟；停止于前向，证明和反向后置。这里 v2 是原论文修订版，不是 FlashAttention-2。

**带着什么问题读**：图中找到不再完整写回的 score/probability 矩阵；复用小 pre-norm Block 建账本。 [打开练习与自查](../weeks/week-06-attention/session-02.md)。

<a id="r-trace"></a>

### R-TRACE · 模型区段与 CPU/GPU 时间线

**中文补充（按需，暂缺）：** Profiler 的 CPU/kernel/等待时间线缺匹配中文正文。 [对应范围](../docs/audits/2026-10-05-chinese-resources.md#source-coverage)。

W6-S03 必读；中等；英文；W3 测量。

**来源**：[PyTorch Profiler](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html)；[Nsight Systems CUDA Trace](https://docs.nvidia.com/nsight-systems/UserGuide/index.html#cuda-trace)。

**读到哪里**：Profiler 步骤 3/4 和 export_chrome_trace，30 分钟；CUDA Trace → Basic CUDA trace，30 分钟。区段标记按需查 Marking and Labeling Regions；不运行整份 ResNet 例子。

**带着什么问题读**：把工具接到自己的 Block，标热点与空档；正式延迟另外计时。 [打开练习与自查](../weeks/week-06-attention/session-03.md)。

<a id="r-compile"></a>

### R-COMPILE · eager、编译和变化输入

**中文补充（按需，部分）：** sum/abs 融合例子；graph break、重编译和回本分析仍缺。 [对应范围](#cn-compile)。

W13 三段必读；中等；英文；W6 小 Block、计时。

**来源**：[Introduction to torch.compile](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html)。

**读到哪里**：S01 Basic Usage 30 分钟；S02 Demonstrating Speedups 与计时 60 分钟；S03 Graph Breaks，遇卡点查 Troubleshooting，45 分钟。停止于一处 graph break 与第二个 shape。

**带着什么问题读**：把正确性、首次/稳态、graph break/重编译分开；不增加 GELU 或完整 CS336 作业。 [打开练习与自查](../weeks/week-13-systems/README.md)。

<a id="r-memory-lifetime"></a>

### R-MEMORY-LIFETIME · 活对象、缓存与阶段峰值

**中文补充（按需，部分）：** 中文 detach 例子；allocated/reserved/peak 等未覆盖。 [对应范围](#cn-memory)。

W6 第四段必学；P8、单卡训练与 W1 字节账本后；复用基础小模型。

**来源与范围**：[CUDA semantics 2.14 / Memory management](https://docs.pytorch.org/docs/2.14/notes/cuda.html#memory-management) 开头两段，约 10 分钟，停止于高级分配器配置前。接口按需查 [memory_allocated](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.memory.memory_allocated.html)、[memory_reserved](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.memory.memory_reserved.html)、[max_memory_allocated](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.memory.max_memory_allocated.html)、[reset_peak_memory_stats](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.memory.reset_peak_memory_stats.html) 的首段与参数，约 10 分钟，计入本节。

**检查**：[小模型状态表和八份 Tensor 留存](../weeks/week-06-attention/session-04.md) 区分引用释放、缓存保留和峰值。单独采样会同步，只用于诊断；不拿这里的阶段时间冒充训练吞吐。正文与本地有界例子的核验见 [记录](../docs/audits/2026-10-04-knowledge.md)。

## 中文补充：从模型形状接到执行

<a id="cn-attention"></a>

### CN-Attention：先追踪 query 能读到哪些位置

**中文视频：** 李沐，2021 [注意力分数](https://www.bilibili.com/video/BV1Tb4y167rb/)。看缩放点积与掩蔽的解释，能说清 Q/K/V 的作用后回 W6；加性注意力不要求补学。

**中文正文：** 作者团队[§10.3 注意力评分函数](https://zh.d2l.ai/chapter_attention-mechanisms/attention-scoring-functions.html)的 §10.3.1、§10.3.3，以及[§10.5 多头注意力](https://zh.d2l.ai/chapter_attention-mechanisms/multihead-attention.html)开头和 §10.5.1 模型公式。PyTorch 示例只辅助跟踪 shape，不运行整套翻译模型。

正文指定范围已预读；视频讲次由作者课表确认，字幕/画面未检查。这是同主题中文讲解。原书的 valid_lens 不是 SDPA 的布尔 mask；继续按 R-SDPA 核对 True 的含义、is_causal 和 dropout_p。图中的列向量记法也要先转换成本课 batch/sequence/head 的维度约定。

<a id="cn-flash"></a>

### CN-Flash：块内归一化以后，为什么还要改旧结果

**中文图文：** Bowen Zhou，2024 [图解 Flash Attention](https://bowenzhou.top/posts/2024/illustrated-flash-attention)，只读“Softmax Tiling”及“在 Flash Attention 中的应用”的最大值、指数和、输出更新公式；先完成 W5 分块合并，再看 W6 的输出更新。

这是作者原站的同主题中文讲解；指定文字和公式已预读，网页动画未逐帧核验。用本课变量重新写出两块合并，不要求额外实现 FlashAttention。文章前部口述输出修正时省略了旧最大值的指数因子，以下方完整公式和原论文 Algorithm 1 为准；“复杂度分析”不在推荐范围，其中 d 被误称为头数，本课 d 是每头维度。

<a id="cn-compile"></a>

### CN-Compile：融合后为什么仍可能有两个 kernel

**中文正文：** NVIDIA / Daniel Rodriguez，2026-07-10 [NVIDIA CUDA 中的内核融合](https://developer.nvidia.cn/blog/kernel-fusion-in-nvidia-cuda-optimizing-memory-traffic-and-launch-overhead/)，只读“隐式内核融合”：sum(abs(x))、torch.compile、两个生成的归约 kernel，到“显式核函数融合”前。

这是 NVIDIA 发布的中文版本，不是 CS336 译文。指定段落已预读，适合 W13 第一段用具体例子理解融合。文中 CUDA 13.2 C++ 接口、性能表与本课无关，均跳过；生成几个 kernel 依赖形状与版本，不能照抄作者观察。首次编译、回本次数、graph break/recompile 和 Profiler 操作仍读原英文范围，中文对应资料暂缺。

<a id="cn-memory"></a>

### CN-Memory：中文解释能帮助到哪里

W6 显存寿命可回看[中文自动微分](foundations.md#cn-autograd)的 detach 例子，理解为什么保留计算关系会影响对象寿命。这仅补梯度路径；allocated、reserved、峰值重置、inference_mode 和当前版本显存诊断，尚未找到已预读且足够准确的外部中文补充。继续使用 R-MEMORY-LIFETIME 和本课图解，不用旧缓存清理经验替代实际测量。
