"""绘制课程原创示意图；所有数值均为推演例子，不是性能测量。"""

import argparse
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
from PIL import Image, ImageOps, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "figures"
COLORS = {"input": "#E4EFFB", "compute": "#EDE6F7", "output": "#E3F2E9",
          "transfer": "#FFF0D9", "storage": "#E9EDF1", "error": "#FCE4E3"}
INK = "#203349"
FIGURES = {}


def configure_font():
    candidates = [Path("C:/Windows/Fonts/msyh.ttc"),
                  Path("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")]
    font_path = next((path for path in candidates if path.is_file()), None)
    if font_path is None:
        raise SystemExit("未找到中文字体。请安装微软雅黑或 Noto Sans CJK，并在 configure_font 中指定字体文件。")
    font_manager.fontManager.addfont(str(font_path))
    family = font_manager.FontProperties(fname=str(font_path)).get_name()
    plt.rcParams.update({"font.family": family, "font.size": 16,
                         "axes.unicode_minus": False, "svg.fonttype": "path",
                         "svg.hashsalt": "infra-learning-figures"})
    warnings.filterwarnings("error", message="Glyph .* missing from font")
    return font_path


def figure(name):
    def register(draw):
        FIGURES[name] = draw
        return draw
    return register


def canvas(title, subtitle, height=6.5):
    drawing, axis = plt.subplots(figsize=(10, height))
    drawing.subplots_adjust(left=0.025, right=0.975, top=0.98, bottom=0.02)
    axis.set(xlim=(0, 100), ylim=(0, 100))
    axis.axis("off")
    text(axis, 2, 95, title, 23, weight="bold", align="left")
    text(axis, 2, 87, subtitle, 14, align="left")
    return drawing, axis


def text(axis, horizontal, vertical, label, size=16, align="center", **kwargs):
    return axis.text(horizontal, vertical, label, fontsize=size, color=INK,
                     ha=align, va="center", linespacing=1.6, **kwargs)


def box(axis, horizontal, vertical, width, height, label, kind="compute", size=16, sketch=False):
    patch = FancyBboxPatch((horizontal, vertical), width, height,
                          boxstyle="round,pad=0.25,rounding_size=1.3",
                          facecolor=COLORS[kind], edgecolor=INK, linewidth=1.3)
    if sketch:
        patch.set_sketch_params(scale=0.5, length=100, randomness=1.5)
    axis.add_patch(patch)
    text(axis, horizontal + width / 2, vertical + height / 2, label, size)


def arrow(axis, start, end, label="", dashed=False, label_offset=4):
    axis.add_patch(FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=16,
                                  color=INK, linewidth=1.6,
                                  linestyle="--" if dashed else "-"))
    if label:
        text(axis, (start[0] + end[0]) / 2, (start[1] + end[1]) / 2 + label_offset,
             label, 13, bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})


def cells(axis, horizontal, vertical, values, width=10, height=9, kind="storage", indices=False):
    for index, value in enumerate(values):
        axis.add_patch(Rectangle((horizontal + index * width, vertical), width, height,
                                facecolor=COLORS[kind], edgecolor=INK, linewidth=1.2))
        text(axis, horizontal + (index + 0.5) * width, vertical + height / 2, str(value))
        if indices:
            text(axis, horizontal + (index + 0.5) * width, vertical - 4, str(index), 13)


def note(axis, label):
    text(axis, 2, 5, label, 14, align="left")


@figure("p01-function-call")
def function_call():
    drawing, axis = canvas("函数的结果去了哪里？", "例子：double(3)；实线表示调用与返回，虚线表示屏幕输出")
    box(axis, 2, 57, 29, 18, "调用处\nresult = double(3)", "input")
    box(axis, 42, 57, 26, 18, "函数内部\nreturn value * 2")
    arrow(axis, (31, 70), (42, 70), "参数 3")
    arrow(axis, (42, 61), (31, 61), "返回 6", label_offset=-7)
    box(axis, 3, 24, 28, 17, "print(result)", "compute")
    box(axis, 44, 24, 24, 17, "屏幕显示 6", "output")
    arrow(axis, (17, 57), (17, 41))
    arrow(axis, (31, 32), (44, 32), "显示", dashed=True)
    box(axis, 76, 31, 21, 41, "若函数只\nprint(value * 2)\n\n调用者得到\nNone", "error", 15)
    note(axis, "先追踪返回给变量的值，再看输出；看到数字不代表函数返回了数字。")
    return drawing


@figure("w01-tensor-layout")
def tensor_layout():
    drawing, axis = canvas("转置改变访问方式，不必搬动数据", "手算例子：2 × 2 Tensor；stride 的单位是元素，偏移从 0 开始", 7.5)
    text(axis, 2, 76, "同一份 storage", 16, align="left")
    cells(axis, 37, 71, [0, 1, 2, 3], 13, indices=True)
    text(axis, 33, 81, "位置索引标在格下", 12, align="left")
    box(axis, 3, 31, 41, 26, "原 Tensor\nshape = (2, 2)\nstride = (2, 1)", "input")
    box(axis, 56, 31, 41, 26, "转置视图\nshape = (2, 2)\nstride = (1, 2)", "input")
    arrow(axis, (24, 57), (43, 71), "共享", label_offset=-3)
    arrow(axis, (76, 57), (70, 71), "共享", label_offset=-3)
    text(axis, 24, 21, "第 0 行读位置 0、1", 16)
    text(axis, 76, 21, "第 0 行读位置 0、2", 16)
    note(axis, "位置 = storage_offset + 行索引 × stride[0] + 列索引 × stride[1]")
    return drawing


@figure("w08-request-timeline")
def request_timeline():
    drawing, axis = canvas("一次请求：首 token、后续 token、结束事件", "假设的客户端时间戳；单位 s。间隔可以不相等，不是实测性能。", 7)
    times = [0, 0.40, 0.50, 0.70, 0.75]
    labels = ["发出", "token 1", "token 2", "token 3", "结束"]
    coordinates = [8 + stamp * 104 for stamp in times]
    arrow(axis, (5, 56), (94, 56))
    for index, (position, stamp, label) in enumerate(zip(coordinates, times, labels)):
        axis.plot([position, position], [53, 59], color=INK)
        text(axis, position, 66 if index != 4 else 77, label, 14)
        text(axis, position, 46 if index != 4 else 36, f"{stamp:.2f}", 14)
    arrow(axis, (8, 29), (49.6, 29), "TTFT = 0.40 s")
    arrow(axis, (49.6, 20), (80.8, 20), "TPOT = (0.70 − 0.40) / 2 = 0.15 s")
    note(axis, "E2E = 0.75 s；末 token 延迟 = 0.70 s；服务端阶段不能由这几个点精确反推。")
    return drawing


@figure("p02-branch-boundary")
def branch_boundary():
    drawing, axis = canvas("边界值，应该走哪一条路径？", "示例约定：用量不超过容量就接收；图中只画一个二选一判断")
    box(axis, 33, 65, 34, 15, "required = 8\ncapacity = 8", "input")
    box(axis, 32, 39, 36, 15, "required <= capacity ?", "compute")
    arrow(axis, (50, 65), (50, 54), "比较")
    box(axis, 6, 12, 33, 15, "接收：返回 True", "output")
    box(axis, 63, 12, 33, 15, "拒绝：返回 False", "error")
    arrow(axis, (36, 39), (23, 27), "是")
    arrow(axis, (64, 39), (79, 27), "否")
    note(axis, "先写清“等于时怎么办”，再选 < 或 <=；不要用模糊的“大概够用”。")
    return drawing


@figure("p03-loop-state")
def loop_state():
    drawing, axis = canvas("循环保存的是“到目前为止”的结果", "演示输入 [2, 5]；每读一个元素，更新一次 total")
    text(axis, 3, 73, "列表位置", align="left")
    cells(axis, 30, 68, [2, 5], 15, indices=True, kind="input")
    for horizontal, label in [(4, "开始\ntotal = 0"), (36, "读位置 0\ntotal = 0 + 2"), (68, "读位置 1\ntotal = 2 + 5")]:
        box(axis, horizontal, 30, 27, 20, label)
    arrow(axis, (31, 40), (36, 40))
    arrow(axis, (63, 40), (68, 40))
    text(axis, 50, 18, '字典记录 {"count": 2, "total": 7}；用键 "total" 取结果', 16)
    note(axis, "列表按位置访问，字典按键访问；初始化放在循环外，才能保留上一轮贡献。")
    return drawing


