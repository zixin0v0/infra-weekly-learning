# W5 第一段备课：Triton program 与数据块

[单元范围](README.md) · [三段导学](study-guide.md) · [资料复核](refresh-2026-10-01.md)

备课日期：2026-10-01。资料预算：45 分钟。状态：备课已准备；Triton 环境与练习待验证。

## 目标与先修

把 W2 的数组覆盖映射到 Triton program，解释 arange 与 mask。先通过 W4；运行前确认目标 Linux/WSL2、所选 Triton/PyTorch 与最小 kernel，本次未安装或运行。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 15 分钟 | [CS336 L6 视频](https://www.youtube.com/watch?v=xnDHaNUvHBg)，配 [固定讲义](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py) 的 triton_introduction | 只看引入与编程映射；不读后续其他算子 |
| 20 分钟 | [Vector Addition 教程](https://triton-lang.org/main/getting-started/tutorials/01-vector-add.html) 的 Compute Kernel、add_kernel | offsets、load/store mask 结束 |
| 10 分钟 | 同页封装 add | grid 与编译参数说明结束；Benchmark 留作已有计时方法对照 |

访问日：2026-10-01。网站是 main 浮动文档；[源码快照](https://github.com/triton-lang/triton/blob/aad2a60d958f945420c5c40936b37d411fb02e89/python/tutorials/01-vector-add.py) 固定阅读代码，不能拿此开发提交冒充已安装版本。视频分钟数未核验。

## 中文助读

一个 program 处理一个逻辑数据块，内部数据怎样映射到线程由编译器组织；program 不是单个 CUDA 线程。`program_id × BLOCK_SIZE + arange` 给出这一块的偏移，load/store 的 mask 限制有效元素。

长度 10、逻辑块 4 的纸面映射与 W2 一样覆盖 [0..3]、[4..7]、[8..11]；硬件执行映射不能据此认定完全相同。BLOCK_SIZE 等编译参数与运行时 N 的职责不同。

## 暂停题与预测

1. 第 2 号 program 的 offsets 与有效 mask 是什么？只在 store 加 mask、load 不加会怎样？
2. N 改为 13 或 BLOCK_SIZE 改变时，grid 怎样变化？代码更短能否证明访问更少？

先区分“逻辑数据块”和“硬件线程”，再画三个 program，最后回 add_kernel 与 add。

## 动手与检查

唯一入口：`labs/03-triton-attention/softmax/`。Vector Add 是本周环境/映射热身，输入与检查复用 W2，动手时保存为 `vector_add_triton.py`，不另建项目。

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
