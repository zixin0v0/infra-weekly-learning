# W7 第 2 段：为什么报表里有两种带宽？

[本单元](README.md) · [课程目录](../../course/README.md)

同一行 nccl-tests 会给出时间、algbw 和 busbw。它们不是三份独立测量；后两项由时间和数据量换算，必须知道分母、单位以及 rank 因子才能解释。

## 视频与正文

主要阅读下列正文与图解；视频范围待核验。读到暂停题时，先预测再运行。

## 目标与先修

读懂 nccl-tests 的计量，手算核对任意一行。先通过两卡 collective 语义与环境；构建/排错另计，不占资料选读。

## 读哪里，在哪里停

| 阅读参考 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 25 分钟 | [nccl-tests 固定 README](../../resources/training.md#r-nccl-tests) | Build、Usage、单进程多 GPU 例子与大小参数结束 |
| 25 分钟 | [固定 PERFORMANCE.md](../../resources/training.md#r-nccl-tests) 的 Time、Algorithm bandwidth、Bus bandwidth → AllReduce | AllReduce 换算结束，其他 collective 性能后置 |
| 10 分钟 | 手算一个假设报表行 | 单位、rank 因子与 in-place/out-of-place 分组清楚即停 |

访问日：2026-10-01。源码 commit 是阅读/构建定位，实际 CUDA/NCCL 与构建选项需独立记录。

## 先复算一个普通除法，再加归一化因子

**算法带宽（algbw）**用操作定义中的逻辑字节数除以耗时。**总线带宽指标（busbw）**再按特定 collective 的公式换算，方便在其模型下讨论传输成本；它不是在某条 PCIe 链路上直接采样得到的速度。

先把微秒转换成秒，用 B/s 算完，再除以 10^9 得 GB/s。两 rank AllReduce 的换算因子恰好为 1，不能据此认为两个术语完全等价。回看 [S2 的延迟与带宽图](../../course/bridges/s02.md)，小消息的启动成本仍可能主导时间。

algbw 是操作对应逻辑数据量除时间；AllReduce 的 busbw=algbw×2×(P−1)/P，P 是 rank 数。两 rank 因子为 1，四 rank 为 1.5；它是归一化计量，不是直接采样 PCIe/NVLink 的瞬时链路带宽。

大小参数的 KiB/MiB 类后缀与表中 GB/s 的单位约定分别核对；dtype 决定元素数怎样转字节。报表的 in-place 与 out-of-place 两组不能混成同一测量。

## 暂停题与预测

1. 假设每 rank 传 1,000,000 字节、操作 100 微秒，两 rank 的 algbw/busbw 是多少？四 rank 同时间时 busbw 呢？
2. 消息字节数相同但 dtype 改变，元素数是否相同？错误数非零的一行能用来证明加速吗？

先写字节/秒，再计算 rank 因子，最后回 PERFORMANCE.md 定义。

## 读图与自查

```text
每 rank 逻辑字节数 ÷ 操作耗时（秒） ÷ 10^9 → algbw（GB/s）
                                           ↓ × 2(P−1)/P
                                      AllReduce busbw（GB/s）
P=2：因子 1                 P=4：因子 1.5
```

读图时沿两个箭头分别验算。busbw 是按公式换算的指标，没有在图中测量任何物理链路；in-place 与 out-of-place 各走一遍，不混合两组报表。

<details>
<summary>写下预测后，再核对本段问题</summary>

**题 1**：1,000,000/0.0001/10^9=10 GB/s。两 rank busbw=10 GB/s；四 rank 假设时间仍为 100 微秒时，busbw=15 GB/s。因子变化本身不证明四卡更快。

**题 2**：相同字节数下，元素数=字节数/元素宽度，因此换 dtype 后元素数可能改变。错误数非零的行不进入有效性能曲线。小型复算先确认字节、元素数、时间单位、rank 总数和所选报表组，逐项定位差异。

保留自己的推导，再与实际结果比较。若不一致，按下面的回看位置找出最早出现差异的一步。

</details>

## 可选：问 AI

先独立作答和核对，仍有疑问时再使用；跳过本节不影响完成本段。

> 我从 nccl-tests 选了一行：【bytes、count、dtype、world size、time、algbw、busbw、错误数、报表组】。请先让我手算两种带宽，再检查单位或 rank 因子。不要把 busbw 称为实测 PCIe 带宽，不要忽略非零错误数。

## 动手与检查

继续 `labs/04-collectives/allreduce/`。按固定源码构建，先做小消息两卡正确性运行，再扫描多个消息大小；选择保守上限并确认显存，4 卡留作扩展。启动方式、进程数与每进程 GPU 数写清；实际总 rank 数不能只看一个参数。

保存原始输出及解析小表：bytes、count、dtype、world size、时间单位、algbw、busbw、错误数、in-place/out-of-place、warmup/重复配置。至少三组独立运行，固定选卡、环境与负载，随机一行手工复算。

原始 `.log` 默认忽略；可公开小型记录保存为 `nccl-tests.txt` 或 CSV，大日志放 `artifacts/` 并在报告记录生成命令。数值错误、超时与失败单列，不能混入有效曲线。

## 结果不对时，从哪里查起

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 手算不匹配 | Time、Algorithm bandwidth | 时间与字节单位 |
| 卡数增加 busbw 变高 | Bus bandwidth → AllReduce | 归一化因子与真实延迟 |

- [ ] 正确性错误数为零，失败独立记录。
- [ ] 两卡扫描与原始重复记录齐全。
- [ ] 任意一行可复算，指标局限明确。

在 `notes.md` 的 `W7-S02` 留下预测、命令与结果；通过后进入 [第三段](session-03.md)。

## 完成后

把代码、预测与实际结果记在同一份笔记中。完成本段检查后，沿下方链接继续。

[上一课](session-01.md) · [下一课](session-03.md)
