# 环境与硬件安排

硬件来自用户提供的路线：本地 RTX 4060 Laptop 8GB，服务器 4 × RTX 4090 24GB。本轮仅据此规划，尚未探测设备、驱动、服务器权限或 GPU 互连。

## 按阶段选择环境

| 单元 | 建议环境 | 说明 |
| --- | --- | --- |
| W1 | Windows 或 Linux，CPU 可完成 | C++ 编译、Tensor 与资源计算 |
| W2～W6 | 本地 GPU；优先统一到 WSL2/Linux | CUDA、Triton 和 profiler 的支持范围分别核对 |
| W13，紧接 W6 | 沿用小 Block 环境，优先 Linux 单卡 | 单独确认 torch.compile 可用，记录编译成本 |
| W7 | Linux 服务器，先2卡，4卡选做 | 先记录拓扑，再测 NCCL |
| W8～W10 | Linux 服务器，单张4090 | 先建立单卡服务基线 |
| W11～W12、W14 | Linux 服务器，先2卡，4卡选做 | 控制模型规模与全局 batch；W14 可先在 CPU 验证代数 |
| W15～W16 | Linux；先 CPU 模拟，再小型 GPU 作业 | 单机实验，不提前引入集群部署 |

## Windows 与 Linux 的边界

[Triton 上游兼容说明](https://github.com/triton-lang/triton#compatibility) 列出 Linux；[vLLM GPU 安装文档](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/) 也以 Linux 为运行环境，并说明 Windows 可采用 WSL。仓库主线因此采用 Linux 工具链。

使用本地 WSL2 前，按 [NVIDIA CUDA on WSL 指南](https://docs.nvidia.com/cuda/wsl-user-guide/index.html) 核对 Windows 驱动、发行版和 profiling 限制。某项计数器不可用时记录限制，再迁移该实验到服务器；不能将 CPU 结果当成 GPU 性能结果。

W7 的 NCCL 实验安排在服务器。[PyTorch DDP 教程](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html) 对 Windows 后端另有说明，不能照搬 Linux NCCL 启动假设。

## 每个实验记录的环境信息

- 操作系统、是否 WSL/容器、CPU、内存、GPU 型号及数量。
- 驱动版本、CUDA Toolkit、Python、PyTorch 及本实验所用的 Triton/NCCL/vLLM/Ray 版本。
- 依赖锁定文件或导出的依赖列表、第三方仓库 commit/tag。
- GPU 可见设备、显存余量、电源模式、是否存在其他作业。
- 多卡实验额外记录 GPU 拓扑与通信后端，不根据 GPU 数量假设存在高速互连。

下面是未来实验开始时的只读检查命令，不代表本轮已运行；未安装某个工具时按实际记录缺失。

```text
nvidia-smi
nvcc --version
python --version
python -m torch.utils.collect_env
```

## 版本管理方式

各阶段开始前完成 [先修检查 A](prerequisites.md) 中相应的最小运行验证。正式性能实验前记录依赖锁文件或版本清单；环境调试时间超出预算时单独安排，不挤占正确性检查。多卡环境尚未就绪时，可先完成满足先修条件的单卡推理。

算子实验、vLLM 服务和 CS336 作业分别使用独立环境。在线文档的 `latest`、`stable` 和 `main` 会变化，实际运行前对照安装版本；不要为这份计划预先把所有框架安装到同一环境。

W1～W6 和 W13 先选择能在8GB显存中完成的小输入。模型权重、KV Cache、激活、框架开销要分别估算；W8 选模型时再核对配置与显存需求。
