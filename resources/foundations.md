# 基础与工具资料

[资料目录](README.md)

函数、文件和环境操作不熟时，先从这里找到对应解释。每张资料卡都给出阅读范围和本地练习；按当前课页选择，不需要从头读完全部链接。

<a id="p-py"></a>

### P-PY · 从零开始的 Python 主教材

**中文补充（按需，部分）：** P1～P8 有逐段中文正文；中文原创视频分集仍缺。 [对应范围](#cn-python)。

从零入门；官方英文视频与 Notes，配各节中文解释。

**主来源**：[CS50P](https://cs50.harvard.edu/python/) 的 0～6、8 单元。逐段 notes 链接、起止范围、练习和核对在 [P1～P8](../course/foundations/README.md)，按本地学习顺序 0→1→2→3→4→6→5→8 学习；文件先用于保存真实输入输出，接着用测试核对小工具。7 正则与 9 Et Cetera 按需选读。

**查阅**：[Python 官方教程](https://docs.python.org/3/tutorial/) 假设已有一般编程基础，用于语法/标准库核对，作为语法查阅，不承担零基础讲解。CLI 与日志查 argparse/Logging HOWTO，具体范围在 P7。视频无已核验时间轴时，直接用完整指定讲义范围学习。

**先后与计时**：P1～P7 在 W1 前，P8 类与模块在 W6 前。预计范围按基础页记录，已包含本地练习，不能再与资源阅读重复相加。能独立完成工具、改变输入并修好一个错误后，再进入对应单元。

<a id="p-shell"></a>

### P-SHELL · Shell 导航与重定向

**中文补充（按需，部分）：** 2026 Shell 社区译文；视频字幕与画面未核验。 [对应范围](#cn-shell)。

基础补学；入门；英文；无需 Linux 经验。

**来源**：[Missing Semester 2026 Shell](https://missing.csail.mit.edu/2026/course-shell/)。

**读到哪里**：读 What is the shell?、Navigating in the shell、What is available in the shell?；The shell language (bash) 只读开头管道/重定向，再看练习 5 的三种流。按 pwd、cd、ls、>、2> 找示例。停在能导航和分离输出处，视频非必看；45～60 分钟原文。

**带着什么问题读**：为编译和日志定位建立入口；完成先修 A 的失败脚本与修复记录。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-env"></a>

### P-ENV · 独立环境与 Git 改动

**中文补充（按需，部分）：** venv 沿用原有官方中文；Git 补 2020 社区译文，与 2026 讲次区分。 [对应范围](#cn-shell)。

基础补学；入门；中/英文；先完成 P-SHELL。

**来源**：[Python 虚拟环境](https://docs.python.org/zh-cn/3/tutorial/venv.html)；[MIT Git](https://missing.csail.mit.edu/2026/version-control/)。

**读到哪里**：依次读 §12.2 创建环境、§12.3 包管理；Git 读 Git’s data model 开头和 Git command-line interface → Basics 的 status、diff、log。60～90 分钟，停止于查看改动，不要求远程协作或改写历史。

**带着什么问题读**：把解释器、依赖和文件版本分开；先修 A 用 sys.executable 与日志核对。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-cpp"></a>

### P-CPP · C++ 从最小程序到数组

**中文补充（按需，部分）：** 地址、固定数组与边界；完整类型、引用和生命周期仍读原文。 [对应范围](#cn-cpp)。

基础补学；入门；英文；会 P 的循环与函数更容易。

**来源**：[程序结构](https://cplusplus.com/doc/tutorial/program_structure/) → [变量](https://cplusplus.com/doc/tutorial/variables/) → [控制流](https://cplusplus.com/doc/tutorial/control/) → [函数](https://cplusplus.com/doc/tutorial/functions/) → [LearnCpp 指针](https://www.learncpp.com/cpp-tutorial/introduction-to-pointers/) → [std::array](https://www.learncpp.com/cpp-tutorial/introduction-to-stdarray/)。

**读到哪里**：前四页只读 main/输出、基础类型/初始化、if/for、参数/返回值；函数读到按引用传参，跳过递归。指针读 address-of、dereference 与 dangling；array 读定义、索引、size。原文 2～3 小时，总练习 6～10 小时；不学模板元编程。

**带着什么问题读**：作者入门教程先于 CS106L 幻灯片；先修 B 编译求和、改边界并解释局部对象生命周期。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-tensor"></a>

### P-TENSOR · PyTorch Tensor 入门

**中文补充（按需，部分）：** 李沐中文视频与数据操作；拼接等接口仍查原文。 [对应范围](#cn-tensor)。

基础补学；入门；英文；P 与 M1。

**来源**：[Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)。

**读到哪里**：依次读 Initializing a Tensor、Attributes、Operations：索引、拼接、矩阵/逐元素运算；到 Single-element tensors 为止。先 CPU，NumPy bridge 按需；原文 45～60 分钟，总练习 2～3 小时。

**带着什么问题读**：不把 shape/张量语法默认为已会；先修 B 的 2×3 矩阵检查，之后 W1 专学布局。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-math"></a>

### P-MATH · 矩阵、点积与形状

**中文补充（按需，沿用）：** 已有作者中文对应页；2026-10-05 已可访问，整段预读仍未重做，英文指定范围保持。 [对应范围](../docs/audits/2026-10-05-chinese-resources.md#source-coverage)。

基础补学 M1；入门；英文；中学代数。

**来源**：[D2L Linear Algebra](https://d2l.ai/chapter_preliminaries/linear-algebra.html)；[中文对应页](https://zh.d2l.ai/chapter_preliminaries/linear-algebra.html)。

**读到哪里**：依次读 Scalars、Vectors、Matrices、Reduction、Dot Products、Matrix–Vector Products、Matrix–Matrix Multiplication；停止于乘法，不读特征分解。原文约 90 分钟，总练习 3～5 小时。中文页在 2026-10-05 已可访问，整段中文预读尚未复核；可用已预读的英文作者版，配本地中文算例。

**带着什么问题读**：支撑 W1/W4/W6 的 shape 和 FLOPs；完成 M1 的乘法与单位核对。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-softmax"></a>

### P-SOFTMAX · 从指数到概率权重

**中文补充（按需，沿用）：** 已有作者中文 §3.4.2～3.4.3，保持原范围，不重复加来源。 [对应范围](../docs/audits/2026-10-05-chinese-resources.md#source-coverage)。

基础补学 M2；入门；中文；M1 与指数运算。

**来源**：[D2L Softmax 回归](https://zh.d2l.ai/chapter_linear-networks/softmax-regression.html)。

**读到哪里**：只读 §3.4.2 网络架构、§3.4.3 softmax 运算；对照分子指数、分母求和。30～45 分钟；这里不读损失推导和分类训练，总练习 1～2 小时。

**带着什么问题读**：为 W5 减最大值与归约建立直觉；完成 [0,ln(3)] 的平移不变例子。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-calculus"></a>

### P-CALCULUS · 导数与链式法则

**中文补充（按需，沿用）：** 已有作者中文指定小节，保持原范围；未新增视频要求。 [对应范围](../docs/audits/2026-10-05-chinese-resources.md#source-coverage)。

基础补学 M3；入门；中文；函数与代数。

**来源**：[D2L 微积分](https://zh.d2l.ai/chapter_preliminaries/calculus.html)。

**读到哪里**：读 §2.4.1 导数、§2.4.3 偏导、§2.4.4 梯度、§2.4.5 链式法则；先跳过绘图代码和极限证明。原文 60～90 分钟，总练习 3～5 小时。

**带着什么问题读**：为 backward 与 loss 缩放提供手算参考；完成 M3 的标量梯度和 SGD 一步。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-stats"></a>

### P-STATS · 均值、波动与统计口径

**中文补充（按需，暂缺）：** 已找到中文版，但与英文节号不同；尚未完成随机变量、期望/方差对应范围预读，暂不推荐新范围。 [对应范围](../docs/audits/2026-10-05-chinese-resources.md#source-coverage)。

基础补学 M4；入门；英文；列表与四则运算。

**来源**：[D2L Probability and Statistics](https://d2l.ai/chapter_preliminaries/probability.html)。

**读到哪里**：只读 §2.6.3 Random Variables 和 §2.6.6 Expectations 的均值/方差；在向量协方差之前停止；30～45 分钟，停止于基础统计，不进入条件概率推导。分位数的具体算法采用本地 M4 定义；总练习 1～2 小时。

**带着什么问题读**：支撑 W8/W10/W16 的汇总方法；计算五个样本的均值、中位数与指定算法 p95，解释样本不足。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-model"></a>

### P-MODEL · Attention 与 Block 结构

**中文补充（按需，部分）：** 原有作者中文正文保留；补注意力分数视频，字幕与画面待核验。 [对应范围](models.md#cn-attention)。

基础补学 C；入门到中等；中文；M1、M2、P-TENSOR。

**来源**：[注意力评分](https://zh.d2l.ai/chapter_attention-mechanisms/attention-scoring-functions.html) → [多头注意力](https://zh.d2l.ai/chapter_attention-mechanisms/multihead-attention.html) → [Transformer](https://zh.d2l.ai/chapter_attention-mechanisms/transformer.html)。

**读到哪里**：读缩放点积注意力与 masked softmax；多头图和模型公式；Transformer 位置前馈网络、残差连接和层规范化。约 2 小时原文，停止于组件及 shape，不执行完整翻译训练；总补学 4～6 小时。

**带着什么问题读**：作者中文教材先于 FlashAttention 论文；完成 C 的 18 元素 score 与 causal mask，随后用 W6 的 pre-norm 结构。 [打开练习与自查](../course/prerequisites.md)。

<a id="p-train"></a>

### P-TRAIN · 梯度、验证、权重重载与训练恢复

**中文补充（按需，部分）：** 自动求导、训练循环与权重读回；完整恢复继续读原文。 [对应范围](#cn-training)。

P8、Tensor、M3 后学习；训练/验证/重载在 W6 前，Adam 下一步恢复在 W11 前。

**来源**：[Autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html) → [Optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) → [Quickstart](https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html) → [Saving and Loading Models](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html)。

**读到哪里**：保留 Computing Gradients、Disabling Gradient Tracking；Loss Function、Optimizer、Full Implementation 的训练循环。Quickstart 只用 Optimizing the Model Parameters 核对 train/test，再读 Saving Models、Loading Models 的 state_dict 与预测；重复循环不再重读。W11 前读 General Checkpoint 的保存/加载及紧接的状态说明。原文合计约 2 小时，已含在训练课 5～8 小时与恢复段 2～4 小时之内。

**视频替代**：[Fundamentals of Autograd](https://docs.pytorch.org/tutorials/beginner/introyt/autogradyt_tutorial.html) 的 Simple Example、[Training with PyTorch](https://docs.pytorch.org/tutorials/beginner/introyt/trainingyt.html) 的 loss/optimizer/training/validation；画面与时间轴未核验，使用正文仍能完成。旧录制和当前文档的接口年份不混为一谈。

**带着什么问题读**：同一模型为什么分训练、验证和恢复？用五点直线核对手算，换系数后独立实现，再比较连续 3 步与重启 2+1。[打开训练课](../course/foundations/training.md)。官方示例的图像下载、分类指标与 torch.accelerator 不作为本地小练习前置。

<a id="r-numerics"></a>

### R-NUMERICS · 范围、舍入和误差判断

**中文补充（按需，暂缺）：** 浮点范围、舍入、累加顺序和容差的完整中文对应待补。 [对应范围](../docs/audits/2026-10-05-chinese-resources.md#source-coverage)。

W1 第四段必学；Tensor 标量运算后；本地讲解约 2～4 小时含练习，原文阅读包含其中。

**来源与范围**：[Numerical accuracy 2.14](https://docs.pytorch.org/docs/2.14/notes/numerical_accuracy.html) 的引言、Batched computations、Extremal values，到 Linear algebra 前停，约 20 分钟；[torch.finfo](https://docs.pytorch.org/docs/2.14/type_info.html#torch-finfo) 只查 bits/eps/max/tiny 与非正规数注释；[torch.isclose](https://docs.pytorch.org/docs/2.14/generated/torch.isclose.html) 只查不等式、参数与非有限值语义，共约 10 分钟。

**带着什么问题读**：两字节为何有不同范围？加法顺序改变为何影响结果？[本地例子与误差报告练习](../weeks/week-01-foundations/session-04.md) 先查 shape 和有限性，再设容差；线性代数病态性和完整 IEEE 编码留作后续。指定正文已预读，运行环境与资料版本分别记在 [核验记录](../docs/audits/2026-10-04-knowledge.md)。

## 进入单元后使用的资料

<a id="r-cpp"></a>

### R-CPP · 类型、地址与生命周期

**中文补充（按需，部分）：** 微软中文指针/数组小例子；不替代 CS106L 类型与寿命范围。 [对应范围](#cn-cpp)。

W1-S01 必读；入门巩固；英文；先修 B。

**来源**：[CS106L 类型 PDF](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-02-TypesAndStructs.pdf)；[指针 PDF](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-06-Iterators.pdf)。

**读到哪里**：阅读器页序 35～48、70～85；停在 Array pointer。约 35 分钟，与 R-L2 共用 W1-S01 的 50 分钟。首次不懂引用时回 P-CPP，不在未核验的第 3 讲 PDF 猜页码。

**带着什么问题读**：把 C++ 地址与 Tensor 元素字节联系起来；数组求和、六元素字节与生命周期自查。 [打开练习与自查](../weeks/week-01-foundations/session-01.md)。

**遇到困难时查阅**：英文规范 [指针加减](https://eel.is/c++draft/expr.add) §4～5、[std::array 概述](https://eel.is/c++draft/array.overview) §1。仅当地址差或连续性有疑问时用 5～10 分钟核对，读到同一数组的元素差与 contiguous container 即停；难度较高，不替代入门示例。W1 的六元素地址图是自查依据。

<a id="r-l2"></a>

### R-L2 · Tensor 存储、FLOPs 与 Roofline 讲义

**中文补充（按需，部分）：** 形状和基础运算有中文补充；FLOPs/显存账本/Roofline 未完整覆盖。 [对应范围](#cn-tensor)。

W1/W4 必读指定函数；中等；英文；B、M1。

**来源**：[CS336 lecture_02.py 固定提交](https://github.com/stanford-cs336/lectures/blob/6ff836dd5dfcbe7e848fe1a1734f1886f1116a7a/lecture_02.py)；[配套视频](https://www.youtube.com/watch?v=kuYAsz7zspQ)。

**读到哪里**：W1-S01：tensors_basics、tensors_memory 的 FP32/FP16，到 bf16 前停，15 分钟；S03：tensor_operations_flops 的 matmul，50 分钟含推导。W4-S03：arithmetic_intensity_matmul、roofline_plots，15 分钟。视频替换同主题讲义阅读，不叠加；未核验时间戳。

**带着什么问题读**：同一讲按不同知识点分三次读；W1 核对 Linear 账本，W4 预测算术强度，不重复整讲。 [打开练习与自查](../weeks/week-01-foundations/README.md)。

<a id="r-views"></a>

### R-VIEWS · Tensor 的视图、转置与复制

**中文补充（按需，部分）：** 先补 shape/广播；stride、共享、复制语义仍以原文为准。 [对应范围](#cn-tensor)。

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

## 中文补充：按卡住的地方选读

以下资料与上面的英文材料并列使用，不增加第二轮必读。标为“已预读”的仅指这里列出的正文范围；视频统一按[核验记录](../docs/audits/2026-10-05-chinese-resources.md)区分入口、字幕和画面。看懂当前概念后，回原课练习。

<a id="cn-python"></a>

### CN-Python：把语法接到自己写的小工具

**来源与关系：** 廖雪峰《Python 教程》是作者原站的中文讲解，不是 CS50P 译文；Python 官方中文教程用来补查精确语义。先完成本地小例子，再按下面范围回看。

| 用在哪里 | 中文正文与范围 | 读时留意 |
| --- | --- | --- |
| P1 | [定义函数](https://liaoxuefeng.com/books/python/function/define-function/index.html)：开头的 `def`、参数、`return`、`None`，到“空函数”前 | 例中的条件判断将在 P2 展开；重点追踪返回值 |
| P2 | [条件判断](https://liaoxuefeng.com/books/python/basic/if/index.html)：`if/elif/else` 和输入转换，到练习前 | 条件检查有顺序；用本课容量边界重新预测 |
| P3 | [循环](https://liaoxuefeng.com/books/python/basic/loop/index.html)：`for/range/while`，到 break 前；[列表](https://liaoxuefeng.com/books/python/basic/list-tuple/index.html)：list 小节，到 tuple 前 | 字典另看官方[§5.5](https://docs.python.org/zh-cn/3/tutorial/datastructures.html#dictionaries)开头至 `in` 示例；暂跳推导式 |
| P4 | [错误处理](https://liaoxuefeng.com/books/python/error-debug-test/error/index.html)：try 和调用栈，到“记录错误”前 | 开头的错误码例子指系统调用，Python 的 `open` 失败会抛异常；本课捕获具体异常类型 |
| P5 | [使用模块](https://liaoxuefeng.com/books/python/module/use-module/index.html)：导入、`sys.argv`、`__name__`，到“作用域”前 | 文件头格式不是必需模板；理解“导入”和“直接运行”的区别 |
| P6 | Python 官方[§7.2 读写文件](https://docs.python.org/zh-cn/3/tutorial/inputoutput.html#reading-and-writing-files)、§7.2.1 到 `write`、§7.2.2 到 `json.load` | 显式 UTF-8；先跳 seek、pickle。关闭文件不等于断电后持久化保证 |
| P7 | [单元测试](https://liaoxuefeng.com/books/python/error-debug-test/unit-test/index.html)：开头用 `abs` 选择正数、负数、零及非法输入，到“我们来编写一个 Dict 类”前 | 只借用选测试输入的方法；仍用本课 pytest，不提前引入继承 |
| P8 | [类和实例](https://liaoxuefeng.com/books/python/oop/class/index.html)：实例、`__init__`、`self` 与数据封装，到小结前 | 回本课检查两个实例；类属性共享与 `nn.Module` 仍按原文核对 |

**准备状态：** 上表指定正文已预读。字典改用官方中文查阅，因为候选博客的“顺序无关”表述不适用于本仓库使用的 Python 3。尚未确认一套能逐段对应 P1～P8 的中文原创视频分集；CS50P 视频保持原安排，不用未核验的大合集增加负担。

<a id="cn-shell"></a>

### CN-Shell：路径、标准流和自己的进程

**中文正文：** Missing Semester 中文社区的 [2026 Shell](https://missing-semester-cn.github.io/2026/course-shell/)，看“Shell 是什么”“在 Shell 中导航”“Shell 中有哪些可用的程序”中的 PATH，以及“Shell 语言（bash）”开头的管道、重定向和 tee；工具安装推荐及长日志命令先跳过。[2020 命令行环境](https://missing-semester-cn.github.io/2020/command-line/)只看“任务控制”，到“终端多路复用”前。[2020 Git](https://missing-semester-cn.github.io/2020/version-control/)只看“快照”“暂存区”及“基础”里的 status、diff、log。

**怎样搭配：** 这是英文课程的社区译文。Shell 与现有 2026 讲次对应；进程控制与 Git 明确使用 2020 正文，不套用 2026 视频章节。S1 读路径和进程；P5/P7 或环境自测卡住时回查标准流与 Git。正文已预读；中文站不等于中文配音视频，字幕与画面未检查。示例面向 Unix/bash，在 WSL/Linux 使用，不能直接当 PowerShell 语法。

<a id="cn-cpp"></a>

### CN-CPP：地址和数组先看小例子

**中文正文：** Microsoft Learn [原始指针](https://learn.microsoft.com/zh-cn/cpp/cpp/raw-pointers?view=msvc-170)开头的 `int* p`、取地址与解引用例子；[数组](https://learn.microsoft.com/zh-cn/cpp/cpp/arrays-cpp?view=msvc-170)只看“堆栈声明”中初始化 `numbers`、循环赋值和下标范围，到零大小数组讨论前。这些是微软发布的中文文档，可辅助 P-CPP 与 W1/W2 读代码；复杂类、智能指针和函数指针先跳过。

**准备状态与范围：** 指定正文已预读。未初始化的元素不能当作“随机数”读取；下标也要检查负值。这里只补地址、固定数组和边界，不覆盖整个 C++ 先修。原文的 MSVC 页面不改变本仓库的编译器设置；指针宽度要用自己的构建结果核对。中文视频和完整基础类型/引用讲解仍缺合适的逐段对应。

<a id="cn-tensor"></a>

### CN-Tensor：形状、广播与索引

**中文视频：** 李沐，2021《动手学深度学习》[数据操作](https://www.bilibili.com/video/BV1CV411Y7i4)，看到 reshape 和广播时暂停，先预测输出形状。

**中文正文：** 作者团队[§2.1 数据操作](https://zh.d2l.ai/chapter_preliminaries/ndarray.html)的 §2.1.1～2.1.5，选择 **PyTorch** 页签。对应 P-TENSOR 与 W1；是同主题中文讲解，不是 PyTorch 官方视频的译文。

**边界：** 正文已预读；视频讲次由[作者课表](https://c.d2l.ai/zh-v2/)确认，字幕、画面与分钟范围未检查。书中广播的“复制”是解释数值对应，不保证实际复制；`id(tensor)` 也不是底层数据指针。stride、storage offset、视图共享、`reshape` 何时复制，继续读 R-VIEWS 并完成原实验。

<a id="cn-autograd"></a>

### CN-Autograd：算出梯度以后，还没有更新参数

**中文视频：** 李沐，2021 [自动求导](https://www.bilibili.com/video/BV1KA411N7Px)。用它理解计算关系，看到 backward 后检查参数值是否改变。

**中文正文：** 作者团队[§2.5 自动微分](https://zh.d2l.ai/chapter_preliminaries/autograd.html)的 §2.5.1 和 §2.5.3（PyTorch），分别看标量输出求梯度、detach 截断梯度路径。需要 P1～P3 与向量点积；§2.5.2 的一般非标量反传先跳过。

**边界：** 指定正文已预读；视频仅作者课表对应已确认。detach 不等于复制数据，计算图与底层存储是两种关系；它也不能替代 W6 对 allocated/reserved/peak 的检查。

<a id="cn-training"></a>

### CN-Train：用线性回归看完整训练循环

**中文视频：** 李沐，2021 [线性回归：从零实现，P3](https://www.bilibili.com/video/BV1PX4y1g7KC?p=3)。先看每一批怎样经过预测、损失、反传和更新。

**中文正文：** 作者团队[§3.2 线性回归的从零开始实现](https://zh.d2l.ai/chapter_linear-networks/linear-regression-scratch.html)，PyTorch 的 §3.2.2～3.2.7；单卡训练课用全段，S4 只回看 §3.2.2“读取数据集”。生成器 `yield` 可先理解为“逐批交回数据”；自己的实现仍用原课 Dataset/DataLoader。

**边界：** 正文已预读，视频分集由作者课表确认，字幕/画面未检查。这里 `loss.sum().backward()` 后在更新中除以 batch size；本课若已使用 mean loss，不能再除一次。原书还使用平方误差的一半，比较 loss 前先统一定义。该例没有覆盖 workers、pin_memory 或 GPU 等待测量，S4 对照仍必做。

<a id="cn-save"></a>

### CN-Save：先区分权重读回与训练恢复

**中文视频：** 李沐，2021 [模型构造：读写文件，P4](https://www.bilibili.com/video/BV1AK4y1P7vs?p=4)。

**中文正文：** 作者团队[§5.5 读写文件](https://zh.d2l.ai/chapter_deep-learning-computation/read-write.html)的 §5.5.1～5.5.2（PyTorch），从 Tensor 保存读回到 `state_dict`；先会 P6/P8，再看模型例子。

**边界：** 正文已预读，视频分集由课表确认，字幕/画面未检查。它只补保存与加载参数；完整 optimizer、随机状态、数据位置及 DCP 恢复仍读原英文材料。旧例未显式写 `weights_only`，按安装的 PyTorch 版本核对，练习只加载自己生成的文件。
