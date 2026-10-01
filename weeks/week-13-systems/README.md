# 单元 W13：torch.compile 与 Systems 综合实验

[总路线](../../README.md) · [学习方式](../../docs/learning-workflow.md) · [资源索引](../../resources/README.md) · [当前做法与相关进展](context.md)

建议学习位置：第 7 个学习周。W13 是固定单元 ID，按下方导航推进。

状态：未开始。预算：9 小时，必要时顺延。环境：优先 Linux 单卡 GPU。

## 本周要解决什么

比较 PyTorch eager、torch.compile 与已有算子实现，理解框架优化如何传递到模型区段。以 CS336 Systems 的问题设计作参考，默认实践使用本仓库的独立练习。

先修：CUDA、Triton 与W6模型分析已完成。要回答：编译优化减少了什么？首次编译与稳态时间为何要分开？单算子收益是否传递到模型？

## 按顺序学习

先用30分钟看 [本周补充阅读](context.md)，按 [更新流程](../../docs/weekly-refresh.md) 核对资料。时间从原报告时段划出，总预算不变。

按 [章节导学](study-guide.md) 分三段学习，每段读完就动手。下面只列安排，具体链接、阅读位置和检查方法都在导学里。

| 学习段 | 指定范围 | 读后立即做 | 资料预算 |
| --- | --- | --- | --- |
| 1. 编译正确性 | CS336 L6 对照函数；compile Basic Usage | eager/compile 误差核对 | 45 分钟 |
| 2. 首次与稳态 | compile Demonstrating Speedups；L6 benchmarking | 算子与模型区段计时 | 60 分钟 |
| 3. 变化与中断 | compile Graph Breaks、Troubleshooting | 第二个 shape 与中断证据 | 45 分钟 |

阅读共150分钟，包含视频、教程和论文。补充材料按需替换阅读内容；选修另排时间。

## 遇到问题再看

自定义 Attention 作为扩展，可阅读 [FlashAttention-2 论文](https://arxiv.org/abs/2307.08691) 和 [作者机构博客](https://crfm.stanford.edu/2023/07/17/flash2.html)。先限定形状与功能，完整 forward/backward 另排时间。不要同时把编译实验和手写 Attention 都列为本周必做。

## 实践任务

建议目录：labs/03-triton-attention/systems-study/；整合 projects/gpu-performance-lab/。

1. 复用 W5 的逐元素/归约表达式或 W6 的小模型区段，先限定固定形状的前向，保留 eager 参考。
2. 加入 torch.compile，检查输出误差，分别保存首次编译、预热与稳态计时。已有 Triton 实现语义一致时可加入第三组，不新增算子实现要求。
3. 从算子表或时间线比较 kernel 数量、启动间隙和整体延迟，不能仅凭减少 kernel 数就断言更快。
4. 用第二个形状检查是否发生重编译；遇到 graph break 时记录原因与影响。主线只解释一个例子，不要求消除所有 graph break。
5. 将一个优化用于模型区段，报告稳态收益是否传递、首次成本和适用条件。无加速也是有效结果。

## 验收

- [ ] 练习范围、依赖版本和编译配置明确；不把自选练习声称为完成官方作业。
- [ ] eager/compile 正确性通过，首次编译和稳态分开计时。
- [ ] 记录形状变化、重编译或 graph break 的观察，unsupported 情况不静默删除。
- [ ] 有原始数据，并能解释算子收益为何能或不能传递到模型区段。
- [ ] 项目 README 可以让后来者复现同一个问题。
- [ ] 按补充阅读的要求，在报告中解释一个实际使用问题，注明哪些结论还没验证。

## 实验记录

实验与报告：尚未创建。自评与验收日期：待完成。

[上一单元](../week-06-attention/README.md) · [下一单元](../week-07-collectives/README.md)
