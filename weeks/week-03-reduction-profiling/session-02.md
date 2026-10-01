# W3 第二段学习指南：warp 交换与参与 mask

[单元范围](README.md) · [三段学习导航](study-guide.md) · [资料复核](refresh-2026-10-01.md) · [上一段](session-01.md)

整理日期：2026-10-01。原文选读预算：45 分钟。状态：学习指南已整理；实际正确性与同步检查待完成。

本地图解、暂停题与核对另计入本单元的自查时段，完整时间见 [分项预算](../../docs/study-guide.md#time-budget)。

## 目标与先修

将 warp 内交换、warp 间组合、block 间收尾分清。先通过共享内存版本的边界与 memcheck；主线使用完整 warp 组成的 block。

## 读哪里，在哪里停

| 预算 | 原始来源与指定范围 | 停止点 |
| --- | --- | --- |
| 30 分钟 | [NVIDIA Warp-Level Primitives](../../resources/README.md#r-warp) 的 Synchronized Data Exchange、Active Mask Query、Warp Synchronization | 每节对应示例结束；只追踪 shuffle、mask、同步 |
| 15 分钟 | [Compute Sanitizer](../../resources/README.md#r-sanitizer) 的 Using Racecheck、Using Synccheck | 启动与首个报告解释结束；先保证 memcheck 已通过 |

访问日：2026-10-01。博客用于同步语义，旧性能数字不作本机预测。

## 概念说明

shuffle 交换 warp 中线程的寄存器值，不能直接跨 warp。常用分工是每 warp 得到一个部分和，写共享内存，完成 block 同步后再组合。共享内存减少了，仍要说明剩余跨 warp 依赖。

mask 描述参与约定；主线让 block 大小为 warp 大小的整数倍，无效输入填零，所需线程均执行同一交换。不是“写 full mask 就自动安全”；warp 内分歧与读非参与 lane 的值会破坏假设。

## 暂停题与预测

1. 128 线程的 block 最先产生几个 warp 部分和？它们放在哪里，下一步谁读？
2. 一个线程没有有效输入，填 0 但参与交换，与直接跳过交换有什么不同？仅调用 `__activemask()` 能自动解决所有分歧吗？

先画 warp 边界，再标参与线程，最后回三个指定标题；不要直接抄 mask 常量。

## 读图与自查

```text
128 线程 block（本图例）
warp 0：lane 0..31 → s0 ┐
warp 1：lane 0..31 → s1 ├→ shared[0..3] → block barrier
warp 2：lane 0..31 → s2 ┤                         ↓
warp 3：lane 0..31 → s3 ┘          warp 0 读取 4 个和，其余 lane 填 0
                                              ↓
                                        block 部分和
```

箭头跨 warp 的位置经过共享内存。回到主线 256 线程配置时，把图中的 4 个 warp 改为 8 个，其他依赖保持。

<details>
<summary>写下预测后，再核对本段问题</summary>

**题 1**：128/32=4 个 warp 部分和。每 warp 的一个线程写入共享数组，同步后再由一个 warp 合并。最后一次合并只有 4 个有效值，也可以让完整 warp 参与，其他 lane 置 0。

**题 2**：填 0 仍参与交换保留了同一参与约定；直接跳过可能导致其他 lane 读到未参与者的未定义值。activemask 只反映执行当时活跃线程，不能自动修复此前的分歧、缺少的参与者或跨 warp 共享内存依赖。错在最后合并时先检查填零与 barrier，再检查 mask。

这些说明用于核对推导；运行结果仍需自己验证。答错时保留原答案，回看本段“读哪里”或“卡点”指向的位置，再换一个小输入重做。

</details>

## 可选：问 AI

先独立作答和核对，仍有疑问时再使用；跳过本节不影响完成本段。

> 我认为 shuffle 的 mask 表示【自己的解释】，跨 warp 的合并过程是【列步骤】。请给一个能检验这段解释的四 warp 小例子，先让我标参与 lane，再指出遗漏的同步。不要只给 full mask 常量或完整实现。

## 动手与检查

继续 `labs/02-cuda/reduction/`，新增 warp 版本。固定输入、累加 dtype、block 大小、第二阶段和计时边界，仅改变第一阶段归约方式；沿用上一段的尾部与近零测试。

顺序运行 memcheck、racecheck、synccheck，工具检查不参与计时。保存各工具命令与结果；racecheck 主要检查共享内存访问危险，零报告不能证明全部竞态不存在。当前不支持部分 warp 的实现明确写出约束，不把未覆盖输入写已通过。

## 卡点与过关

| 卡点 | 最小回看位置 | 重新检查 |
| --- | --- | --- |
| 非整齐长度错 | Synchronized Data Exchange | 尾部线程是否填零并参与 |
| warp 内正确、全 block 错 | Warp Synchronization、跨 warp 共享读写 | 写完部分和后谁等待谁 |

- [ ] 解释参与 mask 的条件。
- [ ] 两个版本用同一参考、尾部和收尾检查。
- [ ] 记录省去的操作与剩余同步，不以工具结果代替语义证明。

在 `notes.md` 的 `W3-S02` 留下预测、命令和限制；通过后进入 [第三段](session-03.md)。
