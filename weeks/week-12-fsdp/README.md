# 单元 W12：FSDP2、ZeRO 与恢复

[总路线](../../README.md) · [学习方式](../../docs/learning-workflow.md) · [资源索引](../../resources/README.md) · [当前做法与相关进展](context.md)

建议学习位置：第 13 个学习周。W12 是固定单元 ID，按下方导航推进。

状态：未开始。预算：先按 9 小时起步，可分两次完成。环境：Linux 服务器，主线使用 2 卡。

## 本周要解决什么

理解参数、梯度与优化器状态的分片，以及显存节省、通信和恢复之间的权衡。

先修：W11 DDP 有可信基线。要回答：FSDP2 在什么时机收集和释放参数？ZeRO 的分片对象是什么？checkpoint 是否真的恢复了训练状态？

## 按顺序学习

先用30分钟看 [本周补充阅读](context.md)，按 [更新流程](../../docs/weekly-refresh.md) 核对资料。时间从原报告时段划出，总预算不变。

按 [章节导学](study-guide.md) 分三段学习，每段读完就动手。下面只列安排，具体链接、阅读位置和检查方法都在导学里。

| 学习段 | 指定范围 | 读后立即做 | 资料预算 |
| --- | --- | --- | --- |
| 1. 训练状态 | ZeRO §3.1～3.2、§5.1～5.3 | DDP/分片状态账本 | 45 分钟 |
| 2. 分片时序 | FSDP2 初始化与 Forward/Backward with Prefetching | 2 卡 DDP/FSDP2 对照 | 60 分钟 |
| 3. 恢复验证 | FSDP2 State Dict；DCP Saving/Loading | 连续/恢复路径比较 | 45 分钟 |

阅读共150分钟，包含视频、教程和论文。补充材料按需替换阅读内容；选修另排时间。

## 遇到问题再看

视频沿用 [CS336 2026 播放列表](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV) 的并行主题。ZeRO 是理解分片的材料，不能把论文阶段与任意框架 API 无条件视为一一对应。

## 实践任务

建议目录：labs/06-training/fsdp2/；整合 projects/distributed-training-lab/。

1. 保持W11模型、全局 batch、精度和优化器不变，比较 DDP 与 FSDP2。
2. 在包含 optimizer step 的完整训练步骤中测峰值显存和稳态吞吐；注明 allocated/reserved 的口径。
3. 画前向与反向中的参数聚合、梯度通信位置，联系W7基线解释成本。
4. 保存模型、优化器、步数及必要的 RNG/数据进度，重启后恢复。
5. 在小型确定性配置下比较“连续训练”和“中断恢复”后的下一步 loss/参数。

任务 1～3 完成分片对照，任务 4～5 完成恢复验证。基础范围限定为相同 world size、相同模型与依赖环境；跨卡数恢复、offload 和 activation checkpointing 留作扩展。先前已验证的单卡 checkpoint 经验可以复用，但不能代替本周的分片状态恢复检查。

## 验收

- [ ] 明确使用 FSDP2 fully_shard，版本与教程匹配。
- [ ] 显存比较涵盖同样训练状态，DDP OOM 时单独标记，另找双方都能运行的公平配置。
- [ ] 恢复检查验证优化器和训练进度，而非只证明权重能加载。
- [ ] 报告解释省显存的代价；小模型无加速也属于有效结果。
- [ ] 按补充阅读的要求，在报告中解释一个实际使用问题，注明哪些结论还没验证。

## 实验记录

实验与报告：尚未创建。自评与验收日期：待完成。

[上一单元](../week-11-ddp/README.md) · [下一单元](../week-14-parallelism/README.md)
