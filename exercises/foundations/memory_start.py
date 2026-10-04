"""有界显存观察与待补全训练步。默认 CPU；CUDA 只在显式选择时使用。"""

import argparse
import json

import torch


def measure_stage(label, device):
    record = {"stage": label, "device": str(device)}
    if device.type == "cuda":
        torch.cuda.synchronize(device)
        record.update(allocated=torch.cuda.memory_allocated(device),
                      reserved=torch.cuda.memory_reserved(device),
                      peak_allocated=torch.cuda.max_memory_allocated(device))
    else:
        record["cuda_memory"] = "未测量"
    return record


def train_step_with_records(model, optimizer, inputs, targets):
    raise NotImplementedError("复用自己的训练步，在前向、反向、更新、清理后采样；返回记录列表")


def retained_outputs(device):
    records = [measure_stage("before", device)]
    outputs = []
    for index in range(8):
        outputs.append(torch.full((256, 256), float(index), device=device).detach())
    records.append(measure_stage("retained_8", device))
    if device.type == "cuda":
        torch.cuda.empty_cache()
    records.append(measure_stage("empty_cache_while_live", device))
    outputs.clear()
    records.append(measure_stage("cleared", device))
    if device.type == "cuda":
        torch.cuda.empty_cache()
    records.append(measure_stage("empty_cache_after_clear", device))
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cpu")
    arguments = parser.parse_args()
    if arguments.device == "cuda" and not torch.cuda.is_available():
        parser.error("CUDA 不可用；先用 CPU 解释引用，显存实测留待补做")
    device = torch.device(arguments.device)
    if device.type == "cuda":
        torch.cuda.init()
        torch.cuda.reset_peak_memory_stats(device)
    print(json.dumps(retained_outputs(device), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
