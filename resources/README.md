# 视频与资料

[课程目录](../course/README.md) · [从基础开始](../course/foundations/README.md)

这里用于找到来源；具体先看哪段、在哪里暂停、练什么，以当前课页为准。完整主题可以连续看，重复讲义用来回查。

## 按当前主题找视频

| 用在哪里 | 直接入口 | 怎么用 |
| --- | --- | --- |
| P1～P8 | [CS50P](https://cs50.harvard.edu/python/) | 下面逐讲打开；本地顺序是 0、1、2、3、4、6、5、8 |
| Linux 与命令行 | [Missing Semester 2026 Shell](https://missing.csail.mit.edu/2026/course-shell/) | S1 导航、PATH、标准流；2020 Job Control 为单独正文补充 |
| Tensor | [PyTorch Tensors 视频与正文](https://docs.pytorch.org/tutorials/beginner/introyt/tensors_deeper_tutorial.html) | 先修 B 与 W1；从创建、shape、dtype 接布局 |
| 自动求导 | [PyTorch Autograd 视频与正文](https://docs.pytorch.org/tutorials/beginner/introyt/autogradyt_tutorial.html) | 先修 D；手算梯度后观察计算图 |
| 单卡训练、输入数据 | [Training with PyTorch](https://docs.pytorch.org/tutorials/beginner/introyt/trainingyt.html) | 先修 D 和 S4；不要求下载原例图像数据 |
| CUDA 入门 | [GPU MODE Lecture 3](https://www.youtube.com/watch?v=nOxKexn3iBo) | W2 CPU 循环到 kernel；代码见 GPU 资料 |
| 资源与性能 | [CS336 2026 L2](https://www.youtube.com/watch?v=kuYAsz7zspQ) | W1/W4 的 Tensor、FLOPs 与算术强度 |
| 测量、Triton、编译 | [CS336 2026 L6](https://www.youtube.com/watch?v=xnDHaNUvHBg) | W3/W5/W13 各看当前主题 |
| 并行 | [CS336 2026 官方课表与 Recordings](https://cs336.stanford.edu/) | W7/W14，按 L7 标题选择；不套用 2025 的讲次 |
| 推理 | [CS336 2026 L10](https://www.youtube.com/watch?v=EfM546A79aM) | W8/W9/W10，各课复用相应主题 |
| DDP | [PyTorch Multi GPU training with DDP](https://docs.pytorch.org/tutorials/beginner/ddp_series_multigpu.html) | W11 单机多卡段；设备条件另行确认 |

## CS50P 逐讲入口

| 本地学习段 | 完整视频 | 配套正文 |
| --- | --- | --- |
| [P1](../course/foundations/p01.md) | [Lecture 0 · Functions, Variables](https://video.cs50.io/JP7ITIXGpHk) | [Notes 0](https://cs50.harvard.edu/python/notes/0/) |
| [P2](../course/foundations/p02.md) | [Lecture 1 · Conditionals](https://video.cs50.io/_b6NgY_pMdw) | [Notes 1](https://cs50.harvard.edu/python/notes/1/) |
| [P3](../course/foundations/p03.md) | [Lecture 2 · Loops](https://video.cs50.io/-7xg8pGcP6w) | [Notes 2](https://cs50.harvard.edu/python/notes/2/) |
| [P4](../course/foundations/p04.md) | [Lecture 3 · Exceptions](https://video.cs50.io/LW7g1169v7w) | [Notes 3](https://cs50.harvard.edu/python/notes/3/) |
| [P5](../course/foundations/p05.md) | [Lecture 4 · Libraries](https://video.cs50.io/MztLZWibctI) | [Notes 4](https://cs50.harvard.edu/python/notes/4/) |
| [P6](../course/foundations/p06.md) | [Lecture 6 · File I/O](https://video.cs50.io/KD-Yoel6EVQ) | [Notes 6](https://cs50.harvard.edu/python/notes/6/) |
| [P7](../course/foundations/p07.md) | [Lecture 5 · Unit Tests](https://video.cs50.io/tIrcxwLqzjQ) | [Notes 5](https://cs50.harvard.edu/python/notes/5/) |
| [P8](../course/foundations/p08.md) | [Lecture 8 · Object-Oriented Programming](https://video.cs50.io/e4fwY9ZsxPw) | [Notes 8](https://cs50.harvard.edu/python/notes/8/) |

使用官网当前链接的 2022 录制版。课页给概念暂停点；尚未核验的分钟位置不填写。入口、正文预读与画面检查的详细边界见 [2026-10-04 核验记录](../docs/audits/2026-10-04-video.md)。

## 按主题回查

- [编程、数学、工具与 PyTorch](foundations.md)
- [GPU 与算子](gpu.md)
- [模型与编译](models.md)
- [推理服务](serving.md)
- [通信与训练](training.md)
- [任务与调度](scheduling.md)
- [按需拓展](optional.md)

Docker、存储、Ray、Kubernetes 的当前主材料为课页操作和指定正文；还没有核验到合适视频的主题，按课页的完整中文步骤继续。网页更新版本不是本机环境版本。
