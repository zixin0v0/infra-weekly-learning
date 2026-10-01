# W12 补充阅读：状态分片、恢复与容错

[范围与验收](README.md) · [三段导学](study-guide.md) · [更新流程](../../docs/weekly-refresh.md) · [来源登记](../../resources/frontier-watchlist.md#s12)

资料快照：2026-10-01。开课复核：待进行。本地状态：仅阅读，相关实现尚未运行。

开课前用30分钟核对本页资料。这里的练习并入本周报告，额外实现留作选修。

## 现在怎样做

FSDP2 的分片实验和 DCP 同 world size 恢复是主线。模型、优化器、步数、RNG 与数据位置都要纳入恢复语义；保存成功不是恢复正确的证明。

## 这一方向还有哪些进展

把故障处理放进训练运行时，研究副本组、成员变化与训练持续性。它与从持久 checkpoint 恢复有关联，但不是相同的保证。

**读哪里**：[TorchFT 的故障容忍训练](https://github.com/meta-pytorch/torchft)。torchtitan (Fault Tolerant HSDP)、Fault Tolerant DDP、Design 和 Lighthouse 的说明；DiLoCo 只看实验状态与适用边界。

**目前的状态**：官方作者开源实现，部分路径如 LocalSGD/DiLoCo 明确带 experimental 标记；单个故障演示不能推断所有训练配置可用。

**在我们的设备上**：本周只在自己的隔离小实验里保存/恢复，不对共享服务器注入故障，不要求运行 TorchFT。

## 真正用起来，还要考虑什么

工程问题包括恢复时间、丢失多少工作、故障检测、状态一致性和资源回收；同规模恢复不能声称已覆盖弹性或节点故障。

**写进本周报告**：在原恢复报告写明故障模型和未覆盖范围，给出下一步参数/优化器/RNG/数据位置核对证据；再用两列区别当前 checkpoint 恢复与 TorchFT 类运行时容错。

## 下次更新时

复查实验标签、所需框架版本和恢复保证；若计划改变 world size，必须另设计验证，不沿用本周通过状态。更新写入 [开课记录](../../templates/weekly-refresh.md)，保留旧实验的配置。
