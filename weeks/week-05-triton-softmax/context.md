# W5 补充阅读：融合、持久化与资源约束

[范围与验收](README.md) · [三段学习导航](study-guide.md) · [更新流程](../../docs/weekly-refresh.md) · [来源登记](../../resources/frontier-watchlist.md#s05)

资料快照：2026-10-01。[学习资料复核已完成](refresh-2026-10-01.md)，实际开始学习日仍须复查。本地状态：仅阅读，相关实现尚未运行。

本页为基础学习后的可选拓展，另排时间；不作为本单元开始或完成条件。开始学习前的 30 分钟用于核对必读材料，若决定选读本页，再核对其来源与支持条件。

## 现在怎样做

用 PyTorch softmax 作语义参考，完成稳定的 Triton fused softmax 与 online 合并。融合收益必须来自减少搬运或启动等可解释机制；同时检查行宽、mask、数值稳定与资源占用。

## 这一方向还有哪些进展

让有限数量的 program 持续处理多个 tile，进一步控制调度与复用。把它当作 program 生命周期的延伸概念，不把持久化、融合和自动加速画等号。

**读哪里**：[Triton Persistent Matmul](https://triton-lang.org/main/getting-started/tutorials/09-persistent-matmul.html)。教程开头的变体概览；对照 matmul_kernel 和 matmul_kernel_persistent 的 program/tile 分工；先看硬件能力判断再读 TMA 或 warp specialization 变体。

**目前的状态**：官方进阶教程，不是本周 softmax 的可直接替换实现；各变体能力要求不同。

**设备条件**：普通路径与 TMA/架构专属变体分别判断。当前只阅读调度部分，不要求在 4090 上运行教程全部模式。

## 真正用起来，还要考虑什么

kernel 的参数最优点可能随行宽、dtype 和版本变化；寄存器或共享内存压力可能抵消减少启动的收益，自动调优也有首次成本。

**选读后可写进报告**：沿用 softmax 的一张性能曲线，选一个收益缩小的输入，用资源/启动/访存提出可检验解释；在报告说明 persistent matmul 为什么不能直接证明 softmax 也会更快。

## 下次更新时

核对教程函数名、能力判断与 Triton 版本；未来版本改变调度时，仅更新这一阅读片段。更新写入 [学习资料复核记录](../../templates/weekly-refresh.md)，保留旧实验的配置。
