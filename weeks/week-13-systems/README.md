# 单元 W13：torch.compile 与 Systems 综合实验

[课程目录](../../course/README.md) · [我的进度](../../course/progress.md) · [环境准备](../../course/environment.md)

预计 10～18 小时用于本单元，变式与排错另留 1～3 小时；桥接只计新发生的时间。按实际掌握推进，记录规则见 [学习方法](../../course/guide.md#time-budget)。

## 这一单元要弄清什么

同一个小 Block，打开编译后会少做哪些事，又会多付出哪些成本？复用 W6 的实现，对齐 eager 与 torch.compile 的结果，分别测首次调用和稳态，再改变输入形状观察重编译或 graph break。CS336 Systems 提供问题背景，实际完成的是本仓库的小型实验。

## 开始前

紧接 W6 的正确性与时间线分析，复用 P8 模型结构和 W2 异步计时，不依赖 DDP。先说明首次编译与稳态为什么不能混在一次平均里；不清楚时回 [W2 计时](../week-02-cuda-execution/session-03.md)。

<details>
<summary>先解释，再展开核对</summary>

首次调用包含编译等一次性成本，不能与预热后的 eager 单次延迟直接比较；回 W2 计时与 W6 时间线。

</details>

## 按顺序学习

- [W13 第 1 段：一行 Python，会变成几个 kernel？](session-01.md)。
- [W13 第 2 段：第一次慢下来，后面能省回来吗？](session-02.md)。
- [W13 第 3 段：第二种 shape 更慢，一定是重编译吗？](session-03.md)。

- [本单元掌握检查](assessment.md)：实验完成要求、变式与排错题。

## 实践任务

建议目录：labs/03-triton-attention/systems-study/；整合 projects/gpu-performance-lab/。

1. 复用 W5 的逐元素/归约表达式或 W6 的小模型区段，先限定固定形状的前向，保留 eager 参考。
2. 加入 torch.compile，检查输出误差，分别保存首次编译、预热与稳态计时。已有 Triton 实现语义一致时可加入第三组，不新增算子实现要求。
3. 从算子表或时间线比较 kernel 数量、启动间隙和整体延迟，不能仅凭减少 kernel 数就断言更快。
4. 用第二个形状检查是否发生重编译；遇到 graph break 时记录原因与影响。先解释一个例子，不要求消除所有 graph break。
5. 将一个优化用于模型区段，报告稳态收益是否传递、首次成本和适用条件。无加速也是有效结果。

## 按需回看

自定义 Attention 作为扩展，可阅读 [FlashAttention-2 论文](../../resources/optional.md#x-fa2) 和 [作者机构博客](../../resources/optional.md#x-fa2)。先限定形状与功能，完整 forward/backward 另排时间。不要同时把编译实验和手写 Attention 都列为本周必做。

完成后做 [阶段复习](../../course/reviews.md#stages)。

[上一单元](../week-06-attention/README.md) · [下一步](../week-07-collectives/README.md)
