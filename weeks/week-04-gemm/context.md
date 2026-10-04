# W4 补充阅读：从分块 GEMM 到架构匹配

[返回本单元](README.md) · [来源登记](../../resources/optional.md#s04)

资料快照：2026-10-01。[学习资料复核已完成](../../docs/audits/2026-10-01-week-04.md)，实际开始学习日仍须复查。本地状态：仅阅读，相关实现尚未运行。

完成本单元后，若想继续了解这个问题，再读下面的指定范围。选读前核对当前版本与设备条件；页面保留 2026-10-01 的来源快照，没有把旧结论重新标为已验证。

## 从已经做过的实验出发

朴素/分块 GEMM 用于解释数据复用；同输入、同精度设置的 torch.matmul 是工程基线。记录 TF32 等计算模式，不把不同数值精度的速度差归因于 tiling。

## 接着想清一个问题

现代 GEMM 优化进一步围绕 Tensor Core、异步搬运、流水线与布局组织展开。这部分帮助辨认学习 tile 与高性能组件之间的层次，不要求本周手写完整 Tensor Core kernel。

**读哪里**：[CuTe 的分层矩阵运算与流水线](https://docs.nvidia.com/cutlass/latest/media/docs/pythonDSL/overview.html)。Core Abstractions 中 Atom、Tiled operation、Pipelines；Architecture Coverage 中三类架构；Relationship to CUTLASS C++ 的性能与库范围说明。

**来源快照中的状态**：官方实现与文档可供研究，但 Python DSL 的覆盖范围、接口与 C++ 库不完全相同。

**设备条件**：计划中的 Ada 与文档中的 Hopper/Blackwell 路径不同。只讨论对应架构能力，不照搬新架构原语或峰值数字。

## 真正用起来，还要考虑什么

可用组件还要覆盖不同 shape、尾块、dtype、workspace 与融合算子；单个方阵的加速不能代表模型全部 GEMM。

**选读后可写进报告**：把 torch.matmul 加入原有小规模测量表，注明精度条件；在报告解释练习版本、库基线的差距和最可能的两个原因。未知的 Tensor Core 使用情况写待验证，不凭速度猜测。

## 选读前核对

核对架构支持与精度默认值，若后续选 kernel 分支再挑一个对应 Ada 的例子；本周不扩大实现范围。
