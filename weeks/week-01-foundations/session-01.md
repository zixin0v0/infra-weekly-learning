# W1 第一段备课：类型、地址与元素字节

[三段导学](study-guide.md) · [开课更新](refresh-2026-10-01.md) · [范围与验收](README.md)

备课日期：2026-10-01。状态：资料核验与环境烟雾检查完成；学习者诊断、指定阅读和段内练习待完成。

本段要回答：**类型怎样影响运算和地址移动？同样 6 个元素，怎样算出数据区的字节数？**

## 今天怎样推进

按仓库的 [导学规则](../../docs/study-guide.md) 和 [学习方式](../../docs/learning-workflow.md)，每个小块都先读指定位置，再写预测，随后动手核对。卡住时先针对自己的解释补一句提示，再回到原材料；检查通过后进入下一块。

周 README 的 20 分钟诊断计入原有实现预算。诊断答案尚未收到，不能把已有工具或备课完成当成先修通过。

| 顺序 | 阅读位置与停止点 | 中文重点 | 暂停时留下什么 | 资料预算 |
| --- | --- | --- | --- | --- |
| A. 类型 | CS106L 第 2 讲，阅读器第 35～48 页；第 44 页先暂停，第 48 页结束 | 运算使用操作数的类型；赋值目标类型与表达式求值要分开看 | 一条类型与结果的预测 | 15 分钟 |
| B. 地址 | CS106L 第 6 讲，第 70～85 页；第 78 页先暂停，读完第 85 页 `Array pointer` 结束 | 值、地址、指针对象是不同对象；指针移动按元素计 | 一幅数组地址图与一条指针移动预测 | 20 分钟 |
| C. Tensor | 固定版本讲义的 `tensors_basics` 与 `tensors_memory` 中 FP32/FP16 小例子；到 `## bf16` 前结束 | 元素数乘以单元素字节数 | 两种 dtype 的字节预测与计数范围 | 15 分钟 |

50 分钟包括选读和纸上预测；完整实现与核对使用 W1 原有实践时段。视频替换 C 块的相应阅读时间，全周资料预算仍为 150 分钟。

## A. 类型：先判断表达式，再看接收它的变量

