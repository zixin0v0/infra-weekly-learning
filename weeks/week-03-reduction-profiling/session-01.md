# W3 第一段备课：归约树与 block 同步

[单元范围](README.md) · [三段导学](study-guide.md) · [资料复核](refresh-2026-10-01.md)

备课日期：2026-10-01。资料预算：45 分钟。状态：备课已准备；学习实现与检查待完成。

## 目标与先修

解释每轮谁写、谁读以及何时需要同步。先通过 W2 的边界、错误与计时；本段只新增归约语义，继续同一 CUDA 环境。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 25 分钟 | [shared_reduce.cu 固定版本](https://github.com/gpu-mode/lectures/blob/77a8df418834e5789c12da23e7d2719e0efabef1/lecture_009/shared_reduce.cu) 的 SharedMemoryReduction | 加载、stride 循环、同步与输出；核对固定启动条件后停 |
| 20 分钟 | [Writing SIMT Kernels §2.3.2.1](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html) | block 同步语义结束，画自己的读写依赖 |

访问日：2026-10-01。源码固定 BLOCK_DIM=1024、单 block 处理 2048 个元素，不是通用多 block 实现。树仍不直观时用 [Reduction #3](https://developer.download.nvidia.com/assets/cuda/files/reduction.pdf) 阅读器第 14～15 页替换前 15 分钟；旧隐式 warp 同步不作现代模板。

## 中文助读

SUM 的空位填 0。每个 block 先归约自己的数据，再由统一第二阶段组合部分和；后续两个版本必须复用同一收尾方法。线程即使没有有效输入，也要参与该 block 所需的 barrier，不能提前退出而留下其他线程等待。

```mermaid
flowchart LR
    input["8 个输入"] --> pairs["4 个部分和"]
    pairs --> quarters["2 个部分和"]
    quarters --> total["1 个结果"]
```

这是逻辑归约树，实际线程和地址需另列映射；树形相同不代表两种实现访存相同。

## 暂停题与预测

1. 对 [1,-2,3,4,-5,6,7,-8] 逐轮画树并算最终值；改变配对顺序会影响 FP32 舍入吗？
2. 最后一个 block 不满时，哪些线程仍要走到 barrier？为何不能只对有效线程调用同步？

先提示“本轮读上一轮谁的值”，再用四元素例子画依赖，最后回同步小节。

## 动手与检查

唯一入口：`labs/02-cuda/reduction/`。先手算，再写 shared-memory 版本，每 block 输出一个部分和。自己补 block offset、尾部填零和多 block 收尾；边界可用 1、8、257、block 覆盖量前后各一值。

输入含负数，固定 FP32 输入与累加策略，用 FP64 sum 或可靠库参考检查绝对/相对误差；接近零的结果不能只看相对误差。先 memcheck 再计时，保存大小、容差、实际误差与命令；无需一开始优化多个配置。

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 小输入对、大输入错 | 源码加载与输出、自己的 block offset | 各部分和是否覆盖独立区间 |
| 卡住或不稳定 | §2.3.2.1 | 同一 block 的 barrier 参与是否一致 |

- [ ] 逐轮解释依赖和 SUM 的填充值。
- [ ] 多 block 与尾部输入通过参考检查。
- [ ] 部分和、第二阶段与工具限制有记录。

在 `notes.md` 的 `W3-S01` 留下预测、命令和未解决问题；通过后进入 [第二段](session-02.md)。
