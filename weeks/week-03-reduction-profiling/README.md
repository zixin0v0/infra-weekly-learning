# 单元 W3：Reduce 与性能分析

[课程目录](../../course/README.md) · [我的进度](../../course/progress.md) · [环境准备](../../course/environment.md)

预计 10～18 小时用于本单元，变式与排错另留 1～3 小时；桥接只计新发生的时间。按实际掌握推进，记录规则见 [学习方法](../../course/guide.md#time-budget)。

## 这一单元要弄清什么

几千个线程各算出一个部分和，谁来得到最后的总和？本单元先追踪树形归约，再比较共享内存与 warp 内交换两种实现。结果对齐之后，用计时和 profiler 检查同步、访存与资源占用，说明两个正确版本为什么仍可能快慢不同。

## 开始前

完成 W2 的尾部保护、错误检查和同步计时。先解释：同一 block 的线程共享数据时，为什么需要等待彼此？如果这一点还不清楚，回看 [W2 内存与同步](../week-02-cuda-execution/session-02.md)。

<details>
<summary>先解释，再展开核对</summary>

block barrier 要求参与路径满足同步约束；越界线程不能在其他线程执行 block barrier 前随意提前返回。回 W2 内存与错误段核对。

</details>

## 按顺序学习

- [W3 第 1 段：很多线程的结果，怎样合成一个数？](session-01.md)。
- [W3 第 2 段：warp 内能交换，为什么还需要共享内存？](session-02.md)。
- [W3 第 3 段：指标变好了，为什么程序没有变快？](session-03.md)。

- [本单元掌握检查](assessment.md)：实验完成要求、变式与排错题。

## 实践任务

建议目录：labs/02-cuda/reduction/。

1. 写共享内存树形归约与 warp shuffle 归约两个版本，保留相同数学语义。
2. 覆盖小输入、非整除输入和包含负值的输入；为浮点归约设置合适容差。
   对小型输入另做共享内存访问与同步检查。racecheck 主要检查共享内存访问危险，不能据此声称排除了所有并发问题。
3. 在相同输入与启动条件下计时；单独对一个有代表性的输入采集 Nsight 报告。
4. 选一条假设，用对应指标和受控比较检查它。只凭利用率截图不能证明瓶颈。
5. 整理短报告《我的 Reduce 优化省掉了什么，证据在哪里？》。

两个 GPU kernel 都输出每 block 部分和，随后用同一个 CPU FP64 函数收尾。性能主表比较 GPU 第一阶段，完整流程时间另列；`torch.sum` 可作为完整归约库参考，不能与第一阶段直接计算加速比。多级 GPU 收尾留作扩展。

## 按需回看

[PyTorch Profiler 教程](../../resources/models.md#r-trace)：Python 调用链不清楚时选读。优先学会回答一个问题，不在同一周同时掌握所有 profiler。

[上一单元](../week-02-cuda-execution/README.md) · [下一步](../week-04-gemm/README.md)
