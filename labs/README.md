# 实验目录

这里保存我自己的实现、笔记和真实输出。开始练习时再创建相应目录；输入和待补全代码从 [exercises](../exercises/README.md) 复制过来，独立实现题从空文件开始。

| 使用的目录 | 对应内容 | 主要内容 |
| --- | --- | --- |
| `00-foundations/` | P1～P8、先修 | 统计工具、类、C++/Tensor 与单卡训练入门 |
| `01-foundations/` | 1 | C++ 内存示例、Tensor 检查、资源账本 |
| `02-cuda/` | 2～4 | Vector Add、Reduce、GEMM |
| `03-triton-attention/` | 5～6、13 | Softmax、Attention、模型 Profiling |
| `04-collectives/` | 7 | NCCL 与最小 DDP |
| `05-serving/` | 8～10 | 服务基线、缓存、负载控制 |
| `06-training/` | 11～12、14 | DDP、FSDP2、并行切分 |
| `07-scheduling/` | 15～16 | Ray 执行、排队与调度策略 |

学习指南保存在各周 `session-XX.md`，学习作答在本实验 `notes.md` 按段号追加；同单元所有段复用一个目录。记录方法见 [学习指南](../course/guide.md)。

## 单个实验的约定

例如第 2 周动手后可以形成以下结构，文件名按语言与实验需求调整：

```text
02-cuda/vector-add/
├── README.md           问题、机制、运行命令、结果与局限
├── vector_add.cu       实现与正确性检查
├── benchmark.py        计时入口；需要时才建立
├── config.json         输入规模、精度、预热与重复次数
├── environment.txt     实际运行环境
├── results/
│   ├── raw.csv         真实测量的原始小型数据
│   └── summary.csv     可由原始数据生成的汇总
├── plot.py             用原始数据或汇总数据绘图
└── figures/            报告用图
```

使用 [实验报告模板](../templates/experiment-report.md)。还没有实验结果时不创建带示例数字的 `raw.csv`；可以写预期趋势，但必须明确它是待验证的假设。

周页面链接到这个实验目录；后续项目复用同一实现。只有多处真实复用出现后，才提取公共计时或绘图函数。

## 我的笔记怎样接着用

按 P1、S1、WXX-S01 等段号追加笔记，写下原来的预测、实际结果和修正原因。之后改变输入或排错时，继续记录在同一实验下。到了 [阶段复习](../course/reviews.md)，用这些记录重新解释结果；实际用时与尚未完成的运行单独写清，资料准备状态不放进实验结果。
