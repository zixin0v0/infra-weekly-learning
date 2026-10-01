# W6 第三段备课：模型热点与 CPU—GPU 时间线

[单元范围](README.md) · [三段导学](study-guide.md) · [资料复核](refresh-2026-10-01.md) · [上一段](session-02.md)

备课日期：2026-10-01。资料预算：60 分钟。状态：备课已准备；模型采样与正式计时待完成。

## 目标与先修

用算子表找热点，再用时间线区分执行、拷贝与等待。先让同一个 Block 正确运行；前向是否建立 autograd 图必须明确，backward 留作扩展。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 25 分钟 | [PyTorch Profiler recipe](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html) 的步骤 3、4 | 执行时间与内存表解释结束；不增加 ResNet 实验 |
| 10 分钟 | 同页 export_chrome_trace 示例 | trace 导出方法结束 |
| 25 分钟 | [Nsight Systems User Guide](https://docs.nvidia.com/nsight-systems/UserGuide/index.html#cuda-trace) 的 CUDA Trace → Basic CUDA trace、Marking and Labeling Regions | 识别调用/拷贝/kernel 与区段标记后停 |

访问日：2026-10-01。工具覆盖与权限需在实际设备确认；官方示例时间不是本机结果。

## 中文助读

算子表按聚合耗时寻找热点，时间线展示先后和重叠。CPU 等待、提交间隙、拷贝与 GPU kernel 不是一个指标；GPU 有空档不能直接证明某个 kernel 内部效率低。

allocated 是框架当前 Tensor 占用，reserved 包括缓存分配器保留空间，设备占用还可能含其他上下文/进程；三者不能直接相加。峰值测量须说明何时重置、哪些初始化和临时分配被计入。

## 暂停题与预测

1. Attention 单次更快但 Block 延迟不变，先看哪张表、再看时间线的哪段？
2. reserved 大于 allocated 能否直接判内存泄漏？异步执行下 CPU 区段耗时能代表 GPU 完成时间吗？

先区分聚合表与执行顺序，再标一段等待，最后回 trace 示例。

## 动手与检查

继续 `labs/03-triton-attention/decoder-profiling/`。固定上一段 shape、dtype、eval/autograd、后端和输入；无 profiler 预热并重复测 Block 延迟，另采样短窗口。

标注 Attention、MLP，保存算子表、一个可读时间线和 allocated/reserved 口径；若 Nsight Systems 不可用先保存 PyTorch trace，并标系统级证据缺口。大型 trace 放忽略的 `artifacts/`，小型关键摘要、生成命令与报告纳入版本管理。

至少一条观察与机制假设分开写；需要单 kernel 内部指标再复用 W3 的 Nsight Compute，不要求本周同时穷举所有工具。

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 汇总耗时超过墙钟 | trace 中重叠关系 | 是否把嵌套/并行时间重复相加 |
| 内存数据矛盾 | 步骤 4、自己的测量范围 | 峰值重置与分配器口径 |

- [ ] 正式延迟与采样分开，原始测量可复现。
- [ ] 至少一张时间线能解释热点与空档。
- [ ] 账本、观测与未验证机制分别说明。

在 `notes.md` 的 `W6-S03` 整理 [周报告](README.md)，验收后进入 [W13](../week-13-systems/session-01.md)，复用同一 Block。
