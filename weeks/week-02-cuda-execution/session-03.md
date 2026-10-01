# W2 第三段备课：可靠计时与有效带宽

[单元范围](README.md) · [三段导学](study-guide.md) · [资料复核](refresh-2026-10-01.md) · [上一段](session-02.md)

备课日期：2026-10-01。资料预算：45 分钟。状态：备课已准备；真实测量待完成。

## 目标与先修

让时间对应明确的工作区间，计算带单位的有效带宽。先通过前两段正确性和内存检查；工具缺失项须保留，不能用计时掩盖错误。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 20 分钟 | [CUDA Best Practices §9.1.2](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html) Using CUDA GPU Timers | Event 创建、记录、完成与 elapsed time 示例结束 |
| 15 分钟 | 同页 §9.2 Bandwidth，重点 Effective Bandwidth Calculation | 读写字节与时间的单位换算结束 |
| 10 分钟 | [Intro to CUDA C++ §2.1.4](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/intro-to-cuda-cpp.html) | 回看异步完成，画两种计时区间后停 |

访问日：2026-10-01。Best Practices 页标 13.4；这是阅读版本，实际 CUDA 版本待记录。

## 中文助读

FP32 Vector Add 每元素逻辑上读两次、写一次，有效字节数为 12N。若只计 kernel，`GB/s = 12N / 秒 / 10^9`。这衡量完成这些逻辑读写的速度；缓存与实际事务会让它不同于 DRAM 硬件计数器值。

kernel 区间使用同 stream 的 Event 并等结束事件完成；端到端区间覆盖约定的拷贝和 kernel，CPU 计时必须等 GPU 完成。预先分配还是把分配计入，要在两组分别说明。

## 暂停题与预测

1. N=1000、FP32、kernel 时间为 10 微秒，理论换算得到多少 GB/s？如果误把毫秒直接当秒，结果错多少倍？
2. 小输入 kernel 很短，为什么端到端可能依然慢？若反复复用同一输入，能直接称为冷缓存 DRAM 带宽吗？

先写单位链，再区分“提交”和“完成”，最后回 §9.1.2 与 §9.2。

## 动手与检查

继续 `labs/02-cuda/vector-add/`。固定 dtype、block 大小和输入内容；至少四个规模，例如 257、4096、65536、1048576，先确认实际显存可容纳。完成正确性后预热，按 [测量约定](../../docs/learning-workflow.md) 至少三组独立测量，组内重复数与同步方法写进配置。

分别保存 kernel 与端到端每次原始时间、有效字节数、汇总方式与曲线。短 kernel 可重复启动后除以次数，同时说明该平均包含的开销。sanitizer/profiler 采样独立运行；不把工具耗时混进正式数据。

<details>
<summary>先预测，再核对纸面值</summary>

12,000 字节 / 0.00001 秒 = 1.2×10^9 B/s，即 1.2 GB/s；它不是本机测量。

</details>

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 看似不随规模增长 | §9.1.2 | 是否只计 CPU 提交 |
| 两张曲线矛盾 | §9.2、自己的计时边界 | 是否比较同一工作与单位 |

- [ ] 正确性、工具检查和计时分开。
- [ ] 至少四个规模与原始重复数据可追溯。
- [ ] 独立计算带宽并说明缓存与计时边界。

在 `notes.md` 的 `W2-S03` 整理预测与结果；合并为 [周报告](README.md)，验收通过后进入 [W3](../week-03-reduction-profiling/session-01.md)。
