# 单元 W15：Ray 任务与资源

[课程目录](../../course/README.md) · [我的进度](../../course/progress.md) · [环境准备](../../course/environment.md)

预计 12～22 小时用于本单元，变式与排错另留 1～3 小时；桥接只计新发生的时间。按实际掌握推进，记录规则见 [学习方法](../../course/guide.md#time-budget)。

## 这一单元要弄清什么

提交一个函数后，拿到的 ObjectRef 为什么还不是计算结果？你会把普通函数改成 Task，用 Actor 保存状态，再记录提交、开始、结束与重试。改变资源声明之后，从日志判断任务是在等待资源、等待依赖，还是已经执行出错。

## 开始前

能写函数、类与 JSON 文件，并完成 [先修 A](../../course/prerequisites.md)。第一段前做 [S6 的依赖图、准入与重试](../../course/bridges/s06.md#s6)，类不熟时回 [P8](../../course/foundations/p08.md)。课程安排在 W14 后；CPU Task 本身不依赖训练性能实验。

<details>
<summary>先解释，再展开核对</summary>

两个独立 Counter 对象应各自保存计数；函数返回值和指向未来结果的引用不是同一种对象。Python 类回 P8 复习。

</details>

## 按顺序学习

- [S6 的任务依赖图与资源准入](../../course/bridges/s06.md)。
- [W15 第 1 段：函数返回的是结果，还是指向未来结果的引用？](session-01.md)。
- [W15 第 2 段：声明一个 CPU，是否真的只用一个线程？](session-02.md)。
- [W15 第 3 段：任务没开始，是资源忙、永远放不下，还是已经失败？](session-03.md)。

- [本单元掌握检查](assessment.md)：实验完成要求、变式与排错题。

## 实践任务

建议目录：labs/07-scheduling/ray-basics/。

1. 写几个有已知输入与输出的 Task，再用 Actor 保存一个简单状态。
2. 显式声明资源，提交一组任务，记录提交、开始、结束时间和执行设备。
3. 改变任务数与资源请求，观察等待与并发；先用 CPU 验证记录逻辑。
4. 有可用 GPU 时运行小型计算任务，并记录真实 GPU 占用；模拟任务明确标记。
5. 说明 Ray 的资源是调度层面的逻辑约束；num_gpus 或自定义 memory 资源不能自动构成显存硬隔离。

## 按需回看

API 有疑问时，查 [Tasks 与 ray.remote 示例](../../resources/scheduling.md#r-ray-task)，暂不阅读调度器 C++ 内部实现。

[上一单元](../week-14-parallelism/README.md) · [下一步](../week-16-scheduling/README.md)
