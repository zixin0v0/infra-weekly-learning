import torch


def scalar_step(initial_weight, learning_rate):
    raise NotImplementedError("使用 (weight * 2 - 6) ** 2 求梯度，返回更新前梯度和更新后的权重")
