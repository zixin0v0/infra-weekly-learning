# W3 补充阅读：归约、布局与可信性能证据

[范围与验收](README.md) · [三段导学](study-guide.md) · [更新流程](../../docs/weekly-refresh.md) · [来源登记](../../resources/frontier-watchlist.md#s03)

资料快照：2026-10-01。[备课资料复核已完成](refresh-2026-10-01.md)，实际开课日仍须复查。本地状态：仅阅读，相关实现尚未运行。

开课前用30分钟核对本页资料。这里的练习并入本周报告，额外实现留作选修。

## 现在怎样做

两种小型 Reduce 解释并行归约；PyTorch 的同语义 sum 作为数值参考和工程对照。先固定输入/累加 dtype、归约维度、同步与容差，再解释性能，不要求手写实现击败库。

## 这一方向还有哪些进展

更显式地控制数据在线程/warp 中的分布，是理解布局变换与生成高效代码的一条方向。阅读目标是解释通信来源，不在 W3 新学整套 DSL。

**读哪里**：[Gluon 显式布局与 Linear Layouts](https://triton-lang.org/main/getting-started/tutorials/gluon/layouts.html)。开头关于布局的说明，以及 BlockedLayout 的第一个示例；搜索 triton.experimental.gluon，确认使用的是实验接口。配套：[Linear Layouts 论文摘要](https://arxiv.org/abs/2505.23819)。

**目前的状态**：官方教程使用 experimental Gluon 命名空间；论文入口本轮核对摘要，不据此声称精读全文或复现编译器。

**在我们的设备上**：主线继续现有 CUDA 环境。Gluon 教程的具体硬件和版本需另查，不默认与已装 Triton 兼容。

## 真正用起来，还要考虑什么

论文或 kernel 曲线需对应完整归约语义；非整齐长度、累加顺序、重复测量与工作区都会改变判断。一个 Nsight 指标不能单独证明根因。

**写进本周报告**：复用已有正确性脚本，给报告增加同语义 torch.sum 的计时参考；若参考路径包含不同分配/启动开销，明确边界。用自己的归约图标出一次跨线程交换，解释布局为什么影响它。

## 下次更新时

检查 Gluon 接口是否仍 experimental、布局示例是否迁移；布局前沿只观察，主线保持两种 Reduce。更新写入 [开课记录](../../templates/weekly-refresh.md)，保留旧实验的配置。
