# 模型与编译资料

[资料目录](README.md)

沿着“Tensor 怎样组成模型、模型怎样成为设备上的工作”回查。Attention 的语义、资源开销与编译成本分别有对应练习，不以读完论文替代数值和计时检查。

<a id="r-sdpa"></a>

### R-SDPA · Attention 语义和后端

W6-S01 必读；中等；英文；先修 C、W5。

**来源**：[SDPA 教程](https://docs.pytorch.org/tutorials/intermediate/scaled_dot_product_attention_tutorial.html)；[SDPA API 2.14](https://docs.pytorch.org/docs/2.14/generated/torch.nn.functional.scaled_dot_product_attention.html)。

**读到哪里**：教程开头接口与 Explicit Dispatcher Control；API 只核对 mask、is_causal、dropout_p，40 分钟；停在前向对照。

**带着什么问题读**：显式 Attention 与 SDPA 统一语义；函数式 dropout 显式设 0，布尔 True 表示可参与；后端需证据。 [打开练习与自查](../weeks/week-06-attention/session-01.md)。

<a id="r-flash"></a>

### R-FLASH · Attention 的 IO 与在线分块

W6-S02 必读；进阶起步；英文论文；W4、W5、W6-S01。

**来源**：[FlashAttention 原论文 arXiv v2](https://arxiv.org/pdf/2205.14135v2)。

**读到哪里**：§2.1～2.2 → §3.1 Algorithm 1 → §3.2 IO 结论，50 分钟；停止于前向，证明和反向后置。这里 v2 是原论文修订版，不是 FlashAttention-2。

**带着什么问题读**：图中找到不再完整写回的 score/probability 矩阵；复用小 pre-norm Block 建账本。 [打开练习与自查](../weeks/week-06-attention/session-02.md)。

<a id="r-trace"></a>

### R-TRACE · 模型区段与 CPU/GPU 时间线

W6-S03 必读；中等；英文；W3 测量。

**来源**：[PyTorch Profiler](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html)；[Nsight Systems CUDA Trace](https://docs.nvidia.com/nsight-systems/UserGuide/index.html#cuda-trace)。

**读到哪里**：Profiler 步骤 3/4 和 export_chrome_trace，30 分钟；CUDA Trace → Basic CUDA trace，30 分钟。区段标记按需查 Marking and Labeling Regions；不运行整份 ResNet 例子。

**带着什么问题读**：把工具接到自己的 Block，标热点与空档；正式延迟另外计时。 [打开练习与自查](../weeks/week-06-attention/session-03.md)。

<a id="r-compile"></a>

### R-COMPILE · eager、编译和变化输入

W13 三段必读；中等；英文；W6 小 Block、计时。

**来源**：[Introduction to torch.compile](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html)。

**读到哪里**：S01 Basic Usage 30 分钟；S02 Demonstrating Speedups 与计时 60 分钟；S03 Graph Breaks，遇卡点查 Troubleshooting，45 分钟。停止于一处 graph break 与第二个 shape。

**带着什么问题读**：把正确性、首次/稳态、graph break/重编译分开；不增加 GELU 或完整 CS336 作业。 [打开练习与自查](../weeks/week-13-systems/README.md)。

<a id="r-memory-lifetime"></a>

### R-MEMORY-LIFETIME · 活对象、缓存与阶段峰值

W6 第四段必学；P8、单卡训练与 W1 字节账本后；复用基础小模型。

**来源与范围**：[CUDA semantics 2.14 / Memory management](https://docs.pytorch.org/docs/2.14/notes/cuda.html#memory-management) 开头两段，约 10 分钟，停止于高级分配器配置前。接口按需查 [memory_allocated](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.memory.memory_allocated.html)、[memory_reserved](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.memory.memory_reserved.html)、[max_memory_allocated](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.memory.max_memory_allocated.html)、[reset_peak_memory_stats](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.memory.reset_peak_memory_stats.html) 的首段与参数，约 10 分钟，计入本节。

**检查**：[小模型状态表和八份 Tensor 留存](../weeks/week-06-attention/session-04.md) 区分引用释放、缓存保留和峰值。单独采样会同步，只用于诊断；不拿这里的阶段时间冒充训练吞吐。正文与本地有界例子的核验见 [记录](../docs/audits/2026-10-04-knowledge.md)。
