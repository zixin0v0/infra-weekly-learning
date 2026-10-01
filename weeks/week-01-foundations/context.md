# W1 补充阅读：Tensor 表示与资源账本

[范围与验收](README.md) · [三段导学](study-guide.md) · [更新流程](../../docs/weekly-refresh.md) · [来源登记](../../resources/frontier-watchlist.md#s01)

资料快照：2026-10-01。开课复核：待进行。本地状态：仅阅读，相关实现尚未运行。

开课前用30分钟核对本页资料。这里的练习并入本周报告，额外实现留作选修。

## 现在怎样做

先用普通 dense Tensor 的 FP32 结果建立账本，再选 FP16 或 BF16 作对照，比较存储、布局和误差。框架负责张量与算子；C++ 数组用于理解地址和生命周期。第一周先把 dtype、stride 和 storage 学清楚，量化实现放到后面。

## 这一方向还有哪些进展

把“元素占几个字节”推进到“打包数据、scale、padding 和执行 kernel 共同决定存储与性能”。只认识这个变化，量化算法和质量评估留到推理分支。

**读哪里**：[TorchAO 的低精度表示](https://docs.pytorch.org/ao/stable/contributing/quantization_overview.html)。Quantized Tensors (derived dtypes and packing format)、Quantization Primitive Ops；再在 Inference Workflows 查 NVFP4DynamicActivationNVFP4WeightConfig 的支持条件。 配套：[Inference Workflows](https://docs.pytorch.org/ao/stable/workflows/inference.html)。

**目前的状态**：官方文档已描述量化工作流，但功能成熟度按配置区分；本次所查 NVFP4 动态激活/权重量化配置仍标 prototype，要求 SM100+。不能把这个限制推广到所有量化方法。

**在我们的设备上**：W1 主线可用 CPU。计划中的 RTX 40 系列不能据此假定能运行 SM100+ 路径；不安装该前沿配置。

## 真正用起来，还要考虑什么

论文中的理想位宽压缩率还需要计入元数据、对齐、解量化、算子覆盖和精度变化。共享视图的逻辑字节数也不能简单相加成实际分配量。

**写进本周报告**：在第三段账本报告加一行假设算例：N=1024 个 4-bit 值、每组32个值带一个 FP32 scale，忽略 padding 时为512+128=640字节；这是格式假设，不是 NVFP4 实际存储公式。与 FP16 的2048字节比较，再列出尚未计入项。


## 下次更新时

核对配置的 prototype/硬件状态与实际存储格式。只要基础 Tensor 语义未变，保留原三段导学；新格式不挤掉视图与复制练习。 更新写入 [开课记录](../../templates/weekly-refresh.md)，保留旧实验的配置。
