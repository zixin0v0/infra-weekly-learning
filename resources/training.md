# 通信与训练资料

[资料目录](README.md)

从每个 rank 持有什么数据开始，逐步读到梯度同步、状态分片与恢复。先用小例子对齐语义，再把文档中的接口接到自己的训练循环。

<a id="r-collective"></a>

### R-COLLECTIVE · 各 rank 的输入输出

**中文补充（按需，部分）：** 中文手动 allreduce 小函数；其余 collective 与 torchrun 仍查原文。 [对应范围](#cn-data-parallel)。

W7-S01 必读；中等；英文；Tensor、进程/设备区分。

**来源**：[NCCL Collective Operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html)；[torchrun 2.14](https://docs.pytorch.org/docs/2.14/elastic/run.html)。

**读到哪里**：四节 AllReduce、Broadcast、AllGather、ReduceScatter，30 分钟；运行前查 torchrun 的单机启动和 LOCAL_RANK，计入实现准备。停止于最小 2 rank 语义。

**带着什么问题读**：先分清求和与拼接；手算后运行并核对各 rank 输出，不能只看进程启动。 [打开练习与自查](../weeks/week-07-collectives/session-01.md)。

<a id="r-l7"></a>

### R-L7 · 通信、TP 和 PP 讲义

**中文补充（按需，部分）：** 中文 TP MLP 与 PP 概念；固定讲义代码/计量仍按原范围。 [对应范围](#cn-parallel)。

W7/W14 指定函数必读；中等；英文；对应单元前置。

**来源**：[CS336 lecture_07.py 固定提交](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_07.py)。

**读到哪里**：W7-S01：torch_distributed、collective_operations_main，15 分钟；S03：hardware、benchmarking、all_reduce，45 分钟。W14-S01：tensor_parallelism(_main)，20 分钟；S03：pipeline_parallelism(_main)，20 分钟。每次读到函数结束。

**带着什么问题读**：让图与具体张量对应，W7 不提前读 DDP/TP，W14 不重复 collective 入门。 [打开练习与自查](../weeks/week-07-collectives/README.md)。

<a id="r-nccl-tests"></a>

### R-NCCL-TESTS · 通信计时与两种带宽

**中文补充（按需，暂缺）：** algbw/busbw、构建与测量缺准确中文对应。 [对应范围](#cn-training-gaps)。

W7-S02 必读；中等；英文；四类 collective。

**来源**：[nccl-tests README](https://github.com/NVIDIA/nccl-tests/blob/b4d5beebca8a76cf01335f724d154b9b9d394d96/README.md)；[PERFORMANCE.md](https://github.com/NVIDIA/nccl-tests/blob/b4d5beebca8a76cf01335f724d154b9b9d394d96/doc/PERFORMANCE.md)。

**读到哪里**：构建/运行说明 20 分钟；Time、Algorithm bandwidth、Bus bandwidth → AllReduce 40 分钟；不读其他 collective 换算。

**带着什么问题读**：随机取日志一行换算 algbw 与 busbw；归一化指标不是 PCIe 链路直接采样。 [打开练习与自查](../weeks/week-07-collectives/session-02.md)。

<a id="r-ddp-start"></a>

### R-DDP-START · rank、模型副本与样本归属

**中文补充（按需，部分）：** 中文数据并行步骤；不是 DDP/DistributedSampler 接口教程。 [对应范围](#cn-data-parallel)。

W11-S01 必读；中等；英文文档配视频；先修 D、W7。

**来源**：[Multi GPU training with DDP](https://docs.pytorch.org/tutorials/beginner/ddp_series_multigpu.html)。

**读到哪里**：Constructing the process group → Constructing the DDP model → Distributing input data，45 分钟。只读单机文本示例，视频替换同段阅读，时间轴未核验；多机后置。

**带着什么问题读**：用样本 ID 核对 DistributedSampler 与 set_epoch，不把进程启动当作正确性。 [打开练习与自查](../weeks/week-11-ddp/README.md)。

<a id="r-ddp"></a>

### R-DDP · 梯度同步和公平更新

**中文补充（按需，部分）：** 中文梯度求和直觉；DDP 平均、不同步与恢复仍查原文。 [对应范围](#cn-data-parallel)。

W11-S02 必读；中等；英文；单卡参考已通过。

**来源**：[DDP 教程](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)。

**读到哪里**：Basic Use Case、Skewed Processing Speeds、Save and Load Checkpoints，60 分钟；停止于固定全局 batch 的 1/2 卡。no_sync 的累积实验只作拓展，先保持累积步数 1。

**带着什么问题读**：小例子核对等大小本地 mean loss 的平均梯度，再测相同样本数的 step 与吞吐。 [打开练习与自查](../weeks/week-11-ddp/README.md)。

<a id="r-amp"></a>

### R-AMP · 精度与输入路径的分离

**中文补充（按需，暂缺）：** autocast/GradScaler 与异步加载调优缺合适中文对应。 [对应范围](#cn-training-gaps)。

W11-S03 必读概念；中等；英文；FP32 单卡/DDP、[W1 数值精度](../weeks/week-01-foundations/session-04.md)、[W6 显存寿命](../weeks/week-06-attention/session-04.md)。

**来源**：[AMP recipe](https://docs.pytorch.org/tutorials/recipes/recipes/amp_recipe.html)；[Performance Tuning Guide](https://docs.pytorch.org/tutorials/recipes/recipes/tuning_guide.html)。

**读到哪里**：AMP 的 Adding torch.autocast、Adding GradScaler、All together，原文起步估计 30 分钟；Enable asynchronous data loading and augmentation，15 分钟。到 dtype 与输入等待概念停止；AMP 实验可选，[S4 的 Dataset/DataLoader 与输入等待对照](../course/bridges/s04.md#s4) 必做，更复杂的预取优化留作拓展。

**带着什么问题读**：列状态 dtype 表；autocast 不等于所有状态减半，卡数/精度/输入路径分别比较。 [打开练习与自查](../weeks/week-11-ddp/README.md)。

<a id="r-zero"></a>

### R-ZERO · 训练状态分片的对象

**中文补充（按需，部分）：** 中文三阶段分片分类；账本假设、其余状态仍按原论文。 [对应范围](#cn-sharding)。

W12-S01 必读；进阶起步；英文论文；W11 状态表。

**来源**：[ZeRO v3](https://arxiv.org/pdf/1910.02054v3)。

**读到哪里**：§3.1～3.2 模型与其余状态 → §5.1～5.3 三阶段，45 分钟；停止于分片对象，不读 offload。

**带着什么问题读**：用自己的 FP32/Adam 假设建立理论表，另外列激活、通信缓冲和重聚合峰值。 [打开练习与自查](../weeks/week-12-fsdp/README.md)。

<a id="r-fsdp"></a>

### R-FSDP · FSDP2 参数聚合与分片

**中文补充（按需，暂缺）：** 已核验的 FSDP2 fully_shard/DTensor 中文教程待补，不能用 FSDP1。 [对应范围](#cn-training-gaps)。

W12-S02 必读；进阶；英文；W11 与 R-ZERO。

**来源**：[FSDP2 教程](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)。

**读到哪里**：Model Initialization → Forward/Backward with Prefetching → Gradient Clipping and Optimizer with DTensor，75 分钟。先读默认路径，额外预取调参后置。optimizer 在 fully_shard 后创建；不混用 FSDP1 包装器。

**带着什么问题读**：画参数 gather/reshard 与梯度通信；保持模型、精度、batch 相同，完整 optimizer step 后比峰值。 [打开练习与自查](../weeks/week-12-fsdp/README.md)。

<a id="r-dcp"></a>

### R-DCP · 模型、优化器与应用状态恢复

**中文补充（按需，暂缺）：** DCP + FSDP2 完整状态恢复缺匹配中文材料。 [对应范围](#cn-training-gaps)。

W12-S03 必读；进阶；英文；先修 D 的单卡恢复、W12-S02。

**来源**：[FSDP2 State Dict with DCP APIs](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)；[DCP 教程](https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html)。

**读到哪里**：先看 FSDP2 同名小节，再读 DCP How DCP works、Saving、Loading 中 AppState/get_state_dict/set_state_dict；75 分钟。停在同 world size；RNG/步数/数据位置按自己的状态清单补齐。

**带着什么问题读**：指定 DCP 例子使用 fully_shard；开始运行前核对两页与安装版本。重启后比较下一步，不用“文件存在”代替恢复正确。 [打开练习与自查](../weeks/week-12-fsdp/README.md)。

<a id="r-megatron"></a>

### R-MEGATRON · TP 的两层 MLP 代数

**中文补充（按需，部分）：** 中文两层 MLP/f/g；bias、Attention 切分仍查原文。 [对应范围](#cn-parallel)。

W14-S01 必读；进阶起步；英文论文；矩阵、collective、DDP/FSDP 概念。

**来源**：[Megatron-LM v4](https://arxiv.org/pdf/1909.08053v4)。

**读到哪里**：§3 Model Parallel Transformers 的 MLP/Attention 切分，30 分钟；先看本地无 bias 数字例子，停在切分，不读大模型性能结果。

**带着什么问题读**：列切第一层、行切第二层；解释非线性不能随意穿过求和，CPU 合并先对齐。 [打开练习与自查](../weeks/week-14-parallelism/README.md)。

<a id="r-parallel"></a>

### R-PARALLEL · TP 通信与 PP 流水线

**中文补充（按需，部分）：** 中文 TP/PP 概念；Interleaved 调度与配置字段仍查原文。 [对应范围](#cn-parallel)。

W14-S02/S03 必读；中等；英文；R-MEGATRON、W7。

**来源**：[Megatron Bridge Parallelisms Guide](https://docs.nvidia.com/nemo/megatron-bridge/latest/parallelisms.html)。

**读到哪里**：S02 Tensor Parallelism 50 分钟含读图；S03 Pipeline Parallelism、Interleaved Pipeline Parallel Schedule 概念 30 分钟，配 R-L7 20 分钟。配置字段只帮助理解，停止于 2 stage 前向时间线。

**带着什么问题读**：标通信 shape 与输出合并；不部署 Megatron，不把前向流水线当完整训练调度。 [打开练习与自查](../weeks/week-14-parallelism/README.md)。

## 中文补充：先分清数据、梯度与保存状态

<a id="cn-data-parallel"></a>

### CN-DP：每张卡计算什么，最后怎样合起来

**中文视频：** 李沐，2021 [多 GPU 训练](https://www.bilibili.com/video/BV1vU4y1V7rd/)，关注拆分 batch、合并梯度与同步更新。

**中文正文：** 作者团队[§12.5 多 GPU 训练](https://zh.d2l.ai/chapter_computational-performance/multiple-gpus.html)，W11 读 §12.5.2 的数据并行步骤；W7 只看 §12.5.4“数据同步”的 PyTorch `allreduce` 小函数，追踪求和后各 GPU 拿到的数据。

指定正文已预读；视频讲次由作者课表确认，字幕/画面未检查。这里用单进程手动加总来说明概念，不是 DDP/NCCL 实现。每卡 batch 相等是说明条件；原文扩大总 batch 的性能做法不能带入本课固定 global batch 的正确性比较。rank/LOCAL_RANK、DistributedSampler、梯度平均和通信重叠仍按原课核对。

<a id="cn-sharding"></a>

### CN-Sharding：先看分片的是哪一类状态

**中文图文：** Datawhale《DIY-LLM》[第八章：分布式训练](https://datawhalechina.github.io/diy-llm/chapter8/chapter8_第八章分布式训练.html)，只读 §8.2.1 中“ZeRO 解决 DP（数据并行）的内存开销问题”标题下、从颜色说明到 120 GB → 31.4 GB → 16.6 GB → 1.9 GB 的三阶段解释；在“第一步”操作前停止。

这是社区对相关课程和论文的中文整理，不是本仓库 CS336 2026 讲义的逐段译文。限定文字已预读，适合 W12 区分 optimizer、gradient、parameter 的分片；图中数字有特定模型、精度与卡数假设，不是普遍每参数字节数。只借其分片分类，不采用后续通信量概括和旧包装器代码。**FSDP2 fully_shard、DTensor 与 DCP 完整恢复的中文对应仍缺**，实现继续使用 R-FSDP/R-DCP。

<a id="cn-storage"></a>

### CN-Storage：容器退出与文件消失不是同一个条件

**中文图文首选：**《Docker — 从入门到实践》[8.1 数据卷](https://yeasy.gitbook.io/docker_practice/di-er-bu-fen-jin-jie-pian/08_data/8.1_volume)，读 8.1.1～8.1.3 的生命周期，再看 8.1.5 的 source/target 参数说明。不要顺着读清理、删除和 prune；本课只操作自己创建的练习数据。

**不同用途的补充：** AWS 官方中文 [什么是 Amazon S3](https://docs.aws.amazon.com/zh_cn/AmazonS3/latest/userguide/Welcome.html)，读“存储桶”的第一段定义，跳过桶类型清单，再读“对象”“密钥”的术语解释。“密钥”在这里对应 object key，即对象名称，不是登录凭据。理解 bucket + key 后回到本课画路径，不需要云账户。

限定概念段落已预读。GitBook 动态命令块未作为已核验操作；实际挂载仍按 S5。AWS 页面为官方发布的中文译文。数据卷、对象存储与 DCP 不是同一层次；卷可读仍不能证明恢复后下一步一致。权重文件的中文示例另见 [CN-Save](foundations.md#cn-save)。

<a id="cn-parallel"></a>

### CN-Parallel：把两层 MLP 的切分画在同一张纸上

**中文图文：** Datawhale [DIY-LLM 第八章](https://datawhalechina.github.io/diy-llm/chapter8/chapter8_第八章分布式训练.html)的 §8.2.2“张量并行”中，从 `Y=GeLU(XA)` 两层 MLP 例子读到前向/反向的 f、g 同步点解释；在后面的性能百分比和经验卡数之前停止。先会 W4 矩阵维度、W7 求和，再对照本课 A/B 切分。

限定推演已预读；属于中文社区整理。文章省略了本课要单独检查的 bias，不能因此漏算或重复加。PP 可用 NVIDIA 中文[推理优化](https://developer.nvidia.cn/blog/mastering-llm-techniques-inference-optimization/)中的“管道并行”理解按层分设备；它不覆盖完整训练流水线。W14 的微批次时间线仍按原课；不加入交错调度实现。

<a id="cn-training-gaps"></a>

### 中文覆盖到概念，还没覆盖哪些接口

数据加载可回看 [CN-Train](foundations.md#cn-training)的读取 batch；它没有验证多 worker 等待。AMP 的 autocast/GradScaler、NCCL tests 的 algbw/busbw、FSDP2/DCP、完整 PP 训练调度、Profiler 通信重叠，尚未接入与现有范围匹配且已预读的中文说明。不能用旧 FSDP1、单进程 DataParallel 或“求和后除卡数”的无条件公式补这些缺项。
