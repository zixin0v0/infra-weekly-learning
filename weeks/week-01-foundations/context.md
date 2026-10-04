# W1 补充阅读：Tensor 表示与资源账本

[返回本单元](README.md) · [来源登记](../../resources/optional.md#s01)

资料快照：2026-10-01。开始学习复核：[已完成](../../docs/audits/2026-10-01-week-01.md)。本地状态：C++ / PyTorch CPU 最小运行检查已通过；学习练习与低精度实现尚未运行。

完成本单元后，若想继续了解这个问题，再读下面的指定范围。选读前核对当前版本与设备条件；页面保留 2026-10-01 的来源快照，没有把旧结论重新标为已验证。

## 从已经做过的实验出发

先用普通 dense Tensor 的 FP32 结果建立账本，再选 FP16 或 BF16 作对照，比较存储、布局和误差。框架负责张量与算子；C++ 数组用于理解地址和生命周期。第一周先把 dtype、stride 和 storage 学清楚，量化实现放到后面。

## 接着想清一个问题

把“元素占几个字节”推进到“打包数据、scale、padding 和执行 kernel 共同决定存储与性能”。只认识这个变化，量化算法和质量评估留到推理分支。

**读哪里**：[TorchAO 的低精度表示](https://docs.pytorch.org/ao/stable/contributing/quantization_overview.html)。Quantized Tensors (derived dtypes and packing format)、Quantization Primitive Ops；再在 Inference Workflows 查 NVFP4DynamicActivationNVFP4WeightConfig 的支持条件。 配套：[Inference Workflows](https://docs.pytorch.org/ao/stable/workflows/inference.html)。

**来源快照中的状态**：官方文档已描述量化工作流，但功能成熟度按配置区分；快照所查 NVFP4 动态激活/权重量化配置仍标 prototype，要求 SM100+。不能把这个限制推广到所有量化方法。

**2026-10-01 的来源记录**：[TorchAO v0.18.0](https://github.com/pytorch/ao/releases/tag/v0.18.0) 新增 dense Linear 的 NVFP4 训练原型，示例要求 SM100+、BF16 模型和可被 128 整除的 Linear 维度，最低 PyTorch 为 2.11；快照访问时的 stable 文档仍标 0.17，两种来源分开记录。该训练路径只作同一低精度方向的观察，不增加 W1 练习。

**设备条件**：W1 使用已完成最小运行检查的 Windows CPU 环境，本机 PyTorch 为 2.5.1。C++ 运行时需在当前进程优先使用 g++ 目录，方法见 [第一段学习指南](session-01.md)。计划中的 RTX 40 系列不能据此假定能运行 SM100+ 路径；不安装该前沿配置。

## 真正用起来，还要考虑什么

论文中的理想位宽压缩率还需要计入元数据、对齐、解量化、算子覆盖和精度变化。共享视图的逻辑字节数也不能简单相加成实际分配量。

**选读后可写进报告**：在第三段账本报告加一行假设算例：N=1024 个 4-bit 值、每组32个值带一个 FP32 scale，忽略 padding 时为512+128=640字节；这是格式假设，不是 NVFP4 实际存储公式。与 FP16 的2048字节比较，再列出尚未计入项。

## 选读前核对

核对配置的 prototype/硬件状态与实际存储格式。只要基础 Tensor 语义未变，保留原单元课表；新格式不挤掉视图与复制练习。
