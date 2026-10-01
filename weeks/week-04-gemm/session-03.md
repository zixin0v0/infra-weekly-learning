# W4 第三段备课：Roofline 预测与库基线

[单元范围](README.md) · [三段导学](study-guide.md) · [资料复核](refresh-2026-10-01.md) · [上一段](session-02.md)

备课日期：2026-10-01。资料预算：45 分钟。状态：备课已准备；性能数据待测。

## 目标与先修

先写计算与搬运假设，再用同精度的三组实现检查预测。先通过朴素/tile GEMM 的正确性与边界。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 15 分钟 | [CS336 L2 视频](https://www.youtube.com/watch?v=kuYAsz7zspQ)，配 [固定讲义](https://github.com/stanford-cs336/lectures/blob/6ff836dd5dfcbe7e848fe1a1734f1886f1116a7a/lecture_02.py) 的 arithmetic_intensity_matmul、roofline_plots | 两个定位函数结束 |
| 20 分钟 | [Scaling Book Roofline](https://jax-ml.github.io/scaling-book/roofline/) 的 Visualizing rooflines、Matrix multiplication | 矩阵计算模型结束；不照搬书中设备数字 |
| 10 分钟 | 用当前 GEMM 写 FLOPs、字节、算术强度 | 各量单位和搬运假设完整即停 |

访问日：2026-10-01。视频时间轴未核验，使用讲义函数定位。

## 中文助读

采用每乘加 2 FLOPs 的约定，GEMM 为 2MNK FLOPs。若每个输入只读一次、输出写一次、C 不需要先读，理想搬运下界为元素字节数×(MK+KN+MN)。这是假设下界，不是实际 DRAM 计数。

算术强度 AI=FLOPs/字节；理想吞吐上界为 min(同精度计算上限, 带宽×AI)。教学朴素实现的逻辑重复加载和缓存实际事务不同，需分别说明。设备峰值、持续带宽与 TF32/FP32 路径不能混用。

## 暂停题与预测

1. M=N=K=16、FP32 时，按上述下界计算 FLOPs、字节与 AI。改变 batch 或 reuse 假设为什么会改变 AI？
2. tile 版本没有比库快，是否说明复用原理错误？如果库允许 TF32，而手写使用 FP32，能否把全部速度差归因于 tile？

先写量纲，再区分模型下界与实测事务，最后回 Roofline 两标题。

## 动手与检查

继续 `labs/02-cuda/gemm/`，加入同输入的 `torch.matmul` 基线。记录实际 dtype、TF32/精度策略、布局、输出分配与同步范围；可比较的数值语义先通过误差检查。

选小/中/大方阵和一个长方形，提前检查显存容量；三组无 profiler 预热、重复测量，保留原始延迟与由同一 FLOPs 口径计算的吞吐。分别列理想下界和实现搬运估计，未知缓存或 Tensor Core 路径写待验证。只对一个代表形状采样已有 W3 sections。

<details>
<summary>先预测，再核对纸面值</summary>

16³×2=8192 FLOPs；4×(256+256+256)=3072 字节；AI≈2.67 FLOPs/B。它们是给定假设的推导，不是设备测量。

</details>

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| AI 与图差很大 | Matrix multiplication 与自己的字节公式 | 是否重复读、是否计 C 初值 |
| 速度与误差同时变 | 自己的精度配置 | 是否改变了计算模式 |

- [ ] 三组正确性与计时条件可比较。
- [ ] 原始数据、预测与实测图可追溯。
- [ ] 区分模型、观察和机制推断。

在 `notes.md` 的 `W4-S03` 整理 [周报告](README.md)，通过后进入 [W5](../week-05-triton-softmax/session-01.md)。
