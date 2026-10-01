# W5 第二段备课：数值稳定与算子融合

[单元范围](README.md) · [三段导学](study-guide.md) · [资料复核](refresh-2026-10-01.md) · [上一段](session-01.md)

备课日期：2026-10-01。资料预算：60 分钟。状态：备课已准备；正确性与性能待测。

## 目标与先修

分别解释减最大值和融合解决的问题，写出可检查的逐行 Softmax。先通过本周 program/mask 热身和 W3 的归约理解。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 20 分钟 | [Fused Softmax](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html) 的 Motivations、naive_softmax | 中间 Tensor 与逻辑读写比较结束 |
| 25 分钟 | 同页 Compute Kernel 的 softmax_kernel 与封装 | 行内 max/sum、padding、资源条件；启动优化只辨认 |
| 15 分钟 | 同页 Unit Test、Benchmark | 误差与比较边界；不照搬加速比 |

访问日：2026-10-01；[对应源码快照](https://github.com/triton-lang/triton/blob/aad2a60d958f945420c5c40936b37d411fb02e89/python/tutorials/02-fused-softmax.py)。主线一行需适合 kernel 的资源约束，不能宣称任意宽度支持。

## 中文助读

稳定 Softmax 是 exp(x−max)/sum(exp(x−max))；减同一最大值不改变数学归一化结果，却降低指数溢出风险。融合让 max、减法、exp、sum、除法尽量在一次 kernel 内完成，减少中间 Tensor 搬运。

非 2 的幂列宽需要 padding；无效位置用 −∞ 参与 max/exp，使 exp 为 0，再用有效 mask 写回。只检查每行和为 1 仍可能漏掉列顺序或元素值错误。

## 暂停题与预测

1. [1000,1001] 直接求 exp 与先减最大值有什么区别？输出相加应为什么，哪个元素较大？
2. 列宽 5 补到 8，若把 padding 填 0，会怎样影响全为负数的有效输入？

先解释共同平移，再列 padding 的 max 与 exp，最后回 softmax_kernel。

## 动手与检查

继续 `labs/03-triton-attention/softmax/`，动手时写 `softmax.py`，比较稳定朴素表达式、`torch.softmax` 与 Triton。固定 FP32 与行布局，测试列宽 1、5、33、128，以及若干行数；输入含全负数和大幅值，主线不包含全行 −∞ 或 NaN 等特殊语义。

检查逐元素最大误差与行和，先设容差再运行；资源不支持的宽度如实拒绝或单列，不悄悄删点。正确性通过后保持相同分配/同步边界，预热与重复测量；教程已有启动策略按版本记录，不要求自主调优全部策略。

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 行和对但输出错 | Unit Test、逐元素参考 | 列顺序与 mask |
| 宽行报错或变慢 | Compute Kernel 的资源/启动说明 | 支持范围与实际配置 |

- [ ] 稳定性与融合收益分别解释。
- [ ] 普通、大幅值、非整齐宽度对齐。
- [ ] 同语义曲线、原始数据和不支持项齐全。

在 `notes.md` 的 `W5-S02` 留下预测、命令与局限；通过后进入 [第三段](session-03.md)。
