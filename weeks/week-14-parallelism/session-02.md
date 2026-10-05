# W14 第 2 段：少算了一半矩阵，为什么还要付出通信？

[本单元](README.md) · [课程目录](../../course/README.md)

局部矩阵变小，只说明每张卡的一部分计算减少。完整输出仍需要合并，通信量和等待决定了这种切分是否值得；先保证结果和 bias 没有重复计数。

## 视频与正文

先看 [CS336 2026 Lecture 7 · Parallelism](https://cs336.stanford.edu/)：TP 主题暂停标出合并通信与数据形状；PP 留在下一段。

视频分钟位置待核验；下列章节或函数用于正文定位，也可以直接按正文完成练习。

## 中文补充（按需）

Datawhale 中文[张量并行的两层 MLP](https://datawhalechina.github.io/diy-llm/chapter8/chapter8_第八章分布式训练.html)只回看 §8.2.2 里 f/g 的对偶关系：前向求和在哪里，反向求和又在哪里。限定文字已预读；它没有为本课逐条列出 collective 的 shape，也没有涵盖 bias。把每个同步点重新写入自己的通信表，性能数字不作为完成依据。[范围与版本](../../resources/training.md#cn-parallel)。

## 开始前

先能解释上一段两层 MLP 的切分；AllReduce 的输出归属回看 [W7](../week-07-collectives/session-01.md)。

资源定位：[TP 通信与 PP 流水线](../../resources/training.md#r-parallel)。

**先读**：[Megatron Bridge Parallelisms Guide](../../resources/training.md#r-parallel) 的 `Model Parallelism → Tensor Parallelism`。配置示例只帮助理解维度，不要求部署 Megatron。

**接着想一想**：回 W7 的 collective 图，为每次通信标数据 shape 与目的；回 W4 计算局部 GEMM 的工作量，避免只看到每卡计算变少。

## 通信要写清目的、形状和时点

沿[两层 MLP 切分图](session-01.md)，第二层各 rank 得到同一输出形状的部分和。SUM AllReduce 让每个 rank 得到完整和，下一步才可把它当原模型输出使用。通信前的局部输出与通信后的完整输出 shape 相同，语义却不同。

bias 属于最终线性输出。两片各加一次同一 bias 再求和，会把它放大两倍。因此先用无 bias 版本确认代数，再单独添加 bias 检查位置。CPU 的显式求和可验证这个等式；通信延迟则只能由真实设备运行得到。

**暂停题：输出与通信形状**

沿上例，输入是 (1,2)，两片第一层输出各为 (1,1)，第二层部分输出也各为 (1,1)。最后用 SUM AllReduce 后，两片是否都拿到最终结果？若两片各自先加同一个输出 bias=1 再求和，得到什么？

<details>
<summary>核对依据</summary>

AllReduce 后双方均有 6；各先加 bias 会得到 (0+1)+(6+1)=8，而正确输出为 6+1=7。bias 应只计一次。CPU 用显式求和检验代数，2 卡才检验通信；记录元素数、dtype、各次 collective 的 shape，而不是把 CPU 合并耗时当成 NCCL 测量。

</details>

**动手练习**：用固定权重和输入比较未切分 MLP 与两个分片组合。CPU 路径用显式合并验证，2 卡路径使用对应 collective；bias 若加入，单独检查是否被重复求和。

**检查结果**：数值误差通过，通信量估算明确，CPU 模拟与真实通信结果分开记录。

## 完成后

把代码、预测与实际结果记在同一份笔记中。完成本段检查后，沿下方链接继续。

[上一课](session-01.md) · [下一课](session-03.md)
