# W2 章节导学：把 Vector Add 变成可信实验

[本周范围与验收](README.md) · [导学规则](../../docs/study-guide.md) · [当前做法与相关进展](context.md)

资料预算：60 + 45 + 45 = 150 分钟。视频与文档交叉使用，看到能解释当前代码的位置就暂停。

## 1. 线程怎样覆盖数组（60 分钟）

**先看**：[Jeremy Howard 的 CUDA 入门视频](https://www.youtube.com/watch?v=nOxKexn3iBo)，配 [lecture_003/pmpp.ipynb](https://github.com/gpu-mode/lectures/blob/main/lecture_003/pmpp.ipynb)。本轮核验到 notebook 文件，未核验视频分段时间；以线程索引、kernel 启动为观看目标，后续精确位置以文档为准。

**立即联读**：[Programming Model §1.2](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html) 的执行层级，再读 [Writing SIMT Kernels §2.3.2](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html) 的线程索引；启动语法查 [Intro to CUDA C++ §2.1.2](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/intro-to-cuda-cpp.html)。只覆盖这些位置，不通读整章。

**重点问题**：总线程数大于数组长度时会怎样？block 与 warp 是否同一层级？

**动手练习**：给长度 10、每 block 4 个线程画索引表，标出无效线程；随后写 CPU 参考与 CUDA Vector Add。先验证小数组，再扩大输入。

**检查结果**：能从 `blockIdx`、`blockDim`、`threadIdx` 推导下标，非整除长度输出正确。

## 2. 数据在哪里，错误在哪里发现（45 分钟）

**先读**：CUDA C++ 入门的 §2.1.3.2 显式内存管理和 §2.1.4 CPU/GPU 同步。若视频采用统一内存，画图比较两种路径，本实验先保持一种内存管理方式。

**配合阅读**：[Compute Sanitizer](https://docs.nvidia.com/compute-sanitizer/ComputeSanitizer/index.html) 的 `Using Memcheck` 与其后错误报告说明；只学启动与定位首个非法访问的方法。

**动手练习**：为分配、拷贝和启动添加错误检查；用长度 1、10、257 以及一个较大输入验证输出，对小输入运行 memcheck。保留错误日志或通过记录，检查工具运行不参与性能计时。

**检查结果**：能说明每次拷贝方向和同步点；环境不支持检查时明确记为待补测。

## 3. 测到的是 kernel，还是提交请求（45 分钟）

**先读**：[CUDA Best Practices](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html) §9.1.2 GPU Event 计时、§9.2 中有效带宽的计算说明。与 CUDA C++ 入门 §2.1.4 对照：CPU 返回不意味着 GPU 工作完成。

**动手练习**：做预热和重复计时，分别记录 kernel 区间与包含拷贝的端到端区间；至少扫描 4 个规模。每个元素两次读、一次写，用 `3 × N × 元素字节数 / 时间` 算有效带宽。

**完成后检查**：说明计时同步、单位、重复次数，以及有效带宽为何不等于硬件计数器测出的 DRAM 带宽。将计时方法留给 W3～W5。

## 课后整理与选修

在 `labs/02-cuda/vector-add/` 保存实现、原始计时、正确性/内存检查记录和曲线。

卡点补充：[NVIDIA 入门博客](https://developer.nvidia.com/blog/even-easier-introduction-cuda/) 中 CPU 循环改为 GPU kernel 的代码段，用于还不能解释线程映射时，替换第一段部分观看。进阶可比较两种 block 大小；暂不加入多 stream 和 Unified Memory 调优。
