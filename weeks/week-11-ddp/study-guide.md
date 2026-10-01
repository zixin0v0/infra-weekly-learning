# W11 章节导学：从单卡更新到 DDP 扩展性

[本周范围与验收](README.md) · [导学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

资料预算：45 + 60 + 45 = 150 分钟。先修 D 必须通过；主线 FP32、1/2 卡，AMP 和输入流水线只安排一个可选对照。

## 1. 给进程、设备和样本各确定归属（45 分钟）

**先看/读**：[PyTorch Multi GPU training with DDP](https://docs.pytorch.org/tutorials/beginner/ddp_series_multigpu.html) 的嵌入视频，配页面 `Constructing the process group`、`Constructing the DDP model`、`Distributing input data`。三个标题是页面定位，不是已核验的视频时间点。

**接着想一想**：将 W7 的 rank 图接到训练数据，明确每个进程使用的设备、样本和模型副本。检查 `DistributedSampler` 及 `set_epoch()` 的角色；主线选样本数可整除的确定性数据，避免补齐样本改变比较口径。

**动手练习**：让 2 个 rank 打印或保存样本 ID，核对没有非预期重复/遗漏；复用同一个初始化和数据生成方式运行单卡参考。

**检查结果**：模型更新前的状态与全局实际样本集合明确，不以“两个进程都启动了”作为 DDP 正确性证明。

## 2. 把同步放到训练步骤的时间线上（60 分钟）

**先读**：[DDP 入门](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html) 的 `Basic Use Case`、`Skewed Processing Speeds`、`Save and Load Checkpoints`；主线不读与模型并行组合的示例。

**接着想一想**：以 W7 的 AllReduce 数据量和 W1 参数账本估算梯度通信规模，再用 W6 的时间线方法检查实际同步位置。

**动手练习**：先固定累积步数为 1，用 microbatch 调整保持全局 batch 不变；比较 1/2 卡的一次更新、稳态 step time、吞吐和峰值显存。若增加累积，必须另查所用版本的 `no_sync` 与 loss 缩放规则，不能沿用未经核对的假设。

**检查结果**：loss/参数差异在规定容差内；比较处理的样本数、计时边界一致，解释小模型通信开销可能占主导。

## 3. 将精度与输入路径从卡数变量中分离（45 分钟）

**先读**：[AMP recipe](https://docs.pytorch.org/tutorials/recipes/recipes/amp_recipe.html) 的 `Adding torch.autocast`、`Adding GradScaler`、`All together`，约 30 分钟。理解操作精度和梯度缩放，FP16/BF16 的实际选择须与支持情况匹配。

**配合阅读**：[Performance Tuning Guide](https://docs.pytorch.org/tutorials/recipes/recipes/tuning_guide.html) 的 `Enable asynchronous data loading and augmentation`，约 15 分钟，只查 `num_workers`、`pin_memory` 的作用。

**动手练习**：主线先列参数、梯度、优化器状态的 dtype 表，并给计时区间画边界。验收后有余力再二选一：做数值验证后的 AMP 对照，或在有输入等待证据时比较预备数据与 DataLoader 路径。

**完成后检查**：读过 AMP 不算完成 AMP 实验；明确哪些为 FP32 基线、哪些扩展未做。状态账本交给 W12。

## 课后整理与选修

在 `labs/06-training/ddp-scaling/` 保存样本核对、参数更新比较、1/2 卡结果和通信解释，逐步整理 `projects/distributed-training-lab/`。

进阶选择 4 卡或梯度累积之一；多机、通信 hook 与输入流水线全面调优后置。
