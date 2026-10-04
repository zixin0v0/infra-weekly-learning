# 通信与训练资料

[资料目录](README.md)

从每个 rank 持有什么数据开始，逐步读到梯度同步、状态分片与恢复。先用小例子对齐语义，再把文档中的接口接到自己的训练循环。

<a id="r-collective"></a>

### R-COLLECTIVE · 各 rank 的输入输出

W7-S01 必读；中等；英文；Tensor、进程/设备区分。

**来源**：[NCCL Collective Operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html)；[torchrun 2.14](https://docs.pytorch.org/docs/2.14/elastic/run.html)。

**读到哪里**：四节 AllReduce、Broadcast、AllGather、ReduceScatter，30 分钟；运行前查 torchrun 的单机启动和 LOCAL_RANK，计入实现准备。停止于最小 2 rank 语义。

**带着什么问题读**：先分清求和与拼接；手算后运行并核对各 rank 输出，不能只看进程启动。 [打开练习与自查](../weeks/week-07-collectives/session-01.md)。

<a id="r-l7"></a>

### R-L7 · 通信、TP 和 PP 讲义

W7/W14 指定函数必读；中等；英文；对应单元前置。

**来源**：[CS336 lecture_07.py 固定提交](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py)。

**读到哪里**：W7-S01：torch_distributed、collective_operations_main，15 分钟；S03：hardware、benchmarking、all_reduce，45 分钟。W14-S01：tensor_parallelism(_main)，20 分钟；S03：pipeline_parallelism(_main)，20 分钟。每次读到函数结束。

**带着什么问题读**：让图与具体张量对应，W7 不提前读 DDP/TP，W14 不重复 collective 入门。 [打开练习与自查](../weeks/week-07-collectives/README.md)。

<a id="r-nccl-tests"></a>

### R-NCCL-TESTS · 通信计时与两种带宽

W7-S02 必读；中等；英文；四类 collective。

**来源**：[nccl-tests README](https://github.com/NVIDIA/nccl-tests/blob/b4d5beebca8a76cf01335f724d154b9b9d394d96/README.md)；[PERFORMANCE.md](https://github.com/NVIDIA/nccl-tests/blob/b4d5beebca8a76cf01335f724d154b9b9d394d96/doc/PERFORMANCE.md)。

**读到哪里**：构建/运行说明 20 分钟；Time、Algorithm bandwidth、Bus bandwidth → AllReduce 40 分钟；不读其他 collective 换算。

**带着什么问题读**：随机取日志一行换算 algbw 与 busbw；归一化指标不是 PCIe 链路直接采样。 [打开练习与自查](../weeks/week-07-collectives/session-02.md)。

<a id="r-ddp-start"></a>

### R-DDP-START · rank、模型副本与样本归属

W11-S01 必读；中等；英文文档配视频；先修 D、W7。

**来源**：[Multi GPU training with DDP](https://docs.pytorch.org/tutorials/beginner/ddp_series_multigpu.html)。

**读到哪里**：Constructing the process group → Constructing the DDP model → Distributing input data，45 分钟。只读单机文本示例，视频替换同段阅读，时间轴未核验；多机后置。

**带着什么问题读**：用样本 ID 核对 DistributedSampler 与 set_epoch，不把进程启动当作正确性。 [打开练习与自查](../weeks/week-11-ddp/README.md)。

<a id="r-ddp"></a>

### R-DDP · 梯度同步和公平更新

W11-S02 必读；中等；英文；单卡参考已通过。

**来源**：[DDP 教程](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)。

**读到哪里**：Basic Use Case、Skewed Processing Speeds、Save and Load Checkpoints，60 分钟；停止于固定全局 batch 的 1/2 卡。no_sync 的累积实验只作拓展，先保持累积步数 1。

**带着什么问题读**：小例子核对等大小本地 mean loss 的平均梯度，再测相同样本数的 step 与吞吐。 [打开练习与自查](../weeks/week-11-ddp/README.md)。

<a id="r-amp"></a>

### R-AMP · 精度与输入路径的分离

W11-S03 必读概念；中等；英文；FP32 单卡/DDP、[W1 数值精度](../weeks/week-01-foundations/session-04.md)、[W6 显存寿命](../weeks/week-06-attention/session-04.md)。

**来源**：[AMP recipe](https://docs.pytorch.org/tutorials/recipes/recipes/amp_recipe.html)；[Performance Tuning Guide](https://docs.pytorch.org/tutorials/recipes/recipes/tuning_guide.html)。

**读到哪里**：AMP 的 Adding torch.autocast、Adding GradScaler、All together，原文起步估计 30 分钟；Enable asynchronous data loading and augmentation，15 分钟。到 dtype 与输入等待概念停止；AMP 实验可选，[S4 的 Dataset/DataLoader 与输入等待对照](../course/bridges/s04.md#s4) 必做，更复杂的预取优化留作拓展。

**带着什么问题读**：列状态 dtype 表；autocast 不等于所有状态减半，卡数/精度/输入路径分别比较。 [打开练习与自查](../weeks/week-11-ddp/README.md)。

<a id="r-zero"></a>

### R-ZERO · 训练状态分片的对象

W12-S01 必读；进阶起步；英文论文；W11 状态表。

**来源**：[ZeRO v3](https://arxiv.org/pdf/1910.02054v3)。

**读到哪里**：§3.1～3.2 模型与其余状态 → §5.1～5.3 三阶段，45 分钟；停止于分片对象，不读 offload。

**带着什么问题读**：用自己的 FP32/Adam 假设建立理论表，另外列激活、通信缓冲和重聚合峰值。 [打开练习与自查](../weeks/week-12-fsdp/README.md)。

<a id="r-fsdp"></a>

### R-FSDP · FSDP2 参数聚合与分片

W12-S02 必读；进阶；英文；W11 与 R-ZERO。

**来源**：[FSDP2 教程](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)。

**读到哪里**：Model Initialization → Forward/Backward with Prefetching → Gradient Clipping and Optimizer with DTensor，75 分钟。先读默认路径，额外预取调参后置。optimizer 在 fully_shard 后创建；不混用 FSDP1 包装器。

**带着什么问题读**：画参数 gather/reshard 与梯度通信；保持模型、精度、batch 相同，完整 optimizer step 后比峰值。 [打开练习与自查](../weeks/week-12-fsdp/README.md)。

<a id="r-dcp"></a>

### R-DCP · 模型、优化器与应用状态恢复

W12-S03 必读；进阶；英文；先修 D 的单卡恢复、W12-S02。

**来源**：[FSDP2 State Dict with DCP APIs](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)；[DCP 教程](https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html)。

**读到哪里**：先看 FSDP2 同名小节，再读 DCP How DCP works、Saving、Loading 中 AppState/get_state_dict/set_state_dict；75 分钟。停在同 world size；RNG/步数/数据位置按自己的状态清单补齐。

**带着什么问题读**：指定 DCP 例子使用 fully_shard；开始运行前核对两页与安装版本。重启后比较下一步，不用“文件存在”代替恢复正确。 [打开练习与自查](../weeks/week-12-fsdp/README.md)。

<a id="r-megatron"></a>

### R-MEGATRON · TP 的两层 MLP 代数

W14-S01 必读；进阶起步；英文论文；矩阵、collective、DDP/FSDP 概念。

**来源**：[Megatron-LM v4](https://arxiv.org/pdf/1909.08053v4)。

**读到哪里**：§3 Model Parallel Transformers 的 MLP/Attention 切分，30 分钟；先看本地无 bias 数字例子，停在切分，不读大模型性能结果。

**带着什么问题读**：列切第一层、行切第二层；解释非线性不能随意穿过求和，CPU 合并先对齐。 [打开练习与自查](../weeks/week-14-parallelism/README.md)。

<a id="r-parallel"></a>

### R-PARALLEL · TP 通信与 PP 流水线

W14-S02/S03 必读；中等；英文；R-MEGATRON、W7。

**来源**：[Megatron Bridge Parallelisms Guide](https://docs.nvidia.com/nemo/megatron-bridge/latest/parallelisms.html)。

**读到哪里**：S02 Tensor Parallelism 50 分钟含读图；S03 Pipeline Parallelism、Interleaved Pipeline Parallel Schedule 概念 30 分钟，配 R-L7 20 分钟。配置字段只帮助理解，停止于 2 stage 前向时间线。

**带着什么问题读**：标通信 shape 与输出合并；不部署 Megatron，不把前向流水线当完整训练调度。 [打开练习与自查](../weeks/week-14-parallelism/README.md)。
