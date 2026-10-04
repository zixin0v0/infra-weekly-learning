# 单元 W9：KV Cache 与 PagedAttention

[课程目录](../../course/README.md) · [我的进度](../../course/progress.md) · [环境准备](../../course/environment.md)

预计 10～18 小时用于本单元，变式与排错另留 1～3 小时；桥接只计新发生的时间。按实际掌握推进，记录规则见 [学习方法](../../course/guide.md#time-budget)。

## 这一单元要弄清什么

生成越来越长的文本时，KV Cache 为什么持续增长？先算出每个 token 保存的 K/V 字节，再用逻辑块到物理块的映射解释分页与共享。实验复用 W8 服务，比较前缀缓存的冷、热状态；APC 开关只检验前缀复用，不能直接测出分页分配器单独带来的加速。

## 开始前

先让 W8 的单请求与 token 长度检查可以重做，再回看 W1 的字节计算。分清层数、query heads 与 KV heads；不清楚时回 [W8 第一段](../week-08-serving-baseline/session-01.md)。[S3 Docker 操作](../../course/bridges/s03.md#s3) 若尚未完成，在 W10 阶段检查前补做。

<details>
<summary>先解释，再展开核对</summary>

GQA 的 KV 容量使用 KV heads；输出 token 数和字符数不可互换。若分不清先回 W8 第一段。

</details>

## 按顺序学习

- [W9 第 1 段：每增加一个 token，KV 要多占多少空间？](session-01.md)。
- [W9 第 2 段：共享前缀以后，谁可以修改那块 KV？](session-02.md)。
- [W9 第 3 段：热请求变快，怎样确认是前缀缓存起作用？](session-03.md)。

- [本单元掌握检查](assessment.md)：实验完成要求、变式与排错题。

## 实践任务

建议目录：labs/05-serving/prefix-cache/。

1. 沿用模型、精度、采样策略、并发与请求到达率。
2. 构造有共同前缀与无共同前缀的两组请求，保持 token 长度可比，保存实际 token IDs 或可重建的输入。
3. 分别测缓存开启/关闭以及冷/热状态；确认清理方法，必要时重启服务。首次请求与复用请求分开记录。
4. 除 TTFT 与吞吐外，寻找缓存命中或复用的日志/指标证据；缺乏该证据时将机制归因标记为待验证。
5. 估算 KV 字节数时写明层数、KV 头数、head dimension、token 数与 dtype；GQA 模型不能直接用 query 头数。

按官方 APC 文档，将复用的直接作用定位为减少重复 prefill。TPOT 或吞吐变化还可能受到排队、批处理与负载变化影响，不能仅凭缓存开关推断 decode 算子加速。

## 按需回看

复看 [CS336 2026 Lecture 10](../../resources/serving.md#r-inference) 中 KV Cache 相关内容，替换一部分论文阅读时间。论文设计与当前 vLLM 实现要分开记录。

[上一单元](../week-08-serving-baseline/README.md) · [下一步](../week-10-serving-benchmark/README.md)