打开 [CS106L 第 2 讲 PDF](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-02-TypesAndStructs.pdf#page=35)。页码均为阅读器从 1 开始的页序。

第 35 页从 `Types` 开始，随后看静态类型与错误检查。到第 44 页 `Your turn` 先尝试原页练习，再看后面的核对页。第 48 页是总结；函数重载只理解“参数类型影响选用哪个函数”，本段不展开 structs。

中文重点：编译器依据类型检查操作是否合法；表达式内部的运算先发生，再把结果赋给目标变量。用下面的自拟例子区分这两步。

```cpp
double integer_result = 9 / 4;
double floating_result = 9.0 / 4;
```

**暂停题 A**：两行结果是否相同？分别指出除法两边的类型，并解释把结果放进 `double` 是否会改变先前的除法过程。先写预测，再编译核对。

过关条件：能解释自己的预测依据；若预测不一致，能指出出错的是表达式类型还是赋值步骤。

## B. 地址：读懂指针指向什么

打开 [CS106L 第 6 讲 PDF](https://web.stanford.edu/class/archive/cs/cs106l/cs106l.1266/lectures/2026Spring-06-Iterators.pdf#page=70)。

阅读顺序：第 70 页 `Pointers and Memory` → 第 72～74 页 `Memory Basics` → 第 78 页取地址与解引用 → 第 84 页连续数组图 → 第 85 页 `Array pointer`。跳过过场问答页；迭代器的分类和容器 API 巡览留在本段之外。

中文重点：`&value` 取得对象地址，`*pointer` 访问其指向的对象。指针变量自身也需要存储；`sizeof(pointer)` 与 `sizeof(*pointer)` 分别描述指针对象和所指元素。材料中的 `int` 四字节示意不能推广为所有 C++ 实现的保证，实际类型大小用 `sizeof` 检查。

```cpp
std::array<float, 6> values{1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f};
float* first_element = values.data();
float* second_element = first_element + 1;
```

**暂停题 B**：`second_element - first_element` 的单位是什么？在本次已检查的环境里，相邻元素起始地址的数值间距应是多少字节？`sizeof(first_element)` 能否拿来计算这 6 个元素的数据量？

在同一数组内，指针加减按元素索引计算，两个元素指针的差是元素数；字节间距还要乘元素大小。这一补充依据 [C++ 标准草案的加减运算规则](https://eel.is/c++draft/expr.add)。`std::array` 的连续性依据 [array 概述](https://eel.is/c++draft/array.overview)，不额外加入必读预算。

用这张自拟图辅助预测。偏移相对于第一个元素，表示普通连续数据区；这是布局推导，不是实测地址。

| 元素索引 | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| FP32 起始字节偏移 | 0 | 4 | 8 | 12 | 16 | 20 |
| FP16 起始字节偏移 | 0 | 2 | 4 | 6 | 8 | 10 |

过关条件：能从图中解释连续存储和地址移动，知道最后一个元素后面仍有一个完整元素的存储宽度。局部数组的生命周期结束后，指向其元素的指针不能继续访问那些元素。

## C. Tensor：把地址图转成字节账本

使用 [CS336 Lecture 2 固定版本讲义](https://github.com/stanford-cs336/lectures/blob/6ff836dd5dfcbe7e848fe1a1734f1886f1116a7a/lecture_02.py)，搜索 `tensors_basics`，只看维度与形状；随后搜索 `tensors_memory`，看 FP32 的 `numel` / `element_size` 和 FP16 小例子。大矩阵分配示例只读其计数思路，实践改用本周 6 个元素，到 `## bf16` 前结束。

配套 [Spring 2026 Lecture 2 官方视频](https://www.youtube.com/watch?v=kuYAsz7zspQ)。已核对标题与主题，未核对播放和字幕时间轴；上述函数是讲义定位词，没有已确认的视频分钟数。视频中找不到对应片段时，按固定讲义完成同一范围。

| 词或接口 | 中文读法与作用 | 本段要区分什么 |
| --- | --- | --- |
| shape / rank | 各维长度 / 维度个数 | `(2, 3)` 有两个维度、六个元素 |
| dtype | 元素类型 | 同一形状可使用不同的元素存储宽度 |
| `numel()` | 元素总数 | 数量单位是元素 |
| `element_size()` | 单个元素的字节数 | 数量单位是字节/元素 |
| `data_ptr()` | 第一个元素的数据地址 | Python 的 `id(tensor)` 表示对象身份，不能用来代替数据地址 |

本段使用普通、独立创建的连续 dense CPU Tensor，计数公式为：

```text
逻辑元素数据字节数 = numel() × element_size()
```

官方接口依据：[numel](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.numel.html)、[element_size](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.element_size.html)、[data_ptr](https://docs.pytorch.org/docs/2.14/generated/torch.Tensor.data_ptr.html)。网页为 2.14；本机为 2.5.1，本次已用本机 docstring 核对这三个接口的核心定义。

**暂停题 C**：分别预测 6 个 FP32 和 FP16 元素的数据区字节数。将形状从 `(6,)` 改成 `(2, 3)`，元素数与逻辑字节数是否变化？写清理由后再运行。

这个数字只计元素数据。对象元数据、分配器开销、共享底层 storage 和峰值显存要另作账本；共享视图的计数留到第二段。低位宽打包、scale 与算子支持的观察留在开课记录和第三段假设算例中。

## 暂停实现：复用 W1 的一个实验目录

计划入口：`labs/01-foundations/resource-accounting/`。本次备课没有创建这些学习实现或结果文件，动手时再建立；三段共用同一目录。

1. 创建 `array_memory.cpp`：对上述 `std::array<float, 6>` 求和，打印 `sizeof(float)`、`sizeof(float*)`、相邻元素地址和同数组的指针差。用手算求和作参考；把元素总字节数与指针大小分别记录。
2. 创建 `tensor_bytes.py`：用相同数值、相同 CPU 设备，分别创建 FP32/FP16 Tensor；打印 shape、dtype、device、numel、element_size、data_ptr 和逻辑字节数。只改变 dtype；形状对照另做一组。
3. 保留一个元素、零个元素与本周六个元素的核对。空数组不访问首元素，空 Tensor 不依据数据指针作布局推断；求和与字节数均与相应手算比较。
4. 在同目录 `notes.md` 记录预测、真实输出与差异解释。没有结果前不创建带示例数字的结果文件。

Python 入口为 `C:\Users\cao\anaconda3\python.exe`。C++ 使用已通过烟雾检查的 MinGW g++ 15.2.0，按 C++17 编译。下列 PowerShell 命令在练习源文件创建后、从仓库根目录执行；临时优先使用编译器目录，退出后恢复当前进程原 PATH。

```powershell
$w1OriginalPath = $env:PATH
try {
    $env:PATH = 'D:\mingw64\bin;' + $w1OriginalPath
    g++ -std=c++17 -Wall -Wextra -pedantic .\labs\01-foundations\resource-accounting\array_memory.cpp -o .\labs\01-foundations\resource-accounting\array_memory.exe
    if ($LASTEXITCODE -ne 0) { throw '数组练习编译失败' }
    & .\labs\01-foundations\resource-accounting\array_memory.exe
    if ($LASTEXITCODE -ne 0) { throw '数组练习运行失败' }
} finally {
    $env:PATH = $w1OriginalPath
}
& 'C:\Users\cao\anaconda3\python.exe' .\labs\01-foundations\resource-accounting\tensor_bytes.py
```

## 进入第二段前的检查

- [ ] 能用自己的话解释表达式类型、取地址和解引用。
- [ ] 能区分元素指针的差、字节地址间距、指针对象大小。
- [ ] 数组求和、元素总字节数与手算一致，边界输入处理明确。
- [ ] FP32/FP16 的元素字节账本与预测一致，计数对象写清楚。
- [ ] 保存环境、完整命令和真实输出，并解释至少一个原先不确定的点。

<details>
<summary>完成预测与运行后，再展开核对提示</summary>

在本次环境中，`float` 是 4 字节、指针是 8 字节。同数组相邻 `float*` 的差为 1 个元素，对应 4 字节间距；六个 `float` 的元素数据为 24 字节。FP16 六元素的逻辑数据为 12 字节。这些是核对期望，不是已完成学习练习的结果。

整数除法例子两行分别得到 2.0 与 2.25；求和例子的手算是 21。改 shape 而保持元素数量与 dtype 时，逻辑字节计数不变。第二段再检查改变布局是否共享数据。

</details>

## 本段记录

在本实验 `notes.md` 用 `W1-S01` 分节，与后两段的段号一致；保存实际阅读位置、原预测、完整运行命令、结果解释和一个未解决问题。

- 实际读到的标题或函数：待填写。
- 自己的预测：待填写。
- 练习代码与运行命令：待创建并填写。
- 手算、实际结果与差异解释：未运行学习练习。
- 尚未解决的一个问题：待填写。

先完成 A 块的暂停题，再沿 B、C 推进；通过段内检查后回到 [第二段导学](study-guide.md)。
