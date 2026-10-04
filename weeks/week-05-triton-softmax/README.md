# 单元 W5：Triton 与 Online Softmax

[课程目录](../../course/README.md) · [我的进度](../../course/progress.md) · [环境准备](../../course/environment.md)

预计 10～18 小时用于本单元，变式与排错另留 1～3 小时；桥接只计新发生的时间。按实际掌握推进，记录规则见 [学习方法](../../course/guide.md#time-budget)。

## 这一单元要弄清什么

一行数先取指数再除以总和，看似简单，却可能因为大数溢出而失败；行被分成多块后，也不能把各块概率直接相加。你会用 Triton 实现稳定的行 Softmax，再手算分块最大值与指数和怎样合并，理解融合究竟省掉了哪些中间数据。

## 开始前

完成 W4，先做 [M2 指数与 Softmax 诊断](../../course/prerequisites.md)。试算 softmax([0, ln 3])，说明同时减去一个常数为什么不改变概率。广播、类型与 mask 在第一段结合代码补齐。

<details>
<summary>先解释，再展开核对</summary>

结果为 [1/4, 3/4]；同时减一个常数不改变比例，减最大值限制指数范围。

</details>

## 按顺序学习

- [W5 第 1 段：一个 program 负责多少数据？](session-01.md)。
- [W5 第 2 段：减最大值与融合，各解决什么问题？](session-02.md)。
- [W5 第 3 段：只保存两个数，怎样合并不同块的分母？](session-03.md)。

- [本单元掌握检查](assessment.md)：实验完成要求、变式与排错题。

## 实践任务

建议目录：labs/03-triton-attention/softmax/。

1. 完成 Triton Vector Add 热身后实现 Fused Softmax。
2. 测普通数值、大幅值输入、非 2 的幂列宽；记录误差与容差。
3. 比较朴素 PyTorch 表达式、torch.softmax 与 Triton，固定相同输入和 dtype。
4. 推导两块在线状态的合并：新最大值取两者较大值，原归一化因子按最大值变化重新缩放。
5. 扫描列宽，指出资源限制和不支持的输入，不照搬教程的加速比。

## 按需回看

安装或接口有差异时，回 [Triton 资源卡](../../resources/gpu.md#r-triton) 与实际安装版本核对；不读编译器内部实现。

[上一单元](../week-04-gemm/README.md) · [下一步](../week-06-attention/README.md)
