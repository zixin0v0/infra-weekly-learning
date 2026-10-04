# 单元 W12：FSDP2、ZeRO 与恢复

[课程目录](../../course/README.md) · [我的进度](../../course/progress.md) · [环境准备](../../course/environment.md)

预计 12～22 小时用于本单元，变式与排错另留 1～3 小时；桥接只计新发生的时间。按实际掌握推进，记录规则见 [学习方法](../../course/guide.md#time-budget)。

## 这一单元要弄清什么

把训练状态分给两张卡之后，为什么计算时仍可能出现显存峰值？先列清参数、梯度和优化器状态，再追踪 FSDP2 的聚合与分片。最后重启训练，比较恢复后的下一批数据和下一次更新，检查 checkpoint 是否保存了继续训练所需的状态。

## 开始前

完成 W11 的一步更新对照，能解释 Adam 状态、step、AllGather 与 ReduceScatter。先修 D 的单卡恢复必须做过。恢复段前完成 [S5 存储与持久化](../../course/bridges/s05.md#s5)，其中会复用 S3 的容器操作。

<details>
<summary>先解释，再展开核对</summary>

仅加载权重不会恢复 Adam 动量、步数和数据位置；先修 D 的连续/恢复对照必须已完成。

</details>

## 按顺序学习

- [S5 存储与持久化，先完成 S3 和单卡训练](../../course/bridges/s05.md)。
- [W12 第 1 段：分片以后，显存到底省了哪几项？](session-01.md)。
- [W12 第 2 段：平时只留分片，执行这一层时怎么办？](session-02.md)。
- [W12 第 3 段：权重一样，为什么恢复后的下一步仍然不同？](session-03.md)。

- [本单元掌握检查](assessment.md)：实验完成要求、变式与排错题。

## 实践任务

建议目录：labs/06-training/fsdp2/；整合 projects/distributed-training-lab/。

1. 保持W11模型、全局 batch、精度和优化器不变，比较 DDP 与 FSDP2。
2. 在包含 optimizer step 的完整训练步骤中测峰值显存和稳态吞吐；注明 allocated/reserved 的口径。
3. 画前向与反向中的参数聚合、梯度通信位置，联系W7基线解释成本。
4. 保存模型、优化器、步数及必要的 RNG/数据进度，重启后恢复。
5. 在小型确定性配置下比较“连续训练”和“中断恢复”后的下一步 loss/参数。

任务 1～3 完成分片对照，任务 4～5 完成恢复验证。基础范围限定为相同 world size、相同模型与依赖环境；跨卡数恢复、offload 和 activation checkpointing 留作扩展。先前已验证的单卡 checkpoint 经验可以复用，但不能代替本周的分片状态恢复检查。

## 按需回看

视频沿用 [CS336 2026 播放列表](../../resources/optional.md#x-navigation) 的并行主题。ZeRO 是理解分片的材料，不能把论文阶段与任意框架 API 无条件视为一一对应。

[上一单元](../week-11-ddp/README.md) · [下一步](../week-14-parallelism/README.md)
