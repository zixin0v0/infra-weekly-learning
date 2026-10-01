# W7 第二段备课：时间、algbw 与 busbw

[单元范围](README.md) · [三段导学](study-guide.md) · [资料复核](refresh-2026-10-01.md) · [上一段](session-01.md)

备课日期：2026-10-01。资料预算：60 分钟。状态：备课已准备；构建与两卡测量待完成。

## 目标与先修

读懂 nccl-tests 的计量，手算核对任意一行。先通过两卡 collective 语义与环境；构建/排错另计，不占资料选读。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 25 分钟 | [nccl-tests 固定 README](https://github.com/NVIDIA/nccl-tests/blob/b4d5beebca8a76cf01335f724d154b9b9d394d96/README.md) | Build、Usage、单进程多 GPU 例子与大小参数结束 |
| 25 分钟 | [固定 PERFORMANCE.md](https://github.com/NVIDIA/nccl-tests/blob/b4d5beebca8a76cf01335f724d154b9b9d394d96/doc/PERFORMANCE.md) 的 Time、Algorithm bandwidth、Bus bandwidth → AllReduce | AllReduce 换算结束，其他 collective 性能后置 |
| 10 分钟 | 手算一个假设报表行 | 单位、rank 因子与 in-place/out-of-place 分组清楚即停 |

访问日：2026-10-01。源码 commit 是阅读/构建定位，实际 CUDA/NCCL 与构建选项需独立记录。

## 中文助读

algbw 是操作对应逻辑数据量除时间；AllReduce 的 busbw=algbw×2×(P−1)/P，P 是 rank 数。两 rank 因子为 1，四 rank 为 1.5；它是归一化计量，不是直接采样 PCIe/NVLink 的瞬时链路带宽。

大小参数的 KiB/MiB 类后缀与表中 GB/s 的单位口径分别核对；dtype 决定元素数怎样转字节。报表的 in-place 与 out-of-place 两组不能混成同一测量。

## 暂停题与预测

1. 假设每 rank 传 1,000,000 字节、操作 100 微秒，两 rank 的 algbw/busbw 是多少？四 rank 同时间时 busbw 呢？
2. 消息字节数相同但 dtype 改变，元素数是否相同？错误数非零的一行能用来证明加速吗？

先写字节/秒，再计算 rank 因子，最后回 PERFORMANCE.md 定义。

## 动手与检查

继续 `labs/04-collectives/allreduce/`。按固定源码构建，先做小消息两卡正确性运行，再扫描多个消息大小；选择保守上限并确认显存，4 卡留作扩展。启动方式、进程数与每进程 GPU 数写清；实际总 rank 数不能只看一个参数。

保存原始输出及解析小表：bytes、count、dtype、world size、时间单位、algbw、busbw、错误数、in-place/out-of-place、warmup/重复配置。至少三组独立运行，固定选卡、环境与负载，随机一行手工复算。

原始 `.log` 默认忽略；可公开小型记录保存为 `nccl-tests.txt` 或 CSV，大日志放 `artifacts/` 并在报告记录生成命令。数值错误、超时与失败单列，不能混入有效曲线。

<details>
<summary>先预测，再核对纸面值</summary>

1,000,000 / 0.0001 / 10^9 = 10 GB/s；两 rank busbw=10，四 rank同假设时间 busbw=15 GB/s。该假设并不表示四卡会保持相同时间。

</details>

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 手算不匹配 | Time、Algorithm bandwidth | 时间与字节单位 |
| 卡数增加 busbw 变高 | Bus bandwidth → AllReduce | 归一化因子与真实延迟 |

- [ ] 正确性错误数为零，失败独立记录。
- [ ] 两卡扫描与原始重复记录齐全。
- [ ] 任意一行可复算，指标局限明确。

在 `notes.md` 的 `W7-S02` 留下预测、命令与结果；通过后进入 [第三段](session-03.md)。
