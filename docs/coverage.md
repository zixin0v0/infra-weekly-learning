# 知识覆盖与资料准备

[路线设计](design.md) · [基础入口](../course/foundations/README.md) · [历史预读记录](audits/2026-10-03-sources.md) · [能力掌握检查](../course/reviews.md)

每行对应一项需要理解和实践的内容，列出基础、材料、练习与检查方式。遇到卡点时，沿最后一列回到具体例子。这里维护资料覆盖；个人是否学会只在进度页和实验记录中体现。

## 正式基础阶段

| 知识点与能力 | 先修/使用前 | 主要材料 | 练习 | 检查与卡点回看 |
| --- | --- | --- | --- | --- |
| 变量、类型、参数、返回值：追踪执行 | 能运行文件；W1 前 | [P1](../course/foundations/p01.md#p1)，CS50P 0 | 字节函数、秒转毫秒 | 24 B、250/0/1500 ms；print/return 误用回 Returning Values |
| 条件、边界：选择正确分支 | P1；W1 前 | [P2](../course/foundations/p02.md#p2)，CS50P 1 | 容量判断与边界值 | 小于/等于/大于都覆盖，回本段分支 |
| 循环、列表、字典：分解统计 | P2；W1 前 | [P3](../course/foundations/p03.md#p3)，CS50P 2 | 汇总 count/sum，换输入 | 空输入、共享列表、执行次序；回容器例子 |
| 异常、调试：读报错和定位 | P3；W1 前 | [P4](../course/foundations/p04.md#p4)，CS50P 3 | 非法整数、空数组 | 错误分类与修复证据，回异常范围 |
| 模块、库、入口：组织代码 | P4；W1 前 | [P5](../course/foundations/p05.md#p5)，CS50P 4 | 分离统计函数与 CLI | import 不触发意外执行，回 main guard |
| 文件、CSV、JSON：读取与保存 | P5；W1 前 | [P6](../course/foundations/p06.md#p6)，CS50P 6 | 统计结果写入、重读 | 新进程读回一致，坏输入明确失败 |
| 测试、参数、配置、日志：独立小工具 | P6；W1 前 | [P7](../course/foundations/p07.md#p7)，CS50P 5 与标准库 | 空文件写统计工具，修分母错误 | 正常/边界/失败测试；[基础检查](../course/foundations/README.md#foundation) |
| 类、实例、继承与模型调用 | P7；W6 前 | [P8](../course/foundations/p08.md#p8)，CS50P 8 / PyTorch Define the Class | Counter→Recorder→读 nn.Module | 状态独立、构造与 forward 可解释；回实例状态 |
| 路径、环境、权限、标准流 | P5/P6；W2 前 | [A](../course/prerequisites.md)、[S1](../course/bridges/s01.md#s1) | 换工作目录、找解释器、读错误流 | 文件/依赖/权限错误逐层定位 |
| 进程、线程、退出、CPU/GPU 分工 | A；W2 前 | [S1](../course/bridges/s01.md#s1) | 观察自己 PID/线程并停止 | 线程数不当核心数，进程退出不等于保存 |
| C++ 编译、数组、指针、引用、寿命 | Python 函数/循环；W1 最小/W2 完整 | [B](../course/prerequisites.md)、[P-CPP](../resources/foundations.md#p-cpp) | 数组求和、改长度、解释边界 | 编译运行；越界/悬垂回作用域 |
| Tensor 创建、shape、广播、乘法 | Python 核心、M1；W1 前 | [B](../course/prerequisites.md)、[P-TENSOR](../resources/foundations.md#p-tensor) | 2×3 矩阵加法与乘转置 | 矩阵 [[5,14],[14,50]]，广播回 shape |
| 矩阵、单位；指数；链式法则；统计 | 各使用前先诊断 | [M1～M4](../course/prerequisites.md) | 换数手算与尾分位数 | 已会直接跳过；不按阅读时长判断掌握 |
| Attention、残差、归一化与形状 | P8、M1/M2；W6 前 | [C](../course/prerequisites.md)、[P-MODEL](../resources/foundations.md#p-model) | 画 Q/K/V 与 pre-norm Block | score 18 元素、mask/模式分开 |
| 自动求导、训练、验证与权重重载 | P8、Tensor、M3；W6 前 | [单卡训练](../course/foundations/training.md)、[P-TRAIN](../resources/foundations.md#p-train) | 标量→五点直线→验证→新模型重载 | 梯度 -16、一步 2.6；验证不更新，重载预测一致 |
| Adam 状态与下一步恢复 | 单卡训练；W11 前 | [训练恢复](../course/foundations/training.md#resume) | 连续 3 步对重启 2+1；故意缺 optimizer | 下一批、模型与优化器状态对齐 |

## GPU、模型与通信

| 知识点与能力 | 先修 | 主要材料 | 练习 | 检查与补学 |
| --- | --- | --- | --- | --- |
| W1 类型/地址：按元素宽度计算偏移 | B/M1 | [W1 第一段](../weeks/week-01-foundations/session-01.md) | 数组地址与字节 | 实测地址关系与边界解释；回 B |
| W1 stride、共享、复制：预测视图 | Tensor/地址 | [W1 第二段](../weeks/week-01-foundations/session-02.md) | 转置、reshape、contiguous | 用修改/布局证据核对；[W1 变式](../weeks/week-01-foundations/assessment.md#w1) |
| W1 参数/激活/FLOPs/元数据：分项账本 | 视图/M1 | [W1 第三段](../weeks/week-01-foundations/session-03.md) | Linear 计算器 | 参数不随 batch 变，逻辑字节不冒充峰值 |
| W1 浮点范围、舍入与容差 | Tensor/dtype | [W1 第四段](../weeks/week-01-foundations/session-04.md) | FP16/BF16、加法顺序、误差报告 | shape/有限性先检查，atol/rtol 有依据 |
| W2 SM/warp、内存层次与 occupancy | W1/S1 | [W2 硬件关系](../weeks/week-02-cuda-execution/session-01.md)、R-GPU-HARDWARE | 手算 block/shared/warp 上限 | 容量与耗时分开，硬件参数不套用虚构例子 |
| W2 host/device、线程覆盖、搬运 | W1、S1 | [W2 第一/二段](../weeks/week-02-cuda-execution/README.md) | Vector Add | 1000/1025 尾部；[W2 变式](../weeks/week-02-cuda-execution/assessment.md#w2) |
| W2 异步/同步、正确性/计时 | 线程覆盖 | [W2 第三段](../weeks/week-02-cuda-execution/session-03.md) | 端到端与 kernel 分开 | 错误检查与同步边界；回 S1 |
| W3 树形、warp、mask/barrier | W2 | [W3 第一/二段](../weeks/week-03-reduction-profiling/README.md) | 两种 Reduce | 全覆盖、合法参与与容差；[W3](../weeks/week-03-reduction-profiling/assessment.md#w3) |
| W3 profiler：证据区分于推断 | 完整归约 | [W3 第三段](../weeks/week-03-reduction-profiling/session-03.md) | 代表输入热点分析 | 收尾计时、profiler 开销分开 |
| W4 合并访存、shared tile、同步 | W3/M1 | [W4 第一/二段](../weeks/week-04-gemm/README.md) | 朴素/分块 GEMM | 非整除 shape、数值与地址；[W4](../weeks/week-04-gemm/assessment.md#w4) |
| W4 复杂度、算术强度、Roofline | W1 字节/FLOPs | [W4 第三段](../weeks/week-04-gemm/session-03.md) | 预测再测曲线 | 上界不当结果，搬运不等于计算 |
| W5 program、mask、广播、融合 | W4/M2 | [W5 第一/二段](../weeks/week-05-triton-softmax/README.md) | Triton Softmax | 尾部与大值；[W5](../weeks/week-05-triton-softmax/assessment.md#w5) |
| W5 online max/sum：稳定状态合并 | 稳定 Softmax | [W5 第三段](../weeks/week-05-triton-softmax/session-03.md) | 分块手算/实现 | 共同最大值重缩放，回 M2 |
| W6 mask、SDPA、Attention IO | P8/C/W5 | [W6 第一/二段](../weeks/week-06-attention/README.md) | 显式/SDPA 对齐 | mask/dropout/dtype、[W6](../weeks/week-06-attention/assessment.md#w6) |
| W6 模型 shape、资源、整体时间 | Attention | [W6 第三段](../weeks/week-06-attention/session-03.md) | 小 Block 时间线 | kernel/CPU/搬运/等待，回 W2/W4 |
| W6 训练对象寿命与显存统计 | 单卡训练、W1 | [W6 第四段](../weeks/week-06-attention/session-04.md)、R-MEMORY-LIFETIME | 小模型状态表、八份输出引用对照 | allocated/reserved/peak；detach 不等于释放 |
| W13 计算图、kernel、graph break | W6 | [W13 第一/三段](../weeks/week-13-systems/README.md) | eager/compile 原 Block | 数值和 shape 变化；[W13](../weeks/week-13-systems/assessment.md#w13) |
| W13 首次/稳态/缓存、回本 | W2 计时 | [W13 第二段](../weeks/week-13-systems/session-02.md) | 编译成本分项 | 60 次持平、61 次起收益的假设明确 |
| W7 rank、collective、数据归属 | W2/S2 | [W7 第一段](../weeks/week-07-collectives/session-01.md) | rank 输入输出表 | SUM 与拼接不可混；[W7](../weeks/week-07-collectives/assessment.md#w7) |
| W7 带宽/延迟、拓扑、algbw/busbw | 数据归属/S2 | [W7 第二/三段](../weeks/week-07-collectives/README.md) | 2 卡消息曲线 | 真实路径、调用次序、计量定义 |

## 服务、训练、存储与调度

| 知识点与能力 | 先修 | 主要材料 | 练习 | 检查与补学 |
| --- | --- | --- | --- | --- |
| W8 token、模板、prefill/decode | W6 | [W8 第一段](../weeks/week-08-serving-baseline/README.md) | 同请求 token 长度核对 | 字符≠token，回 Attention |
| W8 HTTP/端口/请求生命周期 | P6/S1 | [S2](../course/bridges/s02.md#s2)、W8 第二段 | 单请求日志/时间轴 | 连接失败与应用错误分开；[W8](../weeks/week-08-serving-baseline/assessment.md#w8) |
| W8 容器、部署、日志、健康就绪 | S2 | [S3](../course/bridges/s03.md#s3) | 实际运行、请求、停止、重建 | Docker 必做；进程存活≠模型 ready |
| W8 延迟/吞吐、测量口径 | 请求生命周期/M4 | W8 第三段 | 固定负载基线 | TTFT/TPOT、失败和输出检查 |
| W9 KV 容量、分页、碎片、共享 | W1/W8 | [W9 第一/二段](../weeks/week-09-kv-cache/README.md) | 字节/块表/写时复制 | [W9 变式](../weeks/week-09-kv-cache/assessment.md#w9) |
| W9 APC、冷/热、命中证据 | 分页/请求 token | W9 第三段 | 受控前缀复用 | APC 开关不当分页开关 |
| W10 到达率、并发、批处理、SLO | W8/W9/M4 | [W10 第一/二段](../weeks/week-10-serving-benchmark/README.md) | 两个单因素扫描 | [W10 变式](../weeks/week-10-serving-benchmark/assessment.md#w10)，实际发送≠配置 |
| W10 日志/指标/trace、尾延迟、goodput | S2/负载 | W10 第三段 | 明细重算与时窗关联 | 9 req/s 与 7 goodput 可分清 |
| W11 Dataset/DataLoader、预处理与等待 | P8/D | [S4](../course/bridges/s04.md#s4) | 合成/文件数据、延迟与 workers 对照 | batch ID/shape；先数据正确再性能 |
| W11 DDP、global batch、loss/更新 | D/S4/W7 | [W11 第一/二段](../weeks/week-11-ddp/README.md) | 同样本单步对齐 | 不等局部 batch 的梯度权重；[W11](../weeks/week-11-ddp/assessment.md#w11) |
| W11 计算通信重叠、输入与精度 | 更新正确 | W11 第二/三段 | 时间线与输入对照 | AMP 概念必学、性能对照选做；数据等待必做；同步诊断不当自然吞吐 |
| W12 文件/volume/对象存储 | P6/S3/D | [S5](../course/bridges/s05.md#s5) | 进程和容器重建读文件 | 路径/mount 可追踪；无云账户要求 |
| W12 分片、聚合、状态/峰值 | W11/W7 | [W12 第一/二段](../weeks/week-12-fsdp/README.md) | DDP/FSDP2 状态对照 | 稳态不冒充峰值；[W12](../weeks/week-12-fsdp/assessment.md#w12) |
| W12 完整 checkpoint/恢复 | S5/D | W12 第三段 | 连续 3 步与重启 2+1 | 下一批/RNG/optimizer/更新一致 |
| W14 TP 代数、通信、非线性 | W4/W7/W12 | [W14 第一/二段](../weeks/week-14-parallelism/README.md) | 两层 MLP 分片 | bias 不重复加；[W14](../weeks/week-14-parallelism/assessment.md#w14) |
| W14 PP 依赖、气泡与重叠 | TP/更新语义 | W14 第三段 | 原前向时间线 | 模拟与实测、前向与完整训练分开 |
| W15 DAG、任务依赖、资源准入 | P8/S1 | [S6](../course/bridges/s06.md#s6) | ready 集合→拓扑→ObjectRef | 环/不可行资源/等待/执行错误区分 |
| W15 Task/Actor、控制与执行 | S6 | [W15](../weeks/week-15-ray/README.md) | 原记录器、task_id/attempt | 逻辑资源≠隔离、重试去重；[W15](../weeks/week-15-ray/assessment.md#w15) |
| W15 超时、重试、幂等与业务 ID | P4/P8、W15 Task/Actor | [第三段故障模拟](../weeks/week-15-ray/session-03.md#retry)、R-RETRY | 已发生效果后丢确认；补去重并换参数 | 重放不重复效果，错误输入拒绝，说明崩溃/并发缺口 |
| W16 K8s 对象、配置、事件诊断 | S3/S6 | [S6 配置题](../course/bridges/s06.md#s6) | Job YAML、三类事件 | requests/limits、selector/readiness；不要求建集群 |
| W16 FIFO/SJF、估计时长、事件顺序 | W15/M4 | [W16](../weeks/week-16-scheduling/README.md) | 原事件仿真，改变轨迹 | 无丢失/超配；[W16](../weeks/week-16-scheduling/assessment.md#w16) |
| W16 公平性、等待与局限 | 调度策略 | W16 与 S6 | 最长等待、估计误差比较 | 有限轨迹不证明无饥饿 |

## 回顾与完成

W13 后、W10 后、W14 后、W16 后分别做 [四阶段复习](../course/reviews.md#stages)。最后做 [综合掌握检查](../course/reviews.md#final) 与 [约束下的方案选择](../course/reviews.md#choose)，九领域的解释、小型实现、变化条件与证据排错逐项核对。检查未通过时回本表对应先修或段内最小卡点，而不是重新通读所有链接。

完整生产集群运维、大规模容灾、框架内部开发、复杂并行组合、完整质量评估等另属进阶，不是为了按时学完而被删掉的基础。基础与进阶的依据是完成能力所需的知识依赖和实践深度。

## 材料准备与待核验项

### 外部中文补充 · 2026-10-05

P1～P8、单卡训练、S1～S6 和全部 50 个 W 学习段均已逐页给出中文补充或具体缺项；原有 56 张基础/核心资源卡逐项登记对应关系。资料按需使用，不增加重复必读，英文材料与练习要求保留。完整范围与筛选理由见[中文资料核验](audits/2026-10-05-chinese-resources.md#source-coverage)。

| 准备对象 | 当前状态 | 尚未覆盖 |
| --- | --- | --- |
| 中文正文 | 廖雪峰、官方中文、D2L、Triton 社区译文、作者博客等按指定范围预读 | 预读只覆盖卡片列出的段落/公式，不代表整站或所有代码可用 |
| 中文视频 | 9 个视频/分集从作者课表或配套仓库确认；课页有直接入口 | B 站读取受限；字幕、画面与分钟范围均未检查 |
| 精确接口与性能 | 稳定概念配中文帮助理解，原接口资料继续使用 | FSDP2/DCP、Ray、AMP、NCCL 指标、现代 warp、Profiler、APC 等仍有[明确缺项](audits/2026-10-05-chinese-resources.md#pending) |
| 原内容保护 | 原英文链接、指定范围、实验、掌握检查与学习进度纳入差异检查 | 文件检查不等于个人已学会或 GPU/Docker/多卡已运行 |

### 原有材料与运行状态

| 内容 | 当前准备 | 仍需的证据 |
| --- | --- | --- |
| P1～P8 | 指定 Notes 继承 2026-10-03 预读，直接视频入口与暂停练习已接入 | 视频画面和分钟轴未逐段核验 |
| S1～S6 | 文字操作、例子、输入材料与返回位置已整理 | Docker、数据、持久化实际操作由个人记录体现 |
| W1～W16 | 50 个 session 与 16 个独立掌握检查页；W1/W6 各四段 | 原始材料预读沿用对应核验日期，文字改写不等于重读全部论文 |
| 六项知识补充 | 训练课、数值、硬件、显存、故障模拟和方案选择已接入；指定正文与检查见 [核验记录](audits/2026-10-04-knowledge.md) | 小例子验证与完整课程实验分开，个人独立作答仍待完成 |
| PyTorch 视频 | 具体讲次入口及2026-10-04 查阅正文已记录 | 旧录制与更新后代码的一致性、画面和时间轴待核验 |
| CS336 / GPU MODE | 官方讲次与已选视频、原有固定代码范围对应 | 未完成逐帧检查，不把函数名当视频时间点 |

材料缺项不填入个人学习完成栏。链接和语法检查的交付结果记录在对应日期的核验页；小规模运行只覆盖核验记录中的指定例子，不代表所有 GPU 或集群实验已通过。

## 图解与文字的覆盖

当前学习页面按问题、例子、解释和练习组织；基础 8 段及单卡训练课、系统衔接 6 段、50 个 W 小节均接入核心图解。16 份单元检查保留独立实现、变式与排错要求。原图文范围见 [2026-10-04 图文记录](audits/2026-10-04-language-figures.md)；其后的四张图与知识补充见 [知识核验记录](audits/2026-10-04-knowledge.md)。

| 使用位置 | 图解覆盖 | 正文怎样连接 |
| --- | --- | --- |
| P1～P8 | 函数返回、分支边界、循环状态、异常、模块入口、文件、工具组成、实例状态 | 每段跟随小输入推演，再改变输入练习 |
| 单卡训练课 | 求梯度与更新参数的区别 | 标量步骤图接独立单卡训练 |
| S1～S6 | 进程与 GPU、请求路径、延迟/带宽、容器、数据等待、持久化、DAG、Kubernetes 对象 | 图注接命令、配置与故障判断 |
| W1～W4 | 字节/布局/复制、Linear、浮点间隔、SM/warp、线程尾部、计时、归约、分块与 Roofline | 元素偏移、参与线程、计算量与搬运量逐项核对 |
| W5/W6/W13 | 稳定分块状态、Attention/Block、显存对象寿命、计算图与编译回本 | 形状、数值与局部/整体耗时分开解释 |
| W7/W11/W12/W14 | collective 输出与分步、拓扑、梯度同步、分片聚合、下一步恢复、TP 切分、PP 时间线 | 语义图先于多卡性能结论 |
| W8～W10 | 请求时间线、prefill/decode、KV 块共享、排队直觉 | 模拟时间与真实压测分开，暂停题接指标计算 |
| W15/W16 与复习 | ObjectRef/Actor、重复效果与去重、FIFO/SJF、跨系统关系 | 按任务 ID 重建等待，从系统关系寻找验证方法 |

图片存放、字体与导出规则见 [维护规则](maintenance.md)。视频画面和时间轴、完整 GPU/多卡/容器实验按原状态保留；本地示例运行单独列在知识核验记录，不代替个人练习。
