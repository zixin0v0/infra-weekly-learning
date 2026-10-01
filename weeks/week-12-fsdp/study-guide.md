# W12 章节导学：分片状态与可信恢复

[本周范围与验收](README.md) · [导学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

资料预算：45 + 60 + 45 = 150 分钟。实现可分两次：先完成分片对照，再完成恢复。第二次未做时不标为整周完成。

## 1. 省掉的具体是哪一份状态（45 分钟）

**先读**：[ZeRO PDF](https://arxiv.org/pdf/1910.02054)，本轮 v3：§3.1 模型状态、§3.2 其余内存，随后 §5.1～5.3 的三类分片。先不读 offload、激活重计算及大规模实验。

**接着想一想**：用 W11 的真实 dtype 表替换论文中的特定精度假设，分别估算参数、梯度和优化器状态；再列激活、临时通信缓冲等没有被该简化公式覆盖的项。

**动手练习**：给相同模型画 DDP 与理想分片状态表，写出随 world size 变化的部分和不会自动按卡数缩小的部分。

**检查结果**：不把论文的某个固定“每参数字节数”当作所有配置通用值，也不把 ZeRO 阶段与框架 API 机械等同。

## 2. 把状态账本对应到 fully_shard 的时序（60 分钟）

**先读**：[FSDP2 教程](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) 的 `How to use FSDP2 → Model Initialization`、`Forward/Backward with Prefetching`。本周精度先沿用 DDP；Mixed Precision 章节按需再看。

**接着想一想**：在一张前向/反向图上标参数聚合和梯度通信，结合 W7 解释数据量和等待。教程预取用于理解时序，不要求把所有预取参数都调一遍。

**动手练习**：保持 W11 的模型、精度、优化器和全局 batch，在 2 卡上比较 DDP/FSDP2；包含完整 optimizer step 后的状态，测稳态吞吐和峰值显存。

**检查结果**：正确性与测量范围一致；DDP OOM 的配置单列，另选双方可运行的配置比较速度。

## 3. 权重能加载为什么还不等于训练可恢复（45 分钟）

**先读**：FSDP2 教程的 `State Dict with DCP APIs`，再联读 [DCP 教程](https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html) 的 `How DCP works`、`Saving`、`Loading`，追踪 `get_state_dict` / `set_state_dict` 的状态处理。

**接着想一想**：DCP 页面中的具体模型包装示例需要与 FSDP2 教程核对，不把旧 `FSDP` 包装器直接混入 `fully_shard` 代码。模型和优化器之外的步数、RNG 和数据进度需要明确保存方案。

**动手练习**：确定性小配置运行两条路径：连续训练，与中断后重启恢复；比较恢复后的下一步 loss/参数。保持 world size 和依赖环境相同。

**完成后检查**：恢复验证涵盖优化器与训练进度，报告里能找到状态清单及比较结果。

## 课后整理与选修

在 `labs/06-training/fsdp2/` 保存状态账本、DDP/FSDP2 对照和恢复验证记录；关联训练项目，不复制 W11 的数据与测量实现。

进阶只选跨 world size 恢复或 activation checkpointing，分别另设正确性和性能检查，不能与主线结果混报。
