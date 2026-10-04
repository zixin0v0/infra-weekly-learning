# 2026-10-04：基础知识衔接与六项补充核验

[覆盖记录](../coverage.md) · [当前设计](../design.md)

这份记录说明材料和示例的准备情况，不表示个人学习已完成。此前的图文核验保留在原日期记录中；本次不重写既有实验数据或进度。

## 内容与使用位置

| 补充 | 具体位置 | 保留的范围 |
| --- | --- | --- |
| 完整的小训练过程 | [训练课](../../course/foundations/training.md) | P8 后、W6 前训练/验证/权重重载；Adam 下一步恢复在 W11 前完成，S4 复用同一实现 |
| 浮点范围、精度与误差 | [W1 第四段](../../weeks/week-01-foundations/session-04.md) | FP16/BF16、加法顺序、有限性和容差；W3/W5/W11 按需回看 |
| GPU 硬件关系 | [W2 第一段](../../weeks/week-02-cuda-execution/session-01.md) | SM/block/warp、寄存器/shared/缓存/global、occupancy 与速度的区别 |
| 显存对象寿命 | [W6 第四段](../../weeks/week-06-attention/session-04.md) | 小训练模型和有界引用留存；Decoder Block 仍保持既有前向实验范围 |
| 重试与重复效果 | [W15 第三段](../../weeks/week-15-ray/session-03.md#retry) | 串行本地故障模型、业务 ID 去重接口、非法输入及持久化/原子性边界 |
| 约束下的选择 | [综合自查](../../course/reviews.md#choose) | 显存与长度分布、延迟目标、替代方案及否定条件；复用服务/训练/调度实验 |

同步修改先修、各单元课表、掌握检查、资源卡、时间范围与实验报告模板。基础与桥接目录原有锚点标签误显示为正文的问题已修复；检查脚本增加可见链接标签与连续课页导航检查。

## 指定正文实际预读范围

| 来源 | 本次实际读取的范围 | 处理与前置 |
| --- | --- | --- |
| [PyTorch Quickstart](https://docs.pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html) | Creating Models、Optimizing the Model Parameters、Saving Models、Loading Models 的代码与说明 | 只取训练/验证/状态字典概念，图像分类与新 accelerator 接口不作为练习前置；沿用旧资料卡的 Autograd/Optimization 范围 |
| [Saving and Loading Models](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html) | state_dict、权重保存加载、General Checkpoint 的保存加载与紧接说明 | 区分推理重载与训练继续；明确 state_dict 内存快照需要复制 |
| [Numerical accuracy 2.14](https://docs.pytorch.org/docs/2.14/notes/numerical_accuracy.html) | 引言、Batched computations、Extremal values；另查看低精度累加说明 | 本地用独立 FP32 加减例子解释舍入，病态线性代数不列为本节前置 |
| [Type Info](https://docs.pytorch.org/docs/2.14/type_info.html#torch-finfo)、[isclose](https://docs.pytorch.org/docs/2.14/generated/torch.isclose.html) | finfo 字段与 tiny 注释；isclose 不等式、参数和非有限值说明 | 本地有限输出检查比 isclose 本身更严格，不接受 inf 对 inf 通过 |
| [CUDA Writing SIMT Kernels §2.3.7](https://docs.nvidia.com/cuda/cuda-programming-guide/02-basics/writing-cuda-kernels.html#kernel-launch-and-occupancy) | block 分配到 SM、资源列表、occupancy 与设备算例 | 必读只到设备表前；用明确标为虚构的本地资源约束练习，不套用新架构规格 |
| [CUDA Best Practices §11.1](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#occupancy) | occupancy 定义、寄存器约束、分配粒度与线程/block 的说明 | 必读停在特定架构算例之前；高 occupancy 不当成提速结论 |
| [CUDA semantics / Memory management](https://docs.pytorch.org/docs/2.14/notes/cuda.html#memory-management) | 开头两段：缓存分配器、allocated/reserved/peak、empty_cache | 不扩展到高级分配器配置；显存小例子使用本机 2.5.1 可用 API |
| [allocated](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.memory.memory_allocated.html)、[reserved](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.memory.memory_reserved.html)、[peak](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.memory.max_memory_allocated.html)、[reset](https://docs.pytorch.org/docs/2.14/generated/torch.cuda.memory.reset_peak_memory_stats.html) | 首段定义、device 参数及相关注释 | 更正了旧别名形态的文档 URL；API 字节单位和重置起点已核对 |
| [AMP recipe](https://docs.pytorch.org/tutorials/recipes/recipes/amp_recipe.html) | Adding torch.autocast、Adding GradScaler、All together 的代码与说明 | 概念必学，性能对照仍选做；不宣称所有状态都减半 |
| [AWS Retry with backoff](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/retry-backoff.html) | Intent、Motivation、Applicability、Issues and considerations | 不引入 AWS 部署；提取暂时性故障、幂等、退避与失败边界 |
| [ray.get](https://docs.ray.io/en/latest/ray-core/api/doc/ray.get.html) | timeout、GetTimeoutError 与结果等待说明 | 不把调用方超时等同于业务未执行或效果已回滚 |

以上为 2026-10-04 可访问的官方正文；固定 2.14 的文档与本机 2.5.1 明确分开。视频保持原讲次入口，画面、字幕与分钟轴没有因本次文字补充而被标记为已核验。

## 实际运行：材料维护用的小例子

环境：Windows，Python 环境中的 PyTorch 2.5.1，CUDA 构建版本 12.4；设备查询为 NVIDIA GeForce RTX 4060 Laptop GPU，总显存 8585216000 B。没有据此更新个人进度，也没有验证远端 4090、多卡链路或完整 CUDA 工具链。

| 检查 | 结果 | 解释边界 |
| --- | --- | --- |
| CPU 五点 Linear/SGD 参考实现 | 初始 MSE=9；一步参数 0.8/0.2，MSE≈3.52；50 步训练与验证 MSE 均约 2.05×10⁻¹⁰ | 验证公式、输入与阈值；不是个人独立实现 |
| 换直线系数、验证不更新参数、权重保存/重载 | 变式 MSE < 10⁻⁶；参数不变；同 CPU 预测精确一致 | 无随机层、无真实数据泛化结论 |
| Adam 连续 3 步与保存 2 步后新进程恢复 | 模型、优化器、更新前 loss、step 精确一致；故意缺 optimizer 后下一步分歧 | 固定数据/初始化，未验证 shuffle、多卡和随机层恢复 |
| `python exercises/foundations/numerics_start.py` | FP16 的 70000→inf；BF16→70144；1.001 分别→1.0009765625 与 1；FP32 两种顺序为 0/1 | CPU 指定数值，不代表所有后端归约误差范围 |
| 容差及容量手算的程序核对 | 近零变式按预期失败；简化 KV 容量 65536 token | 容量题忽略的项已在正文明确，不能作为真实服务准入承诺 |
| `python exercises/foundations/memory_start.py --device cuda` | 八份输出 2097152 B；活对象存在时 empty_cache 不改变 allocated | 只分配 2 MiB 逻辑数据的有界例子，未做模型性能压测 |
| `python exercises/systems/retry_start.py` | 无去重计数为 4；临时参考去重实现为 2，效果增量为 2/0；变式与非法输入通过 | 去重函数在练习起点中仍待补全；没有声称 Ray 集成或真实网络故障通过 |

显存示例的原始阶段值（单位 B）：

| 阶段 | allocated | reserved | peak allocated |
| --- | ---: | ---: | ---: |
| before | 0 | 0 | 0 |
| retained_8 | 2097152 | 2097152 | 2097152 |
| empty_cache_while_live | 2097152 | 2097152 | 2097152 |
| cleared | 0 | 2097152 | 2097152 |
| empty_cache_after_clear | 0 | 0 | 2097152 |

参考验证使用临时脚本和临时 checkpoint，未把完整独立题答案或维护运行写入 labs。环境出现既有 pynvml 弃用提示，不影响这些检查；未因此改动依赖。

## 图片与文档检查

新增四张原创图：`w01-float-spacing`、`w02-gpu-hardware`、`w06-memory-lifetime`、`w15-retry-dedup`，各有 PNG/SVG；训练图复用既有 `d01-training-step`。使用已有 Matplotlib/Pillow 脚本和微软雅黑字体，四张正常宽度与缩小预览均已查看；没有外部课件截图或虚构实测曲线。

交付检查结果：`python scripts/check_docs.py` 检查 161 份 Markdown、1847 个本地链接、16 个单元、52 次图片引用及 52 组 PNG/SVG，PASS、0 errors；12 个 scripts/exercises Python 文件通过 AST 语法检查；错误链接标题与跳课的两种回归输入均被检测到。发布前还检查暂存差异，避免仅检查已跟踪的旧文件。个人进度与本次开始时逐字比较一致。完整 GPU 模型、Docker、多卡、Ray 集成、集群和视频时间轴仍按已有未验证边界保留。

暂存检查发现 Matplotlib 在 Windows 导出的 SVG 含 CRLF 与路径行末空格，已在导出器统一为 LF 并去除行末空白。重新导出 52 组，全部 PNG 的 SHA256 与修正前一致；SVG 只规范化空白，不改变图形内容。
