# 基础阶段与先修诊断

[学习路线](../README.md) · [资源索引](../resources/README.md) · [时间安排](guide.md#time-budget)

先用下面的小题找起点。能独立解释、换一组输入仍能做对的内容，可以跳过重复讲解；暂时不会的，按对应入口补学。预计时间包含小练习，与 W 单元分别记录。我的实际掌握情况仍以作答、代码和运行结果为准。

## 怎么选入口

| 开始前 | 必须完成的基础 | 可延后内容 |
| --- | --- | --- |
| W1 | P1～P7：Python 核心；M1：矩阵与单位；B 的 C++ 最小程序、Tensor 入门 | 微积分、训练、完整 Transformer |
| W2 | A：Linux 与环境；B：数组、指针和 W1 布局检查 | 多卡登录与通信配置可到 W7 |
| W5 | M2：指数、归一化；W3 归约和 W4 访存 | 反向传播推导 |
| W6 | P8；D 的训练、验证与权重重载；M3；C 的模型前向 | D 的 Adam 恢复部分在 W11 前完成 |
| W8 | C；S2 请求；HTTP/JSON 和 token 入门在 W8 第一、二段补齐，S3 Docker 在服务段后完成 | W7 多卡实验不阻塞单卡服务 |
| W11 | D 的 Adam 下一步恢复；S4 数据管线；W7 通信与 2 卡环境 | AMP 性能对照、4 卡、多机；AMP 概念仍必学 |
| W15 | P 的函数、字典、类与日志；A 的运行能力 | 不要求完成多卡训练性能实验 |

## P. Python：能把小计算写成可重复的脚本

**检查**：不用复制答案，写函数读取一组数，返回元素个数、总和、均值，并把结果保存为 JSON。再读回来比较；空列表应明确报错，不能除以零。

**正式入口**：[P1～P8 编程基础](foundations/README.md) 以 CS50P 0～6、8 为主教材，配连续中文学习与递进练习；Python 官方教程用于查阅。P1～P7 在 W1 前完成；P8 类与模块在 W6 前完成，不推迟到 W15。预计范围见基础指南，真实耗时另外记录。此处的小检查是诊断，不能代替整段学习或独立掌握检查。

函数把输入转换为输出；循环依次处理元素；字典把字段名与值对应；JSON 保存的是可重建的数据。报错时先读 traceback 最后一行，再找自己脚本的行号。

<details>
<summary>先写，再核对</summary>

输入 `[2, 4, 6]` 应得到个数 3、总和 12、均值 4。改为 `[-2, 0, 5]` 应得到总和 3、均值 1；空列表走自己的异常分支。关闭程序再读取仍得到相同字段，说明记录落到了文件里。P8（W6 前）的类练习：两个计数器各从 0 开始，分别加 2、5，结果必须分别为 2、5。

</details>

**完成标准**：两组输入和空输入均有解释与实际输出；能修改函数参数，能从文件重建结果。脚本与输出保存在自己的补学目录，不要求接入 GPU。

## A. Linux、Python 环境与基本工具

**检查**：说出当前命令运行在 Windows、WSL 还是服务器；打印当前目录、解释器位置，运行脚本并分别保存正常输出和错误输出。

**补学顺序**：完成 [S1 进程/线程/权限/环境练习](bridges/s01.md#s1)，其中 shell 阅读沿用 [P-SHELL](../resources/foundations.md#p-shell) 的 shell 导航与重定向，再读 [P-ENV](../resources/foundations.md#p-env) 的虚拟环境和 Git 改动查看。A 与 S1 是同一组练习，合计预计 3～6 小时，不重复相加；驱动安装、网络和服务器权限另计。

在 Linux/WSL 的自己的练习目录运行 `pwd`、`ls`、`python --version`，用 `python -c "import sys; print(sys.executable)"` 确认解释器。已有 `practice.py` 后运行 `python practice.py > output.txt 2> error.txt`。在脚本中制造一个不存在的变量，再查 `error.txt`；修好后重跑。这里只操作自己的练习文件。

~~~text
终端工作目录 → Python 解释器 → 当前环境里的依赖 → 脚本
                                  ├→ 标准输出 output.txt
                                  └→ 错误输出 error.txt
~~~

<details>
<summary>核对环境判断</summary>

`sys.executable` 应指向你实际选择的环境；只看提示符名字不足以确认。不存在的变量产生 NameError，错误日志应含脚本位置。版本号只证明命令存在，不能证明 CUDA 程序可运行。Git 的 `status` 显示改了哪些文件，`diff` 显示改了什么内容。

</details>

**完成标准**：能重现一次失败、定位并修复；能区分脚本问题与找错解释器；在 [环境记录](environment.md) 填写实际信息。W2 前另编译 CUDA 最小程序并验证输出，W7 前核对服务器设备和通信；没有实际运行的检查，继续记为待做。

## B. C++ 与 Tensor：先会编写，再研究布局

**C++ 补学**：[P-CPP](../resources/foundations.md#p-cpp) 依次读程序结构、变量、条件/循环、函数，再读指针和 `std::array`。先理解 `main` 是入口、编译把源文件变成可执行程序。已会 Python 但没写过 C++，安排 6～10 小时；CS106L 的少量幻灯片只适合之后巩固，不能承担从零入门。

在已配置的 Linux/WSL 编译器中，自己创建 `array_sum.cpp`，用 `std::array<float, 4>` 存 `{1, 2, 3, 4}`，用循环求和，函数返回结果。用 `g++ -std=c++17 array_sum.cpp -o array_sum` 编译，再运行 `./array_sum`。Windows 可沿用 W1 已记录的编译器配置。编译错误从第一条看起，不额外引入 CMake。

先读下面的最小函数，再遮住循环补全；独立实现时自行写 include、main、调用与打印，不复制整份程序：

```cpp
float sum_values(const std::array<float, 4>& values) {
    float total = 0;
    for (std::size_t index = 0; index < values.size(); ++index) {
        total += values[index];
    }
    return total;
}
```

调用方的数组在函数执行时仍存在；`const ...&` 是只读引用，避免复制整个数组；`std::size_t` 是用于大小/下标的无符号整数类型。程序顶部需要 `<array>`，打印需要 `<iostream>`。改成 5 元素时同步改类型中的长度与初始化；随后改用 `values.at(index)` 观察越界检查，再解释为何不能依赖 `operator[]` 自动报告错误。不要为了观察悬垂指针而解引用失效地址，先用作用域图指出失效时刻。

<details>
<summary>C++ 自查</summary>

结果为 10；四个有效下标是 0～3，循环不能访问下标 4。`&values[0]` 是首元素地址，解引用取得元素；引用是已有对象的别名。局部数组在函数返回后结束生命周期，返回它的指针不能延长存储寿命。函数可返回求和的值。

</details>

**Tensor 补学**：[P-TENSOR](../resources/foundations.md#p-tensor) 读创建、属性、张量运算，约 2～3 小时含实践；先用 CPU。创建 0～5 的六个数，排为 2×3，分别做逐元素加法和矩阵乘法。

读懂 `torch.arange(6).reshape(2, 3)` 后遮住 shape 补全，从空文件重写；再把逐元素加 1 改为加 `[10,20,30]`，预测每行的结果。广播从末维对齐，维度相等或某一维为 1 才可扩展；shape 为 [2] 的向量不能直接按“每行一个值”加到 [2,3]，应先明确排成 [2,1]。用这个反例诊断广播误解，再进入 W1 的内存布局。

<details>
<summary>Tensor 自查</summary>

`[[0,1,2],[3,4,5]] + 1` 得到 `[[1,2,3],[4,5,6]]`。原矩阵乘其转置得到 `[[5,14],[14,50]]`，shape 为 2×2。逐元素乘法要求可广播的 shape；矩阵乘法匹配内维。布局/别名在 W1 深入，此处不提前重复整段。

</details>

**完成标准**：C++ 能独立编译、改长度、解释边界；Tensor 小例子先预测再运行。达到后开始 W1；W1 的布局与计数检查通过后进入 W2。

## M. 数学：按使用时点补学

| 小段 | 何时需要 | 材料与预算 | 立即练习 |
| --- | --- | --- | --- |
| M1 矩阵与单位 | W1 前 | [P-MATH](../resources/foundations.md#p-math) 标量、向量、矩阵、点积、矩阵乘法；3～5 小时含手算 | 算 2×3 乘 3×2；将元素数换算为 B、KiB、MiB |
| M2 指数与归一化 | W5 前 | [P-SOFTMAX](../resources/foundations.md#p-softmax) Softmax 运算；1～2 小时 | 手算 `[0, ln(3)]`，再给两数同时加 100 |
| M3 导数与链式法则 | 单卡训练前 | [P-CALCULUS](../resources/foundations.md#p-calculus) 导数、偏导、链式法则；3～5 小时 | 对 `loss=(weight*2-6)^2` 求 weight=1 时的梯度 |
| M4 汇总统计 | W8/W16 前 | [P-STATS](../resources/foundations.md#p-stats) 随机变量、均值与方差；1～2 小时，配本段分位数定义 | 对 `[1,2,3,4,100]` 算均值、中位数、nearest-rank p95 |

<details>
<summary>数学核对依据</summary>

M1：`[[1,2,3],[4,5,6]] × [[1,0],[0,1],[1,1]] = [[4,5],[10,11]]`。第一个输出是 `1*1+2*0+3*1=4`。六个 FP32 数按每个 4 B 为 24 B；1 KiB=1024 B，1 MiB=1024² B，GB 与 GiB 分开。

M2：指数为 `[1,3]`，除以和 4 得 `[0.25,0.75]`。同时加同一常数不改变比值；计算时先减最大值避免指数过大。W5 再学习浮点与分块细节。

M3：先求平方外层，再乘内层导数：`2*(2*weight-6)*2`，weight=1 时为 -16。学习率 0.1 的一步 SGD 得 2.6；这是单个平方误差的约定，不是自动适用所有 mean loss。

M4：均值 22，中位数 3。这里 p95 用排序后第 `ceil(0.95*n)` 个数，因此为 100；插值算法可能给出其他数，报告要写方法。5 个样本的尾部分位数不稳定，不能宣称测出了生产尾延迟。

</details>

**完成标准**：每小段换一组数字能重算，明确矩阵乘法内维、单位及 loss/分位数约定；不要求重复通读同一本教材。

图与依赖关系在 [S6](bridges/s06.md#s6) 用 ready 集合和环诊断补齐，进入 W15 前完成。数学已会的部分可直接用迁移题通过，不要求重学。

## C. 模型结构：W6 前完成

先通过 [P8 类与模块](foundations/p08.md#p8)，再按 [P-MODEL](../resources/foundations.md#p-model) 读 Attention 的 Q/K/V 与多头图，再读残差、LayerNorm 和位置前馈网络；最后对照 W6 的小型 pre-norm Block。安排 4～6 小时含 shape 推演和 CPU 前向。教材完整编码器—解码器仅作结构参考，不要求实现机器翻译或训练语言模型。

~~~text
输入 X[B,S,W] → 每个位置的 Linear → Q/K/V[B,H,S,D]
                                      ↓ QKᵀ / √D
                                 score[B,H,S,S]
                                      ↓ causal mask → softmax → 乘 V
                                    [B,H,S,D] → 合并头[B,S,W]
残差：把同 shape 的输入加回；MLP：逐位置 W → F → W
~~~

**暂停题**：B=1、S=3、H=2、D=4 时，W 是多少，score 有多少元素？第 2 个位置可关注第 3 个位置吗？`eval()` 是否等同于关闭 autograd？

<details>
<summary>模型自查</summary>

W=H×D=8；score 是 1×2×3×3，共 18 个元素。从第 1 个位置开始数，causal 条件下第 2 个位置只能看前两个。残差相加两端 shape 必须一致。`eval()` 切换 dropout 等模块行为，`no_grad()` 控制梯度记录，二者独立；W6 的函数式 SDPA 还要显式传 `dropout_p=0`。

</details>

**完成标准**：逐箭头说明 shape，能运行 CPU 小前向并解释 mask；不把整张 score、KV Cache 和模型参数混为一项。prefill/decode 由 W8 第一段正式引入，不要求提前读 W8。

<a id="d-单卡训练w11-前完成"></a>

## D. 单卡训练：先会训练，再研究模型成本

**检查**：从零参数的 Linear(1,1) 出发，拟合五点直线；解释一次 mean MSE 的参数更新，验证时不改参数，保存后用新模型加载并预测。再说明“加载后预测一致”和“恢复后下一步更新一致”为什么是两项检查。

**正式入口**：[单卡训练入门](foundations/training.md)。P8、Tensor 与 M3 完成后，先做训练、验证、权重重载，预计 5～8 小时，W6 前完成；[Adam 下一步恢复](foundations/training.md#resume) 预计另 2～4 小时，W11 前完成，再接 S4。示例、练习与核对只在这份讲解维护。

**完成标准**：W6 前能独立完成 CPU 小训练与验证、重载；W11 前连续 3 步与恢复 2+1 的输入、模型和优化器状态对齐。单卡 GPU 尚未运行时，不能把 CPU 结果写成 GPU 验证。

## 依赖和硬件等待

完整顺序见 [课程目录](README.md)。W7 需要 2 卡才能完成测量；等待时可先学 W8～W10。W14 可在 CPU 验证 TP 代数；W15、W16 可在 CPU 完成规定练习。未完成的硬件检查留在进度表，不用纸面计算替代实测。

不熟悉英文术语时，先按中文图例写出对象和操作，再只查指定原文；不要求依靠 AI 翻译整份材料。基础检查通过后保留笔记，后续遇到同一概念直接回看。

## PyTorch 视频怎么接入

先修 B：打开 [Introduction to PyTorch Tensors](https://docs.pytorch.org/tutorials/beginner/introyt/tensors_deeper_tutorial.html) 页内视频，先看创建、shape 与 dtype；每个主题暂停预测本页小 Tensor。转置与复制接 W1，广播按本页 B 的输入核对。

训练视频与正文范围统一见 [单卡训练课](foundations/training.md)。先理解参数梯度与输入梯度的区别，再用标量例子核对；画面和时间轴未逐段核验时，按可独立完成的正文继续。

[练习输入与待补全代码](../exercises/README.md) · [返回基础自测](prerequisites.md#怎么选入口)
