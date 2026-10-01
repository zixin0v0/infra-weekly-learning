# W3 章节导学：归约、同步和性能证据

[本周范围与验收](README.md) · [导学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

详细备课：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md) · [2026-10-01 资料复核](refresh-2026-10-01.md)。先按备课单预测，再在本周同一实验目录核对；未来实际开课仍须重查资料。

资料预算：45 + 45 + 60 = 150 分钟。主线先做每 block 输出一个部分和；大输入的第二阶段对两个版本使用相同方法，避免只优化其中一组的收尾。

## 1. 先画归约树，再写共享内存（45 分钟）

**先读**：[GPU MODE shared_reduce.cu](https://github.com/gpu-mode/lectures/blob/77a8df418834e5789c12da23e7d2719e0efabef1/lecture_009/shared_reduce.cu)，只看 kernel 内加载、归约循环和同步。该例固定单 block、2048 元素；启动、block offset、尾部和多 block 收尾按自己的输入重写。

**配合阅读**：[CUDA §2.3.2.1](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html) 的 block 同步。树形过程仍不直观时，替换 15 分钟阅读为 [NVIDIA Reduction 幻灯片](https://developer.download.nvidia.com/assets/cuda/files/reduction.pdf) 中 `Reduction #3`，阅读器第 14～15 页。

**重点问题**：每一轮由谁写、谁读？无效输入应该填什么值？为什么不能让部分线程跳过整个 block 的 barrier？旧幻灯片用于算法图解，后面的隐式 warp 同步写法不作为现代实现模板。

**动手练习**：手算 8 个带负数的值，再实现共享内存版本。覆盖非整除输入，保留 FP64 或可靠库参考并设置误差容差。

**检查结果**：逐轮解释数据依赖，边界与同步检查没有已知错误。

## 2. 将 warp 内交换与 block 间组合分开（45 分钟）

**先读**：[NVIDIA Warp-Level Primitives](https://developer.nvidia.com/blog/using-cuda-warp-level-primitives/) 的 `Synchronized Data Exchange`、`Active Mask Query`、`Warp Synchronization`，聚焦 `__shfl_down_sync`、参与 mask 与共享内存的同步区别。

**配合阅读**：[Compute Sanitizer](https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html) 的 `Using Racecheck` 和 `Using Synccheck`，先保证 memcheck 已通过。racecheck 的范围主要是共享内存访问危险。

**动手练习**：第二个版本先做 warp 内归约，再组合各 warp 的部分和；主线选择 block 大小为 warp 大小的整数倍，让无效元素填零且线程仍参与所需通信。部分 warp 支持留作扩展，不能直接假设 full mask 对所有控制流都安全。

**检查结果**：两个版本语义、输入与最终输出一致；能说明寄存器交换替代了哪几次共享内存操作。

## 3. 从“更快”推进到“证据支持什么”（60 分钟）

**先看/读**：[CS336 Lecture 6 视频](https://www.youtube.com/watch?v=xnDHaNUvHBg)，配 [lecture_06.py](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py) 的 `benchmarking`、`profiling`，约 20 分钟。暂不读后面的 Triton 算子。

**立即联读**：[Nsight Compute](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html) §2.2.1～2.2.3，查 section 选择与 replay；在 sections 表只看 `SpeedOfLight`、`MemoryWorkloadAnalysis`、`Occupancy` 三项。

**动手练习**：先无 profiler 计时，再对一个代表规模采样。写出一条可检验的假设，例如减少共享内存操作是否改善该规模延迟；记录支持证据和仍无法排除的解释。较高 occupancy 不能单独作为优化成功标准。

**完成后检查**：保留两组原始计时和一份代表性报告，说明采样干扰与归约顺序造成的浮点差异。

## 课后整理与选修

在 `labs/02-cuda/reduction/` 形成两个版本、检查记录、对照曲线和“假设—证据—限制”短报告。W4 继续复用这套采样方法。

进阶只选择 [lecture_009](https://github.com/gpu-mode/lectures/tree/main/lecture_009) 的 `reduce_coarsening.cu`，检查每线程处理多个元素的影响；multistream 与全面调参暂缓。
