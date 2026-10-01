# W7 第一段备课：每个 rank 的输入与输出

[单元范围](README.md) · [三段导学](study-guide.md) · [资料复核](refresh-2026-10-01.md)

备课日期：2026-10-01。资料预算：45 分钟。状态：备课已准备；多卡通信待验证。

## 目标与先修

手算四种 collective，明确 shape、rank 顺序和操作语义。需要 W1～W6 的张量与测量知识，以及运行时可用的至少两张 GPU；W13 不是通信的硬性前置。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 25 分钟 | [NCCL Collective Operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html) 的 AllReduce、Broadcast、AllGather、ReduceScatter | 四类输入输出图结束 |
| 20 分钟 | [CS336 L7 固定讲义](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py) 的 torch_distributed、collective_operations_main，配 [官方视频列表](https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV) 第 7 讲 | collective 例子结束，不进入数据并行训练 |

访问日：2026-10-01；NCCL 文档标 2.32.3，运行版本待选。视频没有已核验时间轴，函数用于讲义定位。

## 中文助读

rank 是进程组中的编号，不自动等于物理 GPU 编号。AllReduce 对应位置归约后每 rank 获得完整结果；Broadcast 从 root 复制；AllGather 按 rank 顺序拼接；ReduceScatter 先归约再按 rank 切分。

对 rank 0=[1,2,3,4]、rank 1=[10,20,30,40]，SUM AllReduce 给双方 [11,22,33,44]，ReduceScatter 给各自两元素区间。通信各端需遵守一致操作、dtype、数量和调用顺序；“各自调用成功”不能代替跨 rank 契约。

## 暂停题与预测

1. 用上述输入写四类操作的全部输出；Broadcast 指定 root=0，AllGather 的输出有几个元素？
2. 两 rank 用不同 collective 顺序，可能产生什么行为？改变卡号是否会自动改变拼接顺序？

先画 rank 输入，再用颜色标来自谁的数据，最后回四类操作图。

## 动手与检查

唯一入口：`labs/04-collectives/allreduce/`。先保存纸面语义表；实际 Linux 两卡环境就绪后，写小型 `collective_semantics.py`，设置进程组、rank 与设备映射，所有 rank 按同序运行。

使用整数可精确表示的小输入或 FP32，逐 rank 核对值和 shape；保存 world size、root、归约类型、版本、完整命令与输出。不直接运行讲义全部大型 launcher。CPU 手算或单进程模拟只证明代数理解，不能标 NCCL 通信通过。

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 把 gather 当求和 | AllGather 与 AllReduce | 元素数与来源 |
| 运行卡住 | 自己的进程组/调用序列 | 每 rank 操作、数量与设备是否匹配 |

- [ ] 四类语义与 rank 顺序独立解释。
- [ ] 实际两卡输出与纸面参考一致。
- [ ] 环境未就绪项不写通过。

在 `notes.md` 的 `W7-S01` 留下预测、命令与限制；通过后进入 [第二段](session-02.md)。
