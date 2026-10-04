# 练习起点

这些是示例输入、待补全代码和模拟故障，尚未代表你的实现或运行结果。先读当前课页，再把需要的文件复制到对应 labs 目录；独立实现题从空文件开始，先自己设计函数和入口。

| 对应内容 | 输入或待补全代码 | 要完成什么 |
| --- | --- | --- |
| P3/P6/P7 | [数值输入](foundations/numbers.json)、[CSV](foundations/records.csv)、[统计待补全代码](foundations/summary_start.py)、[错误版本](foundations/mean_bug.py) | 汇总 count/sum/mean，保存重读；为正常、空、负数和非法输入编写检查；定位错误版本 |
| P7 独立小工具 | [接口约定](foundations/independent-tool.md) | 从空文件实现，不提供完整解答 |
| P8 | [Recorder 待补全代码](foundations/recorder_start.py) | 两实例各自保存历史；检查追加后的状态 |
| 先修 B | [C++ 待补全代码](foundations/array_start.cpp)、[Tensor 待补全代码](foundations/tensor_start.py) | 数组边界与生命周期、形状和广播预测 |
| 单卡训练 D | [标量起点](foundations/train_start.py)、[小模型起点](foundations/training_start.py) | 先在 W6 前完成训练/验证/权重重载；W11 前完成 Adam 下一步恢复 |
| W1 数值精度 | [数值例子与误差报告起点](foundations/numerics_start.py) | 默认可运行表示/顺序例子；误差报告需补全，独立实现仍从空文件开始 |
| W6 显存寿命 | [有界留存与采样起点](foundations/memory_start.py) | 默认 CPU；显式选择 CUDA 后记录引用、allocated/reserved/peak；训练步需补全 |
| W15 故障重试 | [重复效果模拟](systems/retry_start.py) | 默认运行无去重版本；补全 apply_once 后检查重复、变参数与错误输入 |
| S2/W8 | [请求示例](systems/request.json)、[模拟请求时间线](systems/request-trace.csv) | 核对端点和字段；计算 TTFT、TPOT 与失败统计，模拟记录不能作压测 |
| S3 | [容器配置](systems/compose.yaml) | 阅读端口映射、启动、发请求、日志、停止与重建 |
| S4 | [8 条样本](systems/samples.csv)、[Dataset 待补全代码](systems/dataset_start.py) | 保留 ID，batch=3，再比较人工等待和 workers=0/2 |
| S5 | [持久化配置](systems/persistence.yaml) | 创建命名卷，两个不同容器中写入和读回，和无卷路径对照 |
| S6 | [Job 配置](systems/job.yaml)、[模拟事件](systems/events.txt) | 解释对象、requests/limits、重试；区分资源不足、拉取失败、程序错误 |

P6 的字典输入 `{"values": [2, 4, 6]}` 需要自己另存；这里的 `numbers.json` 是顶层列表，供 P3/P7 直接读取。两种结构的取值方式不同，先看清当前练习的输入约定。

## 做过之后，再展开核对

<details><summary>输入、形状与 batch 的参考结果</summary>

numbers 为 [2,4,6]：count=3、sum=12、mean=4；mean_bug 对相同输入给出错误值，先解释原因再修复。CSV 的逗号字段必须用 csv 模块处理。

Recorder：A 添加 1、3 后为 [1,3]，B 添加 2 后仍为 [2]。Tensor：输入 [[0,1,2],[3,4,5]] 与转置相乘为 [[5,14],[14,50]]；每行加 [10,20,30] 后为 [[10,21,32],[13,24,35]]。

samples 的 ID 0～7 每轮应各出现一次，batch=3 且 drop_last=False 时大小为 3、3、2。首次 batch 与稳定取样时间分开；CPU 人工等待不冒充 GPU 性能结论。

</details>

## 容器练习怎样运行

compose 在 exercises/systems 中用 `docker compose -f compose.yaml up -d` 启动；停止并移除本练习容器用对应 `down`。镜像先拉取并记录 digest；示例使用浮动标签，自己的运行应固定实际版本。持久化配置先执行 `docker compose -f persistence.yaml run --rm writer`，再执行 `docker compose -f persistence.yaml run --rm reader`；两个命令从本目录的 systems 中运行。down 不带 -v 时命名卷保留。只有确实准备删除本练习数据时才清理该卷。

本目录待补全代码含 NotImplementedError 或明确失败返回，执行失败表示尚待补全。标准库待补全代码只做语法核对；PyTorch、Docker 和 Kubernetes 按自己的环境完成。Kubernetes 的 YAML 与模拟事件题必做，本地集群操作可后续进行。
