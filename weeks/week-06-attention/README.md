# 单元 W6：Attention 资源账本

[课程目录](../../course/README.md) · [我的进度](../../course/progress.md) · [环境准备](../../course/environment.md)

预计 14～26 小时用于本单元，变式与排错另留 1～3 小时；桥接只计新发生的时间。按实际掌握推进，记录规则见 [学习方法](../../course/guide.md#time-budget)。

## 这一单元要弄清什么

把序列长度翻倍，Attention 的哪些对象会翻倍，哪些会变成四倍？沿 Q、K、V 的形状追踪显式 Attention，再与 SDPA 对齐，最后把它放进一个小 Decoder Block。这样才能判断省下的中间矩阵是否真的改变整个模型的显存与耗时。

## 开始前

完成 W5、[P8 类与模块](../../course/foundations/p08.md#p8) 和 [先修 C](../../course/prerequisites.md)。先说出 head、残差与 LayerNorm 的位置，并区分 eval 与禁用梯度。先完成 [单卡训练的训练、验证和重载](../../course/foundations/training.md)，能解释 backward 与 step；Adam 恢复在 W11 前完成。Block 实验仍研究前向，第四段复用小训练模型学习显存生命周期。

<details>
<summary>先解释，再展开核对</summary>

QKᵀ 产生每个 head 的 S×S 分数；eval 改变部分模块行为，no_grad/inference_mode 才控制梯度记录。形状例子见先修 C。

</details>

## 按顺序学习

- [W6 第 1 段：每个 query，究竟可以读哪些 key？](session-01.md)。
- [W6 第 2 段：没有完整存下分数矩阵，还能算出 Attention 吗？](session-02.md)。
- [W6 第 3 段：GPU 的空档，应该去哪里找原因？](session-03.md)。
- [W6 第 4 段：一轮计算结束了，显存为什么没有降回去？](session-04.md)。

- [本单元掌握检查](assessment.md)：实验完成要求、变式与排错题。

## 实践任务

建议目录：labs/03-triton-attention/decoder-profiling/。

1. 按 [W6 第 2 段：没有完整存下分数矩阵，还能算出 Attention 吗？](session-02.md) 建立小型 pre-norm Decoder Block，写明 batch、序列长度、隐藏维度、头数和 dtype。这组实验只分析固定形状的前向，明确 eval、dropout 和 autograd 状态；backward 留作扩展。
2. 估算参数、Attention/MLP FLOPs 与显存项，再采集算子耗时。
3. 比较显式 Attention 与 PyTorch SDPA：统一 causal mask、dropout、输入与 dtype，检查输出误差。
4. 记录实际选到的 SDPA 后端；无法确认时写“未确认”，不将所有 SDPA 结果都称为 FlashAttention。
5. 用已有小训练模型追踪状态寿命，完成有界 Tensor 留存对照，解释 allocated/reserved/peak。
6. 整理短报告《一个 Decoder Block 的计算和显存花在哪里？》。

在报告中加入一段 CPU—拷贝—GPU 时间线，区分 kernel 忙碌与 GPU 空档。优先采一次 Nsight Systems CUDA trace；受平台限制时用 PyTorch trace 标注可见范围，并保留 Nsight 补测项。显存记录区分 allocated、reserved 与设备整体占用，不能将它们直接相加。

## 按需回看

作者机构博客：[FlashAttention-2](../../resources/optional.md#x-fa2)，用于理解 IO 优化后为何还要优化工作划分；基础完成后另排 30 分钟。

视频可复看 [CS336 2026 Lecture 6](../../resources/gpu.md#r-l6) 的相关部分。先读指定论文段落，再做模型测量，不增加整讲观看任务。

[上一单元](../week-05-triton-softmax/README.md) · [下一步](../week-13-systems/README.md)
