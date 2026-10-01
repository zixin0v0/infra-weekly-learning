# 单元 W5：Triton 与 Online Softmax

[总路线](../../README.md) · [学习方式](../../docs/learning-workflow.md) · [资源索引](../../resources/README.md) · [当前做法与相关进展](context.md)

建议学习位置：第 5 个学习周。W5 是固定单元 ID，按下方导航推进。

状态：未开始。预算：约 11 小时（[分项](../../docs/study-guide.md#time-budget)）。环境：Linux/WSL2 GPU，先确认 Triton 可运行。

## 本周要解决什么

用 Triton 实现稳定 Softmax，连接 mask、归约、kernel fusion 与在线归一化。

先修：W4通过。要回答：为什么先减最大值？融合减少哪些中间 Tensor？分块后如何更新归一化状态？

## 按顺序学习

先用 30 分钟按 [资料复核流程](../../docs/weekly-refresh.md) 核对必读材料、版本和运行条件。[补充阅读](context.md) 在基础完成后选读，单独安排时间.

按 [分段学习指南](study-guide.md) 分三段学习，每段读完就动手。各段学习指南包含原文定位、图例、暂停题与折叠核对说明；先自行作答，再检查理由和运行结果。AI 理解提示词可以跳过，完成要求不依赖 AI 评价。

学习指南已整理：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md)。[本次资料复核](refresh-2026-10-01.md) 已完成；学习未开始，实际开始学习日仍按更新流程复查。

| 学习段 | 指定范围 | 读后立即做 | 资料预算 |
| --- | --- | --- | --- |
| 1. Triton 数据块 | CS336 L6 triton_introduction；Vector Addition | 带 mask 的 Vector Add | 45 分钟 |
| 2. 稳定与融合 | Fused Softmax 的四个指定章节 | Softmax 实现与误差曲线 | 60 分钟 |
| 3. 在线归一化 | Online normalizer §2、§3、§3.1 | 两块状态合并验证 | 45 分钟 |

原文选读共 150 分钟，本地图解与自查另计 60 分钟。材料元信息统一在资源索引；可选拓展另排时间。

## 遇到问题再看

安装或接口有差异时，回 [Triton 资源卡](../../resources/README.md#r-triton) 与实际安装版本核对；不读编译器内部实现。

## 实践任务

建议目录：labs/03-triton-attention/softmax/。

1. 完成 Triton Vector Add 热身后实现 Fused Softmax。
2. 测普通数值、大幅值输入、非 2 的幂列宽；记录误差与容差。
3. 比较朴素 PyTorch 表达式、torch.softmax 与 Triton，固定相同输入和 dtype。
4. 推导两块在线状态的合并：新最大值取两者较大值，原归一化因子按最大值变化重新缩放。
5. 扫描列宽，指出资源限制和不支持的输入，不照搬教程的加速比。

## 验收

- [ ] 正确处理 mask 和稳定性；对不支持的形状有明确说明。
- [ ] 能手算在线最大值与归一化因子的更新。
- [ ] 曲线包含可信库基线和原始计时。
- [ ] 能解释融合节省的数据搬运，以及何时未观察到收益。

可选：完成基础后，从补充阅读选一个实际问题写进报告；未选不影响本单元完成。

## 实验记录

实验与报告：尚未创建。自评与验收日期：待完成。

[上一单元](../week-04-gemm/README.md) · [下一单元](../week-06-attention/README.md)
