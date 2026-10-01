# W3 分段学习指南：归约、同步和性能证据

[本周范围与验收](README.md) · [自学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

详细学习指南：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md) · [2026-10-01 资料复核](refresh-2026-10-01.md)。每段先作答，再读图例与折叠核对说明，最后在本周同一实验目录验证；AI 提示词可跳过。未来实际开始学习仍须重查资料。

原文选读预算：45 + 45 + 60 = 150 分钟；本地例子与自查另计 60 分钟，动手与正确性检查 270 分钟。含资料复核、分析和报告，本单元约 11 小时，详见 [时间表](../../docs/study-guide.md#time-budget)。

## 学习目标与前置检查

本单元知识点：树形归约、barrier、warp mask、性能证据。学完应当能比较共享内存与 warp 归约，在一致计时范围内用数据说明瓶颈。

**开始前检查**：通过 W2 的边界检查和同步计时；能说明一个 block 的线程为什么可能互相等待。 缺项按 [基础补学入口](../../docs/prerequisites.md) 的材料、范围和练习完成；补学时间另计。

<details>
<summary>前置问题核对</summary>

block barrier 要求参与路径满足同步约束；越界线程不能在其他线程执行 block barrier 前随意提前返回。回 W2 内存与错误段核对。

</details>

资源的难度、语言、前置要求、原始 URL 和停止位置统一保存在 [资源索引](../../resources/README.md)，下文按学习顺序链接。先读必读范围，卡点材料替换复习时间，可选拓展不影响基础完成。

## 1. 先画归约树，再写共享内存（45 分钟）

资源定位：[共享内存归约代码](../../resources/README.md#r-reduce)。

**先读**：[GPU MODE shared_reduce.cu](../../resources/README.md#r-reduce)，只看 kernel 内加载、归约循环和同步。该例固定单 block、2048 元素；启动、block offset、尾部和多 block 收尾按自己的输入重写。

**配合阅读**：[CUDA §2.3.2.1](../../resources/README.md#r-cuda) 的 block 同步。树形过程仍不直观时，替换 15 分钟阅读为 [NVIDIA Reduction 幻灯片](../../resources/README.md#r-reduce) 中 `Reduction #3`，阅读器第 14～15 页。

**重点问题**：每一轮由谁写、谁读？无效输入应该填什么值？为什么不能让部分线程跳过整个 block 的 barrier？旧幻灯片用于算法图解，后面的隐式 warp 同步写法不作为现代实现模板。

**动手练习**：手算 8 个带负数的值，再实现共享内存版本。覆盖非整除输入，保留 FP64 或可靠库参考并设置误差容差。

**检查结果**：逐轮解释数据依赖，边界与同步检查没有已知错误。

## 2. 将 warp 内交换与 block 间组合分开（45 分钟）

资源定位：[warp 交换、mask 与同步](../../resources/README.md#r-warp) → [内存与共享同步检查](../../resources/README.md#r-sanitizer)。

**先读**：[NVIDIA Warp-Level Primitives](../../resources/README.md#r-warp) 的 `Synchronized Data Exchange`、`Active Mask Query`、`Warp Synchronization`，聚焦 `__shfl_down_sync`、参与 mask 与共享内存的同步区别。

**配合阅读**：[Compute Sanitizer](../../resources/README.md#r-sanitizer) 的 `Using Racecheck` 和 `Using Synccheck`，先保证 memcheck 已通过。racecheck 的范围主要是共享内存访问危险。

**动手练习**：第二个版本先做 warp 内归约，再组合各 warp 的部分和；主线选择 block 大小为 warp 大小的整数倍，让无效元素填零且线程仍参与所需通信。部分 warp 支持留作扩展，不能直接假设 full mask 对所有控制流都安全。

**检查结果**：两个版本语义、输入与最终输出一致；能说明寄存器交换替代了哪几次共享内存操作。

## 3. 从“更快”推进到“证据支持什么”（60 分钟）

资源定位：[测量、Triton 与编译的讲义例子](../../resources/README.md#r-l6) → [kernel 内部的性能证据](../../resources/README.md#r-ncu)。

**先看/读**：[CS336 Lecture 6 视频](../../resources/README.md#r-l6)，配 [lecture_06.py](../../resources/README.md#r-l6) 的 `benchmarking`、`profiling`，约 20 分钟。暂不读后面的 Triton 算子。

**立即联读**：[Nsight Compute](../../resources/README.md#r-ncu) §2.2.1～2.2.3，查 section 选择与 replay；在 sections 表只看 `SpeedOfLight`、`MemoryWorkloadAnalysis`、`Occupancy` 三项。

**动手练习**：先无 profiler 计时，再对一个代表规模采样。写出一条可检验的假设，例如减少共享内存操作是否改善该规模延迟；记录支持证据和仍无法排除的解释。较高 occupancy 不能单独作为优化成功标准。

**完成后检查**：保留两组原始计时和一份代表性报告，说明采样干扰与归约顺序造成的浮点差异。

## 整理记录与可选拓展

在 `labs/02-cuda/reduction/` 形成两个版本、检查记录、对照曲线和“假设—证据—限制”短报告。W4 继续复用这套采样方法。

进阶可在现有归约上研究每线程处理多个元素，先重新列索引和尾部范围；multistream 与全面调参暂缓，不追加未定位的整库阅读。
