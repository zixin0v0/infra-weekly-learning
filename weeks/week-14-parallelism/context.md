# W14 补充阅读：稠密并行与 MoE 通信

[范围与验收](README.md) · [三段学习导航](study-guide.md) · [更新流程](../../docs/weekly-refresh.md) · [来源登记](../../resources/frontier-watchlist.md#s14)

资料快照：2026-10-01。开始学习复核：待进行。本地状态：仅阅读，相关实现尚未运行。

本页为基础学习后的可选拓展，另排时间；不作为本单元开始或完成条件。开始学习前的 30 分钟用于核对必读材料，若决定选读本页，再核对其来源与支持条件。

## 现在怎样做

先用两层 MLP 解释 DP/TP/PP 的张量与通信语义，再看 Megatron/TorchTitan 的组合方式。CPU shape 模拟能验证代数，真实通信与性能需要另有测量证据。

## 这一方向还有哪些进展

MoE 将 token 路由与 expert 通信变成关键系统问题。它补充 TP/PP 之外的 EP 视角，不替换本周稠密 MLP 的基础推导。

**读哪里**：[DeepEP / DeepEveryParallel](https://github.com/deepseek-ai/DeepEP)。README 开头的 MoE dispatch/combine 说明、Requirements，以及标为 experimental 的扩展原语说明；从 expert token 交换映射到 all-to-all。

**目前的状态**：作者维护的高性能实现；当前要求 Hopper 或更新架构，一些非 EP 扩展仍为 experimental。不要把仓库名称理解成全部并行路径都成熟。

**设备条件**：规划中的 4090 不满足这里所列 Hopper+ 条件；只画通信和不均衡案例，不安装或声称复现 DeepEP 性能。

## 真正用起来，还要考虑什么

真实路由存在负载倾斜、容量约束和拓扑差异；均匀合成 all-to-all 的结果不等于端到端 MoE 收益。

**选读后可写进报告**：复用并行切分图，另画8个 token 分到2个 expert 的均匀/倾斜两种情况，说明 TP 和 EP 为什么不是同一种切分；不新增 MoE 训练项目。

## 下次更新时

查硬件、网络与实验接口条件；只有选定训练系统分支后才把 EP 实验纳入计划。更新写入 [学习资料复核记录](../../templates/weekly-refresh.md)，保留旧实验的配置。
