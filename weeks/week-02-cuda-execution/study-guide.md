# W2 分段学习指南：把 Vector Add 变成可信实验

[本周范围与验收](README.md) · [自学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

详细学习指南：[第一段](session-01.md) · [第二段](session-02.md) · [第三段](session-03.md) · [2026-10-01 资料复核](refresh-2026-10-01.md)。每段先作答，再读图例与折叠核对说明，最后在本周同一实验目录验证；AI 提示词可跳过。未来实际开始学习仍须重查资料。

原文选读预算：60 + 45 + 45 = 150 分钟；本地例子与自查另计 60 分钟，动手与正确性检查 270 分钟。含资料复核、分析和报告，本单元约 11 小时，详见 [时间表](../../docs/study-guide.md#time-budget)。

## 学习目标与前置检查

本单元知识点：线程覆盖、host/device 内存、异步计时、带宽。学完应当能实现有尾部保护的 Vector Add，定位访存错误，并解释 kernel 与端到端时间。

**开始前检查**：通过 W1；完成先修 A/B。先画 N=10、每块 4 个线程的覆盖表，说明指针和所指数据的区别。 缺项按 [基础补学入口](../../docs/prerequisites.md) 的材料、范围和练习完成；补学时间另计。

<details>
<summary>前置问题核对</summary>

需要 3 个 block；最后一块只有索引 8、9 有效。host 指针变量的存在不证明 device 数据已经分配或复制。

</details>

资源的难度、语言、前置要求、原始 URL 和停止位置统一保存在 [资源索引](../../resources/README.md)，下文按学习顺序链接。先读必读范围，卡点材料替换复习时间，可选拓展不影响基础完成。

## 1. 线程怎样覆盖数组（60 分钟）

资源定位：[CUDA 线程与 host/device 数据路径](../../resources/README.md#r-cuda)。

**先看**：[Jeremy Howard 的 CUDA 入门视频](../../resources/README.md#x-cuda)，配 [lecture_003/pmpp.ipynb](../../resources/README.md#x-cuda) 的 `rgb_to_grayscale_kernel`、`rgb_to_grayscale`。本轮已读索引与启动代码，未核验视频分段时间；只用该例解释映射，不增加灰度图项目。

**立即联读**：[Programming Model §1.2](../../resources/README.md#r-cuda) 的执行层级，再读 [Writing SIMT Kernels §2.3.2](../../resources/README.md#r-cuda) 的线程索引；启动语法查 [Intro to CUDA C++ §2.1.2](../../resources/README.md#r-cuda)。只覆盖这些位置，不通读整章。

**重点问题**：总线程数大于数组长度时会怎样？block 与 warp 是否同一层级？

**动手练习**：给长度 10、每 block 4 个线程画索引表，标出无效线程；用 CPU 循环检查覆盖，再写 CPU 参考与 CUDA kernel 草稿。第二段补齐内存管理后再运行完整 GPU 程序。

**检查结果**：能从 `blockIdx`、`blockDim`、`threadIdx` 推导下标，CPU 索引模拟对非整除长度没有遗漏或重复；GPU 输出在第二段检查。

## 2. 数据在哪里，错误在哪里发现（45 分钟）

资源定位：[CUDA 线程与 host/device 数据路径](../../resources/README.md#r-cuda) → [内存与共享同步检查](../../resources/README.md#r-sanitizer)。

**先读**：CUDA C++ 入门的 §2.1.3.2 显式内存管理、§2.1.4 CPU/GPU 同步和 §2.1.7 错误检查。若视频采用统一内存，画图比较两种路径，本实验先保持一种内存管理方式。

**配合阅读**：[Compute Sanitizer](../../resources/README.md#r-sanitizer) 的 `Using Memcheck` 与其后错误报告说明；只学启动与定位首个非法访问的方法。

**动手练习**：为分配、拷贝和启动添加错误检查；用长度 1、10、257 以及一个较大输入验证输出，对小输入运行 memcheck。保留错误日志或通过记录，检查工具运行不参与性能计时。

**检查结果**：能说明每次拷贝方向和同步点；环境不支持检查时明确记为待补测。

## 3. 测到的是 kernel，还是提交请求（45 分钟）

资源定位：[计时、有效带宽与 GEMM 数据复用](../../resources/README.md#r-best)。

**先读**：[CUDA Best Practices](../../resources/README.md#r-best) §9.1.2 GPU Event 计时、§9.2 中有效带宽的计算说明。与 CUDA C++ 入门 §2.1.4 对照：CPU 返回不意味着 GPU 工作完成。

**动手练习**：做预热和重复计时，分别记录 kernel 区间与包含拷贝的端到端区间；至少扫描 4 个规模。每个元素两次读、一次写，用 `3 × N × 元素字节数 / 时间` 算有效带宽。

**完成后检查**：说明计时同步、单位、重复次数，以及有效带宽为何不等于硬件计数器测出的 DRAM 带宽。将计时方法留给 W3～W5。

## 整理记录与可选拓展

在 `labs/02-cuda/vector-add/` 保存实现、原始计时、正确性/内存检查记录和曲线。

卡点补充：[NVIDIA 入门博客](../../resources/README.md#x-cuda) 中 CPU 循环改为 GPU kernel 的代码段，用于还不能解释线程映射时，替换第一段部分观看。进阶可比较两种 block 大小；暂不加入多 stream 和 Unified Memory 调优。
