# W7 补充阅读：通信接口、重叠与拓扑

[返回本单元](README.md) · [来源登记](../../resources/optional.md#s07)

资料快照：2026-10-01。[学习资料复核已完成](../../docs/audits/2026-10-01-week-07.md)，实际开始学习日仍须复查。本地状态：仅阅读，相关实现尚未运行。

完成本单元后，若想继续了解这个问题，再读下面的指定范围。选读前核对当前版本与设备条件；页面保留 2026-10-01 的来源快照，没有把旧结论重新标为已验证。

## 从已经做过的实验出发

先学 host 发起的 NCCL collectives 与 torch.distributed 语义，用 nccl-tests 建立消息大小曲线。rank 数据含义、完成时刻和带宽口径先于复杂通信优化。

## 接着想清一个问题

通信可更紧密地嵌入 GPU 计算过程，研究点转向计算/通信重叠和设备侧协作。它不会消除同步与数据依赖。

**读哪里**：[NCCL Device API](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/deviceapi.html)。页首对 device-side communication 的介绍，以及 LSA、Multimem、GIN、CFT 的说明和条件；不要只读 API 名称。

**来源快照中的状态**：本次文档标 2.32.3：Device API 自 NCCL 2.28 引入，GIN 自 2.28.7 引入，CFT 自 2.31 引入。CFT 要求 Blackwell+、编译 CUDA 13.3+ 及对应驱动；各模块的拓扑、网络与软件条件分别判断，当前 RTX 40 系列规划不进入该路径。

**设备条件**：4 张 GPU 的数量不能证明 P2P、NVLink SHARP 或合适网络存在。先记录实际拓扑，Device API 不作为当前 2 卡基线的先决条件。

## 真正用起来，还要考虑什么

工程上还要面对 rank 卡住、错误传播、超时和拓扑差异。单机均匀通信曲线不能替代多机训练表现。

**选读后可写进报告**：在现有 collective 报告画出计算、发起、完成、消费结果的顺序，指出一处可重叠区段与必须等待的依赖；不增加自定义通信 kernel。

## 选读前核对

查所用 NCCL 版本及 Device API 支持条件；无法验证网络条件时只保留机制分析。