@figure("p04-exception-path")
def exception_path():
    drawing, axis = canvas("错误在哪里发生，在哪里处理？", '例子：main 调用 parse_count("abc")；转换失败后，不会完成赋值')
    box(axis, 3, 57, 27, 21, "main()\n显示有用的错误", "output")
    box(axis, 38, 57, 25, 21, "parse_count(text)\n检查输入")
    box(axis, 71, 57, 26, 21, "int(text)\n尝试转换", "input")
    arrow(axis, (30, 72), (38, 72), "调用")
    arrow(axis, (63, 72), (71, 72), "调用")
    arrow(axis, (71, 59), (30, 59), "ValueError 沿调用栈传播", label_offset=-8)
    box(axis, 6, 16, 88, 21, "读 traceback：先看异常类型与失败行 → 再向上找调用者\n捕获预期输入错误；不要 except 后继续使用未赋值的 count", "error", 16)
    note(axis, "异常处理要让失败路径结束或明确重试；不能把失败伪装成正常的 0。")
    return drawing


@figure("p05-module-entry")
def module_entry():
    drawing, axis = canvas("同一个文件，直接运行和导入有什么不同？", "statistics_tool.py 中定义 summarize，并用 main guard 保护命令行入口")
    box(axis, 3, 62, 43, 17, "python statistics_tool.py 2 4", "input")
    box(axis, 54, 62, 43, 17, "import statistics_tool", "input")
    box(axis, 3, 32, 43, 19, '__name__ == "__main__"\n定义函数，再调用 main()')
    box(axis, 54, 32, 43, 19, '__name__ == "statistics_tool"\n定义函数，不自动调用 main()')
    arrow(axis, (24, 62), (24, 51))
    arrow(axis, (75, 62), (75, 51))
    text(axis, 24, 20, "解析字符串参数 → 计算 → 输出", 15)
    text(axis, 75, 20, "由其他代码选择何时调用函数", 15)
    note(axis, "导入也会执行模块顶层代码；入口保护只约束缩进在 guard 下面的部分。")
    return drawing


@figure("p06-file-lifetime")
def file_lifetime():
    drawing, axis = canvas("程序退出后，结果怎样留下来？", "例子：从 input.json 读取数值，在内存里计算，再保存 result.json")
    box(axis, 3, 61, 24, 18, "输入文件\ninput.json", "storage")
    box(axis, 38, 61, 24, 18, "进程 A 内存\n列表 → 统计", "compute")
    box(axis, 73, 61, 24, 18, "输出文件\nresult.json", "storage")
    arrow(axis, (27, 70), (38, 70), "load")
    arrow(axis, (62, 70), (73, 70), "dump")
    box(axis, 38, 20, 24, 20, "A 退出\n普通变量消失", "error")
    box(axis, 73, 20, 24, 20, "新进程 B\n读取并核对", "output")
    arrow(axis, (50, 61), (50, 40))
    arrow(axis, (85, 61), (85, 40), "重新打开")
    note(axis, "能重新读回内容，才完成本例；这不等于证明断电后数据也可靠。")
    return drawing


@figure("p07-tool-parts")
def tool_parts():
    drawing, axis = canvas("一个小工具，怎样连接输入、计算与检查？", "例子：统计工具；实线为数据流，虚线为观察或测试")
    box(axis, 3, 62, 25, 17, "命令行 / 配置\n选择最终参数", "input")
    box(axis, 38, 62, 24, 17, "读取并校验\nJSON 输入", "input")
    box(axis, 72, 62, 25, 17, "summarize\n纯计算函数", "compute")
    arrow(axis, (28, 70), (38, 70))
    arrow(axis, (62, 70), (72, 70))
    box(axis, 3, 23, 25, 17, "日志\n记录阶段与错误", "output")
    box(axis, 38, 23, 24, 17, "测试\n输入 → 预期值", "input")
    box(axis, 72, 23, 25, 17, "输出文件\n保存统计结果", "storage")
    arrow(axis, (15, 62), (15, 40), dashed=True)
    arrow(axis, (62, 32), (76, 62), "调用检查", dashed=True)
    arrow(axis, (85, 62), (85, 40))
    note(axis, "参数优先级：显式命令行 > 配置文件 > 默认值。日志不替代结果文件。")
    return drawing


@figure("p08-instance-state")
def instance_state():
    drawing, axis = canvas("两个实例，为什么应当各记各的数？", "演示：Counter() 创建两个对象；self 指向本次调用的那个对象")
    box(axis, 33, 67, 34, 14, "Counter 类：状态与方法", "compute")
    box(axis, 6, 30, 37, 23, "left 实例\n初值 0 → add(4) → 4", "input")
    box(axis, 57, 30, 37, 23, "right 实例\n初值 0 → 仍是 0", "input")
    arrow(axis, (39, 67), (24, 53), "创建")
    arrow(axis, (61, 67), (76, 53), "创建")
    text(axis, 50, 18, "left.add(4) 中的 self 就是 left；没有修改 right", 16)
    note(axis, "每次 __init__ 内新建列表，才让 Recorder 的记录按实例独立。")
    return drawing


@figure("s01-process-device")
def process_device():
    drawing, axis = canvas("程序在 CPU 上运行，怎样让 GPU 开始工作？", "示意关系：进程拥有状态，线程提交工作；GPU 队列不属于 CPU 线程", 7)
    box(axis, 3, 64, 23, 16, "程序文件\n与启动配置", "storage")
    box(axis, 36, 57, 60, 25, "", "storage")
    text(axis, 66, 77, "CPU 进程：自己的地址空间", 16)
    box(axis, 39, 60, 24, 11, "主线程", "compute", 15)
    box(axis, 68, 60, 24, 11, "工作线程", "compute", 15)
    arrow(axis, (26, 71), (36, 71), "启动")
    box(axis, 4, 20, 31, 18, "CPU 继续执行\n或等待完成", "compute")
    box(axis, 53, 20, 42, 18, "设备队列 → GPU kernel", "compute")
    arrow(axis, (57, 57), (71, 38), "提交")
    arrow(axis, (53, 27), (35, 27), "完成后可同步", dashed=True)
    note(axis, "提交返回不代表 GPU 已算完；进程里的线程通常共享内存，另一个进程不会自动共享。")
    return drawing


@figure("s02-request-path")
def request_path():
    drawing, axis = canvas("先连到服务，应用才有机会检查请求", "本地例子：http://127.0.0.1:8000/v1/completions", 7)
    entries = [(3, 61, "客户端\n方法 / 头 / JSON", "input"),
               (38, 61, "地址与端口\n连接监听服务", "transfer"),
               (73, 61, "应用路由\n检查字段", "compute"),
               (73, 22, "队列与模型\n生成输出", "compute"),
               (38, 22, "响应\n状态 / body", "output"),
               (3, 22, "客户端记录\n时间与结果", "output")]
    for horizontal, vertical, label, kind in entries:
        box(axis, horizontal, vertical, 24, 18, label, kind)
    arrow(axis, (27, 70), (38, 70))
    arrow(axis, (62, 70), (73, 70))
    arrow(axis, (85, 61), (85, 40))
    arrow(axis, (73, 31), (62, 31))
    arrow(axis, (38, 31), (27, 31))
    text(axis, 50, 49, "连接失败：查监听与端口；收到 4xx：再查应用请求", 15)
    note(axis, "127.0.0.1 指当前网络环境自身。数字地址省去域名解析这一层。")
    return drawing


