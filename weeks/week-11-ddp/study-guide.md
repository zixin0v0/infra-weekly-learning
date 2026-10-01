# W11 分段学习指南：从单卡更新到 DDP 扩展性

[本周范围与验收](README.md) · [自学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

原文选读预算：45 + 60 + 45 = 150 分钟；本地例子与自查另计 90 分钟，动手与正确性检查 300 分钟。含资料复核、分析和报告，本单元约 12 小时，详见 [时间表](../../docs/study-guide.md#time-budget)。

## 学习目标与前置检查

本单元知识点：样本划分、平均梯度、全局 batch、精度、输入等待。学完应当能核对 1/2 卡一次更新，保持更新语义一致，并解释扩展性和状态大小。

**开始前检查**：通过 W7 的 2 卡 collective；完成先修 D/M3，能自己跑完单卡前向、backward、step 与保存恢复。 缺项按 [基础补学入口](../../docs/prerequisites.md) 的材料、范围和练习完成；补学时间另计。

<details>
<summary>前置问题核对</summary>

先修标量例子 w=1、loss=(2w−6)² 的梯度是 −16；不会推导或恢复单卡状态时，先完成先修 D。

</details>

资源的难度、语言、前置要求、原始 URL 和停止位置统一保存在 [资源索引](../../resources/README.md)，下文按学习顺序链接。先读必读范围，卡点材料替换复习时间，可选拓展不影响基础完成。

## 1. 给进程、设备和样本各确定归属（45 分钟）

资源定位：[rank、模型副本与样本归属](../../resources/README.md#r-ddp-start)。

**先看/读**：[PyTorch Multi GPU training with DDP](../../resources/README.md#r-ddp-start) 的嵌入视频，配页面 `Constructing the process group`、`Constructing the DDP model`、`Distributing input data`。三个标题是页面定位，不是已核验的视频时间点。

**接着想一想**：将 W7 的 rank 图接到训练数据，明确每个进程使用的设备、样本和模型副本。检查 `DistributedSampler` 及 `set_epoch()` 的角色；主线选样本数可整除的确定性数据，避免补齐样本改变比较口径。

**例子与图解：样本和模型副本**

~~~text
同一个全局 batch [0,1,2,3]
rank 0：样本 [0,2] → 模型副本 → 本地平均梯度
rank 1：样本 [1,3] → 模型副本 → 本地平均梯度
                  ↓ 同步平均后，双方 optimizer.step()
~~~

**暂停题**：单卡 batch=4、两卡每卡 batch=4，这是不是固定全局 batch？DistributedSampler 的 set_epoch 用来做什么？

<details>
<summary>核对依据</summary>

不是。累积步数为 1 时，全局 batch=卡数×每卡 batch；两卡每卡应为 2。set_epoch 让 sampler 在后续 epoch 使用相应的随机排序，不能替代样本 ID 检查。首先选能整除的数据大小、固定初始化与样本集合；日志核对无意外重复/遗漏，再比较参数更新。

</details>

**动手练习**：让 2 个 rank 打印或保存样本 ID，核对没有非预期重复/遗漏；复用同一个初始化和数据生成方式运行单卡参考。

**检查结果**：模型更新前的状态与全局实际样本集合明确，不以“两个进程都启动了”作为 DDP 正确性证明。

## 2. 把同步放到训练步骤的时间线上（60 分钟）

资源定位：[梯度同步和公平更新](../../resources/README.md#r-ddp)。

**先读**：[DDP 入门](../../resources/README.md#r-ddp) 的 `Basic Use Case`、`Skewed Processing Speeds`、`Save and Load Checkpoints`；主线不读与模型并行组合的示例。

**接着想一想**：以 W7 的 AllReduce 数据量和 W1 参数账本估算梯度通信规模，再用 W6 的时间线方法检查实际同步位置。

**例子与自查：DDP 平均的是哪一个梯度**

用标量模型 ŷ=w×x，loss=(ŷ−y)²，w=0，SGD 学习率 0.1。rank0 仅有 (x=1,y=1)，rank1 仅有 (x=3,y=3)。先手算两份梯度、平均梯度与一步后的 w。

<details>
<summary>核对推导</summary>

梯度为 2(wx−y)x：rank0 得 −2，rank1 得 −18；两者平均 −10，更新后 w=0−0.1×(−10)=1。单卡对同两样本取平均 loss 得到同一梯度。该推导要求各 rank 样本数相等、loss reduction 和累积缩放一致；不同样本数的“本地均值再平均”不自动等于全局样本均值。DDP 的默认梯度同步处理平均；不能再手动除一次 world size。

</details>

**动手练习**：先固定累积步数为 1，用 microbatch 调整保持全局 batch 不变；比较 1/2 卡的一次更新、稳态 step time、吞吐和峰值显存。若增加累积，必须另查所用版本的 `no_sync` 与 loss 缩放规则，不能沿用未经核对的假设。

**检查结果**：loss/参数差异在规定容差内；比较处理的样本数、计时边界一致，解释小模型通信开销可能占主导。

## 3. 将精度与输入路径从卡数变量中分离（45 分钟）

资源定位：[精度与输入路径的分离](../../resources/README.md#r-amp)。

**先读**：[AMP recipe](../../resources/README.md#r-amp) 的 `Adding torch.autocast`、`Adding GradScaler`、`All together`，约 30 分钟。理解操作精度和梯度缩放，FP16/BF16 的实际选择须与支持情况匹配。

**配合阅读**：[Performance Tuning Guide](../../resources/README.md#r-amp) 的 `Enable asynchronous data loading and augmentation`，约 15 分钟，只查 `num_workers`、`pin_memory` 的作用。

**暂停题与状态自查**

1024 个 FP32 参数，用普通 FP32 Adam（不启用混合精度或额外副本），完整 step 后参数、梯度、两个逐参数状态各有多少字节？把 pin_memory 打开是否证明输入等待消失？

<details>
<summary>核对答案</summary>

每份 1024×4=4096 字节，四份合计 16384 字节，未计优化器步数标量、激活、临时空间和分配器开销。此例仅是状态账本，不是峰值显存。pin_memory 提供锁页内存条件，实际拷贝、重叠与等待需时间线验证；num_workers 也可能带来额外开销。先交付 FP32 基线；AMP 和输入路径对照属于独立扩展，不能混进卡数变化。

</details>

**动手练习**：主线先列参数、梯度、优化器状态的 dtype 表，并给计时区间画边界。验收后有余力再二选一：做数值验证后的 AMP 对照，或在有输入等待证据时比较预备数据与 DataLoader 路径。

**完成后检查**：读过 AMP 不算完成 AMP 实验；明确哪些为 FP32 基线、哪些扩展未做。状态账本交给 W12。

## 独立完成与可选 AI 帮助

三段都先遮住答案作答，再核对推导；答错保留原答案，回资源卡指定小节，用不同输入重做。每段“检查结果”连同 [单元完成标准](README.md) 都需要真实笔记或运行记录支持。纸面例子正确只能说明该例的理解，不能替代实验。记录在本单元实验目录的 notes.md，按 W11-S01～S03 分节。

可选提示词：

> 我正在学习 W11 的样本划分。我的推导是【粘贴】，我与本段核对说明不同的一步是【填写】。请只用本段的小例子检查这一步，给一个改变单项条件的反例，先让我回答。不要假设我做过实验，也不要用未核验的接口填补解释。

## 整理记录与可选拓展

在 `labs/06-training/ddp-scaling/` 保存样本核对、参数更新比较、1/2 卡结果和通信解释，逐步整理 `projects/distributed-training-lab/`。

进阶选择 4 卡或梯度累积之一；多机、通信 hook 与输入流水线全面调优后置。
