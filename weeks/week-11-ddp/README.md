# 单元 W11：DDP 与训练扩展性

[课程目录](../../course/README.md) · [我的进度](../../course/progress.md) · [环境准备](../../course/environment.md)

预计 12～22 小时用于本单元，变式与排错另留 1～3 小时；桥接只计新发生的时间。按实际掌握推进，记录规则见 [学习方法](../../course/guide.md#time-budget)。

## 这一单元要弄清什么

一张卡处理八个样本，与两张卡各处理四个样本，为什么应该得到相同的一步更新？先核对样本归属和 loss 的平均方式，再观察梯度同步。正确性一致后，才比较增加卡数节省的计算时间，以及额外的数据等待和通信成本。

## 开始前

先完成 [P8](../../course/foundations/p08.md)、[单卡训练的 Adam 恢复检查](../../course/foundations/training.md#resume)、[S4 数据读取与等待](../../course/bridges/s04.md#s4) 和 W7 的两卡通信实验。你应能自己完成前向、backward、step、保存与恢复；W7 的可选 DDP 未做不影响这里按步骤开始。

<details>
<summary>先解释，再展开核对</summary>

先修标量例子 w=1、loss=(2w−6)² 的梯度是 −16；不会推导或恢复单卡状态时，先完成先修 D。

</details>

## 按顺序学习

- [先完成 Adam 下一步恢复](../../course/foundations/training.md#resume)。
- [完成单卡训练后做 S4 数据输入](../../course/bridges/s04.md)。
- [W11 第 1 段：两张卡，是否真的看了同一个全局 batch？](session-01.md)。
- [W11 第 2 段：平均本地梯度，什么时候等于全局平均梯度？](session-02.md)。
- [W11 第 3 段：卡数、精度和取数方式，怎样分开比较？](session-03.md)。

- [本单元掌握检查](assessment.md)：实验完成要求、变式与排错题。

## 实践任务

建议目录：labs/06-training/ddp-scaling/。

1. 选择小型固定模型和可重建的合成数据，先验证单卡 FP32 训练步骤。基础计时使用预先准备的数据，注明是否包含输入搬运。
2. 比较 1、2 卡；记录每卡 microbatch、梯度累积步数，使全局 batch = microbatch × 卡数 × 累积步数保持一致。4 卡单独列为扩展。
3. 确认数据划分与 loss 缩放，避免不同 rank 重复读取全部样本或重复平均梯度。
4. 测量稳态 step time、samples/s 或 tokens/s、峰值显存，并采集一次通信与计算时间线。
5. 比较至少一次更新后的参数或 loss 趋势；如果使用随机层，记录随机性与数值容差。

输入路径与精度分别做单因素对照：S4 的数据加载与等待检查为必做，并在 GPU 环境中比较预先驻留 GPU 的数据与 DataLoader 端到端路径。AMP 的范围/精度、autocast 与梯度缩放概念必学，性能对照选做；先验证数值，再比较时间与显存，不与卡数变化同时引入。记录实际参数、梯度和优化器状态的 dtype；autocast 不代表所有状态都变成相同低精度。

## 按需回看

对照W7的 AllReduce 曲线，判断训练中的通信量是否落在相近区间。需要检查运行语义时优先查官方教程，而不是同时引入新的训练框架。

[上一单元](../week-10-serving-benchmark/README.md) · [下一步](../week-12-fsdp/README.md)
