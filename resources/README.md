# 按知识点查找资源

[全部单元](../docs/study-guide.md) · [基础补学](../docs/prerequisites.md) · [覆盖检查](../docs/coverage-review.md) · [进展索引](frontier-watchlist.md)

核验日期：2026-10-01。先从当前单元进入，只读指定范围。本页维护原始 URL、难度、语言、前置、阅读定位、停止位置和用途；单元保存解释、图例、练习与答案，不再复制一份资源总清单。

**必读**用于本段目标；**遇到困难时查阅**仅补已暴露的卡点；**可选拓展**在基础完成后另排。难度是相对于先修完成后的学习者，不是对零基础的承诺。卡内时间是原文选读，单元的本地图例/自查与实践另见[预算表](../docs/study-guide.md#time-budget)，不要重复相加。先修卡另外列补学总时间。

官方文档解释接口，作者教材/博客帮助形成直觉，论文在小例子和必要基础之后引入。视频不是硬性入口：未核验播放区段就不编造时间戳，使用可定位的讲义/正文完成相同目标。英文卡均有本地中文练习与核对依据。

## 核验边界

新增基础、服务、训练、调度及文章采用来源已实际打开。前八个位置的原有材料同时沿用本会话同日的页面/PDF/代码复核，固定提交和页序见各段与日期记录。可变的 latest/main 页面不是本机安装版本；开始运行前重新记录实际版本。页面读取不等于运行通过，本次没有学习实验。

无法读取的 D2L 中文线性代数、HF 中文 BPE 以及 Ray walkthrough/actors 入口不承担必读解释，替代来源写在卡中。Ray Resources 直接抓取曾失败，随后从官方 Tasks 链接成功读到正文。仅核对目录或摘要的可选项明确标注，不宣称全篇可用。

## 基础补学资源

<a id="p-py"></a>

### P-PY · Python 脚本与日志

基础补学；入门；中文；只需会使用键盘与文件夹。

**来源**：[速览](https://docs.python.org/zh-cn/3/tutorial/introduction.html) → [控制流](https://docs.python.org/zh-cn/3/tutorial/controlflow.html) → [数据结构](https://docs.python.org/zh-cn/3/tutorial/datastructures.html) → [模块](https://docs.python.org/zh-cn/3/tutorial/modules.html) → [输入输出](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html) → [异常](https://docs.python.org/zh-cn/3/tutorial/errors.html)；W15 前读 [类](https://docs.python.org/zh-cn/3/tutorial/classes.html)。

**顺序、范围与停止位置**：依次读 §3.1～3.2；§4 的 if、for、range、定义函数；§5 的列表与字典；§6 开头 import；§7.2 文件和 JSON；§8.1～8.3；类只读 §9.3。跳过 match、泛型、继承、包发布。原文约 3～4 小时，其余时间写小程序；总补学 6～10 小时。

**为什么读、读后做什么**：为全部 Python 实验补上输入、函数、记录能力；完成先修 P 的两组统计与空输入检查。 [打开练习与自查](../docs/prerequisites.md)。

<a id="p-shell"></a>

### P-SHELL · Shell 导航与重定向

基础补学；入门；英文；无需 Linux 经验。

**来源**：[Missing Semester 2026 Shell](https://missing.csail.mit.edu/2026/course-shell/)。

**顺序、范围与停止位置**：读 What is the shell?、Navigating in the shell、What is available in the shell?；The shell language (bash) 只读开头管道/重定向，再看练习 5 的三种流。按 pwd、cd、ls、>、2> 找示例。停在能导航和分离输出处，视频非必看；45～60 分钟原文。

**为什么读、读后做什么**：为编译和日志定位建立入口；完成先修 A 的失败脚本与修复记录。 [打开练习与自查](../docs/prerequisites.md)。

<a id="p-env"></a>

### P-ENV · 独立环境与 Git 改动

基础补学；入门；中/英文；先完成 P-SHELL。

**来源**：[Python 虚拟环境](https://docs.python.org/zh-cn/3/tutorial/venv.html)；[MIT Git](https://missing.csail.mit.edu/2026/version-control/)。

**顺序、范围与停止位置**：依次读 §12.2 创建环境、§12.3 包管理；Git 读 Git’s data model 开头和 Git command-line interface → Basics 的 status、diff、log。60～90 分钟，停止于查看改动，不要求远程协作或改写历史。

**为什么读、读后做什么**：把解释器、依赖和文件版本分开；先修 A 用 sys.executable 与日志核对；本轮不安装环境。 [打开练习与自查](../docs/prerequisites.md)。

<a id="p-cpp"></a>

### P-CPP · C++ 从最小程序到数组

基础补学；入门；英文；会 P 的循环与函数更容易。

**来源**：[程序结构](https://cplusplus.com/doc/tutorial/program_structure/) → [变量](https://cplusplus.com/doc/tutorial/variables/) → [控制流](https://cplusplus.com/doc/tutorial/control/) → [函数](https://cplusplus.com/doc/tutorial/functions/) → [LearnCpp 指针](https://www.learncpp.com/cpp-tutorial/introduction-to-pointers/) → [std::array](https://www.learncpp.com/cpp-tutorial/introduction-to-stdarray/)。

**顺序、范围与停止位置**：前四页只读 main/输出、基础类型/初始化、if/for、参数/返回值；函数读到按引用传参，跳过递归。指针读 address-of、dereference 与 dangling；array 读定义、索引、size。原文 2～3 小时，总练习 6～10 小时；不学模板元编程。

**为什么读、读后做什么**：作者入门教程先于 CS106L 幻灯片；先修 B 编译求和、改边界并解释局部对象生命周期。 [打开练习与自查](../docs/prerequisites.md)。

<a id="p-tensor"></a>

### P-TENSOR · PyTorch Tensor 入门

基础补学；入门；英文；P 与 M1。

**来源**：[Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)。

**顺序、范围与停止位置**：依次读 Initializing a Tensor、Attributes、Operations：索引、拼接、矩阵/逐元素运算；到 Single-element tensors 为止。先 CPU，NumPy bridge 按需；原文 45～60 分钟，总练习 2～3 小时。

**为什么读、读后做什么**：不把 shape/张量语法默认为已会；先修 B 的 2×3 矩阵检查，之后 W1 专学布局。 [打开练习与自查](../docs/prerequisites.md)。

<a id="p-math"></a>

### P-MATH · 矩阵、点积与形状

基础补学 M1；入门；英文；中学代数。

**来源**：[D2L Linear Algebra](https://d2l.ai/chapter_preliminaries/linear-algebra.html)；[中文对应页](https://zh.d2l.ai/chapter_preliminaries/linear-algebra.html)。

**顺序、范围与停止位置**：依次读 Scalars、Vectors、Matrices、Reduction、Dot Products、Matrix–Vector Products、Matrix–Matrix Multiplication；停止于乘法，不读特征分解。原文约 90 分钟，总练习 3～5 小时。中文页本轮抓取失败，英文作者版已读，配本地中文算例。

**为什么读、读后做什么**：支撑 W1/W4/W6 的 shape 和 FLOPs；完成 M1 的乘法与单位核对。 [打开练习与自查](../docs/prerequisites.md)。

<a id="p-softmax"></a>

### P-SOFTMAX · 从指数到概率权重

基础补学 M2；入门；中文；M1 与指数运算。

**来源**：[D2L Softmax 回归](https://zh.d2l.ai/chapter_linear-networks/softmax-regression.html)。

**顺序、范围与停止位置**：只读 §3.4.2 网络架构、§3.4.3 softmax 运算；对照分子指数、分母求和。30～45 分钟；本轮不读损失推导和分类训练，总练习 1～2 小时。

**为什么读、读后做什么**：为 W5 减最大值与归约建立直觉；完成 [0,ln(3)] 的平移不变例子。 [打开练习与自查](../docs/prerequisites.md)。

<a id="p-calculus"></a>

### P-CALCULUS · 导数与链式法则

基础补学 M3；入门；中文；函数与代数。

**来源**：[D2L 微积分](https://zh.d2l.ai/chapter_preliminaries/calculus.html)。

**顺序、范围与停止位置**：读 §2.4.1 导数、§2.4.3 偏导、§2.4.4 梯度、§2.4.5 链式法则；先跳过绘图代码和极限证明。原文 60～90 分钟，总练习 3～5 小时。

**为什么读、读后做什么**：为 backward 与 loss 缩放提供手算参考；完成 M3 的标量梯度和 SGD 一步。 [打开练习与自查](../docs/prerequisites.md)。

<a id="p-stats"></a>

### P-STATS · 均值、波动与统计口径

基础补学 M4；入门；英文；列表与四则运算。

**来源**：[D2L Probability and Statistics](https://d2l.ai/chapter_preliminaries/probability.html)。

**顺序、范围与停止位置**：只读 §2.6.3 Random Variables 和 §2.6.6 Expectations 的均值/方差；在向量协方差之前停止；30～45 分钟，停止于基础统计，不进入条件概率推导。分位数的具体算法采用本地 M4 定义；总练习 1～2 小时。

**为什么读、读后做什么**：支撑 W8/W10/W16 的汇总方法；计算五个样本的均值、中位数与指定算法 p95，解释样本不足。 [打开练习与自查](../docs/prerequisites.md)。

<a id="p-model"></a>

### P-MODEL · Attention 与 Block 结构

基础补学 C；入门到中等；中文；M1、M2、P-TENSOR。

**来源**：[注意力评分](https://zh.d2l.ai/chapter_attention-mechanisms/attention-scoring-functions.html) → [多头注意力](https://zh.d2l.ai/chapter_attention-mechanisms/multihead-attention.html) → [Transformer](https://zh.d2l.ai/chapter_attention-mechanisms/transformer.html)。

**顺序、范围与停止位置**：读缩放点积注意力与 masked softmax；多头图和模型公式；Transformer 位置前馈网络、残差连接和层规范化。约 2 小时原文，停止于组件及 shape，不执行完整翻译训练；总补学 4～6 小时。

**为什么读、读后做什么**：作者中文教材先于 FlashAttention 论文；完成 C 的 18 元素 score 与 causal mask，随后用 W6 的 pre-norm 结构。 [打开练习与自查](../docs/prerequisites.md)。

<a id="p-train"></a>

### P-TRAIN · 梯度、优化器和单卡恢复

基础补学 D；中等；英文；M3、P-TENSOR、Python 类。

**来源**：[Autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) → [Optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) → [Saving and Loading Models](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html)。

**顺序、范围与停止位置**：依次读 Computing Gradients、Disabling Gradient Tracking；Loss Function、Optimizer、Full Implementation 的训练循环；Saving & Loading a General Checkpoint for Inference and/or Resuming Training。原文约 2 小时，停止于单卡 general checkpoint；总补学 5～8 小时。

**为什么读、读后做什么**：先能独立训练和恢复再学 DDP；完成 D 的一步更新与连续/恢复第 3 步对照。 [打开练习与自查](../docs/prerequisites.md)。

## 单元主线资源

<a id="r-cpp"></a>

### R-CPP · 类型、地址与生命周期

W1-S01 必读；入门巩固；英文；先修 B。

**来源**：[CS106L 类型 PDF](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-02-TypesAndStructs.pdf)；[指针 PDF](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-06-Iterators.pdf)。

**顺序、范围与停止位置**：阅读器页序 35～48、70～85；停在 Array pointer。约 35 分钟，与 R-L2 共用 W1-S01 的 50 分钟。首次不懂引用时回 P-CPP，不在未核验的第 3 讲 PDF 猜页码。

**为什么读、读后做什么**：把 C++ 地址与 Tensor 元素字节联系起来；数组求和、六元素字节与生命周期自查。 [打开练习与自查](../weeks/week-01-foundations/session-01.md)。

**遇到困难时查阅**：英文规范 [指针加减](https://eel.is/c++draft/expr.add) §4～5、[std::array 概述](https://eel.is/c++draft/array.overview) §1。仅当地址差或连续性有疑问时用 5～10 分钟核对，读到同一数组的元素差与 contiguous container 即停；难度较高，不替代入门示例。W1 的六元素地址图是自查依据。

<a id="r-l2"></a>

### R-L2 · Tensor 存储、FLOPs 与 Roofline 讲义

W1/W4 必读指定函数；中等；英文；B、M1。

**来源**：[CS336 lecture_02.py 固定提交](https://github.com/stanford-cs336/lectures/blob/6ff836dd5dfcbe7e848fe1a1734f1886f1116a7a/lecture_02.py)；[配套视频](https://www.youtube.com/watch?v=kuYAsz7zspQ)。

**顺序、范围与停止位置**：W1-S01：tensors_basics、tensors_memory 的 FP32/FP16，到 bf16 前停，15 分钟；S03：tensor_operations_flops 的 matmul，50 分钟含推导。W4-S03：arithmetic_intensity_matmul、roofline_plots，15 分钟。视频替换同主题讲义阅读，不叠加；未核验时间戳。

**为什么读、读后做什么**：同一讲按不同知识点分三次读；W1 核对 Linear 账本，W4 预测算术强度，不重复整讲。 [打开练习与自查](../weeks/week-01-foundations/study-guide.md)。

<a id="r-views"></a>

### R-VIEWS · Tensor 的视图、转置与复制

W1-S02 必读；中等；英文；P-TENSOR。

**来源**：[Tensor Views 2.14](https://docs.pytorch.org/docs/2.14/tensor_view.html)。

**顺序、范围与停止位置**：共享存储的 base/view 例子 → 转置非连续例子 → reshape/flatten/contiguous 说明；50 分钟，停止于复制语义。文档版本不代表本地版本。

**为什么读、读后做什么**：解释同 shape 不同布局；修改视图、连续副本和失败 view 的检查见本段。 [打开练习与自查](../weeks/week-01-foundations/session-02.md)。

**接口速查**：[numel](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.numel.html)、[element_size](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.element_size.html)、[data_ptr](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.data_ptr.html)。本次已打开正文；英文、入门，W1 遇到单位问题时各看首句返回值定义，共 5 分钟替换复习。用六元素数据区字节与地址例子自查，不扩展到 storage 完整 API。

<a id="r-cuda"></a>

### R-CUDA · CUDA 线程与 host/device 数据路径

W2-S01/S02、W3 同步必读；中等；英文；A、B、W1。

**来源**：[Programming Model](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html)；[Intro to CUDA C++](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/intro-to-cuda-cpp.html)；[Writing SIMT Kernels](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html)。

**顺序、范围与停止位置**：W2-S01：§1.2、§2.1.2、§2.3.2 的层级/索引，60 分钟；S02：§2.1.3.2、§2.1.4、§2.1.7 的分配/拷贝/同步/错误，30 分钟；W3-S01 只回查 §2.3.2.1 的 barrier。按标题复核节号，不读高级集群。

**为什么读、读后做什么**：先 CPU 模拟 N=10 的覆盖，再组装 Vector Add；W3 解释所有参与线程为何必须到达 barrier。 [打开练习与自查](../weeks/week-02-cuda-execution/study-guide.md)。

<a id="r-sanitizer"></a>

### R-SANITIZER · 内存与共享同步检查

W2/W3 必读；中等；英文；能编译 CUDA。

**来源**：[Compute Sanitizer](https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html)。

**顺序、范围与停止位置**：W2 读 Using Memcheck 与首个错误报告，15 分钟；W3 读 Using Racecheck、Using Synccheck，15 分钟。只查运行与错误位置，不通读工具选项。

**为什么读、读后做什么**：对小型边界输入检查；工具检查与正确性/性能分开，不能用未报错证明任意程序正确。 [打开练习与自查](../weeks/week-03-reduction-profiling/study-guide.md)。

<a id="r-best"></a>

### R-BEST · 计时、有效带宽与 GEMM 数据复用

W2/W4 必读；中等；英文；线程映射与矩阵乘法。

**来源**：[CUDA Best Practices](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html)。

**顺序、范围与停止位置**：W2-S03：§9.1.2、§9.2，45 分钟；W4-S01：§10.2.1 连续/错位访问，45 分钟；S02：§10.2.3.1～2 的 banks 和 C=AB，60 分钟。C=AAᵀ/padding 仅卡点查阅，替换 15 分钟。

**为什么读、读后做什么**：一个来源分别服务计量与复用；做 3N 字节账本、地址表、tile 边界与同步检查。 [打开练习与自查](../weeks/week-04-gemm/study-guide.md)。

<a id="r-reduce"></a>

### R-REDUCE · 共享内存归约代码

W3-S01 必读；中等；英文代码；W2。

**来源**：[GPU MODE shared_reduce.cu 固定提交](https://github.com/gpu-mode/lectures/blob/77a8df418834e5789c12da23e7d2719e0efabef1/lecture_009/shared_reduce.cu)；[NVIDIA 归约图解](https://developer.download.nvidia.com/assets/cuda/files/reduction.pdf)。

**顺序、范围与停止位置**：代码只读加载、循环、同步，约 30 分钟；图解只在卡住时读 Reduction #3，PDF 页序 14～15，替换 15 分钟。旧例固定单 block/2048 元素，不能当任意长度实现。

**为什么读、读后做什么**：画 8 元素树，再写每 block 部分和；CPU FP64 收尾一致，主表只比 GPU 第一阶段。 [打开练习与自查](../weeks/week-03-reduction-profiling/session-01.md)。

<a id="r-warp"></a>

### R-WARP · warp 交换、mask 与同步

W3-S02 必读；中等；英文；W3-S01。

**来源**：[NVIDIA Warp-Level Primitives](https://developer.nvidia.com/blog/using-cuda-warp-level-primitives/)。

**顺序、范围与停止位置**：Synchronized Data Exchange → Active Mask Query → Warp Synchronization，30 分钟；停在这三节。读 __shfl_down_sync 与参与 mask，不复用旧隐式同步技巧。

**为什么读、读后做什么**：把 warp 局部和与 block 合并分开；无效元素填零但仍参与，部分 warp 不列为主线。 [打开练习与自查](../weeks/week-03-reduction-profiling/session-02.md)。

<a id="r-l6"></a>

### R-L6 · 测量、Triton 与编译的讲义例子

W3/W5/W13 指定范围必读；中等；英文；对应前段。

**来源**：[CS336 lecture_06.py 固定提交](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py)。

**顺序、范围与停止位置**：W3：benchmarking/profiling，20 分钟；W5：triton_introduction，15 分钟；W13：naive_vs_builtin_vs_compiled_gelu，15 分钟，benchmarking 仅回查同步。各次到指定函数结束；不额外完成整讲算子。

**为什么读、读后做什么**：分别核对采样边界、program 抽象与 eager/compile 公平对照；练习使用各单元原实验。 [打开练习与自查](../docs/study-guide.md)。

**视频入口**：[CS336 Lecture 6](https://www.youtube.com/watch?v=xnDHaNUvHBg)。沿本卡讲义定位，不增加整讲观看，分钟位置未核验。

<a id="r-ncu"></a>

### R-NCU · kernel 内部的性能证据

W3-S03 必读，W4 查阅；中等；英文；W2 可靠计时。

**来源**：[Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html)。

**顺序、范围与停止位置**：W3：§2.2.1～2.2.3 的 sections/replay；只取 SpeedOfLight、MemoryWorkloadAnalysis、Occupancy，40 分钟。W4 遇到 Roofline 卡点查 §2.9，替换 15 分钟。

**为什么读、读后做什么**：由假设选择指标，正式计时不启用 profiler；占用率不作为单独成功标准。 [打开练习与自查](../weeks/week-03-reduction-profiling/session-03.md)。

<a id="r-roofline"></a>

### R-ROOFLINE · 用 Roofline 连接 FLOPs 与搬运

W4-S03 必读；中等；英文；W1 账本、W4 tile。

**来源**：[Scaling Book Rooflines](https://jax-ml.github.io/scaling-book/roofline/)。

**顺序、范围与停止位置**：Visualizing rooflines → Matrix multiplication；30 分钟，停止于矩阵乘法，硬件数字只作作者案例。

**为什么读、读后做什么**：用自己的输入算强度和上界，再与库及手写版本比较；不拿 TPU 数字当本机参数。 [打开练习与自查](../weeks/week-04-gemm/session-03.md)。

<a id="r-triton"></a>

### R-TRITON · Triton program、mask 与类型

W5-S01 必读；中等；英文；W2 索引、W4 访存。

**来源**：[Vector Addition](https://triton-lang.org/main/getting-started/tutorials/01-vector-add.html)；[Triton Semantics](https://triton-lang.org/main/python-api/triton-semantics.html)。

**顺序、范围与停止位置**：先读 Compute Kernel 的 add_kernel/add，20 分钟；再读 Semantics 的 Broadcasting 与 Type Promotion，10 分钟，替代泛看示例。Differences with NumPy 按需查阅，主线不实现负整数除法。

**为什么读、读后做什么**：文章的中文 Triton 语义链接对应此上游文档；用长度 10/块 4 的映射检查 mask，并预测 (3,1)+(1,4) 为 (3,4)。 [打开练习与自查](../weeks/week-05-triton-softmax/session-01.md)。

**阅读代码快照**：[01-vector-add.py](https://github.com/triton-lang/triton/blob/aad2a60d958f945420c5c40936b37d411fb02e89/python/tutorials/01-vector-add.py)，与本卡相同函数范围；固定阅读版本，不代表安装版本。语义文档仍为 main 页面。

<a id="r-softmax"></a>

### R-SOFTMAX · 稳定 Softmax 与融合

W5-S02 必读；中等；英文；M2、归约、Triton。

**来源**：[Fused Softmax](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html)。

**顺序、范围与停止位置**：Motivations → Compute Kernel → Unit Test → Benchmark，60 分钟；逐项对照 naive_softmax 与 softmax_kernel，启动优化先沿用并记录版本。

**为什么读、读后做什么**：做大幅值、非二次幂列宽与误差检查；正确填充值和逐元素参考不可只靠行和替代。 [打开练习与自查](../weeks/week-05-triton-softmax/session-02.md)。

**阅读代码快照**：[02-fused-softmax.py](https://github.com/triton-lang/triton/blob/aad2a60d958f945420c5c40936b37d411fb02e89/python/tutorials/02-fused-softmax.py)，按本卡四节阅读；固定阅读提交不等于本机安装版本。

<a id="r-online"></a>

### R-ONLINE · 分块 Softmax 的状态合并

W5-S03 必读；进阶起步；英文论文；稳定 Softmax。

**来源**：[Online normalizer v2](https://arxiv.org/pdf/1805.02867v2)。

**顺序、范围与停止位置**：§2 Algorithm 2 → §3 Algorithm 3 → §3.1 并行合并，45 分钟；停在合并，不读 Top-k 融合。

**为什么读、读后做什么**：先手算两块最大值/指数和，再 CPU 核对；不新增分块 GPU Softmax 项目。 [打开练习与自查](../weeks/week-05-triton-softmax/session-03.md)。

<a id="r-sdpa"></a>

### R-SDPA · Attention 语义和后端

W6-S01 必读；中等；英文；先修 C、W5。

**来源**：[SDPA 教程](https://docs.pytorch.org/tutorials/intermediate/scaled_dot_product_attention_tutorial.html)；[SDPA API 2.14](https://docs.pytorch.org/docs/2.14/generated/torch.nn.functional.scaled_dot_product_attention.html)。

**顺序、范围与停止位置**：教程开头接口与 Explicit Dispatcher Control；API 只核对 mask、is_causal、dropout_p，40 分钟；停在前向对照。

**为什么读、读后做什么**：显式 Attention 与 SDPA 统一语义；函数式 dropout 显式设 0，布尔 True 表示可参与；后端需证据。 [打开练习与自查](../weeks/week-06-attention/session-01.md)。

<a id="r-flash"></a>

### R-FLASH · Attention 的 IO 与在线分块

W6-S02 必读；进阶起步；英文论文；W4、W5、W6-S01。

**来源**：[FlashAttention 原论文 arXiv v2](https://arxiv.org/pdf/2205.14135v2)。

**顺序、范围与停止位置**：§2.1～2.2 → §3.1 Algorithm 1 → §3.2 IO 结论，50 分钟；停止于前向，证明和反向后置。这里 v2 是原论文修订版，不是 FlashAttention-2。

**为什么读、读后做什么**：图中找到不再完整写回的 score/probability 矩阵；复用小 pre-norm Block 建账本。 [打开练习与自查](../weeks/week-06-attention/session-02.md)。

<a id="r-trace"></a>

### R-TRACE · 模型区段与 CPU/GPU 时间线

W6-S03 必读；中等；英文；W3 测量。

**来源**：[PyTorch Profiler](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html)；[Nsight Systems CUDA Trace](https://docs.nvidia.com/nsight-systems/UserGuide/index.html#cuda-trace)。

**顺序、范围与停止位置**：Profiler 步骤 3/4 和 export_chrome_trace，30 分钟；CUDA Trace → Basic CUDA trace，30 分钟。区段标记按需查 Marking and Labeling Regions；不运行整份 ResNet 例子。

**为什么读、读后做什么**：把工具接到自己的 Block，标热点与空档；正式延迟另外计时。 [打开练习与自查](../weeks/week-06-attention/session-03.md)。

<a id="r-compile"></a>

### R-COMPILE · eager、编译和变化输入

W13 三段必读；中等；英文；W6 小 Block、计时。

**来源**：[Introduction to torch.compile](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html)。

**顺序、范围与停止位置**：S01 Basic Usage 30 分钟；S02 Demonstrating Speedups 与计时 60 分钟；S03 Graph Breaks，遇卡点查 Troubleshooting，45 分钟。停止于一处 graph break 与第二个 shape。

**为什么读、读后做什么**：把正确性、首次/稳态、graph break/重编译分开；不增加 GELU 或完整 CS336 作业。 [打开练习与自查](../weeks/week-13-systems/study-guide.md)。

<a id="r-collective"></a>

### R-COLLECTIVE · 各 rank 的输入输出

W7-S01 必读；中等；英文；Tensor、进程/设备区分。

**来源**：[NCCL Collective Operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html)；[torchrun 2.14](https://docs.pytorch.org/docs/2.14/elastic/run.html)。

**顺序、范围与停止位置**：四节 AllReduce、Broadcast、AllGather、ReduceScatter，30 分钟；运行前查 torchrun 的单机启动和 LOCAL_RANK，计入实现准备。停止于最小 2 rank 语义。

**为什么读、读后做什么**：文章直接列出 NCCL 原始页，继续沿用；手算后运行并核对各 rank 输出，不能只看进程启动。 [打开练习与自查](../weeks/week-07-collectives/session-01.md)。

<a id="r-l7"></a>

### R-L7 · 通信、TP 和 PP 讲义

W7/W14 指定函数必读；中等；英文；对应单元前置。

**来源**：[CS336 lecture_07.py 固定提交](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py)。

**顺序、范围与停止位置**：W7-S01：torch_distributed、collective_operations_main，15 分钟；S03：hardware、benchmarking、all_reduce，45 分钟。W14-S01：tensor_parallelism(_main)，20 分钟；S03：pipeline_parallelism(_main)，20 分钟。每次读到函数结束。

**为什么读、读后做什么**：让图与具体张量对应，W7 不提前读 DDP/TP，W14 不重复 collective 入门。 [打开练习与自查](../weeks/week-07-collectives/study-guide.md)。

<a id="r-nccl-tests"></a>

### R-NCCL-TESTS · 通信计时与两种带宽

W7-S02 必读；中等；英文；四类 collective。

**来源**：[nccl-tests README](https://github.com/NVIDIA/nccl-tests/blob/b4d5beebca8a76cf01335f724d154b9b9d394d96/README.md)；[PERFORMANCE.md](https://github.com/NVIDIA/nccl-tests/blob/b4d5beebca8a76cf01335f724d154b9b9d394d96/doc/PERFORMANCE.md)。

**顺序、范围与停止位置**：构建/运行说明 20 分钟；Time、Algorithm bandwidth、Bus bandwidth → AllReduce 40 分钟；不读其他 collective 换算。

**为什么读、读后做什么**：随机取日志一行换算 algbw 与 busbw；归一化指标不是 PCIe 链路直接采样。 [打开练习与自查](../weeks/week-07-collectives/session-02.md)。

<a id="r-inference"></a>

### R-INFERENCE · prefill、decode 与请求延迟

W8-S01 必读；中等；英文；W4 Roofline、W6 Attention。

**来源**：[CS336 lecture_10.py](https://github.com/stanford-cs336/lectures/blob/main/lecture_10.py)；[Scaling Book Inference](https://jax-ml.github.io/scaling-book/inference/)。

**顺序、范围与停止位置**：讲义 review_transformer、arithmetic_intensity_of_inference、throughput_and_latency，60 分钟。书的 The Basics of Transformer Inference、What do we actually want to optimize? 仅卡点替换 20 分钟；量化、投机、多加速器后置。

**为什么读、读后做什么**：复用算术强度解释两个阶段；从本地假设时间戳算 TTFT/TPOT，不能拿 GPU 延迟当请求延迟。 [打开练习与自查](../weeks/week-08-serving-baseline/study-guide.md)。

**视频入口**：[CS336 Lecture 10](https://www.youtube.com/watch?v=EfM546A79aM)。用对应讲义函数定位并替换原选读时间，分钟位置未核验。W9 共享机制图解卡住时，可查同讲义 paged_attention，替换 15 分钟复习，不重复 W8 推理开篇。

<a id="r-token"></a>

### R-TOKEN · token、模板与请求格式

W8-S01/S02 新增必读；入门；英文；Python 字典与字符串。

**来源**：[HF Tokenization algorithms](https://huggingface.co/docs/transformers/main/en/tokenizer_summary)；[vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)。

**顺序、范围与停止位置**：HF 页开头的 subword 例子及 BPE 最初合并示例，15 分钟；Quickstart 的请求 JSON 中 model/prompt 或 messages、max_tokens 字段，15 分钟，合计新增 30 分钟。不训练 tokenizer；其他算法后置。

**为什么读、读后做什么**：补齐“字符数不等于 token 数”；结合服务请求路径核对模板、返回状态与实际生成长度。 [打开练习与自查](../weeks/week-08-serving-baseline/study-guide.md)。

<a id="r-serving"></a>

### R-SERVING · 单卡在线服务

W8-S02 必读；中等；英文；R-TOKEN、Linux 环境。

**来源**：[vLLM Quickstart](https://docs.vllm.ai/en/latest/getting_started/quickstart/)。

**顺序、范围与停止位置**：Online Serving → Completions 或 Chat Completions 二选一，45 分钟；停止于一条可追溯请求，不把 Offline Batched Inference 算作在线基线。启动模型名是示例，实际选择与 revision 要自己记录。

**为什么读、读后做什么**：先 3～5 条固定请求检查输出再压测；本轮只完善文档，不启动服务。 [打开练习与自查](../weeks/week-08-serving-baseline/study-guide.md)。

<a id="r-bench"></a>

### R-BENCH · 负载、明细和统计字段

W8-S03/W10-S01 必读；中等；英文；已理解请求路径。

**来源**：[vllm bench serve](https://docs.vllm.ai/en/latest/cli/bench/serve/)。

**顺序、范围与停止位置**：W8 45 分钟：num-prompts、request-rate、max-concurrency、num-warmups、save-result、save-detailed、result-dir；长度只查所选 dataset 参数组。W10 45 分钟：burstiness、percentile-metrics、metric-percentiles、goodput；旧字段回查不重读。

**为什么读、读后做什么**：固定工作负载并保存失败；W10 做两个单因素扫描。CLI goodput 与本地定义先核对再比较。 [打开练习与自查](../weeks/week-10-serving-benchmark/study-guide.md)。

<a id="r-paged"></a>

### R-PAGED · KV 容量、分页和共享

W9-S01/S02 必读；进阶起步；英文论文；W8 与字节账本。

**来源**：[PagedAttention PDF](https://arxiv.org/pdf/2309.06180)；[作者博客图解](https://vllm.ai/blog/2023-06-20-vllm)。

**顺序、范围与停止位置**：S01：论文 §3、§4.1～4.2，60 分钟；S02：§4.3、§4.4 开头 parallel sampling/copy-on-write，45 分钟。博客块映射图只作卡点替换 15 分钟；停在基本共享，不读完整 beam search 或性能评估。

**为什么读、读后做什么**：先本地两请求块表，再追论文；APC 开关实验不能隔离分页分配器贡献。 [打开练习与自查](../weeks/week-09-kv-cache/study-guide.md)。

<a id="r-apc"></a>

### R-APC · 前缀复用的条件与限制

W9-S03 必读；中等；英文；KV 块表、W8 基线。

**来源**：[Automatic Prefix Caching](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/)。

**顺序、范围与停止位置**：Introduction、Enabling APC in vLLM、Example workloads、Limits，45 分钟；跳过 Hybrid Mamba 专项。当前接口在实际开始学习时按安装版本核对。

**为什么读、读后做什么**：构造 token 前缀一致/不同、冷/热、开/关对照；把重复 prefill 的直接作用与其他指标变化分开。 [打开练习与自查](../weeks/week-09-kv-cache/study-guide.md)。

<a id="r-batching"></a>

### R-BATCHING · continuous batching 与 chunked prefill

W10-S02 必读；中等；英文；W8/W9。

**来源**：[CS336 lecture_10.py](https://github.com/stanford-cs336/lectures/blob/main/lecture_10.py)；[vLLM Optimization](https://docs.vllm.ai/en/latest/configuration/optimization/)。

**顺序、范围与停止位置**：讲义 continuous_batching 15 分钟；文档 Chunked Prefill、Performance Tuning with Chunked Prefill 45 分钟。停在 max_num_batched_tokens 的含义，不加入量化/多卡配置。

**为什么读、读后做什么**：一张逐轮调度表区分请求集合变化与长 prefill 拆分；选一个预算变量对照默认值。 [打开练习与自查](../weeks/week-10-serving-benchmark/study-guide.md)。

<a id="r-metrics"></a>

### R-METRICS · 服务状态与有效吞吐

W10-S03 必读，W9 命中证据查阅；中等；英文；M4、R-BENCH。

**来源**：[Production Metrics](https://docs.vllm.ai/en/latest/usage/metrics/)。

**顺序、范围与停止位置**：General Metrics：num_requests_running、num_requests_waiting、prefix_cache_hits/queries 及延迟项，45 分钟。停止于本机实际存在的字段；不要求部署 Prometheus。缓存计数当前按 token，不直接当请求命中率。

**为什么读、读后做什么**：从成功且满足阈值的请求重算 goodput；累计计数用同窗口增量，未暴露字段记缺失。 [打开练习与自查](../weeks/week-10-serving-benchmark/study-guide.md)。

<a id="r-ddp-start"></a>

### R-DDP-START · rank、模型副本与样本归属

W11-S01 必读；中等；英文文档配视频；先修 D、W7。

**来源**：[Multi GPU training with DDP](https://docs.pytorch.org/tutorials/beginner/ddp_series_multigpu.html)。

**顺序、范围与停止位置**：Constructing the process group → Constructing the DDP model → Distributing input data，45 分钟。只读单机文本示例，视频替换同段阅读，时间轴未核验；多机后置。

**为什么读、读后做什么**：用样本 ID 核对 DistributedSampler 与 set_epoch，不把进程启动当作正确性。 [打开练习与自查](../weeks/week-11-ddp/study-guide.md)。

<a id="r-ddp"></a>

### R-DDP · 梯度同步和公平更新

W11-S02 必读；中等；英文；单卡参考已通过。

**来源**：[DDP 教程](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)。

**顺序、范围与停止位置**：Basic Use Case、Skewed Processing Speeds、Save and Load Checkpoints，60 分钟；停止于固定全局 batch 的 1/2 卡。no_sync 的累积实验只作拓展，先保持累积步数 1。

**为什么读、读后做什么**：小例子核对等大小本地 mean loss 的平均梯度，再测相同样本数的 step 与吞吐。 [打开练习与自查](../weeks/week-11-ddp/study-guide.md)。

<a id="r-amp"></a>

### R-AMP · 精度与输入路径的分离

W11-S03 必读概念；中等；英文；FP32 单卡/DDP。

**来源**：[AMP recipe](https://docs.pytorch.org/tutorials/recipes/recipes/amp_recipe.html)；[Performance Tuning Guide](https://docs.pytorch.org/tutorials/recipes/recipes/tuning_guide.html)。

**顺序、范围与停止位置**：AMP 的 Adding torch.autocast、Adding GradScaler、All together，30 分钟；Enable asynchronous data loading and augmentation，15 分钟。到 dtype 与输入等待概念停止；运行 AMP/DataLoader 对照为可选拓展。

**为什么读、读后做什么**：列状态 dtype 表；autocast 不等于所有状态减半，卡数/精度/输入路径分别比较。 [打开练习与自查](../weeks/week-11-ddp/study-guide.md)。

<a id="r-zero"></a>

### R-ZERO · 训练状态分片的对象

W12-S01 必读；进阶起步；英文论文；W11 状态表。

**来源**：[ZeRO v3](https://arxiv.org/pdf/1910.02054v3)。

**顺序、范围与停止位置**：§3.1～3.2 模型与其余状态 → §5.1～5.3 三阶段，45 分钟；停止于分片对象，不读 offload。

**为什么读、读后做什么**：用自己的 FP32/Adam 假设建立理论表，另外列激活、通信缓冲和重聚合峰值。 [打开练习与自查](../weeks/week-12-fsdp/study-guide.md)。

<a id="r-fsdp"></a>

### R-FSDP · FSDP2 参数聚合与分片

W12-S02 必读；进阶；英文；W11 与 R-ZERO。

**来源**：[FSDP2 教程](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)。

**顺序、范围与停止位置**：Model Initialization → Forward/Backward with Prefetching → Gradient Clipping and Optimizer with DTensor，75 分钟。先读默认路径，额外预取调参后置。optimizer 在 fully_shard 后创建；不混用 FSDP1 包装器。

**为什么读、读后做什么**：画参数 gather/reshard 与梯度通信；保持模型、精度、batch 相同，完整 optimizer step 后比峰值。 [打开练习与自查](../weeks/week-12-fsdp/study-guide.md)。

<a id="r-dcp"></a>

### R-DCP · 模型、优化器与应用状态恢复

W12-S03 必读；进阶；英文；先修 D 的单卡恢复、W12-S02。

**来源**：[FSDP2 State Dict with DCP APIs](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)；[DCP 教程](https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html)。

**顺序、范围与停止位置**：先看 FSDP2 同名小节，再读 DCP How DCP works、Saving、Loading 中 AppState/get_state_dict/set_state_dict；75 分钟。停在同 world size；RNG/步数/数据位置按本地状态表追加。

**为什么读、读后做什么**：当前 DCP 例子已用 fully_shard；重点核对两页版本。重启后比较下一步，不用“文件存在”代替恢复正确。 [打开练习与自查](../weeks/week-12-fsdp/study-guide.md)。

<a id="r-megatron"></a>

### R-MEGATRON · TP 的两层 MLP 代数

W14-S01 必读；进阶起步；英文论文；矩阵、collective、DDP/FSDP 概念。

**来源**：[Megatron-LM v4](https://arxiv.org/pdf/1909.08053v4)。

**顺序、范围与停止位置**：§3 Model Parallel Transformers 的 MLP/Attention 切分，30 分钟；先看本地无 bias 数字例子，停在切分，不读大模型性能结果。

**为什么读、读后做什么**：列切第一层、行切第二层；解释非线性不能随意穿过求和，CPU 合并先对齐。 [打开练习与自查](../weeks/week-14-parallelism/study-guide.md)。

<a id="r-parallel"></a>

### R-PARALLEL · TP 通信与 PP 流水线

W14-S02/S03 必读；中等；英文；R-MEGATRON、W7。

**来源**：[Megatron Bridge Parallelisms Guide](https://docs.nvidia.com/nemo/megatron-bridge/latest/parallelisms.html)。

**顺序、范围与停止位置**：S02 Tensor Parallelism 50 分钟含读图；S03 Pipeline Parallelism、Interleaved Pipeline Parallel Schedule 概念 30 分钟，配 R-L7 20 分钟。配置字段只帮助理解，停止于 2 stage 前向时间线。

**为什么读、读后做什么**：标通信 shape 与输出合并；不部署 Megatron，不把前向流水线当完整训练调度。 [打开练习与自查](../weeks/week-14-parallelism/study-guide.md)。

<a id="r-ray-task"></a>

### R-RAY-TASK · Task、Actor 与 ObjectRef

W15-S01 必读；入门到中等；英文；Python 函数/类、A。

**来源**：[Ray Tasks](https://docs.ray.io/en/latest/ray-core/tasks.html)；[ray.remote API](https://docs.ray.io/en/latest/ray-core/api/doc/ray.remote.html)。

**顺序、范围与停止位置**：Tasks 开头 Python 示例 → Passing object refs to Ray tasks → Waiting for Partial Results，30 分钟；remote 页开头函数与 Foo actor 示例，20 分钟。到示例结束，不读全部 API 参数。

**为什么读、读后做什么**：walkthrough/actors 页面本轮未成功抓取，使用可读的官方示例替代；结果检查和计数 Actor 在 W15 完成。 [打开练习与自查](../weeks/week-15-ray/study-guide.md)。

<a id="r-ray-resource"></a>

### R-RAY-RESOURCE · 逻辑资源与实际设备

W15-S02 必读；中等；英文；R-RAY-TASK。

**来源**：[Ray Resources](https://docs.ray.io/en/latest/ray-core/scheduling/resources.html)。

**顺序、范围与停止位置**：Physical Resources and Logical Resources → Specifying Node Resources → Specifying Task or Actor Resource Requirements，50 分钟。停止于 num_cpus/num_gpus 和自定义资源；分数 GPU 按需另读。

**为什么读、读后做什么**：从任务事件计算并发，区分准入令牌、可见设备与显存隔离；本页经官方 Tasks 链接已读。 [打开练习与自查](../weeks/week-15-ray/study-guide.md)。

<a id="r-ray-schedule"></a>

### R-RAY-SCHEDULE · 可行性、可用性与节点选择

W15-S03/W16-S03 必读指定范围；中等；英文；资源/日志。

**来源**：[Ray Scheduling](https://docs.ray.io/en/latest/ray-core/scheduling/index.html)。

**顺序、范围与停止位置**：W15：Resources 与 DEFAULT，50 分钟；W16 只复查 Resources 和策略开头约 10 分钟，另用本地自查时段的 40 分钟做字段映射与检查，不重复全文。SPREAD、节点亲和性后置。

**为什么读、读后做什么**：待提交队列的 FIFO/SJF 与 Ray 内部节点选择不同；日志分出提交层和执行层等待。 [打开练习与自查](../weeks/week-16-scheduling/study-guide.md)。

<a id="r-ostep"></a>

### R-OSTEP · 排队指标、FIFO 与 SJF

W16-S01/S02 必读；中等；英文作者教材；Python、M4、W15 日志。

**来源**：[OSTEP 第 7 章](https://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf)。

**顺序、范围与停止位置**：S01：§7.1～7.4，50 分钟；S02：§7.4 晚到达例子与 §7.5 STCF 的区别，原文 30 分钟；策略推演另计入本地自查。§7.6 只按需区分 response time；主线不实现抢占。

**为什么读、读后做什么**：用同一轨迹算等待/周转/makespan，再实现离散事件；SJF 只能选择已到达任务。 [打开练习与自查](../weeks/week-16-scheduling/study-guide.md)。

## 按需查阅与可选拓展

<a id="x-saved"></a>

### X-SAVED · 反向为什么保留中间 Tensor

W12 完成后可选；进阶；英文；autograd、状态账本。

**来源**：[Hooks for autograd saved tensors](https://docs.pytorch.org/tutorials/intermediate/autograd_saved_tensors_hooks_tutorial.html)。

**顺序、范围与停止位置**：从 Saved tensors 到 Hooks for autograd saved tensors 的 pack/unpack 例子，30 分钟；磁盘 offload 和内存优化实现后置。

**为什么读、读后做什么**：来自参考文章；用 x*x 的反向依赖画出必须保留的值，解释 hooks 与 checkpoint 重计算不相同；不加到 W12 必做项。 [打开练习与自查](../weeks/week-12-fsdp/study-guide.md)。

<a id="x-allocator"></a>

### X-ALLOCATOR · 流顺序分配与显存生命周期

W13 后可选；进阶；中文官方博客；W2 stream/event 与同步。

**来源**：[NVIDIA 流顺序分配器 Part 1](https://developer.nvidia.cn/blog/using-cuda-stream-ordered-memory-allocator-part-1/)；[Part 2](https://developer.nvidia.com/blog/using-cuda-stream-ordered-memory-allocator-part-2/)。

**顺序、范围与停止位置**：Part 1 的流排序效率、流有序分配语义与图 1，25 分钟；到内存池前停止。Part 2 仅有多 GPU/IPC 卡点时查对应节，另计 20 分钟，主线不要求。

**为什么读、读后做什么**：来自参考文章；画 allocate → use → free 与跨流事件依赖。用于理解生命周期，不要求重写分配器，也不套用历史速度数字。 [打开练习与自查](../weeks/week-13-systems/study-guide.md)。

<a id="x-activation"></a>

### X-ACTIVATION · 激活重计算与状态分片的区别

W12/W14 后可选；进阶；英文论文；反向与 TP。

**来源**：[Reducing Activation Recomputation](https://arxiv.org/pdf/2205.05198)。

**顺序、范围与停止位置**：先摘要与 Introduction，再用文内 Activation Memory 的标题定位图和变量，30 分钟，停止于重计算/保存对象；不复现大模型实验。

**为什么读、读后做什么**：文章的原始论文入口已打开；列一张参数/优化器分片与激活重计算的对象对照，勿把二者当同一技术。 [打开练习与自查](../weeks/week-12-fsdp/study-guide.md)。

<a id="x-navigation"></a>

### X-NAVIGATION · 课程视频与中文辅助导航

遇到困难时查阅；难度随章节；中/英文；先有具体问题。

**来源**：[CS336 课程表](https://cs336.stanford.edu/)；[官方视频列表](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV)；[GPU MODE](https://github.com/gpu-mode/lectures)；[Datawhale diy-llm](https://github.com/datawhalechina/diy-llm)；[AIInfraGuide](https://github.com/caomaolufei/AIInfraGuide)。

**顺序、范围与停止位置**：CS336 L2/L6/L7/L10 对应上面的函数；diy-llm README 只用第 3/4/7/8/10 章导航；AIInfraGuide 只用目录。每次 15 分钟查卡点，找到后回原始材料，不把未经逐章核验的目录列为必读。

**为什么读、读后做什么**：Datawhale 来自参考文章；中文二手讲解与官方来源分别标明。没有核验视频时间段，全文/整讲观看不计入主线。 [打开练习与自查](../docs/study-guide.md)。

**其他目录入口**：[AIInfraGuide 网站](https://caomaolufei.github.io/AIInfraGuide/) 仅作中文导航；[CS336 Assignment 2](https://github.com/stanford-cs336/assignment2-systems) 仅核验仓库入口，题面 PDF 未成功读取。两者不承担必读解释，也不宣称全目录资料已核验。完整作业不计入主线；后续选题须先检查题面与范围。

<a id="x-cuda"></a>

### X-CUDA · CUDA 映射与转置图解

遇到困难时查阅；中等；英文；W1/W2。

**来源**：[NVIDIA CUDA 入门](https://developer.nvidia.com/blog/even-easier-introduction-cuda/)；[矩阵转置](https://developer.nvidia.com/blog/efficient-matrix-transpose-cuda-cc/)；[GPU MODE CUDA 视频](https://www.youtube.com/watch?v=nOxKexn3iBo)；[lecture_003 代码](https://github.com/gpu-mode/lectures/blob/77a8df418834e5789c12da23e7d2719e0efabef1/lecture_003/pmpp.ipynb)。

**顺序、范围与停止位置**：W2 看 CPU 循环到 kernel 或 rgb_to_grayscale_kernel/grid，替换 20 分钟；W4 看共享 tile 多一列的 padding 例子，替换 15 分钟。视频无已核验时间戳，以代码为准。

**为什么读、读后做什么**：只解释映射/访存，不添加灰度图或转置项目；历史性能不作为目标。 [打开练习与自查](../weeks/week-02-cuda-execution/study-guide.md)。

<a id="x-fa2"></a>

### X-FA2 · FlashAttention-2 工作划分

W6/W13 后可选；进阶；英文作者博客；R-FLASH。

**来源**：[作者机构博客](https://crfm.stanford.edu/2023/07/17/flash2.html)；[论文摘要](https://arxiv.org/abs/2307.08691)。

**顺序、范围与停止位置**：博客的工作划分与非 matmul FLOPs 讨论，30 分钟；停止于设计图，不实现完整反向。论文本轮仅沿用摘要入口，不填写未核验页码。

**为什么读、读后做什么**：解释 IO 优化后为何还可能有其他开销；不作为 W6 完成前置。 [打开练习与自查](../weeks/week-06-attention/study-guide.md)。

<a id="article-discovery"></a>

## 参考文章的资源取舍

已通过浏览器读到 [AI infra学习汇总（持续更新中）](https://zhuanlan.zhihu.com/p/2075514689602187333)，作者“陌丶一叶知秋”，页面显示编辑于 2026-08-27。网页抓取超时后使用页面正文与链接提取；以下只记录与本项目有关的选择，不复制文章路线或推荐结论。

| 文章发现的原始入口 | 本次访问与判断 | 放置位置 |
| --- | --- | --- |
| PyTorch saved tensors hooks | 已读指定原始教程；前置是反向与保存状态 | [X-SAVED](#x-saved)，W12 后可选 |
| NVIDIA stream-ordered allocator 两篇 | 原始页面已读；涉及跨流生命周期，超出首个 kernel | [X-ALLOCATOR](#x-allocator)，W13 后可选 |
| [Triton 中文语义页](https://triton-lang.cn/main/python-api/triton-semantics.html) | 文章中的翻译入口；采用已读上游官方语义页核对接口 | [R-TRITON](#r-triton)，W5 增加 10 分钟定点阅读，替代泛看代码 |
| [HF 中文 BPE](https://huggingface.co/learn/llm-course/zh-CN/chapter6/6?fw=pt) | 原链接两次抓取失败；换已读 HF Tokenization algorithms | [R-TOKEN](#r-token)，W8 只学 token/子词与请求，不训练 tokenizer |
| NCCL Collective Operations | 已打开，和现有核心资料重复 | [R-COLLECTIVE](#r-collective)，W7 继续沿用，阅读不加倍 |
| 激活重计算论文 2205.05198 | PDF 已打开，限定为原理拓展 | [X-ACTIVATION](#x-activation)，W12/W14 后 |
| Datawhale diy-llm | README/目录已读，未逐章审查中文改编 | [X-NAVIGATION](#x-navigation)，按需导航 |
| [InfraTech](https://github.com/CalvinXKY/InfraTech)、[ai-infra-hpc](https://github.com/jinbooooom/ai-infra-hpc)、[ml-engineering](https://github.com/stas00/ml-engineering)、[BBuf CUDA 优化](https://github.com/BBuf/how-to-optim-algorithm-in-cuda) | 仅核对仓库入口/README，内容范围较广；未逐例验证 | 保留发现记录，不列必读；分别可在 PyTorch、W7 通信、工程分支、W4 算子完成后自行选题 |
| [Megatron Core MoE 论文](https://arxiv.org/abs/2603.07685)、[TorchTitan 论文](https://arxiv.org/abs/2410.06511) | 摘要页已读，不冒充全文阅读 | W14 后训练系统分支；W11/W12 仍采用小模型官方教程 |
| RL/微调、DualPipe、CP/EP、RDMA 与 MoE 性能合集 | 与当前基础目标不直接对应；未逐篇访问，不作质量排名 | 暂不纳入，先完成现有 16 个单元 |

## 维护约定

同一资源第一次读概念，后续只读新函数/新问题。W1/W4 分用 L2，W3/W5/W13 分用 L6，W7/W14 分用 L7，W8/W10 分用 L10。W12 复用 W11 模型与数据；W16 复用 W15 日志字段，避免重新搭建项目。

新增来源应有具体缺口、原始 URL、语言/前置、定位与停止位置、原文时间、读后自查和访问状态。必读增加时修改预算；可选资料不能暗中出现在完成标准里。前沿专题仍在现有 [进展索引](frontier-watchlist.md) 维护，仅在主线完成后选读，不重复登记全套链接。
