# W5 第一段学习指南：Triton program 与数据块

[单元范围](README.md) · [三段学习导航](study-guide.md) · [资料复核](refresh-2026-10-01.md)

整理日期：2026-10-01。原文选读预算：45 分钟。状态：学习指南已整理；Triton 环境与练习待验证。

本地图解、暂停题与核对另计入本单元的自查时段，完整时间见 [分项预算](../../docs/study-guide.md#time-budget)。

## 目标与先修

把 W2 的数组覆盖映射到 Triton program，解释 arange 与 mask。先通过 W4；运行前确认目标 Linux/WSL2、所选 Triton/PyTorch 与最小 kernel，本次未安装或运行。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 15 分钟 | [CS336 L6 视频](../../resources/README.md#r-l6)，配 [固定讲义](../../resources/README.md#r-l6) 的 triton_introduction | 只看引入与编程映射；不读后续其他算子 |
| 20 分钟 | [Vector Addition 教程](../../resources/README.md#r-triton) 的 Compute Kernel、add_kernel 与封装 add | offsets、load/store mask、grid 结束 |
| 10 分钟 | [Triton Semantics](../../resources/README.md#r-triton) 的 Broadcasting、Type Promotion | shape 扩展与浮点类型提升示例结束 |

访问日：2026-10-01。网站是 main 浮动文档；[源码快照](../../resources/README.md#r-triton) 固定阅读代码，不能拿此开发提交冒充已安装版本。视频分钟数未核验。

## 概念说明

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

这些说明用于核对推导；运行结果仍需自己验证。答错时保留原答案，回看本段“读哪里”或“卡点”指向的位置，再换一个小输入重做。

</details>

## 可选：问 AI

先独立作答和核对，仍有疑问时再使用；跳过本节不影响完成本段。

> 我把一个 Triton program 理解为【解释】，offsets 和 mask 表是【粘贴】。请指出它和 CUDA thread/warp 最容易混淆的一处，再给一个尾块练习。先让我回答，不要直接照抄教程代码或推断底层线程映射。

## 动手与检查

实验目录：`labs/03-triton-attention/softmax/`。Vector Add 是本周环境/映射热身，输入与检查复用 W2，动手时保存为 `vector_add_triton.py`，不另建项目。

先对 1、10、257 个 FP32 元素逐元素核对，再测一个较大输入。固定数据与计时边界；本段以正确性为主，不要求抄教程全部调优配置。记录实际包版本与支持条件；环境不可用时保留纸面映射，GPU 检查待补。

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 尾部错误 | add_kernel 的 offsets 与两处 mask | load/store 是否都保护边界 |
| 改 N 后漏元素 | add 的 grid | 启动数量是否向上取整 |

- [ ] 独立画 program 覆盖范围。
- [ ] 环境最小运行与边界输出有真实证据。
- [ ] 运行参数、编译参数和未支持项区分清楚。

在 `notes.md` 的 `W5-S01` 留下预测、命令与限制；通过后进入 [第二段](session-02.md)。