@figure("s02-latency-bandwidth")
def latency_bandwidth():
    drawing, axis = canvas("小消息和大消息，主要等在不同地方", "理论单链路模型 T ≈ L + N/B；L = 10 μs，B = 10 GB/s（十进制）")
    for vertical, size_label, transfer, total in [(60, "1 KB", "0.1 μs", "10.1 μs"), (28, "10 MB", "1000 μs", "1010 μs")]:
        box(axis, 3, vertical, 19, 17, size_label, "input")
        box(axis, 30, vertical, 26, 17, "启动 10 μs", "transfer")
        box(axis, 63, vertical, 33, 17, "搬运 " + transfer, "transfer")
        arrow(axis, (22, vertical + 8), (30, vertical + 8))
        arrow(axis, (56, vertical + 8), (63, vertical + 8), "+")
        text(axis, 80, vertical - 7, "总计 " + total, 15)
    note(axis, "方框不按时间比例绘制；真实 collective 有多个阶段，不能直接套作总耗时。")
    return drawing


@figure("s03-container-port")
def container_port():
    drawing, axis = canvas("端口映射，把请求交给哪个进程？", "命令中的 -p 127.0.0.1:8080:80：左侧是宿主端口，右侧是容器端口", 7)
    box(axis, 30, 17, 67, 62, "", "storage")
    text(axis, 34, 74, "宿主环境（Linux 内核）", 16, align="left")
    box(axis, 55, 25, 38, 35, "", "input")
    text(axis, 74, 53, "容器实例", 17)
    text(axis, 74, 38, "应用监听 :80", 17)
    box(axis, 3, 38, 20, 17, "客户端\n访问 :8080", "input")
    arrow(axis, (23, 46), (55, 46), "转发")
    box(axis, 4, 65, 20, 15, "镜像模板", "storage")
    arrow(axis, (24, 72), (55, 61), "创建实例", dashed=True)
    note(axis, "映射到 :81 不会让应用改为监听 :81；Windows 的 Linux 容器依赖 Linux 环境。")
    return drawing


@figure("s04-data-pipeline")
def data_pipeline():
    drawing, axis = canvas("GPU 的下一批数据，何时准备好？", "假设读取一批 20 ms、计算一批 10 ms；忽略传输，演示稳态等待", 7.5)
    for horizontal, label, kind in [(3, "文件 / 样本", "storage"), (28, "Dataset\n读取与预处理", "input"), (53, "DataLoader\n组 batch", "input"), (78, "传输后\nGPU 计算", "compute")]:
        box(axis, horizontal, 65, 20, 16, label, kind, 14)
    for horizontal in (23, 48, 73):
        arrow(axis, (horizontal, 73), (horizontal + 5, 73))
    text(axis, 3, 48, "读数据", 15, align="left")
    text(axis, 3, 28, "GPU", 15, align="left")
    scale = 1
    for start in (0, 20, 40):
        box(axis, 23 + start * scale, 42, 20 * scale, 12, "读 20", "input", 14)
    for start in (20, 40, 60):
        box(axis, 23 + start * scale, 22, 10 * scale, 12, "算 10", "compute", 13)
    for stamp in (0, 20, 40, 60, 70):
        text(axis, 23 + stamp, 14, str(stamp), 12)
    note(axis, "时间单位 ms；理想流水后每 20 ms 才有下一批，计算之间仍可能等 10 ms。")
    return drawing


@figure("s05-persistence")
def persistence():
    drawing, axis = canvas("容器换了，文件路径怎样接回同一份数据？", "named volume 的生命周期独立于单个容器；图中箭头表示写入或读取")
    box(axis, 3, 59, 27, 21, "容器 A\n/data/step.txt\n写入 2", "compute")
    box(axis, 38, 34, 24, 25, "volume\ninfra-study-data\n保存文件", "storage", 15)
    box(axis, 70, 59, 27, 21, "新容器 B\n/data/step.txt\n读回 2", "output")
    arrow(axis, (28, 59), (40, 55), "写")
    arrow(axis, (61, 55), (73, 59), "读")
    box(axis, 4, 13, 26, 19, "A 退出并删除\n普通内存不保留", "error", 15)
    box(axis, 70, 13, 27, 19, "挂错 volume\n同路径也无此文件", "error", 15)
    note(axis, "训练恢复还要加载模型、优化器、随机状态和数据位置，再比较下一步。")
    return drawing


@figure("s06-task-dependencies")
def task_dependencies():
    drawing, axis = canvas("依赖满足，是否就能立即运行？", "例子：读样本 A → 预处理 B；加载模型 C；推理 D；保存 E", 7)
    for horizontal, vertical, label, kind in [(3, 64, "A 读样本", "input"), (34, 64, "B 预处理", "compute"), (34, 30, "C 加载模型", "storage"), (68, 64, "D 推理", "compute"), (68, 30, "E 保存", "storage")]:
        box(axis, horizontal, vertical, 26, 16, label, kind)
    arrow(axis, (29, 72), (34, 72))
    arrow(axis, (60, 72), (68, 72))
    arrow(axis, (60, 38), (76, 64), "依赖")
    arrow(axis, (81, 64), (81, 46))
    text(axis, 5, 19, "先确认依赖完成 → 再检查空闲资源 → 才能开始执行", 17, align="left")
    note(axis, "箭头表示依赖，不表示占用 CPU 的数量；有空闲 CPU 也不能越过未完成的依赖。")
    return drawing


@figure("s06-kubernetes-objects")
def kubernetes_objects():
    drawing, axis = canvas("配置对象怎样对应到运行中的容器？", "两个不同的例子：Job 管理有限任务；Deployment 维护服务副本", 8)
    box(axis, 3, 66, 27, 14, "Job：有限任务", "input")
    box(axis, 38, 66, 28, 14, "Deployment：副本", "input", 15)
    box(axis, 73, 66, 24, 14, "Service：入口", "transfer")
    box(axis, 3, 31, 27, 22, "任务 Pod\n运行到完成", "compute")
    box(axis, 40, 31, 38, 22, "服务 Pod\n容器运行应用", "compute")
    arrow(axis, (16, 66), (16, 53), "管理", label_offset=0)
    arrow(axis, (51, 66), (51, 53), "经 ReplicaSet", label_offset=0)
    arrow(axis, (84, 66), (72, 53), "选择就绪后端")
    box(axis, 2, 10, 27, 12, "ConfigMap / Secret", "storage", 14)
    box(axis, 73, 10, 24, 12, "PVC → 存储卷", "storage", 14)
    arrow(axis, (24, 22), (43, 31), "配置", label_offset=0)
    arrow(axis, (76, 22), (69, 31), "挂载", label_offset=0)
    note(axis, "控制器维护期望状态；scheduler 选节点；kubelet / 容器运行时负责启动。")
    return drawing


@figure("w01-element-bytes")
def element_bytes():
    drawing, axis = canvas("地址走一步，是一个元素还是一个字节？", "假设示例：4 个元素；每格表示一个元素，标注相对起点的字节偏移")
    text(axis, 3, 66, "FP32\n4 B/元素", align="left")
    cells(axis, 25, 57, [0, 4, 8, 12], 17, 15, "input")
    text(axis, 3, 33, "FP16\n2 B/元素", align="left")
    cells(axis, 25, 25, [0, 2, 4, 6], 8.5, 15, "input")
    text(axis, 83, 32, "总量 8 B", 16)
    text(axis, 79, 47, "上排总量 16 B", 16)
    note(axis, "最后一个起始偏移 + 一个元素宽度 = 数据区长度；指针本身的大小另计。")
    return drawing


@figure("w01-view-copy")
def view_copy():
    drawing, axis = canvas("视图共享原数据；连续副本有自己的数据", "沿用 2 × 2 小例；下方新 storage 按转置后的逻辑顺序保存")
    box(axis, 3, 61, 23, 18, "base / 转置视图", "input", 15)
    cells(axis, 42, 65, [0, 1, 2, 3], 12, indices=True)
    arrow(axis, (26, 70), (42, 70), "共用")
    box(axis, 3, 25, 23, 18, "非连续视图\ncontiguous()", "compute", 15)
    cells(axis, 42, 29, [0, 2, 1, 3], 12, indices=True)
    arrow(axis, (26, 34), (42, 34), "复制")
    arrow(axis, (66, 60), (66, 43), "按逻辑顺序读写", dashed=True)
    note(axis, "本例转置不连续，需要复制；输入已连续时，contiguous() 不保证新分配。")
    return drawing


