# W2 补充阅读：执行模型与 kernel 编程入口

[范围与验收](README.md) · [三段导学](study-guide.md) · [更新流程](../../docs/weekly-refresh.md) · [来源登记](../../resources/frontier-watchlist.md#s02)

资料快照：2026-10-01。开课复核：待进行。本地状态：仅阅读，相关实现尚未运行。

开课前用30分钟核对本页资料。这里的练习并入本周报告，额外实现留作选修。

## 现在怎样做

保留 CUDA C++ 的 Vector Add，明确 host/device、grid/block、边界、异步计时与错误检查。框架同语义操作作为正确性和性能参考；学习显式执行模型，不以增加语言或构建工具数量衡量进度。

## 这一方向还有哪些进展

Python 语法也能显式表达布局、线程分工与数据搬运；语言更易用，并不消除执行与同步语义。W2 只建立 CUDA 术语到 DSL 抽象的映射，W4 再看矩阵运算。

**读哪里**：[CUTLASS Python / CuTe DSL](https://docs.nvidia.com/cutlass/latest/media/docs/pythonDSL/overview.html)。Key Concepts and Approach 下的 Core Abstractions、Pythonic Kernel Expression；接着读 Architecture Coverage 和 Current Status。

**目前的状态**：NVIDIA 官方 DSL，仍在演进；部分接口具有实验性。文档分别列出 Ampere/Ada、Hopper、Blackwell 的不同能力，不能概括成仅支持新一代 GPU。

**在我们的设备上**：Ada 的能力条目可以作为候选入口，实际例子仍需检查架构、CUDA 与平台要求。当前不额外配置 CuTe 环境。

## 真正用起来，还要考虑什么

教学 kernel 的输入和环境很窄；工程组件需要边界处理、版本约束、框架集成与可诊断的失败。代码短不代表更容易维护。

**写进本周报告**：在 Vector Add 报告标注哪些逻辑是算法、哪些是线程映射、哪些是 host 启动与检查。回答改用 Python DSL 后哪些责任仍必须保留；不再实现第二个语言版本。

## 下次更新时

核对 Architecture Coverage、Limitations 和支持平台；只有原 CUDA 教程接口失效才替换主线。更新写入 [开课记录](../../templates/weekly-refresh.md)，保留旧实验的配置。
