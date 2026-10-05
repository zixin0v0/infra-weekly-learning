# W5 第 1 段：一个 program 负责多少数据？

[本单元](README.md) · [课程目录](../../course/README.md)

先用 [W1 的范围与精度](../week-01-foundations/session-04.md) 解释为什么有限输入也可能在指数运算中溢出，再推导这里的稳定写法。

Triton 的表达式看起来像在处理一组向量，但这一组并不等于一个 CUDA 线程。先把逻辑数据块的偏移和有效范围写清楚，再让编译器组织底层执行。

## 视频与正文

先看 [CS336 2026 Lecture 6](https://www.youtube.com/watch?v=xnDHaNUvHBg)：Triton 的 program 与 kernel；看到索引表达式先遮住 mask，预测尾部行为。

视频分钟位置待核验；找不到对应主题时，按下列正文范围阅读。重复内容只需回查。

## 目标与先修

把 W2 的数组覆盖映射到 Triton program，解释 arange 与 mask。先通过 W4；运行前确认目标 Linux/WSL2、所选 Triton/PyTorch 与最小 kernel，实际运行状态以自己的环境记录为准。

## 读哪里，在哪里停

| 阅读参考 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 15 分钟 | [CS336 L6 视频](../../resources/gpu.md#r-l6)，配 [固定讲义](../../resources/gpu.md#r-l6) 的 triton_introduction | 只看引入与编程映射；不读后续其他算子 |
| 20 分钟 | [Vector Addition 教程](../../resources/gpu.md#r-triton) 的 Compute Kernel、add_kernel 与封装 add | offsets、load/store mask、grid 结束 |
| 10 分钟 | [Triton Semantics](../../resources/gpu.md#r-triton) 的 Broadcasting、Type Promotion | shape 扩展与浮点类型提升示例结束 |

访问日：2026-10-01。网站是 main 浮动文档；[源码快照](../../resources/gpu.md#r-triton) 固定阅读代码，不能拿此开发提交冒充已安装版本。

## 中文补充（按需）

HyperAI 社区译文[向量相加](https://triton.hyper.ai/docs/getting-started/tutorials/vector-addition/)，读 `add_kernel` 与 `add`，到基准测试前；先圈出 program_id、offset 和 mask，再追 grid。指定正文已预读。它对应 Triton 上游教程，但版本未固定到本课 commit；实现仍用原课代码，不能把一个 program 直接当作一个 CUDA thread。[范围与版本](../../resources/gpu.md#cn-triton)。

## 先理解一块数据，再比较两种编程方式

`arange(0, BLOCK_SIZE)` 产生这一块内的位置，`program_id` 选择当前块。两者相加后的 offsets 决定读写哪些数据；load 和 store 各有自己的边界，保护输出并不能挽救已经发生的越界读取。

回看 [W2 的线程覆盖图](../week-02-cuda-execution/session-01.md)：覆盖数组的算术相同，但图中的线程不是 Triton 的 program。一个 program 处理多个逻辑元素，内部如何映射到硬件线程需要由编译器和实际配置决定。

一个 program 处理一个逻辑数据块，内部数据怎样映射到线程由编译器组织；program 不是单个 CUDA 线程。`program_id × BLOCK_SIZE + arange` 给出这一块的偏移，load/store 的 mask 限制有效元素。

长度 10、逻辑块 4 的纸面映射与 W2 一样覆盖 [0..3]、[4..7]、[8..11]；硬件执行映射不能据此认定完全相同。BLOCK_SIZE 等编译参数与运行时 N 的职责不同。

广播先对齐尾部维度，长度为 1 的维度可扩展；(3,1)+(1,4) 得到 (3,4)，不表示必须先复制成两份完整大矩阵。FP16 与 FP32 张量相加按该页规则提升到 FP32；最终写回更低精度容器仍可能发生转换。

## 暂停题与预测

1. 第 2 号 program 的 offsets 与有效 mask 是什么？只在 store 加 mask、load 不加会怎样？
2. N 改为 13 或 BLOCK_SIZE 改变时，grid 怎样变化？代码更短能否证明访问更少？

3. (3,1)+(1,4) 的输出形状是什么？FP16 与 FP32 输入相加用什么类型？

先区分“逻辑数据块”和“硬件线程”，再画三个 program，最后回 add_kernel 与 add。

## 读图与自查

```text
N=10，BLOCK_SIZE=4（手算例）
program 0：offsets [0,1,2,3]    mask [真,真,真,真]
program 1：offsets [4,5,6,7]    mask [真,真,真,真]
program 2：offsets [8,9,10,11]  mask [真,真,假,假]
                              load 与 store 都要检查
```

图中的一行是逻辑数据块，不是一个硬件线程，也不承诺对应一个 warp。比较 W2 的索引图：覆盖算法相似，编程抽象不同。

<details>
<summary>写下预测后，再核对本段问题</summary>

**题 1**：第 2 号 program 偏移为 8、9、10、11，只允许前两个位置访问。只保护 store 仍会在 load 时越界。

**题 2**：N=13、BLOCK_SIZE=4 时 grid=ceil(13/4)=4，最后一块仅一个有效元素。改变 BLOCK_SIZE 后重新向上取整。代码行数不衡量访存次数，需数实际逻辑读写，执行映射还由编译器处理。

**题 3**：输出为 (3,4)，参与运算的类型提升到 FP32。形状扩展与类型提升是两个独立规则，不能由一个推出另一个。

保留自己的推导，再与实际结果比较。若不一致，按下面的回看位置找出最早出现差异的一步。

</details>

## 可选：问 AI

先独立作答和核对，仍有疑问时再使用；跳过本节不影响完成本段。

> 我把一个 Triton program 理解为【解释】，offsets 和 mask 表是【粘贴】。请指出它和 CUDA thread/warp 最容易混淆的一处，再给一个尾块练习。先让我回答，不要直接照抄教程代码或推断底层线程映射。

## 动手与检查

实验目录：`labs/03-triton-attention/softmax/`。Vector Add 是本周环境/映射热身，输入与检查复用 W2，动手时保存为 `vector_add_triton.py`，不另建项目。

先对 1、10、257 个 FP32 元素逐元素核对，再测一个较大输入。固定数据与计时边界；本段以正确性为主，不要求抄教程全部调优配置。记录实际包版本与支持条件；环境不可用时保留纸面映射，GPU 检查待补。

## 结果不对时，从哪里查起

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 尾部错误 | add_kernel 的 offsets 与两处 mask | load/store 是否都保护边界 |
| 改 N 后漏元素 | add 的 grid | 启动数量是否向上取整 |

- [ ] 独立画 program 覆盖范围。
- [ ] 环境最小运行与边界输出有真实证据。
- [ ] 运行参数、编译参数和未支持项区分清楚。

在 `notes.md` 的 `W5-S01` 留下预测、命令与限制；通过后进入 [第二段](session-02.md)。

## 完成后

把代码、预测与实际结果记在同一份笔记中。完成本段检查后，沿下方链接继续。

[上一课](README.md) · [下一课](session-02.md)
