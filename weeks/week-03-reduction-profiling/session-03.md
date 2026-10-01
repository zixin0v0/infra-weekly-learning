# W3 第三段备课：假设、采样与性能证据

[单元范围](README.md) · [三段导学](study-guide.md) · [资料复核](refresh-2026-10-01.md) · [上一段](session-02.md)

备课日期：2026-10-01。资料预算：60 分钟。状态：备课已准备；计时与 profiler 采样待完成。

## 目标与先修

用一条可检验假设解释两种正确 Reduce 的差异。先完成两版本数值与同步检查；Nsight Compute 不可用时记录采样缺口，不能虚构指标。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 20 分钟 | [CS336 L6 视频](https://www.youtube.com/watch?v=xnDHaNUvHBg)，配 [固定讲义](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py) 的 benchmarking、profiling | 两函数结束；不进入 Triton |
| 25 分钟 | [Nsight Compute Profiling Guide §2.2.1～2.2.3](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html) | sets、sections、replay 说明结束 |
| 15 分钟 | 同页 sections 表的 SpeedOfLight、MemoryWorkloadAnalysis、Occupancy | 找到每项回答的问题后停 |

访问日：2026-10-01。函数名是讲义定位词，视频分钟数未核验。

## 中文助读

正式延迟先在无 profiler 条件下测量；采样会引入 replay 或其他干扰。指标用来核对机制，不代替最终延迟。occupancy 描述活跃工作资源情况，较高值不自动说明更快。

记录链条：假设 → 预期指标变化 → 一次受控比较 → 支持证据 → 仍不能排除的解释。例如“减少共享内存读写后延迟下降”，还要核对指令、寄存器、输入规模和实际关键路径。

## 暂停题与预测

1. warp 版本在小输入更快、大输入差别很小，你先提出哪两个不同解释？各用什么证据区分？
2. occupancy 更高但延迟更差，哪些记录仍缺失？为何不能直接把 sampler 的时间当正式性能？

先区分观察与因果，再选一个具体规模，最后只查相关 section。

## 动手与检查

继续 `labs/02-cuda/reduction/`。至少四个规模，无 profiler 按 W2 方法做预热与重复计时；加入同语义 `torch.sum` 工程参考，注明累加 dtype、分配和调用开销是否相同。

对一个代表规模和两个实现分别采样指定 sections，保存版本、命令及关键小表；大型 `.ncu-rep` 放忽略的 `artifacts/`，报告记录路径和生成方法。比较时固定输入、block、收尾、计时范围，先只解释一项实现变化。

若驱动权限或设备导致指标不可用，已测时间仍可报告，机制结论标待证实；迁移到服务器后的绝对值独立报告。

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 指标太多 | §2.2.1～2.2.3 | 是否对应预先写出的假设 |
| 工具时间与计时差很大 | replay 说明、L6 benchmarking | 采样与正式运行是否分离 |

- [ ] 两组真实原始计时与误差记录齐全。
- [ ] 一条假设有证据和局限，未知项保留。
- [ ] 库对照语义与计时边界清楚。

在 `notes.md` 的 `W3-S03` 整理记录，完成 [周验收](README.md) 后进入 [W4](../week-04-gemm/session-01.md)。
