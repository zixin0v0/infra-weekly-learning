# W6 补充阅读：Attention 后端与模型语义

[返回本单元](README.md) · [来源登记](../../resources/optional.md#s06)

资料快照：2026-10-01。[学习资料复核已完成](../../docs/audits/2026-10-01-week-06.md)，实际开始学习日仍须复查。本地状态：仅阅读，相关实现尚未运行。

完成本单元后，若想继续了解这个问题，再读下面的指定范围。选读前核对当前版本与设备条件；页面保留 2026-10-01 的来源快照，没有把旧结论重新标为已验证。

## 从已经做过的实验出发

以 PyTorch SDPA 和显式 Attention 对照，保留 causal mask、dtype、dropout 与形状一致性；记录实际后端与回退。模型时间线决定 Attention 是否真是主要热点。

## 接着想清一个问题

在 IO-aware 算法基础上继续利用架构特性与执行流水线。经典 FA 论文仍解释稳定原理，新实现帮助认识算法与硬件协同，不意味着旧论文失去学习价值。

**读哪里**：[FlashAttention-3 / FlashAttention-4](https://github.com/Dao-AILab/flash-attention/blob/616b0e8abab13b87b01525b3916d5a863ab02ae0/README.md)。README 的 FlashAttention-3 beta release、FlashAttention-4 (CuTeDSL)，再回到 NVIDIA CUDA Support 的架构与 dtype 支持说明。

**来源快照中的状态**：README 将 FA3 标为 beta；FA4 使用 CuTe DSL，面向 Hopper/Blackwell 优化。不同代际条目和普通安装入口的支持范围必须分别看。

**设备条件**：规划中的 4090 属于 Ada；不将 H100/B200 路径列作本地必跑，不将 SDPA 成功自动解释为运行 FA4。

## 真正用起来，还要考虑什么

实际模型还存在变长、GQA、mask、dropout、反向与回退覆盖问题；某个 Attention kernel 的收益不一定传递到整个 Block。

**选读后可写进报告**：在原 Block 报告增加后端/支持条件一栏；区分自己已验证的 mask/shape 与未覆盖功能。给出一条保留 SDPA 的理由或需要定制的证据。

## 选读前核对

核验各代支持矩阵、正式/beta 状态与框架集成情况；前沿实现即使更新，也先守住现有语义和 Block 对照。
