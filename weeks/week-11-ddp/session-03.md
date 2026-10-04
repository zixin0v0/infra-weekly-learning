# W11 第 3 段：卡数、精度和取数方式，怎样分开比较？

[本单元](README.md) · [课程目录](../../course/README.md)

从一张卡换成两张卡时，同时开 AMP、换 DataLoader 参数，会让性能变化无法解释。先固定 FP32 的训练语义，再单独观察输入等待与可选的精度变化。

## 视频与正文

主要阅读下列正文与图解。视频范围待核验；已看懂的重复内容只需回查。

## 开始前

先完成一次参数更新对齐；输入样本和 batch 形状用 [S4](../../course/bridges/s04.md) 的同一数据检查。

资源定位：[精度与输入路径的分离](../../resources/training.md#r-amp)。

**先读**：[AMP recipe](../../resources/training.md#r-amp) 的 `Adding torch.autocast`、`Adding GradScaler`、`All together`，约 30 分钟。理解操作精度和梯度缩放，FP16/BF16 的实际选择须与支持情况匹配。

**配合阅读**：[Performance Tuning Guide](../../resources/training.md#r-amp) 的 `Enable asynchronous data loading and augmentation`，约 15 分钟，只查 `num_workers`、`pin_memory` 的作用。

## autocast 与梯度缩放各自改变什么？

先回 [W1 的范围、精度与容差](../week-01-foundations/session-04.md) 和 [W6 的状态寿命](../week-06-attention/session-04.md)。`autocast` 按受支持的运算选择计算 dtype，不是把整个模型永久转为 FP16。把前向与 loss 放在上下文中，退出后做 backward；梯度对应前向选择的计算路径。模型主参数与 Adam 统计常仍为 FP32，应实际打印确认。

FP16 的小梯度可能在表示时变成零。梯度缩放先把 loss 乘尺度，让反向中间梯度更容易表示；更新前再还原梯度尺度，并检查 inf/NaN，发现异常时可能跳过更新并调整尺度。`GradScaler` 不是把所有结果变精确的工具，也不能修复输入或前向已经产生的 NaN。BF16 的范围较大，通常不需要同样的 FP16 缩放策略，但有效数字更少；是否可用、哪些运算支持，要查设备和安装版本。

**先自己解释**：权重是 FP32、某个 Linear 输出是 FP16，能否说整个训练状态已经减半？把已溢出的 FP16 输出再转 FP32，能否恢复正确值？

<details><summary>核对精度角色</summary>

不能。要分别记录参数、激活、梯度、优化器状态和临时空间；autocast 的运算选择不等于统一存储转换。inf 转为 FP32 仍是 inf，应从溢出的运算和 dtype 开始排查。AMP 概念与状态表必学；数值/性能对照仍是选做，不影响原有 FP32/DDP 必做范围。

</details>

## 状态占用和输入等待，是两条不同的线

普通 FP32 Adam 除参数外，还保存梯度与两个逐参数状态。先列每份数据的 dtype、元素数与生命周期，才能算出状态账本。**混合精度（AMP）**会影响部分操作与状态的精度，不能继续把固定“每参数字节数”套到所有配置上。

另一个问题是 GPU 是否拿得到下一批数据。复用 [S4 的数据流水图](../../course/bridges/s04.md)，比较预备数据与 DataLoader 路径，观察等待发生在哪里。开启锁页内存或多 worker 只提供条件，是否重叠、是否更快仍看实际时间线。本单元的输入对照必做，AMP 实验在 FP32 基础通过后选做。

**暂停题与状态自查**

1024 个 FP32 参数，用普通 FP32 Adam（不启用混合精度或额外副本），完整 step 后参数、梯度、两个逐参数状态各有多少字节？把 pin_memory 打开是否证明输入等待消失？

<details>
<summary>核对答案</summary>

每份 1024×4=4096 字节，四份合计 16384 字节，未计优化器步数标量、激活、临时空间和分配器开销。此例仅是状态账本，不是峰值显存。pin_memory 提供锁页内存条件，实际拷贝、重叠与等待需时间线验证；num_workers 也可能带来额外开销。先交付 FP32 基线；S4 输入等待对照是独立的必做检查，AMP 实验选做，二者都不能混进卡数变化。

</details>

**动手练习**：先列参数、梯度、优化器状态的 dtype 表，并给计时区间画边界。复用 S4 的同一 Dataset/训练循环完成输入等待、num_workers 对照，保存样本与时序证据；GPU 条件就绪后比较预备数据与 DataLoader 端到端路径。AMP 的数值/时间/显存对照在基础通过后选做。

**完成后检查**：读过 AMP 不算完成 AMP 实验；明确哪些为 FP32 基线、哪些扩展未做。状态账本交给 W12。

## 整理记录与可选拓展

在 `labs/06-training/ddp-scaling/` 保存样本核对、参数更新比较、1/2 卡结果和通信解释，逐步整理 `projects/distributed-training-lab/`。

进阶选择 4 卡或梯度累积之一；多机、通信 hook 与输入流水线全面调优后置。

## 完成后

把代码、预测与实际结果记在同一份笔记中。完成本段检查后，沿下方链接继续。

[上一课](session-02.md) · [下一课](assessment.md)
