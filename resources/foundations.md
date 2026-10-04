# 基础与工具资料

[资料目录](README.md)

函数、文件和环境操作不熟时，先从这里找到对应解释。每张资料卡都给出阅读范围和本地练习；按当前课页选择，不需要从头读完全部链接。

<a id="p-py"></a>

### P-PY · 从零开始的 Python 主教材

从零入门；官方英文视频与 Notes，配各节中文解释。

**主来源**：[CS50P](https://cs50.harvard.edu/python/) 的 0～6、8 单元。逐段 notes 链接、起止范围、练习和核对在 [P1～P8](../course/foundations/README.md)，按本地学习顺序 0→1→2→3→4→6→5→8 学习；文件先用于保存真实输入输出，接着用测试核对小工具。7 正则与 9 Et Cetera 按需选读。

**查阅**：[Python 官方教程](https://docs.python.org/3/tutorial/) 假设已有一般编程基础，用于语法/标准库核对，作为语法查阅，不承担零基础讲解。CLI 与日志查 argparse/Logging HOWTO，具体范围在 P7。视频无已核验时间轴时，直接用完整指定讲义范围学习。

**先后与计时**：P1～P7 在 W1 前，P8 类与模块在 W6 前。预计范围按基础页记录，已包含本地练习，不能再与资源阅读重复相加。能独立完成工具、改变输入并修好一个错误后，再进入对应单元。

<a id="p-shell"></a>

### P-SHELL · Shell 导航与重定向

基础补学；入门；英文；无需 Linux 经验。

**来源**：[Missing Semester 2026 Shell](https://missing.csail.mit.edu/2026/course-shell/)。

**读到哪里**：读 What is the shell?、Navigating in the shell、What is available in the shell?；The shell language (bash) 只读开头管道/重定向，再看练习 5 的三种流。按 pwd、cd、ls、>、2> 找示例。停在能导航和分离输出处，视频非必看；45～60 分钟原文。

**带着什么问题读**：为编译和日志定位建立入口；完成先修 A 的失败脚本与修复记录。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-env"></a>

### P-ENV · 独立环境与 Git 改动

基础补学；入门；中/英文；先完成 P-SHELL。

**来源**：[Python 虚拟环境](https://docs.python.org/zh-cn/3/tutorial/venv.html)；[MIT Git](https://missing.csail.mit.edu/2026/version-control/)。

**读到哪里**：依次读 §12.2 创建环境、§12.3 包管理；Git 读 Git’s data model 开头和 Git command-line interface → Basics 的 status、diff、log。60～90 分钟，停止于查看改动，不要求远程协作或改写历史。

**带着什么问题读**：把解释器、依赖和文件版本分开；先修 A 用 sys.executable 与日志核对。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-cpp"></a>

### P-CPP · C++ 从最小程序到数组

基础补学；入门；英文；会 P 的循环与函数更容易。

**来源**：[程序结构](https://cplusplus.com/doc/tutorial/program_structure/) → [变量](https://cplusplus.com/doc/tutorial/variables/) → [控制流](https://cplusplus.com/doc/tutorial/control/) → [函数](https://cplusplus.com/doc/tutorial/functions/) → [LearnCpp 指针](https://www.learncpp.com/cpp-tutorial/introduction-to-pointers/) → [std::array](https://www.learncpp.com/cpp-tutorial/introduction-to-stdarray/)。

**读到哪里**：前四页只读 main/输出、基础类型/初始化、if/for、参数/返回值；函数读到按引用传参，跳过递归。指针读 address-of、dereference 与 dangling；array 读定义、索引、size。原文 2～3 小时，总练习 6～10 小时；不学模板元编程。

**带着什么问题读**：作者入门教程先于 CS106L 幻灯片；先修 B 编译求和、改边界并解释局部对象生命周期。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-tensor"></a>

### P-TENSOR · PyTorch Tensor 入门

基础补学；入门；英文；P 与 M1。

**来源**：[Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)。

**读到哪里**：依次读 Initializing a Tensor、Attributes、Operations：索引、拼接、矩阵/逐元素运算；到 Single-element tensors 为止。先 CPU，NumPy bridge 按需；原文 45～60 分钟，总练习 2～3 小时。

**带着什么问题读**：不把 shape/张量语法默认为已会；先修 B 的 2×3 矩阵检查，之后 W1 专学布局。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-math"></a>

### P-MATH · 矩阵、点积与形状

基础补学 M1；入门；英文；中学代数。

**来源**：[D2L Linear Algebra](https://d2l.ai/chapter_preliminaries/linear-algebra.html)；[中文对应页](https://zh.d2l.ai/chapter_preliminaries/linear-algebra.html)。

**读到哪里**：依次读 Scalars、Vectors、Matrices、Reduction、Dot Products、Matrix–Vector Products、Matrix–Matrix Multiplication；停止于乘法，不读特征分解。原文约 90 分钟，总练习 3～5 小时。中文页访问未成功；可用已预读的英文作者版，配本地中文算例。

**带着什么问题读**：支撑 W1/W4/W6 的 shape 和 FLOPs；完成 M1 的乘法与单位核对。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-softmax"></a>

### P-SOFTMAX · 从指数到概率权重

基础补学 M2；入门；中文；M1 与指数运算。

**来源**：[D2L Softmax 回归](https://zh.d2l.ai/chapter_linear-networks/softmax-regression.html)。

**读到哪里**：只读 §3.4.2 网络架构、§3.4.3 softmax 运算；对照分子指数、分母求和。30～45 分钟；这里不读损失推导和分类训练，总练习 1～2 小时。

**带着什么问题读**：为 W5 减最大值与归约建立直觉；完成 [0,ln(3)] 的平移不变例子。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-calculus"></a>

### P-CALCULUS · 导数与链式法则

基础补学 M3；入门；中文；函数与代数。

**来源**：[D2L 微积分](https://zh.d2l.ai/chapter_preliminaries/calculus.html)。

**读到哪里**：读 §2.4.1 导数、§2.4.3 偏导、§2.4.4 梯度、§2.4.5 链式法则；先跳过绘图代码和极限证明。原文 60～90 分钟，总练习 3～5 小时。

**带着什么问题读**：为 backward 与 loss 缩放提供手算参考；完成 M3 的标量梯度和 SGD 一步。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-stats"></a>

### P-STATS · 均值、波动与统计口径

基础补学 M4；入门；英文；列表与四则运算。

**来源**：[D2L Probability and Statistics](https://d2l.ai/chapter_preliminaries/probability.html)。

**读到哪里**：只读 §2.6.3 Random Variables 和 §2.6.6 Expectations 的均值/方差；在向量协方差之前停止；30～45 分钟，停止于基础统计，不进入条件概率推导。分位数的具体算法采用本地 M4 定义；总练习 1～2 小时。

**带着什么问题读**：支撑 W8/W10/W16 的汇总方法；计算五个样本的均值、中位数与指定算法 p95，解释样本不足。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-model"></a>

### P-MODEL · Attention 与 Block 结构

基础补学 C；入门到中等；中文；M1、M2、P-TENSOR。

**来源**：[注意力评分](https://zh.d2l.ai/chapter_attention-mechanisms/attention-scoring-functions.html) → [多头注意力](https://zh.d2l.ai/chapter_attention-mechanisms/multihead-attention.html) → [Transformer](https://zh.d2l.ai/chapter_attention-mechanisms/transformer.html)。

**读到哪里**：读缩放点积注意力与 masked softmax；多头图和模型公式；Transformer 位置前馈网络、残差连接和层规范化。约 2 小时原文，停止于组件及 shape，不执行完整翻译训练；总补学 4～6 小时。

**带着什么问题读**：作者中文教材先于 FlashAttention 论文；完成 C 的 18 元素 score 与 causal mask，随后用 W6 的 pre-norm 结构。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-train"></a>

### P-TRAIN · 梯度、验证、权重重载与训练恢复

P8、Tensor、M3 后学习；训练/验证/重载在 W6 前，Adam 下一步恢复在 W11 前。

**来源**：[Autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) → [Optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) → [Quickstart](https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html) → [Saving and Loading Models](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html)。

**读到哪里**：保留 Computing Gradients、Disabling Gradient Tracking；Loss Function、Optimizer、Full Implementation 的训练循环。Quickstart 只用 Optimizing the Model Parameters 核对 train/test，再读 Saving Models、Loading Models 的 state_dict 与预测；重复循环不再重读。W11 前读 General Checkpoint 的保存/加载及紧接的状态说明。原文合计约 2 小时，已含在训练课 5～8 小时与恢复段 2～4 小时之内。

**视频替代**：[Fundamentals of Autograd](https://docs.pytorch.org/tutorials/beginner/introyt/autogradyt_tutorial.html) 的 Simple Example、[Training with PyTorch](https://docs.pytorch.org/tutorials/beginner/introyt/trainingyt.html) 的 loss/optimizer/training/validation；画面与时间轴未核验，使用正文仍能完成。旧录制和当前文档的接口年份不混为一谈。

**带着什么问题读**：同一模型为什么分训练、验证和恢复？用五点直线核对手算，换系数后独立实现，再比较连续 3 步与重启 2+1。[打开训练课](../course/foundations/training.md)。官方示例的图像下载、分类指标与 torch.accelerator 不作为本地小练习前置。

<a id="r-numerics"></a>

### R-NUMERICS · 范围、舍入和误差判断

W1 第四段必学；Tensor 标量运算后；本地讲解约 2～4 小时含练习，原文阅读包含其中。

**来源与范围**：[Numerical accuracy 2.14](https://docs.pytorch.org/docs/2.14/notes/numerical_accuracy.html) 的引言、Batched computations、Extremal values，到 Linear algebra 前停，约 20 分钟；[torch.finfo](https://docs.pytorch.org/docs/2.14/type_info.html#torch-finfo) 只查 bits/eps/max/tiny 与非正规数注释；[torch.isclose](https://docs.pytorch.org/docs/2.14/generated/torch.isclose.html) 只查不等式、参数与非有限值语义，共约 10 分钟。

**带着什么问题读**：两字节为何有不同范围？加法顺序改变为何影响结果？[本地例子与误差报告练习](../weeks/week-01-foundations/session-04.md) 先查 shape 和有限性，再设容差；线性代数病态性和完整 IEEE 编码留作后续。指定正文已预读，运行环境与资料版本分别记在 [核验记录](../docs/audits/2026-10-04-knowledge.md)。

## 进入单元后使用的资料

<a id="r-cpp"></a>

### R-CPP · 类型、地址与生命周期

W1-S01 必读；入门巩固；英文；先修 B。

**来源**：[CS106L 类型 PDF](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-02-TypesAndStructs.pdf)；[指针 PDF](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-06-Iterators.pdf)。

**读到哪里**：阅读器页序 35～48、70～85；停在 Array pointer。约 35 分钟，与 R-L2 共用 W1-S01 的 50 分钟。首次不懂引用时回 P-CPP，不在未核验的第 3 讲 PDF 猜页码。

**带着什么问题读**：把 C++ 地址与 Tensor 元素字节联系起来；数组求和、六元素字节与生命周期自查。 [打开练习与自查](../weeks/week-01-foundations/session-01.md)。

**遇到困难时查阅**：英文规范 [指针加减](https://eel.is/c++draft/expr.add) §4～5、[std::array 概述](https://eel.is/c++draft/array.overview) §1。仅当地址差或连续性有疑问时用 5～10 分钟核对，读到同一数组的元素差与 contiguous container 即停；难度较高，不替代入门示例。W1 的六元素地址图是自查依据。

<a id="r-l2"></a>

### R-L2 · Tensor 存储、FLOPs 与 Roofline 讲义

W1/W4 必读指定函数；中等；英文；B、M1。

**来源**：[CS336 lecture_02.py 固定提交](https://github.com/stanford-cs336/lectures/blob/6ff836dd5dfcbe7e848fe1a1734f1886f1116a7a/lecture_02.py)；[配套视频](https://www.youtube.com/watch?v=kuYAsz7zspQ)。

**读到哪里**：W1-S01：tensors_basics、tensors_memory 的 FP32/FP16，到 bf16 前停，15 分钟；S03：tensor_operations_flops 的 matmul，50 分钟含推导。W4-S03：arithmetic_intensity_matmul、roofline_plots，15 分钟。视频替换同主题讲义阅读，不叠加；未核验时间戳。

**带着什么问题读**：同一讲按不同知识点分三次读；W1 核对 Linear 账本，W4 预测算术强度，不重复整讲。 [打开练习与自查](../weeks/week-01-foundations/README.md)。

<a id="r-views"></a>

### R-VIEWS · Tensor 的视图、转置与复制

W1-S02 必读；中等；英文；P-TENSOR。

**来源**：[Tensor Views 2.14](https://docs.pytorch.org/docs/2.14/tensor_view.html)。

**读到哪里**：共享存储的 base/view 例子 → 转置非连续例子 → reshape/flatten/contiguous 说明；50 分钟，停止于复制语义。文档版本不代表本地版本。

**带着什么问题读**：解释同 shape 不同布局；修改视图、连续副本和失败 view 的检查见本段。 [打开练习与自查](../weeks/week-01-foundations/session-02.md)。

**接口速查**：[numel](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.numel.html)、[element_size](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.element_size.html)、[data_ptr](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.data_ptr.html)。已预读返回值说明；英文、入门，W1 遇到单位问题时各看首句返回值定义，共 5 分钟替换复习。用六元素数据区字节与地址例子自查，不扩展到 storage 完整 API。

## 系统基础资源与中文导学

下面按系统问题回查主讲解。S1～S6 都要学习；明确标出的平台运行拓展可以后做。接口核对紧邻练习，前沿资料另在选读页。

| 主题 | 主要讲解与原文范围 | 先修、练习与核对 |
| --- | --- | --- |
| 进程、线程、路径、权限、环境、标准流 | 本地 S1 + MIT Shell / Command-line Environment 的 Job Control | P5～P7；[S1](../course/bridges/s01.md#s1) |
| 带宽、延迟、rank、拓扑；HTTP 生命周期、观测 | 本地 S2 + MDN Overview 的 Components/flow/Messages；与 W7/W8/W10 已读部分重合时只回查 | S1；[S2](../course/bridges/s02.md#s2) |
| Docker 镜像、容器、端口、重建与就绪 | Docker What is a container / Publishing ports，范围在 S3 | S1/S2；[S3 必做实操](../course/bridges/s03.md#s3) |
| Dataset/DataLoader、预处理、输入等待 | PyTorch Data tutorial 的 Custom Dataset 到 Iterate through DataLoader | P8、单卡 D；[S4](../course/bridges/s04.md#s4) |
| 文件、volume、对象存储、checkpoint | 本地 S5 + Docker Volumes 指定段、AWS S3 Objects/Keys/Versioning | P6、S3、D；[S5](../course/bridges/s05.md#s5) |
| DAG、资源、控制/执行、Kubernetes 配置/事件、重试公平性 | 本地 S6 + Kubernetes Objects/Pods/Resources/Debug Pods 指定段；Ray 和 OSTEP 的范围见对应资料卡 | P8、S3；[S6](../course/bridges/s06.md#s6) |

PyTorch 类的桥接主文是 [Build the Neural Network](https://docs.pytorch.org/tutorials/beginner/basics/buildmodel_tutorial.html) 的 Define the Class，接在 CS50P 8 的实例/继承后，先在 P8 解释 super/forward，再进入 P-MODEL/P-TRAIN。
