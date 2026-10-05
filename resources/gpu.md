# GPU 与算子资料

[资料目录](README.md)

这些资料帮助你把线程、数据搬运与算子耗时联系起来。先读当前小节指定的部分，再用文档核对接口；同一来源在不同单元出现时，只读这次需要的范围。

<a id="r-cuda"></a>

### R-CUDA · CUDA 线程与 host/device 数据路径

**中文补充（按需，部分）：** 中文入门视频与限定索引例子；保留显式搬运和同步实验。 [对应范围](#cn-cuda)。

W2-S01/S02、W3 同步必读；中等；英文；A、B、W1。

**来源**：[Programming Model](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html)；[Intro to CUDA C++](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/intro-to-cuda-cpp.html)；[Writing SIMT Kernels](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html)。

**读到哪里**：W2-S01：§1.2、§2.1.2、§2.3.2 的层级/索引，60 分钟；S02：§2.1.3.2、§2.1.4、§2.1.7 的分配/拷贝/同步/错误，30 分钟；W3-S01 只回查 §2.3.2.1 的 barrier。按标题复核节号，不读高级集群。

**带着什么问题读**：先 CPU 模拟 N=10 的覆盖，再组装 Vector Add；W3 解释所有参与线程为何必须到达 barrier。 [打开练习与自查](../weeks/week-02-cuda-execution/README.md)。

<a id="r-sanitizer"></a>

### R-SANITIZER · 内存与共享同步检查

**中文补充（按需，暂缺）：** 现代 Compute Sanitizer 运行与判读缺合适中文对应。 [对应范围](../docs/audits/2026-10-05-chinese-resources.md#source-coverage)。

W2/W3 必读；中等；英文；能编译 CUDA。

**来源**：[Compute Sanitizer](https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html)。

**读到哪里**：W2 读 Using Memcheck 与首个错误报告，15 分钟；W3 读 Using Racecheck、Using Synccheck，15 分钟。只查运行与错误位置，不通读工具选项。

**带着什么问题读**：对小型边界输入检查；工具检查与正确性/性能分开，不能用未报错证明任意程序正确。 [打开练习与自查](../weeks/week-03-reduction-profiling/README.md)。

<a id="r-best"></a>

### R-BEST · 计时、有效带宽与 GEMM 数据复用

**中文补充（按需，部分）：** 分块伪代码补复用直觉；合并访存、shared 同步等仍查原指南。 [对应范围](#cn-triton)。

W2/W4 必读；中等；英文；线程映射与矩阵乘法。

**来源**：[CUDA Best Practices](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html)。

**读到哪里**：W2-S03：§9.1.2、§9.2，45 分钟；W4-S01：§10.2.1 连续/错位访问，45 分钟；S02：§10.2.3.1～2 的 banks 和 C=AB，60 分钟。C=AAᵀ/padding 仅卡点查阅，替换 15 分钟。

**带着什么问题读**：一个来源分别服务计量与复用；做 3N 字节账本、地址表、tile 边界与同步检查。 [打开练习与自查](../weeks/week-04-gemm/README.md)。

<a id="r-reduce"></a>

### R-REDUCE · 共享内存归约代码

**中文补充（按需，部分）：** 中文树形合并解释；旧 kernel 不作为正确性参考。 [对应范围](#cn-reduce)。

W3-S01 必读；中等；英文代码；W2。

**来源**：[GPU MODE shared_reduce.cu 固定提交](https://github.com/gpu-mode/lectures/blob/77a8df418834e5789c12da23e7d2719e0efabef1/lecture_009/shared_reduce.cu)；[NVIDIA 归约图解](https://developer.download.nvidia.com/assets/cuda/files/reduction.pdf)。

**读到哪里**：代码只读加载、循环、同步，约 30 分钟；图解只在卡住时读 Reduction #3，PDF 页序 14～15，替换 15 分钟。旧例固定单 block/2048 元素，不能当任意长度实现。

**带着什么问题读**：画 8 元素树，再写每 block 部分和；CPU FP64 收尾一致，主表只比 GPU 第一阶段。 [打开练习与自查](../weeks/week-03-reduction-profiling/session-01.md)。

<a id="r-warp"></a>

### R-WARP · warp 交换、mask 与同步

**中文补充（按需，暂缺）：** 现代 warp 的参与 mask/同步语义缺准确中文对应。 [对应范围](../docs/audits/2026-10-05-chinese-resources.md#source-coverage)。

W3-S02 必读；中等；英文；W3-S01。

**来源**：[NVIDIA Warp-Level Primitives](https://developer.nvidia.com/blog/using-cuda-warp-level-primitives/)。

**读到哪里**：Synchronized Data Exchange → Active Mask Query → Warp Synchronization，30 分钟；停在这三节。读 __shfl_down_sync 与参与 mask，不复用旧隐式同步技巧。

**带着什么问题读**：把 warp 局部和与 block 合并分开；无效元素填零但仍参与，先用完整 warp 练习，部分 warp 留作拓展。 [打开练习与自查](../weeks/week-03-reduction-profiling/session-02.md)。

<a id="r-l6"></a>

### R-L6 · 测量、Triton 与编译的讲义例子

**中文补充（按需，部分）：** Triton 和融合有社区译文；计量、剖析与完整讲义未覆盖。 [对应范围](#cn-triton)。

W3/W5/W13 指定范围必读；中等；英文；对应前段。

**来源**：[CS336 lecture_06.py 固定提交](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py)。

**读到哪里**：W3：benchmarking/profiling，20 分钟；W5：triton_introduction，15 分钟；W13：naive_vs_builtin_vs_compiled_gelu，15 分钟，benchmarking 仅回查同步。各次到指定函数结束；不额外完成整讲算子。

**带着什么问题读**：分别核对采样边界、program 抽象与 eager/compile 公平对照；练习接到各单元已有实现。 [打开练习与自查](../course/guide.md)。

**视频入口**：[CS336 Lecture 6](https://www.youtube.com/watch?v=xnDHaNUvHBg)。沿本卡讲义定位，按完整主题观看与暂停练习，分钟位置未核验。

<a id="r-ncu"></a>

### R-NCU · kernel 内部的性能证据

**中文补充（按需，暂缺）：** 当前 Nsight Compute 指标及 profiler 开销缺匹配中文章节。 [对应范围](../docs/audits/2026-10-05-chinese-resources.md#source-coverage)。

W3-S03 必读，W4 查阅；中等；英文；W2 可靠计时。

**来源**：[Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html)。

**读到哪里**：W3：§2.2.1～2.2.3 的 sections/replay；只取 SpeedOfLight、MemoryWorkloadAnalysis、Occupancy，40 分钟。W4 遇到 Roofline 卡点查 §2.9，替换 15 分钟。

**带着什么问题读**：由假设选择指标，正式计时不启用 profiler；占用率不作为单独成功标准。 [打开练习与自查](../weeks/week-03-reduction-profiling/session-03.md)。

<a id="r-roofline"></a>

### R-ROOFLINE · 用 Roofline 连接 FLOPs 与搬运

**中文补充（按需，暂缺）：** 逻辑字节、实际流量、算术强度与上限的完整中文对应待补。 [对应范围](../docs/audits/2026-10-05-chinese-resources.md#source-coverage)。

W4-S03 必读；中等；英文；W1 账本、W4 tile。

**来源**：[Scaling Book Rooflines](https://jax-ml.github.io/scaling-book/roofline/)。

**读到哪里**：Visualizing rooflines → Matrix multiplication；30 分钟，停止于矩阵乘法，硬件数字只作作者案例。

**带着什么问题读**：用自己的输入算强度和上界，再与库及手写版本比较；不拿 TPU 数字当本机参数。 [打开练习与自查](../weeks/week-04-gemm/session-03.md)。

<a id="r-triton"></a>

### R-TRITON · Triton program、mask 与类型

**中文补充（按需，部分）：** 向量相加的社区译文；类型提升继续查原文。 [对应范围](#cn-triton)。

W5-S01 必读；中等；英文；W2 索引、W4 访存。

**来源**：[Vector Addition](https://triton-lang.org/main/getting-started/tutorials/01-vector-add.html)；[Triton Semantics](https://triton-lang.org/main/python-api/triton-semantics.html)。

**读到哪里**：先读 Compute Kernel 的 add_kernel/add，20 分钟；再读 Semantics 的 Broadcasting 与 Type Promotion，10 分钟，替代泛看示例。Differences with NumPy 按需查阅，这里不实现负整数除法。

**带着什么问题读**：广播和类型以这份上游文档为准；用长度 10/块 4 的映射检查 mask，并预测 (3,1)+(1,4) 为 (3,4)。 [打开练习与自查](../weeks/week-05-triton-softmax/session-01.md)。

**阅读代码快照**：[01-vector-add.py](https://github.com/triton-lang/triton/blob/aad2a60d958f945420c5c40936b37d411fb02e89/python/tutorials/01-vector-add.py)，与本卡相同函数范围；固定阅读版本，不代表安装版本。语义文档仍为 main 页面。

<a id="r-softmax"></a>

### R-SOFTMAX · 稳定 Softmax 与融合

**中文补充（按需，部分）：** 中文 kernel 与动机；运行、测试/benchmark 仍用固定上游版本。 [对应范围](#cn-triton)。

W5-S02 必读；中等；英文；M2、归约、Triton。

**来源**：[Fused Softmax](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html)。

**读到哪里**：Motivations → Compute Kernel → Unit Test → Benchmark，60 分钟；逐项对照 naive_softmax 与 softmax_kernel，启动优化先沿用并记录版本。

**带着什么问题读**：做大幅值、非二次幂列宽与误差检查；正确填充值和逐元素参考不可只靠行和替代。 [打开练习与自查](../weeks/week-05-triton-softmax/session-02.md)。

**阅读代码快照**：[02-fused-softmax.py](https://github.com/triton-lang/triton/blob/aad2a60d958f945420c5c40936b37d411fb02e89/python/tutorials/02-fused-softmax.py)，按本卡四节阅读；固定阅读提交不等于本机安装版本。

<a id="r-online"></a>

### R-ONLINE · 分块 Softmax 的状态合并

**中文补充（按需，部分）：** 中文分块 max/sum 公式，先不读 Attention 扩展。 [对应范围](models.md#cn-flash)。

W5-S03 必读；进阶起步；英文论文；稳定 Softmax。

**来源**：[Online normalizer v2](https://arxiv.org/pdf/1805.02867v2)。

**读到哪里**：§2 Algorithm 2 → §3 Algorithm 3 → §3.1 并行合并，45 分钟；停在合并，不读 Top-k 融合。

**带着什么问题读**：先手算两块最大值/指数和，再 CPU 核对；不新增分块 GPU Softmax 项目。 [打开练习与自查](../weeks/week-05-triton-softmax/session-03.md)。

<a id="r-gpu-hardware"></a>

### R-GPU-HARDWARE · 逻辑线程怎样占用硬件

**中文补充（按需，部分）：** CPU/GPU 与互连关系；SM/warp/occupancy 精确约束仍查原文。 [对应范围](#cn-hardware)。

W2 第一段必学；先会 W1 数据字节；中文主讲在 [硬件关系与容量例子](../weeks/week-02-cuda-execution/session-01.md)。

**来源与范围**：[Writing SIMT Kernels §2.3.7](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html#kernel-launch-and-occupancy) 从分配 block 到 SM 资源列表，停在特定设备表之前；[Best Practices §11.1](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#occupancy) 的定义及 Calculating Occupancy 开头寄存器说明，停在 compute capability 7.0 数字例子之前。约 20 分钟，已包含在本单元，不通读调优参数。

**检查**：手算 block/warp/shared 限制，再解释寄存器、shared、L1/L2、global 的关系。文档正文已预读；真实设备占用率和性能必须实际测量，不能用虚构 SM 数字替代。

## 中文补充：理解索引、搬运与算子

<a id="cn-cuda"></a>

### CN-CUDA：从第一个 kernel 接到数组下标

**中文视频：** coderonion / codingonion《CUDA 12.x 并行编程入门（C++版）》[第 3 集：运行第一个 CUDA 程序](https://www.bilibili.com/video/BV1oc411x7Gt/)与[第 4 集：你好，CUDA](https://www.bilibili.com/video/BV1jueweLEQ1/)。[作者配套仓库](https://github.com/coderonion/cuda-beginner-course-cpp-version)目前列出 4 集；只把 3/4 集用作 W2 入门的可选连续讲解，不当作完整 CUDA 性能课程。

**中文正文首选：** NVIDIA / Mark Harris [CUDA 入门教程：更简单的介绍（更新版）](https://developer.nvidia.cn/blog/even-easier-introduction-cuda-2/)，读“从简单开始”的 CPU 程序、“CUDA 中的显存分配”里的完整三参数 `add` 程序，以及“获取线程”“突破限制”的下标代码；跳过“分析它！”和性能表，停在“统一内存预取”前。它是 NVIDIA 发布的中文版本（页面更新日 2025-05-02），帮助理解 CPU 调用与 GPU kernel 的区别；使用 `cudaMallocManaged`，不替代 W2 的显式分配、H2D/D2H 练习。

译文局部片段混入了四参数 `sum` 版本，不能拼接成完整程序；只追上述完整三参数例子。线程块数量按代码向上取整，不是译文所说的四舍五入；`tg_` 残留标记按代码中的 `blockIdx.x` 等名称核对。32 的倍数是常用选择，不是合法 block 大小的必要条件。

**换一种索引解释：** 谭升 2018 [组织并行线程](https://face2ai.com/CUDA-F-2-3-组织并行线程/)只读“使用块和线程建立矩阵索引”的 ix/iy 与行优先索引例子。需要会 C++ 数组；性能表、旧工具和后续完整加法代码先跳过。

**核验：** 上述指定正文已预读，作者仓库列出的讲次/链接已确认；B 站直接读取受限，视频字幕、画面、分钟轴未检查。旧文 nvprof 不作为当前命令，工具仍按 R-SANITIZER/R-NCU。

<a id="cn-timing"></a>

### CN-Timing：为什么 CPU 必须等 GPU

**中文正文：** 谭升 2018 [给核函数计时](https://face2ai.com/CUDA-F-2-2-核函数计时/)，“用 CPU 计时”中启动 kernel → `cudaDeviceSynchronize` → 结束计时，以及紧接的五个时间事件。读到对“2～4”与“1～5”的解释即停，不读后面的硬件性能断言和 nvprof 操作。

这是作者中文博客，适合 W2 第三段与 W3 计时回查。指定段落已预读。同步后的主机区间仍包含启动与等待成本；本课 CUDA Events、预热、重复与计时范围照旧。不要把文章里的特定形状性能推成通用规律。

<a id="cn-reduce"></a>

### CN-Reduce：先看树形合并，代码仍按同步要求写

**中文正文：** 谭升 2018 [避免分支分化](https://face2ai.com/CUDA-F-3-4-避免分支分化/)，只看“并行规约问题”中的相邻配对、交错配对说明，停在“首先是 CPU 版本”代码前。先会 W2 索引，再把每轮配对写到本课输入上；外部配图未逐像素核验，推演用本课图。

指定文字已预读；这是理解归约树的中文补充，不是任意长度实现。后文旧 kernel 的提前 return、隐式 warp 同步和固定长度条件不能照搬；本课所有线程经过 barrier、尾部置零及 `_sync` 参与 mask 的要求不变。Racecheck/Synccheck 与现代 warp 语义暂缺合适的中文逐段补充。

<a id="cn-triton"></a>

### CN-Triton：对照中文注释读同一个 kernel

**来源：** HyperAI 超神经维护的 Triton 中文教程，属于社区译文，不是另一套 Triton 实验，也不等同于 NVIDIA Triton Inference Server。

| 使用位置 | 指定中文范围 | 具体帮助 |
| --- | --- | --- |
| W5 第一段 | [向量相加](https://triton.hyper.ai/docs/getting-started/tutorials/vector-addition/)“计算内核”的 add_kernel 与 add，到基准测试前 | 对照 program_id、offset、mask 与 grid |
| W5 第二段 | [融合 Softmax](https://triton.hyper.ai/docs/getting-started/tutorials/fused-softmax/)“动机”和 softmax_kernel 函数，到辅助启动函数前 | 把减最大值、归一化与减少中间读写接起来 |
| W4 第一/二段 | [矩阵乘法](https://triton.hyper.ai/docs/getting-started/tutorials/matrix-multiplication/)“动机”的分块伪代码与“计算内核”中的“指针算术”，到 L2 缓存优化前 | 只用来理解 C tile、K 循环和 stride；此时不要求会 Triton 或运行新算子 |

**准备状态：** 指定范围已预读；页面没有固定到本仓库使用的上游 commit，运行仍用原课固定版本。Softmax 译文把元素数写成“字节”，换算须乘元素宽度；`num_warps` 是线程束数量，不是线程块数量。这里不采用其旧 JIT 性能比较或私有启动接口。中文视频及 Triton 类型提升的对应讲解仍待补齐。

<a id="cn-hardware"></a>

### CN-Hardware：把 GPU 放回整台机器里看

**中文视频：** 李沐，2021 [硬件：CPU 和 GPU](https://www.bilibili.com/video/BV1TU4y1j7Wd/)。

**中文正文：** 作者团队《动手学深度学习》[§12.4 硬件](https://zh.d2l.ai/chapter_computational-performance/hardware.html)，只读 §12.4.1 的组件关系、§12.4.6 的 PCIe/网络/NVLink 用途。用于 S1/W2 连接计算与搬运，W7 回看互连路径。指定正文已预读；视频讲次由作者课表确认，字幕/画面未检查。

旧文的设备数量、带宽和架构举例不当作当前机器规格，也不作为 W4 Roofline 上限。SM/warp/寄存器、合并访问、Nsight 指标和 Roofline 的精确规则仍以原英文资料为准；中文性能课程尚未补全。
