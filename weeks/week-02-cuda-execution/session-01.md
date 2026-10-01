# W2 第一段备课：线程怎样覆盖数组

[单元范围](README.md) · [三段导学](study-guide.md) · [资料复核](refresh-2026-10-01.md)

备课日期：2026-10-01。资料预算：60 分钟。状态：备课已准备；学习练习与 GPU 运行待完成。

## 目标与先修

从线程坐标推导数组下标，解释尾部线程为什么必须检查边界。先通过 W1 的类型、字节与连续布局检查；运行前另行确认 CUDA 编译器、驱动和最小 kernel，备课未验证这些条件。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 20 分钟 | [Jeremy Howard 视频](https://www.youtube.com/watch?v=nOxKexn3iBo)，配 [pmpp.ipynb 固定版本](https://github.com/gpu-mode/lectures/blob/77a8df418834e5789c12da23e7d2719e0efabef1/lecture_003/pmpp.ipynb) 的 rgb_to_grayscale_kernel、rgb_to_grayscale | 只追线程下标、尾部保护和启动配置；后续 CUDA matmul 不读 |
| 20 分钟 | [Programming Model §1.2](https://docs.nvidia.com/cuda/cuda-programming-guide/01-introduction/programming-model.html) 与 [Writing SIMT Kernels §2.3.2](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html) | 执行层级和 Thread Hierarchy 结束 |
| 20 分钟 | [Intro to CUDA C++ §2.1.2](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/intro-to-cuda-cpp.html) | 启动语法、下标与尾部保护；后续内存管理留到下一段 |

访问日为 2026-10-01。视频时间轴未核验，讲义用于定位；找不到对应视频片段就按文档完成预算。

## 中文助读

host 提交 kernel；一个 grid 含多个 block，每个 block 含线程。1D 下标是 block 编号乘 block 大小，再加线程局部编号。warp 是硬件执行分组，不能把一个 block 永远当成一个 warp。

对长度 10、block 大小 4，启动 3 个 block，共 12 个线程；下标 10、11 不访问数组。启动足够多线程解决覆盖，边界判断解决多出来的线程。

## 暂停题与预测

1. 不看示例，列出三个 block 的全部下标；为什么不能直接用 `threadIdx.x` 索引全数组？
2. 输入改成 9 或 12 个元素，分别预测启动数量和无效线程数量。改 block 大小会改变数学输出吗？

卡住时先解释“局部编号”和“全局编号”，再手画两个 block，最后回 §2.3.2 核对。

## 动手与检查

唯一入口：`labs/02-cuda/vector-add/`。动手时建立 `vector_add.cu`，先写 CPU 逐元素参考，再写同 dtype 的 CUDA 路径。第一段先测长度 1、10、12、257；包含正负数，逐元素检查，不能只比较总和。

固定输入和 FP32，暂只选择一种 block 大小。打印小输入及预期索引表；学习代码必须独立处理尾部。GPU 不可用时保存纸面表，实际正确性仍待验证。内存路径与可靠计时分别在后两段补齐。

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 漏掉最后一段 | §2.1.2 启动与边界 | 257 个元素全部覆盖 |
| 混淆 block/warp | §1.2 与 §2.3.2 | 用自己的 block 大小说明执行层级 |

- [ ] 独立推导下标与启动数量。
- [ ] 小数组与非整除输入逐元素对齐。
- [ ] GPU 环境与未验证项如实记录。

在实验 `notes.md` 的 `W2-S01` 保存实际阅读位置、预测、完整命令、结果解释和一个未解决问题；通过后进入 [第二段](session-02.md)。
