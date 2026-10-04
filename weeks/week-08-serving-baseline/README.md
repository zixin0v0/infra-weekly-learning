# 单元 W8：小型推理服务基线

[课程目录](../../course/README.md) · [我的进度](../../course/progress.md) · [环境准备](../../course/environment.md)

预计 10～18 小时用于本单元，变式与排错另留 1～3 小时；桥接只计新发生的时间。按实际掌握推进，记录规则见 [学习方法](../../course/guide.md#time-budget)。

## 这一单元要弄清什么

从发出请求到看到第一个 token，中间发生了什么？先拆开 prefill 与 decode，再走通模型加载、HTTP 请求、日志和输出检查。你会建立一个小规模服务基线，解释 TTFT、TPOT、吞吐各在衡量哪一段过程。

## 开始前

完成 W6 的模型分析，复用 W4 的资源计算，并能运行 Python、读取 JSON。第一段补 token 与模板，启动服务前做 [S2 请求部分](../../course/bridges/s02.md#s2)，之后做 [S3 Docker 实操](../../course/bridges/s03.md#s3)，最迟在 W10 阶段检查前完成。需要可用的单卡服务环境；W7 多卡实验不是这里的硬性依赖。

<details>
<summary>先解释，再展开核对</summary>

能写出 Attention 的 KV 对象及脚本 JSON 输入输出即可；网络请求、token 和模板按下方例子学习。

</details>

## 按顺序学习

- [S2 的 HTTP 请求部分](../../course/bridges/s02.md)。
- [W8 第 1 段：prefill 和 decode 为什么资源特征不同](session-01.md)。
- [W8 第 2 段：请求已经发出，为什么还没有生成结果？](session-02.md)。
- [完成 S3 Docker 实操](../../course/bridges/s03.md)。
- [W8 第 3 段：一个吞吐数字，分母究竟是什么？](session-03.md)。

- [本单元掌握检查](assessment.md)：实验完成要求、变式与排错题。

## 实践任务

建议目录：labs/05-serving/baseline/；W10再整合成项目。

1. 选一个能在单卡中留出 KV Cache 余量的小模型，记录模型与 tokenizer revision、精度和完整启动配置。
2. 先用 3～5 条固定请求核对 tokenizer、模板、停止条件与输出，保存基线输出；再建立固定的合成或公开压测集。这只是输出检查，不代表完整模型质量评估。
3. 固定输入/输出 token 长度与采样策略，改变并发上限；请求到达率另行固定并记录。
4. 测 TTFT、TPOT、吞吐、显存与请求失败数；同时记录实际生成长度，避免提前结束改变工作量。
5. 将加载/预热与稳态压测分开，写短报告《并发增加后，推理吞吐和延迟怎样变化？》。

区分配置中的到达率和实际发送速率，并记录并发上限是否触顶。TTFT/端到端延迟包含客户端与网络路径，不能直接视为 GPU kernel 时间。本周先做小规模基线，更完整的客户端与服务端关联在 W10 完成。

## 按需回看

博客：[vLLM 与 PagedAttention](../../resources/serving.md#r-paged)，帮助理解 KV Cache 管理；W9再精读论文。

[上一单元](../week-07-collectives/README.md) · [下一步](../week-09-kv-cache/README.md)
