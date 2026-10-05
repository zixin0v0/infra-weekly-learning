# W6 第 3 段：GPU 的空档，应该去哪里找原因？

[本单元](README.md) · [课程目录](../../course/README.md)

算子表能告诉你某类操作累计用了多少时间，却未必告诉你它为什么迟迟没有开始。把 CPU 提交、设备执行和等待放在同一时间线上，才看得到被平均数藏起来的空档。

## 视频与正文

主要阅读下列正文与图解；视频范围待核验。读到暂停题时，先预测再运行。

沿[Block 数据流图](session-02.md)给 Norm、Attention、MLP 分别标上待测区间。形状不变的残差路径仍可能有内存访问，不能从图中的方框大小判断耗时。

## 目标与先修

用算子表找热点，再用时间线区分执行、拷贝与等待。先让同一个 Block 正确运行；前向是否建立 autograd 图必须明确，backward 留作扩展。

## 读哪里，在哪里停

| 阅读参考 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 25 分钟 | [PyTorch Profiler recipe](../../resources/models.md#r-trace) 的步骤 3、4 | 执行时间与内存表解释结束；不增加 ResNet 实验 |
| 10 分钟 | 同页 export_chrome_trace 示例 | trace 导出方法结束 |
| 25 分钟 | [Nsight Systems User Guide](../../resources/models.md#r-trace) 的 CUDA Trace → Basic CUDA trace、Marking and Labeling Regions | 识别调用/拷贝/kernel 与区段标记后停 |

访问日：2026-10-01。工具覆盖与权限需在实际设备确认；官方示例时间不是本机结果。

## 中文补充（按需）

如果 Block 的组成还不熟，回看《动手学深度学习》[多头注意力 §10.5](https://zh.d2l.ai/chapter_attention-mechanisms/multihead-attention.html)开头到公式 (10.5.2)，停在代码前。作者团队中文说明可帮助你认清各 head 的输入输出；它不覆盖 CPU/kernel/等待时间线，Profiler 仍按本课英文材料读，不能把各层嵌套时间直接相加。[范围与版本](../../resources/models.md#cn-attention)。

## 耗时相加之前，先检查有没有重叠和嵌套

**时间线（timeline）**保留每个事件的起止位置。两个 GPU 操作之间的空档，可能是 CPU 没来得及提交、输入未准备好，或等待其他依赖；它本身不是某个 kernel 内部低效的证据。聚合表把多次事件合在一起，适合找候选热点，却不能单独重建先后关系。

回看 [CPU 与 GPU 的提交关系](../../course/bridges/s01.md)。内存指标也要问“统计了什么”；[第四段](session-04.md) 用训练对象和缓存对照具体解释。

算子表按聚合耗时寻找热点，时间线展示先后和重叠。CPU 等待、提交间隙、拷贝与 GPU kernel 不是一个指标；GPU 有空档不能直接证明某个 kernel 内部效率低。

allocated 是框架当前 Tensor 占用，reserved 包括缓存分配器保留空间，设备占用还可能含其他上下文/进程；三者不能直接相加。峰值测量须说明何时重置、哪些初始化和临时分配被计入。

## 暂停题与预测

1. Attention 单次更快但 Block 延迟不变，先看哪张表、再看时间线的哪段？
2. reserved 大于 allocated 能否直接判内存泄漏？异步执行下 CPU 区段耗时能代表 GPU 完成时间吗？

先区分聚合表与执行顺序，再标一段等待，最后回 trace 示例。

## 读图与自查

```text
时间向右 →（示意，不按耗时比例）
CPU： 提交 Attention ─ 提交 MLP ───────── 等完成
GPU：       [ Attention ] [ MLP ] ─────── 完成
另一种待查情况：
CPU： 提交 Attention ────── 间隙 ─────── 提交 MLP
GPU：       [ Attention ] ── 空档 ───────── [ MLP ]
```

先在真实 trace 中找到对应区段，再谈有没有空档。聚合算子表丢失了这类先后关系，不能单靠表内耗时相加重建时间线。

<details>
<summary>写下预测后，再核对本段问题</summary>

**题 1**：先看 Attention 在 Block 中占多大比例，再看时间线中的 MLP、CPU 提交间隙、拷贝和等待。局部变快可能被其他部分主导，也可能小于测量波动；没有这些记录时只能保留观察。

**题 2**：reserved 大于 allocated 可能只是缓存分配器保留了可复用空间，不能直接判泄漏。CPU 区段可能只覆盖提交，需要 GPU 完成点才能解释整个调用耗时。若怀疑泄漏，要在相同条件的多次迭代间比较仍存活的分配，不能只看一个快照。

保留自己的推导，再与实际结果比较。若不一致，按下面的回看位置找出最早出现差异的一步。

</details>

## 可选：问 AI

先独立作答和核对，仍有疑问时再使用；跳过本节不影响完成本段。

> 这是同一 Block 的算子表、时间线摘要和 allocated/reserved 记录：【粘贴真实数据】。请先区分直接观察与原因猜测，然后只选一个值得继续检查的区段。不要用 GPU 空档直接证明 kernel 低效，不要把 reserved 大于 allocated 判成泄漏。

## 动手与检查

继续 `labs/03-triton-attention/decoder-profiling/`。固定上一段 shape、dtype、eval/autograd、后端和输入；无 profiler 预热并重复测 Block 延迟，另采样短窗口。

标注 Attention、MLP，保存算子表、一个可读时间线和 allocated/reserved 的定义和测量时刻；若 Nsight Systems 不可用先保存 PyTorch trace，并标系统级证据缺口。大型 trace 放忽略的 `artifacts/`，小型关键摘要、生成命令与报告纳入版本管理。

至少一条观察与机制假设分开写；需要单 kernel 内部指标再复用 W3 的 Nsight Compute，不要求本周同时穷举所有工具。

## 结果不对时，从哪里查起

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 汇总耗时超过墙钟 | trace 中重叠关系 | 是否把嵌套/并行时间重复相加 |
| 内存数据矛盾 | 步骤 4、自己的测量范围 | 峰值重置与分配器指标定义 |

- [ ] 正式延迟与采样分开，原始测量可复现。
- [ ] 至少一张时间线能解释热点与空档。
- [ ] 账本、观测与未验证机制分别说明。

在 `notes.md` 的 `W6-S03` 整理 [周报告](README.md)，先完成 [第四段的显存观察](session-04.md)，再做掌握检查并进入 W13，复用同一 Block。

## 完成后

把代码、预测与实际结果记在同一份笔记中。完成本段检查后，沿下方链接继续。

[上一课](session-02.md) · [下一课](session-04.md)