@figure("w01-linear-shapes")
def linear_shapes():
    drawing, axis = canvas("增加 batch，为什么没有增加权重参数？", "手算例子：X[2,3] × W^T[3,4] + bias[4] = Y[2,4]", 7)
    for horizontal, label, rows, columns, kind in [(4, "输入 X", 2, 3, "input"), (37, "参与乘法的 W^T", 3, 4, "storage"), (73, "乘法结果", 2, 4, "output")]:
        text(axis, horizontal + 11, 75, label, 16)
        for row in range(rows):
            cells(axis, horizontal, 57 - row * 8, [""] * columns, 6, 8, kind)
    text(axis, 29, 59, "×", 25)
    text(axis, 66, 59, "=", 25)
    text(axis, 85, 43, "逐行加 bias 后得到 Y", 12)
    box(axis, 6, 17, 88, 20, "2 行输入各用同一组 12 个权重；bias 还有 4 个参数\nbatch 翻倍：输出行数与计算量翻倍，参数仍是 16 个", "compute", 17)
    note(axis, "模块内 W 保存为 [out,in]=[4,3]；GEMM 按每乘加 2 FLOPs 计数。")
    return drawing


@figure("w02-thread-coverage")
def thread_coverage():
    drawing, axis = canvas("线程怎样覆盖数组的每个有效位置？", "手算例子：N = 7，blockDim.x = 4；grid 启动两个 block", 7)
    for block_index, horizontal in [(0, 5), (1, 54)]:
        text(axis, horizontal + 19, 73, f"blockIdx.x = {block_index}", 17)
        cells(axis, horizontal, 51, list(range(4)), 10, 12, "input")
        cells(axis, horizontal, 29, [block_index * 4 + lane for lane in range(4)], 10, 12, "compute")
        text(axis, horizontal + 19, 46, "局部编号 → 全局下标", 14)
    axis.add_patch(Rectangle((84, 29), 10, 12, fill=False, hatch="///", edgecolor=INK, linewidth=1.3))
    text(axis, 50, 18, "global = blockIdx.x × blockDim.x + threadIdx.x", 17)
    note(axis, "映射到下标 7 的线程无有效元素：先判断 global < N；格子不表示执行时间。")
    return drawing


@figure("w02-timing-boundaries")
def timing_boundaries():
    drawing, axis = canvas("CPU 提交返回，GPU 可能才刚开始", "依赖示意，不按耗时比例；预先分配不计入这里的端到端区间", 7)
    for horizontal, label, kind in [(6, "H2D", "transfer"), (36, "kernel", "compute"), (66, "D2H", "transfer")]:
        box(axis, horizontal, 46, 25, 18, label, kind)
    arrow(axis, (31, 55), (36, 55))
    arrow(axis, (61, 55), (66, 55))
    text(axis, 49, 77, "同一 stream 的依赖顺序", 18)
    arrow(axis, (36, 33), (61, 33), "start Event → stop Event", label_offset=-7)
    arrow(axis, (6, 15), (91, 15), "CPU 端到端：开始 → 等 D2H 完成 → 结束", label_offset=6)
    note(axis, "读取 Event 耗时前等待 stop 完成；等待 kernel 本身不会自动把结果复制到 CPU。")
    return drawing


