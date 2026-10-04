import json
from pathlib import Path


def summarize(values):
    raise NotImplementedError("补全 count、sum、mean；空输入抛出 ValueError")


def load_values(input_path):
    raise NotImplementedError("从 UTF-8 JSON 文件读取数值数组并验证输入")


def save_summary(result, output_path):
    raise NotImplementedError("写入 JSON，再由新的进程读回核对")
