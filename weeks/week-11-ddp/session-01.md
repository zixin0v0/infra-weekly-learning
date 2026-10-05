# W11 第 1 段：两张卡，是否真的看了同一个全局 batch？

[本单元](README.md) · [课程目录](../../course/README.md)

数据并行复制模型，再把样本分给不同进程。如果每张卡都读了全部样本，或改卡数时无意改变全局 batch，两个训练结果就不再回答同一个问题。

## 视频与正文

先看 [PyTorch · Multi GPU training with DDP](https://docs.pytorch.org/tutorials/beginner/ddp_series_multigpu.html)：process group、DDP 包装与 DistributedSampler；每一步暂停说明 rank、设备和样本的归属。

视频分钟位置待核验；下列章节或函数用于正文定位，也可以直接按正文完成练习。

## 中文补充（按需）

李沐中文[多 GPU 训练](https://www.bilibili.com/video/BV1vU4y1V7rd/)与作者[§12.5.2 数据并行](https://zh.d2l.ai/chapter_computational-performance/multiple-gpus.html)，可先看每卡复制模型、拆分 batch、汇总梯度和更新的顺序。正文已预读，视频仅讲次确认；这是同主题讲解，书中手动分发不是 DDP。rank/LOCAL_RANK 与 DistributedSampler 仍按原课设置，不能把扩大 global batch 的性能做法带入正确性比较。[范围与版本](../../resources/training.md#cn-data-parallel)。

## 开始前

先完成 [单卡训练 D](../../course/prerequisites.md)、[数据输入 S4](../../course/bridges/s04.md) 和 W7 两卡集合通信；能独立做 forward、backward、step 与恢复。

资源定位：[rank、模型副本与样本归属](../../resources/training.md#r-ddp-start)。

**先看/读**：[PyTorch Multi GPU training with DDP](../../resources/training.md#r-ddp-start) 的嵌入视频，配页面 `Constructing the process group`、`Constructing the DDP model`、`Distributing input data`。三个标题是页面定位，不是已核验的视频时间点。

**接着想一想**：将 W7 的 rank 图接到训练数据，明确每个进程使用的设备、样本和模型副本。检查 `DistributedSampler` 及 `set_epoch()` 的角色；先选样本数可整除的确定性数据，避免补齐样本改变比较口径。

## 分样本，不是让每个进程重复全部样本

**分布式数据并行（DDP）**让各 rank 保存模型副本，用自己的局部 batch 算梯度，再同步以保持更新一致。以全局样本 [0,1,2,3] 为例，可以让 rank 0 读 [0,2]，rank 1 读 [1,3]；样本 ID 的并集和重复情况都应与单卡参考核对。

无梯度累积时，全局 batch 等于 rank 数乘每个 rank 的 batch。单卡 4 个样本改成两卡每卡 4 个，已经把全局 batch 变成 8，不能称为固定工作量的对比。先保存初始化和样本集合，再进入[梯度同步图](session-02.md)。

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

## 完成后

把代码、预测与实际结果记在同一份笔记中。完成本段检查后，沿下方链接继续。

[上一课](README.md) · [下一课](session-02.md)
