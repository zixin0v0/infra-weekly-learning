# GPU 与算子资料

[资料目录](README.md)

这些资料帮助你把线程、数据搬运与算子耗时联系起来。先读当前小节指定的部分，再用文档核对接口；同一来源在不同单元出现时，只读这次需要的范围。

<a id="r-cuda"></a>

### R-CUDA · CUDA 线程与 host/device 数据路径

W2-S01/S02、W3 同步必读；中等；英文；A、B、W1。

**来源**：[Programming Model](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html)；[Intro to CUDA C++](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/intro-to-cuda-cpp.html)；[Writing SIMT Kernels](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html)。

**读到哪里**：W2-S01：§1.2、§2.1.2、§2.3.2 的层级/索引，60 分钟；S02：§2.1.3.2、§2.1.4、§2.1.7 的分配/拷贝/同步/错误，30 分钟；W3-S01 只回查 §2.3.2.1 的 barrier。按标题复核节号，不读高级集群。

**带着什么问题读**：先 CPU 模拟 N=10 的覆盖，再组装 Vector Add；W3 解释所有参与线程为何必须到达 barrier。 [打开练习与自查](../weeks/week-02-cuda-execution/README.md)。

<a id="r-sanitizer"></a>

### R-SANITIZER · 内存与共享同步检查

W2/W3 必读；中等；英文；能编译 CUDA。

**来源**：[Compute Sanitizer](https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html)。

**读到哪里**：W2 读 Using Memcheck 与首个错误报告，15 分钟；W3 读 Using Racecheck、Using Synccheck，15 分钟。只查运行与错误位置，不通读工具选项。

**带着什么问题读**：对小型边界输入检查；工具检查与正确性/性能分开，不能用未报错证明任意程序正确。 [打开练习与自查](../weeks/week-03-reduction-profiling/README.md)。

<a id="r-best"></a>

### R-BEST · 计时、有效带宽与 GEMM 数据复用

W2/W4 必读；中等；英文；线程映射与矩阵乘法。

**来源**：[CUDA Best Practices](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html)。

**读到哪里**：W2-S03：§9.1.2、§9.2，45 分钟；W4-S01：§10.2.1 连续/错位访问，45 分钟；S02：§10.2.3.1～2 的 banks 和 C=AB，60 分钟。C=AAᵀ/padding 仅卡点查阅，替换 15 分钟。

**带着什么问题读**：一个来源分别服务计量与复用；做 3N 字节账本、地址表、tile 边界与同步检查。 [打开练习与自查](../weeks/week-04-gemm/README.md)。

<a id="r-reduce"></a>

### R-REDUCE · 共享内存归约代码

W3-S01 必读；中等；英文代码；W2。

