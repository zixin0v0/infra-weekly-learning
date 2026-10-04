# 单元 W7：集合通信与 NCCL

[课程目录](../../course/README.md) · [我的进度](../../course/progress.md) · [环境准备](../../course/environment.md)

预计 10～18 小时用于本单元，变式与排错另留 1～3 小时；桥接只计新发生的时间。按实际掌握推进，记录规则见 [学习方法](../../course/guide.md#time-budget)。

## 这一单元要弄清什么

同样是两张卡交换数据，求和、广播和拼接会得到完全不同的结果。先为每个 rank 写出输入输出，再运行最小两卡实验，改变消息大小并观察延迟与带宽。最后把曲线放回真实互连拓扑，判断成本可能来自哪里。

## 开始前

复用 W1 的 Tensor、W2 的执行与同步计时，先完成 [S2 通信部分](../../course/bridges/s02.md#s2)。课程按 W13 后学习，但编译与训练不是通信语义的技术前提。实际实验需要至少两张可用 GPU；没有设备时可先推演，运行项继续留待完成。

<details>
<summary>先解释，再展开核对</summary>

rank0=[1,2]、rank1=[3,4] 做 SUM AllReduce 后双方都是 [4,6]。没有 2 卡只能完成纸面检查，不能标记通信实验完成。

</details>

## 按顺序学习

- [S2 的带宽、延迟与 rank](../../course/bridges/s02.md)。
- [W7 第 1 段：集合通信结束后，每个进程拿到什么？](session-01.md)。
- [W7 第 2 段：为什么报表里有两种带宽？](session-02.md)。
- [W7 第 3 段：同一段通信代码，换两张卡为什么会变慢？](session-03.md)。

- [本单元掌握检查](assessment.md)：实验完成要求、变式与排错题。

## 实践任务

建议目录：labs/04-collectives/allreduce/。

1. 记录服务器 GPU 拓扑、通信后端、NCCL 版本与可用卡数。
2. 用 nccl-tests 测 2 卡的多个消息大小，先从 KiB 到较小 MiB 范围开始，再视显存扩展。4 卡是进阶对照，单独记录完成状态。
3. 保存命令、原始日志与整理后的数据；注明 MB/MiB、延迟单位及带宽定义。
4. 扩展：跑通最小 DDP 示例并验证梯度同步；训练先修不足时将本项与完整训练对比一起放到W11。

## 按需回看

示例与带宽列含义优先回 [NCCL 语义](../../resources/training.md#r-collective) 和 [nccl-tests](../../resources/training.md#r-nccl-tests) 的指定范围。

通过 [单卡训练检查 D](../../course/prerequisites.md) 后，可选 [PyTorch DDP 入门](../../resources/training.md#r-ddp)；否则移到 W11。

[上一单元](../week-13-systems/README.md) · [下一步](../week-08-serving-baseline/README.md)
