# 按需先修检查

先检查能力，再安排补课。以下项目均未验收；用已有代码和解释证明掌握后可以跳过。补修时间不硬塞进原有周预算。

## A. 运行环境：W2 前完成，服务器部分在 W7 前完成

- [ ] 能在目标 Linux/WSL 环境进入目录、运行脚本、保存日志并定位报错。
- [ ] 能区分 Windows、本地 WSL 与服务器，知道当前命令在哪台机器运行。
- [ ] 能辨认当前 Python 环境与依赖来源，记录版本并查看 Git 改动。
- [ ] GPU 能完成小 Tensor 运算；CUDA 实验能编译最小程序。版本号输出不足以证明可运行。

缺少工具经验时选读 [Missing Semester 2026 Shell](https://missing.csail.mit.edu/2026/course-shell/) 和 [Git](https://missing.csail.mit.edu/2026/version-control/)，只补卡点，先投入 1～2 小时尝试。完整工具链配置可能需要额外时间。

工具按使用前检查：W2 编译运行，W3 sanitizer 与计数器，W5 Triton，W13 torch.compile，W7 多卡通信，W8 服务。用 [环境记录](environment.md) 保存结果；本轮未执行这些检查。

## B. 编程与张量：W1 内诊断，W2 前补齐

- [ ] 会编译运行 C++ 程序，理解数组、指针、函数参数、越界和生命周期。
- [ ] 能解释 shape、stride、dtype、device 与连续存储，推导矩阵乘法输入输出形状。
- [ ] 能用容差比较参考结果，理解浮点运算顺序可能引入误差。

用 W1 的 [CS106L 选读](../weeks/week-01-foundations/README.md) 补薄弱点。未写过 C++ 时先完成最小程序；60 分钟讲义预算不代表能从零掌握 C++。

## C. 模型结构：W6 前完成

- [ ] 给定 batch、序列长度、隐藏维度与头数，写出 Q/K/V 和 Attention score 的形状。
- [ ] 解释 causal mask、softmax、残差、归一化与 MLP 在 Decoder Block 中的位置。
- [ ] 运行小型前向例子，说明 eval、dropout 与是否记录梯度。
- [ ] 区分 prefill 与逐 token decode，解释 KV Cache 保存什么。

在 [CS336 2026 课程表](https://cs336.stanford.edu/) 定位 Lecture 3: Architectures，配合 [PyTorch SDPA](https://docs.pytorch.org/tutorials/intermediate/scaled_dot_product_attention_tutorial.html)。先用 1～2 小时读图与推形状，再做小例子；不要求训练语言模型。prefill/decode 有困难时可提前选看 W8 的 Lecture 10。

## D. 单卡训练：W7 的 DDP 扩展前完成，最迟 W11 前完成

- [ ] 写出 forward、loss、backward、optimizer step 与清梯度流程，解释清梯度时机。
- [ ] 在固定小批次上让 loss 明显下降，用一次参数更新验证梯度生效。
- [ ] 区分 train/eval 与启用/关闭 autograd。
- [ ] 区分参数、梯度、优化器状态、保存的激活和临时工作区；不套用通用的每参数字节常数。
- [ ] 保存并恢复小模型、优化器与步数，核对恢复后的下一步行为。

材料：[Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)、[Autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)、[Optimization](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)。先用小型 MLP 与合成数据，已有代码可复用。

若这些概念尚未掌握，先安排独立补修单元。不要一边学习 DDP，一边调试基础训练逻辑。混合精度概念在 W11 补入，先保持 FP32 参考。

## 实际依赖与推荐顺序

W 编号是固定单元 ID，推荐顺序以 [总路线](../README.md) 为准：W13 在 W6 后学习。相邻单元也不一定依赖前一个单元的全部硬件实验。

| 要开始的内容 | 必须具备 | 可稍后补做 |
| --- | --- | --- |
| W2～W5 算子 | A、B；前一算子的正确性与测量能力 | 更多输入与优化版本 |
| W6 模型分析 | C；计时与 Softmax 理解 | 手写完整 FlashAttention |
| W13 编译 | W5 表达式或 W6 小模型；正确性检查和 GPU 计时 | 区域编译、完整自定义 Attention |
| W7 通信 | Linux 多卡环境；张量与通信语义 | D 未完成时，最小 DDP 移到 W11 |
| W8 单卡推理 | C；可用的单卡服务环境 | W7 的 4 卡实验 |
| W11～W12 训练 | D；W7 通信概念与至少 2 卡环境 | 4 卡、改变 world size 的恢复 |
| W15～W16 调度 | Python 与任务日志；W15 Ray 基础 | 复杂并行训练实现 |

硬件等待时可进入不依赖它的单元；进度表保留未完成项，不将未测量的任务标为通过。