**来源**：[GPU MODE shared_reduce.cu 固定提交](https://github.com/gpu-mode/lectures/blob/77a8df418834e5789c12da23e7d2719e0efabef1/lecture_009/shared_reduce.cu)；[NVIDIA 归约图解](https://developer.download.nvidia.com/assets/cuda/files/reduction.pdf)。

**读到哪里**：代码只读加载、循环、同步，约 30 分钟；图解只在卡住时读 Reduction #3，PDF 页序 14～15，替换 15 分钟。旧例固定单 block/2048 元素，不能当任意长度实现。

**带着什么问题读**：画 8 元素树，再写每 block 部分和；CPU FP64 收尾一致，主表只比 GPU 第一阶段。 [打开练习与自查](../weeks/week-03-reduction-profiling/session-01.md)。

<a id="r-warp"></a>

### R-WARP · warp 交换、mask 与同步

W3-S02 必读；中等；英文；W3-S01。

**来源**：[NVIDIA Warp-Level Primitives](https://developer.nvidia.com/blog/using-cuda-warp-level-primitives/)。

**读到哪里**：Synchronized Data Exchange → Active Mask Query → Warp Synchronization，30 分钟；停在这三节。读 __shfl_down_sync 与参与 mask，不复用旧隐式同步技巧。

**带着什么问题读**：把 warp 局部和与 block 合并分开；无效元素填零但仍参与，先用完整 warp 练习，部分 warp 留作拓展。 [打开练习与自查](../weeks/week-03-reduction-profiling/session-02.md)。

<a id="r-l6"></a>

### R-L6 · 测量、Triton 与编译的讲义例子

W3/W5/W13 指定范围必读；中等；英文；对应前段。

**来源**：[CS336 lecture_06.py 固定提交](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py)。

**读到哪里**：W3：benchmarking/profiling，20 分钟；W5：triton_introduction，15 分钟；W13：naive_vs_builtin_vs_compiled_gelu，15 分钟，benchmarking 仅回查同步。各次到指定函数结束；不额外完成整讲算子。

**带着什么问题读**：分别核对采样边界、program 抽象与 eager/compile 公平对照；练习接到各单元已有实现。 [打开练习与自查](../course/guide.md)。

**视频入口**：[CS336 Lecture 6](https://www.youtube.com/watch?v=xnDHaNUvHBg)。沿本卡讲义定位，按完整主题观看与暂停练习，分钟位置未核验。

<a id="r-ncu"></a>

### R-NCU · kernel 内部的性能证据

W3-S03 必读，W4 查阅；中等；英文；W2 可靠计时。

**来源**：[Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html)。

**读到哪里**：W3：§2.2.1～2.2.3 的 sections/replay；只取 SpeedOfLight、MemoryWorkloadAnalysis、Occupancy，40 分钟。W4 遇到 Roofline 卡点查 §2.9，替换 15 分钟。

**带着什么问题读**：由假设选择指标，正式计时不启用 profiler；占用率不作为单独成功标准。 [打开练习与自查](../weeks/week-03-reduction-profiling/session-03.md)。

<a id="r-roofline"></a>

### R-ROOFLINE · 用 Roofline 连接 FLOPs 与搬运

W4-S03 必读；中等；英文；W1 账本、W4 tile。

**来源**：[Scaling Book Rooflines](https://jax-ml.github.io/scaling-book/roofline/)。

**读到哪里**：Visualizing rooflines → Matrix multiplication；30 分钟，停止于矩阵乘法，硬件数字只作作者案例。

**带着什么问题读**：用自己的输入算强度和上界，再与库及手写版本比较；不拿 TPU 数字当本机参数。 [打开练习与自查](../weeks/week-04-gemm/session-03.md)。

<a id="r-triton"></a>

### R-TRITON · Triton program、mask 与类型

W5-S01 必读；中等；英文；W2 索引、W4 访存。

**来源**：[Vector Addition](https://triton-lang.org/main/getting-started/tutorials/01-vector-add.html)；[Triton Semantics](https://triton-lang.org/main/python-api/triton-semantics.html)。

**读到哪里**：先读 Compute Kernel 的 add_kernel/add，20 分钟；再读 Semantics 的 Broadcasting 与 Type Promotion，10 分钟，替代泛看示例。Differences with NumPy 按需查阅，这里不实现负整数除法。

**带着什么问题读**：广播和类型以这份上游文档为准；用长度 10/块 4 的映射检查 mask，并预测 (3,1)+(1,4) 为 (3,4)。 [打开练习与自查](../weeks/week-05-triton-softmax/session-01.md)。

**阅读代码快照**：[01-vector-add.py](https://github.com/triton-lang/triton/blob/aad2a60d958f945420c5c40936b37d411fb02e89/python/tutorials/01-vector-add.py)，与本卡相同函数范围；固定阅读版本，不代表安装版本。语义文档仍为 main 页面。

<a id="r-softmax"></a>

### R-SOFTMAX · 稳定 Softmax 与融合

W5-S02 必读；中等；英文；M2、归约、Triton。

**来源**：[Fused Softmax](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html)。

**读到哪里**：Motivations → Compute Kernel → Unit Test → Benchmark，60 分钟；逐项对照 naive_softmax 与 softmax_kernel，启动优化先沿用并记录版本。

**带着什么问题读**：做大幅值、非二次幂列宽与误差检查；正确填充值和逐元素参考不可只靠行和替代。 [打开练习与自查](../weeks/week-05-triton-softmax/session-02.md)。

**阅读代码快照**：[02-fused-softmax.py](https://github.com/triton-lang/triton/blob/aad2a60d958f945420c5c40936b37d411fb02e89/python/tutorials/02-fused-softmax.py)，按本卡四节阅读；固定阅读提交不等于本机安装版本。

<a id="r-online"></a>

### R-ONLINE · 分块 Softmax 的状态合并

W5-S03 必读；进阶起步；英文论文；稳定 Softmax。

**来源**：[Online normalizer v2](https://arxiv.org/pdf/1805.02867v2)。

**读到哪里**：§2 Algorithm 2 → §3 Algorithm 3 → §3.1 并行合并，45 分钟；停在合并，不读 Top-k 融合。

**带着什么问题读**：先手算两块最大值/指数和，再 CPU 核对；不新增分块 GPU Softmax 项目。 [打开练习与自查](../weeks/week-05-triton-softmax/session-03.md)。

<a id="r-gpu-hardware"></a>

### R-GPU-HARDWARE · 逻辑线程怎样占用硬件

W2 第一段必学；先会 W1 数据字节；中文主讲在 [硬件关系与容量例子](../weeks/week-02-cuda-execution/session-01.md)。

**来源与范围**：[Writing SIMT Kernels §2.3.7](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html#kernel-launch-and-occupancy) 从分配 block 到 SM 资源列表，停在特定设备表之前；[Best Practices §11.1](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#occupancy) 的定义及 Calculating Occupancy 开头寄存器说明，停在 compute capability 7.0 数字例子之前。约 20 分钟，已包含在本单元，不通读调优参数。

**检查**：手算 block/warp/shared 限制，再解释寄存器、shared、L1/L2、global 的关系。文档正文已预读；真实设备占用率和性能必须实际测量，不能用虚构 SM 数字替代。
