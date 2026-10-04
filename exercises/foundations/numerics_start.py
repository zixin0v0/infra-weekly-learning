"""练习起点：默认运行可读的小例子；误差报告需要自己补全。"""

import torch


def error_report(actual, reference, atol, rtol):
    raise NotImplementedError("检查 shape、空输入、容差和有限性；返回 finite、max_abs_error、close_count")


def main():
    source = torch.tensor([1.001, 70000.0], dtype=torch.float32)
    for dtype in (torch.float16, torch.bfloat16, torch.float32):
        limits = torch.finfo(dtype)
        converted = source.to(dtype)
        print({"dtype": str(dtype), "max": limits.max, "eps": limits.eps,
               "tiny": limits.tiny, "values": converted.float().tolist(),
               "finite": torch.isfinite(converted).tolist()})
    for dtype in (torch.float32, torch.float64):
        large = torch.tensor(2 ** 24, dtype=dtype)
        small = torch.tensor(1, dtype=dtype)
        print({"dtype": str(dtype), "add_first": ((large + small) - large).item(),
               "cancel_first": ((large - large) + small).item()})


if __name__ == "__main__":
    main()
