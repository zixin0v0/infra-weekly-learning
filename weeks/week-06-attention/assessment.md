# W6 掌握检查

[返回本单元](README.md) · [我的进度](../../course/progress.md)

先自己作答，再展开核对。保存你的解释、代码和运行结果；查接口时保留自己的推导，未运行的实验继续记为待做。

<a id="w6"></a>

## W6：模型形状与整体成本

先不看图，写出 Q、K、V、score 与输出的 shape，再完成小 Block 和显式 Attention/SDPA 对照。说明 mask、dropout 与模式设置怎样保证可比较；这里不要求实现完整 FlashAttention。

**换个条件试试：** 固定 batch/heads/head_dim，sequence 翻倍，显式 score 与 K/V 元素数各如何变？

**找出问题：** eval 后仍传 `dropout_p=0.1` 给函数式 SDPA，却要求确定性对齐，问题在哪里？

<details><summary>展开核对推导；结果不同时，从这里检查</summary>

score 的两个序列维导致四倍，K/V 一条序列维导致两倍；不同后端未必物化完整 score，不能把公式等同于实测峰值。函数式 SDPA 按传入概率处理 dropout，对齐时显式设 0。还需核对 mask、causal、dtype、容差。回 W6 第一/三段；类结构回 P8。


数元素时沿每个维度逐项相乘，再只替换改变的那一维。数学表达式需要的中间对象，与具体后端实际保存的对象，要分开讨论。 [回看 Attention 形状图](session-01.md)。

</details>

## 清理以后还占显存，先查谁在引用

连续八步保存 prediction.detach() 到 GPU 列表，再调用 empty_cache；解释为何数据仍可能存活。把记录改成标量 loss.item()，区分它与“复制一个不连图的 GPU Tensor”。再说明 Adam 第一次 step 前后新增了什么。

<details><summary>核对对象寿命</summary>

detach 切断求导关系但保留数据存储；列表仍引用输出，empty_cache 不能释放活对象。item 得到 Python 标量，但可能同步 GPU；Adam 第一次更新通常建立逐参数统计与步数。回 [第四段](session-04.md)，用有界对照观察 allocated/reserved；没有实测时不能仅凭这些原理诊断某个真实程序泄漏。

</details>

## 掌握检查

- [ ] 解释训练状态寿命，并完成有界留存对照；GPU 未测部分单独注明。
- [ ] 资源账本区分参数、激活、中间矩阵与实测峰值。
- [ ] 明确前向或训练计时范围，两个实现语义一致。
- [ ] 有算子表、原始测量和一段时间线，能区分热点算子与等待时间。
- [ ] 能解释分块与在线 Softmax 的联系；本周不要求完整实现 FlashAttention2。

可选：完成基础后，从补充阅读选一个实际问题写进报告；未选不影响本单元完成。

## 做完之后

把自己的解释、实现、变式结果和排错过程放进 `notes.md`，再按实际完成情况更新进度。若还有一项说不清，回到核对里的链接，用更小的输入重做。

[上一课](session-04.md) · [返回单元课表](README.md) · [下一步](../week-13-systems/README.md)
