# W13 第一段备课：编译前后的语义对齐

[单元范围](README.md) · [三段导学](study-guide.md) · [资料复核](refresh-2026-10-01.md)

备课日期：2026-10-01。资料预算：45 分钟。状态：备课已准备；目标环境与编译运行待验证。

## 目标与先修

先确认 eager 与 compile 算同一件事，再讨论优化。先通过 W6 的 Block 与测量，优先沿用可用 Linux 单卡环境；本机 Windows CPU 检查不代表 GPU 编译已就绪。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 15 分钟 | [CS336 L6 视频](https://www.youtube.com/watch?v=xnDHaNUvHBg)，配 [固定讲义](https://github.com/stanford-cs336/lectures/blob/de53a9f979a6ee35f7d13a5e1aadee5ea1afc58e/lecture_06.py) 的 naive_vs_builtin_vs_compiled_gelu | 只理解三组比较方法，不新增 GELU 项目 |
| 20 分钟 | [torch.compile 教程](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html) 的 Basic Usage | 函数/模块包装与调用结束 |
| 10 分钟 | 对照自己的 W5 表达式或 W6 Block | 列出输入、dtype、dropout、autograd 与误差约定 |

访问日：2026-10-01。教程环境显示 2.14.0+cu130，实际环境另记录；视频函数定位不代表已核验时间轴。

## 中文助读

compile 可以捕获、优化和生成执行代码，但不改变实验应比较的数学目标。编译包装与首次真实调用不是同一时间边界。融合、kernel 数和整体延迟是不同证据，先把输出对齐作为前提。

复用已有表达式或模型，固定参数和输入；避免在两路径之间更换 dtype、dropout 或 grad 模式。Triton 第三组只有语义与精度可比时才加入。

## 暂停题与预测

1. 编译包装很快，是否意味着没有编译启动成本？实际工作可能在哪一步发生？
2. eager 在 eval、compile 在 train，输出不同能归因于编译器吗？还需核对哪些条件？

先列调用阶段，再列数学与运行条件，最后回 Basic Usage。

## 动手与检查

唯一实验入口：`labs/03-triton-attention/systems-study/`，引用 W5/W6 实现，不复制一份 Block。动手时加入 `compare_compile.py` 的编排入口，固定一组 shape 与随机输入。

保存实际 Python/PyTorch/Triton/CUDA、设备与 compile 配置，检查输出最大绝对/相对误差；先设容差，再核对。主线前向 eval、dropout=0，autograd 是否关闭按 W6 对齐。编译失败保留错误和 eager 基线，修环境另计，不把失败写成速度 0。

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 输出不一致 | Basic Usage、W6 语义记录 | 参数/随机性/精度是否相同 |
| 环境不支持 | 教程与本机实际版本/错误 | 区分接口使用与后端依赖 |

- [ ] 两路径语义与数值对齐。
- [ ] 版本、配置、失败与限制可追溯。
- [ ] 复用已有实验而非新造模型。

在 `notes.md` 的 `W13-S01` 留下预测、命令与问题；通过后进入 [第二段](session-02.md)。