@figure("w03-reduction-stages")
def reduction_stages():
    drawing, axis = canvas("归约先合并局部值，再合并部分和", "手算例子：[2, 4, 1, 3]；图画依赖关系，不代表实际线程编号", 8)
    for horizontal, value in [(5, 2), (29, 4), (57, 1), (81, 3)]:
        box(axis, horizontal, 66, 14, 13, str(value), "input")
    box(axis, 16, 40, 25, 14, "2 + 4 = 6")
    box(axis, 63, 40, 25, 14, "1 + 3 = 4")
    for start, end in [((12, 66), (24, 54)), ((36, 66), (33, 54)), ((64, 66), (71, 54)), ((88, 66), (79, 54))]:
        arrow(axis, start, end)
    box(axis, 36, 14, 28, 14, "6 + 4 = 10", "output")
    arrow(axis, (29, 40), (45, 28))
    arrow(axis, (76, 40), (55, 28))
    text(axis, 50, 34, "跨 block：先写部分和，再由后续阶段读取", 13,
         bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
    note(axis, "block 内共享数据要满足同步；本实验跨 block 后把部分和拷回 CPU 收尾。")
    return drawing


@figure("w03-warp-combine")
def warp_combine():
    drawing, axis = canvas("shuffle 不能直接替代跨 warp 的同步", "示意：64 线程 block，两个完整 warp；无效输入填 0，仍遵守参与约定")
    box(axis, 3, 60, 37, 19, "warp 0：32 lanes\n寄存器交换 → s0")
    box(axis, 59, 60, 37, 19, "warp 1：32 lanes\n寄存器交换 → s1")
    cells(axis, 37, 35, ["s0", "s1"], 13, 12)
    arrow(axis, (23, 60), (43, 47), "写共享内存")
    arrow(axis, (78, 60), (57, 47), "写共享内存")
    box(axis, 19, 12, 62, 13, "block barrier 后，由一个 warp 合并", "output", 16)
    arrow(axis, (50, 35), (50, 25))
    note(axis, "mask 声明参与线程；它不是自动修复分歧、缺失 lane 或共享内存竞态的开关。")
    return drawing


@figure("w04-tile-reuse")
def tile_reuse():
    drawing, axis = canvas("一份输入，怎样用于多个输出？", "示例 tile 大小 T=2；两块 FP32 输入 tile 共 2×2²×4 = 32 B", 8)
    for horizontal, label, kind in [(5, "A tile", "input"), (39, "B tile", "input"), (73, "C tile 累加", "output")]:
        text(axis, horizontal + 10, 75, label, 16)
        for row in range(2):
            cells(axis, horizontal, 60 - row * 10, ["", ""], 10, 10, kind)
    arrow(axis, (25, 61), (39, 61), "×")
    arrow(axis, (59, 61), (73, 61), "累加")
    text(axis, 50, 41, "一个 A 元素用于 2 个输出列；一个 B 元素用于 2 个输出行", 15)
    for horizontal, label, kind in [(3, "加载\nA / B", "transfer"), (27, "同步①\n数据齐备", "storage"), (51, "读取并\n累加", "compute"), (75, "同步②\n读完才覆盖", "storage")]:
        box(axis, horizontal, 16, 21, 17, label, kind, 15)
    for horizontal in (24, 48, 72):
        arrow(axis, (horizontal, 24), (horizontal + 3, 24))
    note(axis, "沿 K 方向重复这些步骤；尾部输入填零，最终写 C 时再检查输出边界。")
    return drawing


@figure("w04-roofline-model")
def roofline_model():
    drawing, axis = canvas("计算量和搬运量，哪一项限制理想速度？", "纯理论示例：计算上限 8 GFLOP/s，带宽 2 GB/s；不是任何硬件测量", 7)
    arrow(axis, (13, 20), (91, 20))
    arrow(axis, (13, 20), (13, 77))
    coordinates = [(13 + intensity * 8, 20 + min(8, 2 * intensity) * 6) for intensity in range(10)]
    axis.plot([point[0] for point in coordinates], [point[1] for point in coordinates], color=INK, linewidth=3)
    text(axis, 66, 75, "计算上限 8 GFLOP/s", 16)
    text(axis, 52, 42, "带宽 × 算术强度", 16)
    for intensity in (0, 2, 4, 6, 8):
        text(axis, 13 + intensity * 8, 15, str(intensity), 13)
    text(axis, 64, 8, "算术强度（FLOPs/B）", 14)
    text(axis, 12, 83, "GFLOP/s", 13, align="left")
    text(axis, 7, 68, "8", 13)
    return drawing


@figure("w05-softmax-state")
def softmax_state():
    drawing, axis = canvas("分块 Softmax，为什么旧结果要重新缩放？", "计算状态为最大值 m 与相对这个最大值的指数和 l；不用直接算巨大指数", 8)
    box(axis, 3, 58, 42, 22, "已读块 [2, 3]\nm=3，l=exp(−1)+1", "input", 17)
    box(axis, 56, 58, 41, 22, "新块 [4]\n新最大值 m'=4", "input", 17)
    arrow(axis, (25, 58), (40, 45), "旧块重缩放")
    arrow(axis, (77, 58), (63, 45), "新块贡献")
    box(axis, 7, 23, 86, 22, "l' = l × exp(3−4) + exp(4−4)\n= exp(−2) + exp(−1) + 1", "compute", 20)
    text(axis, 50, 14, "输出每项：exp(value − 4) / l'；所有块使用同一尺度", 16)
    note(axis, "mask 外值用 −∞ 排除；整行全无有效值时，要单独定义行为。")
    return drawing


@figure("w06-attention-shapes")
def attention_shapes():
    drawing, axis = canvas("Attention：先算“看谁”，再组合 Value", "单头手算形状：序列 S=3，head_dim=2；省略 batch 与 head 两维", 8)
    box(axis, 3, 64, 23, 16, "Q[3,2]", "input")
    box(axis, 36, 64, 26, 16, "K^T[2,3]", "input")
    box(axis, 72, 64, 25, 16, "分数[3,3]", "compute")
    text(axis, 31, 72, "×", 24)
    text(axis, 67, 72, "=", 24)
    box(axis, 70, 33, 27, 20, "除以 √2\nmask → softmax", "compute", 16)
    arrow(axis, (84, 64), (84, 53))
    box(axis, 35, 33, 27, 20, "权重[3,3]\n× V[3,2]", "input")
    arrow(axis, (70, 43), (62, 43))
    box(axis, 3, 33, 24, 20, "输出[3,2]", "output")
    arrow(axis, (35, 43), (27, 43))
    text(axis, 50, 18, "因果 mask：第 0 行只看位置 0；第 1 行看 0、1；第 2 行看 0、1、2", 14)
    note(axis, "分数矩阵是 [S,S]；KV Cache 保存历史 Key/Value，不是这张分数矩阵。")
    return drawing


@figure("w06-block-flow")
def block_flow():
    drawing, axis = canvas("Block 中的形状相同，不代表工作相同", "pre-norm 示例；残差两端形状均为 [batch, sequence, d_model]", 7)
    labels = [("X", "input"), ("Norm", "compute"), ("Attention", "compute"), ("加回 X", "compute"), ("Norm → MLP", "compute"), ("再加残差", "output")]
    for index, (label, kind) in enumerate(labels):
        horizontal = 4 + (index % 3) * 33
        vertical = 61 if index < 3 else 22
        box(axis, horizontal, vertical, 26, 17, label, kind, 16)
    arrow(axis, (30, 69), (37, 69))
    arrow(axis, (63, 69), (70, 69))
    arrow(axis, (83, 61), (17, 39), "Attention 输出", label_offset=0)
    arrow(axis, (30, 30), (37, 30))
    arrow(axis, (63, 30), (70, 30))
    arrow(axis, (17, 61), (17, 39), "残差", dashed=True)
    axis.plot([17, 17, 83], [22, 13, 13], color=INK, linestyle="--", linewidth=1.6)
    arrow(axis, (83, 13), (83, 22), dashed=True)
    text(axis, 50, 16, "第二条残差", 13)
    note(axis, "每条加法两端必须形状兼容；测量时还要包含 CPU 提交、搬运与等待。")
    return drawing


@figure("w07-collective-values")
def collective_values():
    drawing, axis = canvas("先看每个 rank 最后拿到什么", "两 rank 手算例子：rank 0 输入 [2,4]；rank 1 输入 [1,3]；使用 SUM", 8)
    rows = [("操作", "rank 0 输出", "rank 1 输出"),
            ("AllReduce", "[3,7]", "[3,7]"),
            ("Broadcast root=0", "[2,4]", "[2,4]"),
            ("AllGather", "[2,4,1,3]", "[2,4,1,3]"),
            ("ReduceScatter", "[3]", "[7]")]
    for row_index, row in enumerate(rows):
        for column_index, label in enumerate(row):
            box(axis, 3 + column_index * 32, 67 - row_index * 13, 30, 11,
                label, "storage" if row_index == 0 else "output", 15)
    note(axis, "拼接保留每个输入元素；归约先逐位置求和。rank 编号不等于物理设备编号。")
    return drawing


@figure("w07-topology")
def topology():
    drawing, axis = canvas("逻辑通信相同，物理路径可能不同", "两种假设连接关系；不代表当前机器的互连或 P2P 支持", 7)
    box(axis, 3, 61, 25, 18, "rank 0\nGPU A", "input")
    box(axis, 72, 61, 25, 18, "rank 1\nGPU B", "input")
    arrow(axis, (28, 70), (72, 70), "路径一：设备间直连")
    box(axis, 3, 19, 25, 18, "GPU A", "input")
    box(axis, 39, 19, 23, 18, "共享连接\n交换 / 中转", "transfer", 15)
    box(axis, 72, 19, 25, 18, "GPU B", "input")
    arrow(axis, (28, 28), (39, 28))
    arrow(axis, (62, 28), (72, 28))
    text(axis, 50, 46, "路径二：经过其他设备或共享链路", 16)
    note(axis, "先记录真实 topo 与通信路径，再解释消息曲线；algbw / busbw 不是链路采样。")
    return drawing


@figure("w08-prefill-decode")
def prefill_decode():
    drawing, axis = canvas("prefill 与 decode，每次处理的行数不同", "单请求示例：提示词 3 个 token；d 是输入宽度，h 是投影输出宽度", 7)
    box(axis, 3, 58, 28, 22, "prefill\n输入 [3,d]", "input")
    box(axis, 39, 58, 25, 22, "× 权重 [d,h]", "storage")
    box(axis, 72, 58, 25, 22, "输出 [3,h]\n各层写入 KV", "output")
    arrow(axis, (31, 69), (39, 69))
    arrow(axis, (64, 69), (72, 69))
    box(axis, 3, 20, 28, 22, "decode 一步\n新位置 [1,d]", "input")
    box(axis, 39, 20, 25, 22, "× 同一组权重\n读历史 KV", "storage", 15)
    box(axis, 72, 20, 25, 22, "输出 [1,h]\n追加新位置 KV", "output", 15)
    arrow(axis, (31, 31), (39, 31))
    arrow(axis, (64, 31), (72, 31))
    note(axis, "图展示投影形状；注意力还要读取历史 KV，不能把 decode 当成只做一次小 GEMM。")
    return drawing


@figure("w09-kv-pages")
def kv_pages():
    drawing, axis = canvas("逻辑 token 连续，物理 KV 块不必连续", "示例：块容量 4 token；请求 A/B 共享已确认相同的完整前缀块", 8)
    box(axis, 3, 64, 28, 16, "A 的块表：[2,5]", "input")
    box(axis, 3, 33, 28, 16, "B 的块表：[2,7]", "input")
    for vertical, label, contents in [(65, "物理块 2", ["p0", "p1", "p2", "p3"]),
                                     (40, "物理块 5", ["a4", "a5", "空", "空"]),
                                     (15, "物理块 7", ["b4", "空", "空", "空"])]:
        text(axis, 65, vertical + 15, label, 15)
        cells(axis, 45, vertical, contents, 12, 10, "storage")
    arrow(axis, (31, 76), (45, 71))
    arrow(axis, (31, 66), (45, 45))
    arrow(axis, (31, 45), (45, 68))
    arrow(axis, (31, 36), (45, 20))
    note(axis, "块表负责映射；共享块不能被某个请求随意改写，必要时复制后再写。")
    return drawing


@figure("w10-queue-intuition")
def queue_intuition():
    drawing, axis = canvas("请求来得比处理快，等待会堆在哪里？", "轻手绘类比：一张工作台代表有限处理能力；真实服务可能批量处理", 7)
    for index, label in enumerate(["请求 C", "请求 B", "请求 A"]):
        box(axis, 4 + index * 18, 47, 16, 19, label, "input", 14, sketch=True)
    box(axis, 69, 42, 27, 29, "工作台\n处理当前请求", "compute", 16, sketch=True)
    arrow(axis, (57, 56), (69, 56), "准入")
    text(axis, 31, 32, "队列等待：尚未开始处理", 17)
    text(axis, 82, 28, "服务时间", 17)
    box(axis, 5, 9, 90, 12, "请求延迟 = 等待 + 服务 + 约定范围内的网络等开销", "output", 17)
    note(axis, "这是排队直觉，不是 GPU 按请求串行执行的架构图，也没有测量吞吐。")
    return drawing


@figure("w11-gradient-sync")
def gradient_sync():
    drawing, axis = canvas("不同数据产生的梯度，怎样得到同一次更新？", "示意：两 rank、局部 batch 等大、loss 为样本均值；先保持相同参数", 8)
    box(axis, 3, 64, 35, 16, "rank 0：本地梯度 g0", "input", 16)
    box(axis, 62, 64, 35, 16, "rank 1：本地梯度 g1", "input", 16)
    box(axis, 23, 36, 54, 17, "同步后：g = (g0 + g1) / 2", "transfer", 19)
    arrow(axis, (22, 64), (38, 53))
    arrow(axis, (80, 64), (63, 53))
    box(axis, 3, 12, 35, 15, "相同 optimizer 更新", "output", 16)
    box(axis, 62, 12, 35, 15, "相同 optimizer 更新", "output", 16)
    arrow(axis, (37, 36), (22, 27))
    arrow(axis, (63, 36), (79, 27))
    note(axis, "图画数值依赖；实际 backward 可按桶与通信重叠，不应把同步梯度再除一次 world size。")
    return drawing


@figure("w12-shard-gather")
def shard_gather():
    drawing, axis = canvas("长期只持有分片，计算前仍可能需要完整参数", "概念示意：4 份参数分到两 rank；只画参数，不把它当峰值显存公式", 8)
    text(axis, 22, 76, "rank 0", 18)
    text(axis, 77, 76, "rank 1", 18)
    cells(axis, 8, 59, ["p0", "p1"], 14, 12)
    cells(axis, 63, 59, ["p2", "p3"], 14, 12)
    arrow(axis, (23, 59), (23, 40), "按需 AllGather")
    arrow(axis, (78, 59), (78, 40), "按需 AllGather")
    cells(axis, 3, 28, ["p0", "p1", "p2", "p3"], 11, 12, "compute")
    cells(axis, 53, 28, ["p0", "p1", "p2", "p3"], 11, 12, "compute")
    text(axis, 50, 18, "计算后是否重新分片、何时释放，由所选策略与执行阶段决定", 15)
    note(axis, "梯度可 ReduceScatter，优化器维护相应分片；峰值还要计激活、通信和临时缓冲。")
    return drawing


@figure("w12-next-step")
def next_step():
    drawing, axis = canvas("恢复后能读文件，还要比较“下一步”", "实验结构：连续 3 步，对照先跑 2 步、保存并重启后再跑 1 步", 7)
    box(axis, 3, 61, 26, 18, "连续运行\nstep 1 → 2", "compute")
    box(axis, 69, 61, 28, 18, "step 3\n下一批 / loss / 更新", "output", 14)
    arrow(axis, (29, 70), (69, 70), "同一状态继续")
    box(axis, 3, 20, 26, 18, "分段运行\nstep 1 → 2", "compute")
    box(axis, 37, 20, 25, 18, "保存 → 重启\n加载完整状态", "storage", 15)
    box(axis, 69, 20, 28, 18, "恢复后的 step 3\n逐项比较", "output", 15)
    arrow(axis, (29, 29), (37, 29))
    arrow(axis, (62, 29), (69, 29))
    arrow(axis, (83, 61), (83, 38), "对照", dashed=True)
    note(axis, "模型权重以外，还需优化器、步数、随机状态与数据位置；失败与容差写入记录。")
    return drawing


@figure("w13-graph-kernels")
def graph_kernels():
    drawing, axis = canvas("Python 表达式，怎样对应到计算图和 kernel？", "示意表达式：relu(X @ W + bias)；具体拆分与融合要看实际后端", 7)
    box(axis, 3, 62, 94, 17, "Python：调用 matmul → add → relu", "input", 20)
    for horizontal, label in [(6, "matmul"), (38, "add"), (70, "relu")]:
        box(axis, horizontal, 32, 24, 15, label, "compute", 17)
    arrow(axis, (30, 39), (38, 39))
    arrow(axis, (62, 39), (70, 39))
    arrow(axis, (50, 62), (50, 47), "捕获数据依赖")
    text(axis, 50, 19, "后端生成执行代码：可能融合部分操作，也可能保留多个 kernel", 16)
    note(axis, "Python 行数、图节点数与 kernel 数不是一一对应；数值等价先于性能比较。")
    return drawing


@figure("w13-amortization")
def amortization():
    drawing, axis = canvas("首次多花的时间，要靠多少次调用补回来？", "理论例子：首次多花 30 ms；此后每次节省 2 ms；忽略重编译", 7)
    box(axis, 3, 59, 28, 20, "首次调用\n额外 +30 ms", "transfer")
    box(axis, 40, 59, 28, 20, "后续每次\n节省 −2 ms", "output")
    arrow(axis, (31, 69), (40, 69))
    text(axis, 83, 69, "重复 N−1 次", 16)
    box(axis, 7, 22, 86, 22, "总差额 = 30 − (N−1) × 2 ms\nN=16 持平；N=17 才有净节省", "compute", 21)
    note(axis, "只有稳态确实更快，重复调用才有助于回本；输入与缓存变化可能改变这个估计。")
    return drawing


@figure("w14-tensor-parallel")
def tensor_parallel():
    drawing, axis = canvas("按列切开第一层，第二层为什么要求和？", "两层 MLP 的代数切分；图用 Y=XW 记号，省略 bias", 8)
    box(axis, 35, 66, 30, 15, "共享输入 X", "input")
    box(axis, 3, 37, 42, 20, "rank 0\nH0 = activation(XW0)", "compute", 16)
    box(axis, 55, 37, 42, 20, "rank 1\nH1 = activation(XW1)", "compute", 16)
    arrow(axis, (39, 66), (25, 57))
    arrow(axis, (61, 66), (77, 57))
    box(axis, 3, 13, 42, 14, "部分输出 H0V0", "output")
    box(axis, 55, 13, 42, 14, "部分输出 H1V1", "output")
    arrow(axis, (24, 37), (24, 27))
    arrow(axis, (76, 37), (76, 27))
    note(axis, "最终 Y = H0V0 + H1V1；求和通信后再加一次最终 bias。")
    return drawing


@figure("w14-pipeline-timeline")
def pipeline_timeline():
    drawing, axis = canvas("流水线的首尾，为什么会空着？", "假设：2 个阶段、3 个微批次，每阶段耗时 1 个时间槽；仅画前向", 7)
    text(axis, 3, 65, "阶段 0", 16, align="left")
    text(axis, 3, 38, "阶段 1", 16, align="left")
    for batch_index in range(3):
        box(axis, 22 + batch_index * 17, 56, 17, 17, f"微批 {batch_index + 1}", "compute", 15)
        box(axis, 39 + batch_index * 17, 29, 17, 17, f"微批 {batch_index + 1}", "output", 15)
        arrow(axis, (30 + batch_index * 17, 56), (47 + batch_index * 17, 46))
    box(axis, 73, 56, 17, 17, "空闲", "storage", 14)
    box(axis, 22, 29, 17, 17, "等待", "storage", 14)
    for slot in range(5):
        text(axis, 22 + slot * 17, 20, str(slot), 14)
    note(axis, "横轴单位：时间槽；总计 4 槽、忙碌 6/8 阶段槽。训练还需反向与更新依赖。")
    return drawing


@figure("w15-ray-objects")
def ray_objects():
    drawing, axis = canvas("拿到 ObjectRef，是否就已经拿到结果？", "关系示意：task 返回对象引用；下游依赖等待结果就绪，Actor 保存自己的状态", 8)
    box(axis, 3, 64, 27, 16, "提交 Task A", "input")
    box(axis, 39, 64, 27, 16, "ObjectRef", "storage")
    arrow(axis, (30, 72), (39, 72), "先返回引用")
    box(axis, 3, 32, 27, 17, "资源可用后\nA 真正执行", "compute")
    box(axis, 39, 32, 27, 17, "结果就绪\n对象可读取", "output")
    box(axis, 73, 32, 24, 17, "下游 Task B\n消费结果", "compute", 15)
    arrow(axis, (16, 64), (16, 49), "准入")
    arrow(axis, (30, 41), (39, 41))
    arrow(axis, (66, 41), (73, 41))
    arrow(axis, (52, 64), (52, 49), "指向", dashed=True)
    box(axis, 5, 10, 90, 13, "Actor：一个实例长期保存状态；方法调用与失败重试仍要明确语义", "storage", 16)
    note(axis, "资源暂时忙、要求永远不满足、开始后抛异常，是三种不同情况。")
    return drawing


@figure("w16-scheduling-trace")
def scheduling_trace():
    drawing, axis = canvas("同一批任务，平均等待与个体等待怎样变化？", "理论例子：一台串行机器；A/B/C 同在 t=0 到达，时长为 4/1/2 s", 8)
    schedules = [("FIFO", [("A", 4), ("B", 1), ("C", 2)], 61),
                 ("SJF", [("B", 1), ("C", 2), ("A", 4)], 34)]
    for label, schedule, vertical in schedules:
        text(axis, 3, vertical + 7, label, 18, align="left")
        start = 0
        for task, duration in schedule:
            box(axis, 22 + start * 10, vertical, duration * 10, 15, task,
                {"A": "compute", "B": "input", "C": "output"}[task], 18)
            start += duration
        for stamp in range(8):
            text(axis, 22 + stamp * 10, vertical - 5, str(stamp), 12)
    text(axis, 50, 18, "FIFO 等待 A/B/C = 0/4/5；SJF = 3/0/1 s", 17)
    note(axis, "平均等待从 3 s 降到 4/3 s，但 A 等得更久；这条有限轨迹不能证明无饥饿。")
    return drawing


@figure("reviews-system-map")
def system_map():
    drawing, axis = canvas("一次训练或请求，在哪些地方等待？", "系统关系示意；箭头表示数据或调度关系，不表示测量出的速度", 8)
    for horizontal, vertical, label, kind in [(3, 64, "文件 / 对象存储\n数据与 checkpoint", "storage"),
        (38, 64, "CPU\n读取 / 预处理 / 提交", "compute"),
        (73, 64, "GPU\n模型计算与显存", "compute"),
        (3, 26, "服务请求\n网络 / 队列", "input"),
        (38, 26, "调度与控制\n依赖 / 资源 / 重试", "transfer"),
        (73, 26, "其他 GPU / 节点\n集合通信", "transfer")]:
        box(axis, horizontal, vertical, 24, 18, label, kind, 14)
    arrow(axis, (27, 73), (38, 73), "读取")
    arrow(axis, (62, 73), (73, 73), "传输")
    arrow(axis, (85, 64), (85, 44), "同步")
    arrow(axis, (27, 35), (38, 35), "准入")
    arrow(axis, (50, 44), (50, 64), "执行")
    arrow(axis, (39, 64), (21, 44), "返回结果", dashed=True, label_offset=-3)
    arrow(axis, (38, 67), (27, 67), "保存", dashed=True, label_offset=-6)
    text(axis, 50, 15, "等待可能在输入、CPU、传输、通信或队列；恢复错误还要查状态与存储路径", 14)
    note(axis, "先找事件和数据经过哪里，再取相应日志、指标或 trace；单个 GPU 利用率不够。")
    return drawing


@figure("d01-training-step")
def training_step():
    drawing, axis = canvas("求出梯度之后，参数为什么还没变？", "标量手算：weight=1，loss=(weight×2−6)²，SGD 学习率 0.1", 8)
    box(axis, 3, 61, 27, 19, "zero_grad\n清理旧梯度", "storage")
    box(axis, 38, 61, 27, 19, "forward / loss\nloss = 16", "compute")
    box(axis, 73, 61, 24, 19, "backward\ngrad = −16", "compute")
    arrow(axis, (30, 70), (38, 70))
    arrow(axis, (65, 70), (73, 70))
    box(axis, 8, 22, 49, 22, "step 更新参数\n1 − 0.1 × (−16) = 2.6", "output", 20)
    box(axis, 67, 22, 30, 22, "梯度存在 .grad\n此时 weight 仍为 1", "storage", 15)
    arrow(axis, (85, 61), (85, 44))
    arrow(axis, (67, 33), (57, 33), "使用梯度")
    note(axis, "backward 负责累加梯度；optimizer.step 才修改参数；下一步仍需明确清梯度。")
    return drawing


@figure("w07-allreduce-steps")
def allreduce_steps():
    drawing, axis = canvas("AllReduce 可以怎样分成两步？", "两 rank 的概念分解：先归约并分片，再收集；不是某次 NCCL 的实际执行轨迹", 8)
    rows = [("输入", "[2, 4]", "[1, 3]", 64, "input"),
            ("ReduceScatter 后", "[3]", "[7]", 38, "compute"),
            ("AllGather 后", "[3, 7]", "[3, 7]", 12, "output")]
    text(axis, 47, 81, "rank 0", 16)
    text(axis, 82, 81, "rank 1", 16)
    for label, left, right, vertical, kind in rows:
        text(axis, 2, vertical + 7, label, 15, align="left")
        box(axis, 35, vertical, 25, 14, left, kind, 18)
        box(axis, 70, vertical, 25, 14, right, kind, 18)
    arrow(axis, (47, 64), (47, 52))
    arrow(axis, (82, 64), (82, 52))
    arrow(axis, (47, 38), (47, 26))
    arrow(axis, (82, 38), (82, 26))
    arrow(axis, (52, 64), (77, 52), dashed=True)
    arrow(axis, (77, 64), (52, 52), dashed=True)
    arrow(axis, (52, 38), (77, 26), dashed=True)
    arrow(axis, (77, 38), (52, 26), dashed=True)
    note(axis, "第一步每人保留一段最终和；第二步交换这些片段，双方得到完整结果。")
    return drawing


@figure("w14-weight-slices")
def weight_slices():
    drawing, axis = canvas("两层 MLP，分别沿矩阵的哪一维切？", "形状例子：X[2,4]；第一层 W[4,6]；第二层 V[6,4]；使用 Y=XW 记号", 8)
    text(axis, 26, 77, "W：按输出列切", 17)
    text(axis, 75, 77, "V：按输入行切", 17)
    for row_index in range(4):
        for column_index in range(6):
            axis.add_patch(Rectangle((8 + column_index * 6, 42 + row_index * 6), 6, 6,
                                     facecolor=COLORS["input" if column_index < 3 else "output"],
                                     edgecolor=INK, linewidth=1))
    for row_index in range(6):
        for column_index in range(4):
            axis.add_patch(Rectangle((63 + column_index * 6, 36 + row_index * 6), 6, 6,
                                     facecolor=COLORS["output" if row_index < 3 else "input"],
                                     edgecolor=INK, linewidth=1))
    text(axis, 17, 36, "W0[4,3]", 15)
    text(axis, 37, 36, "W1[4,3]", 15)
    text(axis, 75, 63, "V0[3,4]", 16)
    text(axis, 75, 45, "V1[3,4]", 16)
    box(axis, 4, 12, 43, 17, "rank 0：XW0 → H0[2,3]\nH0V0 → 部分输出 [2,4]", "input", 15)
    box(axis, 53, 12, 43, 17, "rank 1：XW1 → H1[2,3]\nH1V1 → 部分输出 [2,4]", "output", 15)
    note(axis, "H0/H1 包含逐元素激活；两份部分输出做 SUM，得到最终 [2,4]。")
    return drawing



@figure("w01-float-spacing")
def float_spacing():
    drawing, axis = canvas("相同的两字节，可以有不同的刻度", "上排为 1 附近的相邻数；下排固定使用逐次 FP32 运算", 8)
    text(axis, 3, 74, "FP16", 17, align="left")
    text(axis, 3, 53, "BF16", 17, align="left")
    for vertical, count in ((70, 9), (49, 2)):
        axis.plot([21, 76], [vertical, vertical], color=INK, linewidth=1.3)
        for index in range(count):
            horizontal = 21 + index * 55 / (count - 1)
            axis.plot([horizontal, horizontal], [vertical - 2, vertical + 2],
                      color=INK, linewidth=1.6)
        text(axis, 21, vertical - 6, "1", 14)
        text(axis, 76, vertical - 6, "1.0078125", 14)
    text(axis, 49, 78, "每格 1/1024", 16)
    text(axis, 49, 57, "每格 1/128", 16)
    text(axis, 86, 65, "间隔越大\n区分越粗", 14)
    box(axis, 3, 12, 44, 22, "(2²⁴ + 1) − 2²⁴\n先舍入到 2²⁴，再减去 → 0", "compute", 15)
    box(axis, 53, 12, 44, 22, "(2²⁴ − 2²⁴) + 1\n先相消，再加 1 → 1", "output", 15)
    note(axis, "改变运算顺序可能改变舍入；更宽 dtype 不会找回此前已经丢失的信息。")
    return drawing


@figure("w02-gpu-hardware")
def gpu_hardware():
    drawing, axis = canvas("block 是工作分组，SM 才是执行硬件", "示意：grid 含 4 个 block，每个 128 线程；只画两个 SM，不代表设备规格", 8)
    box(axis, 3, 45, 24, 32, "逻辑 grid\nB0、B1、B2、B3\n每 block 4 warp", "input", 15)
    for horizontal, sm_id, block_id in ((36, 0, 0), (70, 1, 1)):
        box(axis, horizontal, 33, 27, 45, "", "storage")
        text(axis, horizontal + 13.5, 74, f"SM {sm_id}", 18)
        box(axis, horizontal + 2, 55, 23, 12, f"B{block_id} 的 warp\n按就绪情况执行", "compute", 13)
        text(axis, horizontal + 13.5, 44, "寄存器 / shared / L1\n有限片上资源", 13)
    arrow(axis, (27, 63), (36, 63), "分配", label_offset=5)
    arrow(axis, (27, 78), (70, 78), "一种可能安排", dashed=True, label_offset=3)
    text(axis, 14, 36, "B2/B3 可等资源\nblock 次序不保证", 13)
    box(axis, 36, 15, 61, 10, "L2 cache：多个 SM 共享的缓存", "transfer", 15)
    box(axis, 3, 12, 24, 14, "global memory\n设备显存", "storage", 15)
    arrow(axis, (27, 19), (36, 19))
    arrow(axis, (49, 25), (49, 33))
    arrow(axis, (83, 25), (83, 33))
    note(axis, "箭头示意调度或数据供应；不是每次访问都穿过全部层级，缓存也不保证命中。")
    return drawing


@figure("w06-memory-lifetime")
def memory_lifetime():
    drawing, axis = canvas("同一步训练，不同对象在不同时刻保留", "逻辑寿命示意：默认 backward、无额外引用；横向不是耗时，条长不是字节数", 8)
    stages = [(30, "准备"), (44, "前向"), (58, "反向"), (72, "step"), (87, "清理后")]
    for horizontal, label in stages:
        text(axis, horizontal, 77, label, 15)
        axis.plot([horizontal, horizontal], [24, 72], color="#BAC4CF", linewidth=1,
                  linestyle="--", zorder=0)
    rows = [("参数", 63, 26, 68, "storage"),
            ("反向保存值", 51, 41, 20, "compute"),
            ("参数梯度", 39, 55, 26, "output"),
            ("Adam 统计", 27, 69, 25, "storage")]
    for label, vertical, start, width, kind in rows:
        text(axis, 3, vertical + 4, label, 15, align="left")
        box(axis, start, vertical, width, 8, "", kind)
    text(axis, 41, 17, "去掉最后引用 → 可释放活对象", 14)
    text(axis, 76, 17, "空闲块可留在缓存池", 14)
    note(axis, "allocated 统计 Tensor 占用；reserved 包含缓存；重置峰值不等于释放内存。")
    return drawing


@figure("w15-retry-dedup")
def retry_dedup():
    drawing, axis = canvas("没收到确认，不代表效果没有发生", "单进程串行故障模拟；箭头顺序表示事件，不表示真实网络耗时", 8)
    text(axis, 16, 78, "调用方", 18)
    text(axis, 81, 78, "执行端", 18)
    box(axis, 3, 58, 27, 14, "① 提交 A / attempt 1", "input", 14)
    box(axis, 65, 58, 32, 14, "② 已执行：计数 0 → 2\n记录 A 的输入和结果", "storage", 14)
    arrow(axis, (30, 65), (65, 65), "加 2", label_offset=4)
    arrow(axis, (65, 54), (30, 54), "③ 确认丢失；调用方超时", dashed=True, label_offset=-4)
    box(axis, 3, 24, 27, 14, "④ 重试 A / attempt 2", "input", 14)
    box(axis, 65, 21, 32, 19, "⑤ 查询业务 ID：A\n已完成 → 返回首次结果\n不再次产生加法效果", "output", 13)
    arrow(axis, (30, 31), (65, 31), "同一业务输入", label_offset=5)
    arrow(axis, (65, 15), (30, 15), "返回已保存结果", dashed=True, label_offset=3)
    note(axis, "去重依靠 task_id，不靠 attempt_id；崩溃与并发下还需要持久化和原子性。")
    return drawing


def validate_drawing(drawing, name):
    drawing.canvas.draw()
    renderer = drawing.canvas.get_renderer()
    bounds = drawing.bbox
    for axis in drawing.axes:
        for label in axis.texts:
            extent = label.get_window_extent(renderer)
            if extent.x0 < 0 or extent.y0 < 0 or extent.x1 > bounds.width or extent.y1 > bounds.height:
                raise ValueError(f"{name}: 文字超出画布：{label.get_text()}")


def preview_pages(paths, destination):
    destination.mkdir(parents=True, exist_ok=True)
    for source in paths:
        with Image.open(source) as original:
            narrow = original.convert("RGB")
            narrow.thumbnail((600, 1600), Image.Resampling.LANCZOS)
            narrow.save(destination / source.name)
    for start in range(0, len(paths), 4):
        sheet = Image.new("RGB", (1200, 1050), "#FFFFFF")
        for offset, source in enumerate(paths[start:start + 4]):
            with Image.open(destination / source.name) as original:
                thumb = ImageOps.contain(original, (600, 495))
                horizontal = (offset % 2) * 600
                vertical = (offset // 2) * 525
                sheet.paste(thumb, (horizontal, vertical))
                ImageDraw.Draw(sheet).text((horizontal + 10, vertical + 500), source.stem, fill=INK)
        sheet.save(destination / f"contact-{start // 4 + 1:02d}.png")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("names", nargs="*", choices=None)
    parser.add_argument("--preview-dir", type=Path)
    arguments = parser.parse_args()
    font_path = configure_font()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    paths = []
    for name in arguments.names or FIGURES:
        if name not in FIGURES:
            parser.error(f"未知图名：{name}")
        drawing = FIGURES[name]()
        validate_drawing(drawing, name)
        for extension in ("png", "svg"):
            metadata = {"Date": None} if extension == "svg" else {"Software": "infra-learning"}
            drawing.savefig(OUTPUT / f"{name}.{extension}", dpi=140,
                            facecolor="white", metadata=metadata)
            if extension == "svg":
                destination = OUTPUT / f"{name}.svg"
                normalized = "\n".join(line.rstrip() for line in destination.read_text(encoding="utf-8").splitlines())
                destination.write_text(normalized + "\n", encoding="utf-8", newline="\n")
        paths.append(OUTPUT / f"{name}.png")
        plt.close(drawing)
    if arguments.preview_dir:
        preview_pages(paths, arguments.preview_dir)
    print(f"已导出 {len(paths)} 组 PNG/SVG；中文字体：{font_path}")


if __name__ == "__main__":
    main()
