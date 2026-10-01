# 单元 W13：torch.compile 与 Systems 综合实验

[总路线](../../README.md) · [学习方式](../../docs/learning-workflow.md) · [资源索引](../../resources/README.md) · [当前做法与相关进展](context.md)

建议学习位置：第 7 个学习周。W13 是固定单元 ID，按下方导航推进。

状态：未开始。预算：约 10.5 小时（[分项](../../docs/study-guide.md#time-budget)），必要时顺延。环境：优先 Linux 单卡 GPU。

## 本周要解决什么

比较 PyTorch eager、torch.compile 与已有算子实现，理解框架优化如何传递到模型区段。以 CS336 Systems 的问题设计作参考，默认实践使用本仓库的独立练习。

先修：CUDA、Triton 与W6模型分析已完成。要回答：编译优化减少了什么？首次编译与稳态时间为何要分开？单算子收益是否传递到模型？

## 按顺序学习

先用 30 分钟按 [资料复核流程](../../docs/weekly-refresh.md) 核对必读材料、版本和运行条件。[补充阅读](context.md) 在基础完成后选读，单独安排时间.

按 [分段学习指南](study-guide.md) 分三段学习，每段读完就动手。各段学习指南包含原文定位、图例、暂停题与折叠核对说明；先自行作答，再检查理由和运行结果。AI 理解提示词可以跳过，完成要求不依赖 AI 评价。

学习指南已整理：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md)。[本次资料复核](refresh-2026-10-01.md) 已完成；学习未开始，实际开始学习日仍按更新流程复查。

| 学习段 | 指定范围 | 读后立即做 | 资料预算 |
| --- | --- | --- | --- |
| 1. 编译正确性 | CS336 L6 对照函数；compile Basic Usage | eager/compile 误差核对 | 45 分钟 |
| 2. 首次与稳态 | compile Demonstrating Speedups；L6 benchmarking | 算子与模型区段计时 | 60 分钟 |
| 3. 变化与中断 | compile Graph Breaks、Troubleshooting | 第二个 shape 与中断证据 | 45 分钟 |

原文选读共 150 分钟，本地图解与自查另计 60 分钟。材料元信息统一在资源索引；可选拓展另排时间。

## 遇到问题再看

自定义 Attention 作为扩展，可阅读 [FlashAttention-2 论文](../../resources/README.md#x-fa2) 和 [作者机构博客](../../resources/README.md#x-fa2)。先限定形状与功能，完整 forward/backward 另排时间。不要同时把编译实验和手写 Attention 都列为本周必做。

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

可选：完成基础后，从补充阅读选一个实际问题写进报告；未选不影响本单元完成。

## 实验记录

实验与报告：尚未创建。自评与验收日期：待完成。

[上一单元](../week-06-attention/README.md) · [下一单元](../week-07-collectives/README.md)
