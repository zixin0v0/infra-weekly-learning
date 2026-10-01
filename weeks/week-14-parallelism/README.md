# 单元 W14：TP、PP 与 Megatron

[总路线](../../README.md) · [学习方式](../../docs/learning-workflow.md) · [资源索引](../../resources/README.md) · [当前做法与相关进展](context.md)

建议学习位置：第 14 个学习周。W14 是固定单元 ID，按下方导航推进。

状态：未开始。预算：约 10.5 小时（[分项](../../docs/study-guide.md#time-budget)）。环境：Linux 服务器，2 卡即可起步。

## 本周要解决什么

用一个 Transformer 层理解 Tensor Parallel 与 Pipeline Parallel 的切分和通信。

先修：集合通信、DDP/FSDP2 与 GEMM。要回答：一个权重矩阵按哪一维切？输出如何组合？流水线为何会产生气泡？

## 按顺序学习

先用 30 分钟按 [资料复核流程](../../docs/weekly-refresh.md) 核对必读材料、版本和运行条件。[补充阅读](context.md) 在基础完成后选读，单独安排时间。

按 [分段学习指南](study-guide.md) 分三段学习，每段读完就动手。下面只列安排，具体链接、阅读位置和检查方法都在学习指南里。

| 学习段 | 指定范围 | 读后立即做 | 资料预算 |
| --- | --- | --- | --- |
| 1. TP 代数 | Megatron §3；CS336 L7 tensor_parallelism | 两层 MLP 切分图 | 50 分钟 |
| 2. 通信与形状 | Bridge 的 Tensor Parallelism；复用 W7 | 切分与未切分数值对齐 | 50 分钟 |
| 3. PP 时间线 | Bridge 的 PP 两节；L7 pipeline_parallelism | 2 stage 气泡与不均衡分析 | 50 分钟 |

原文选读共 150 分钟，本地图解与自查另计 60 分钟。材料元信息统一在资源索引；可选拓展另排时间。

## 遇到问题再看

回看W4 GEMM 与W7 collective 的实验。CP、EP 暂作术语了解，不加入本周实现范围。

## 实践任务

建议目录：labs/06-training/parallelism/。

1. 给两层 MLP 画张量 shape、权重切分方式、各 rank 的输入输出和通信位置。
2. 用 CPU 张量或 2 卡小实验验证一种 TP 切分，和未切分计算对齐。
3. 画一个 2-stage pipeline 的 microbatch 时间线，解释气泡；实际 PP 训练作为扩展。
4. 写出计算、通信、等待的成本分解，联系现有机器拓扑说明预测。
5. 明确哪些是实测，哪些只是成本估算或时间线演示。

## 验收

- [ ] 每一处通信能指明数据 shape 与 collective 类型。
- [ ] 至少一种切分通过数值对齐。
- [ ] 能区分数据并行、张量并行和流水线并行的粒度。
- [ ] 不将纸面分析或 CPU 模拟当成多卡加速结果。

可选：完成基础后，从补充阅读选一个实际问题写进报告；未选不影响本单元完成。

## 实验记录

实验与报告：尚未创建。自评与验收日期：待完成。

[上一单元](../week-12-fsdp/README.md) · [下一单元](../week-15-ray/README.md)
