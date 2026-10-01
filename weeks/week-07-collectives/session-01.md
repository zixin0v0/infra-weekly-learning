# W7 第一段学习指南：每个 rank 的输入与输出

[单元范围](README.md) · [三段学习导航](study-guide.md) · [资料复核](refresh-2026-10-01.md)

整理日期：2026-10-01。原文选读预算：45 分钟。状态：学习指南已整理；多卡通信待验证。

本地图解、暂停题与核对另计入本单元的自查时段，完整时间见 [分项预算](../../docs/study-guide.md#time-budget)。

## 目标与先修

手算四种 collective，明确 shape、rank 顺序和操作语义。需要 W1～W6 的张量与测量知识，以及运行时可用的至少两张 GPU；W13 不是通信的硬性前置。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 25 分钟 | [NCCL Collective Operations](../../resources/README.md#r-collective) 的 AllReduce、Broadcast、AllGather、ReduceScatter | 四类输入输出图结束 |
| 20 分钟 | [CS336 L7 固定讲义](../../resources/README.md#r-l7) 的 torch_distributed、collective_operations_main，配 [官方视频列表](../../resources/README.md#x-navigation) 第 7 讲 | collective 例子结束，不进入数据并行训练 |

访问日：2026-10-01；NCCL 文档标 2.32.3，运行版本待选。视频没有已核验时间轴，函数用于讲义定位。

## 概念说明

rank 是进程组中的编号，不自动等于物理 GPU 编号。AllReduce 对应位置归约后每 rank 获得完整结果；Broadcast 从 root 复制；AllGather 按 rank 顺序拼接；ReduceScatter 先归约再按 rank 切分。

对 rank 0=[1,2,3,4]、rank 1=[10,20,30,40]，SUM AllReduce 给双方 [11,22,33,44]，ReduceScatter 给各自两元素区间。通信各端需遵守一致操作、dtype、数量和调用顺序；“各自调用成功”不能代替各 rank 的一致调用约定。

## 暂停题与预测

1. 用上述输入写四类操作的全部输出；Broadcast 指定 root=0，AllGather 的输出有几个元素？
2. 两 rank 用不同 collective 顺序，可能产生什么行为？改变卡号是否会自动改变拼接顺序？

先画 rank 输入，再用颜色标来自谁的数据，最后回四类操作图。

## 读图与自查

| 操作 | rank 0 的输出 | rank 1 的输出 |
| --- | --- | --- |
| SUM AllReduce | [11,22,33,44] | [11,22,33,44] |
| Broadcast，root=0 | [1,2,3,4] | [1,2,3,4] |
| AllGather | [1,2,3,4,10,20,30,40] | [1,2,3,4,10,20,30,40] |
| SUM ReduceScatter | [11,22] | [33,44] |

这是题中两个输入的手算数据流表，不是 NCCL 实测。先遮住输出列自己填写，再用两种标记区分“来自某个 rank 的原数据”与“逐位置相加的数据”。

<details>
<summary>写下预测后，再核对本段问题</summary>

**题 1**：AllGather 每个 rank 获得 8 个元素；ReduceScatter 每个 rank 获得归约结果的一半。Broadcast 只复制 root 的数据，AllReduce 才做逐位置求和。

**题 2**：不同调用顺序可能造成等待、超时或错误。rank 顺序决定拼接/切片顺序，物理 GPU 号要通过映射解释；换设备不自动更改进程组编号。出现挂起时，先逐 rank 列出 collective、dtype、count、root 和调用序号，不通过反复随机换卡猜测原因。

这些说明用于核对推导；运行结果仍需自己验证。答错时保留原答案，回看本段“读哪里”或“卡点”指向的位置，再换一个小输入重做。

</details>

## 可选：问 AI

先独立作答和核对，仍有疑问时再使用；跳过本节不影响完成本段。

> 这是我手算的四类 collective 输出和 rank 到设备的映射：【粘贴】。请先检查一处元素来源或 shape，再给一个三 rank 的小题让我画。不要把 rank 直接当物理 GPU 号，也不要代写完整分布式程序。

## 动手与检查

实验目录：`labs/04-collectives/allreduce/`。先保存纸面语义表；实际 Linux 两卡环境就绪后，写小型 `collective_semantics.py`，设置进程组、rank 与设备映射，所有 rank 按同序运行。

使用整数可精确表示的小输入或 FP32，逐 rank 核对值和 shape；保存 world size、root、归约类型、版本、完整命令与输出。不直接运行讲义全部大型 launcher。CPU 手算或单进程模拟只证明代数理解，不能标 NCCL 通信通过。

脚本按讲义读取启动器提供的 rank、world size 和 local rank，用 local rank 选择当前可见设备，初始化 NCCL 进程组；各 rank 执行同样的四次 collective 后销毁进程组。在已确认两张可用 GPU 的 Linux 环境，从实验目录启动已写好的脚本：

```bash
torchrun --standalone --nnodes=1 --nproc-per-node=2 collective_semantics.py
```

先让每个进程打印 rank、local rank 和设备，确认映射再检查输出。首次调试只使用本段的小数组，不进入性能扫描；启动参数依据 [PyTorch torchrun 文档](../../resources/README.md#r-collective) 的单机用法。

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 把 gather 当求和 | AllGather 与 AllReduce | 元素数与来源 |
| 运行卡住 | 自己的进程组/调用序列 | 每 rank 操作、数量与设备是否匹配 |

- [ ] 四类语义与 rank 顺序独立解释。
- [ ] 实际两卡输出与纸面参考一致。
- [ ] 环境未就绪项不写通过。

在 `notes.md` 的 `W7-S01` 留下预测、命令与限制；通过后进入 [第二段](session-02.md)。
