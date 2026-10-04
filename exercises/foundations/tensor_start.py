import torch


def describe_tensor(values):
    raise NotImplementedError("返回 shape、stride、dtype、numel、element_size 和连续性")


def broadcast_then_matmul(values, offset):
    raise NotImplementedError("分别计算广播相加，以及原输入乘原输入转置")
