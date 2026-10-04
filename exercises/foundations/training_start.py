"""练习起点：固定五点回归。补全函数后另从空文件完成保存和重载。"""

import torch


def make_problem():
    train_inputs = torch.tensor([[-2.0], [-1.0], [0.0], [1.0], [2.0]])
    validation_inputs = torch.tensor([[-1.5], [0.5], [1.5]])
    return train_inputs, 2 * train_inputs + 1, validation_inputs, 2 * validation_inputs + 1


def make_model():
    model = torch.nn.Linear(1, 1)
    with torch.no_grad():
        model.weight.zero_()
        model.bias.zero_()
    return model


def train_step(model, optimizer, inputs, targets):
    raise NotImplementedError("返回更新前的 mean MSE 浮点数；完成清梯度、前向、反向和更新")


def evaluate(model, inputs, targets):
    raise NotImplementedError("返回 mean MSE 浮点数；禁用梯度记录且不改变参数")


def main():
    train_inputs, train_targets, validation_inputs, validation_targets = make_problem()
    model = make_model()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    for step in range(50):
        train_loss = train_step(model, optimizer, train_inputs, train_targets)
        if (step + 1) % 10 == 0:
            validation_loss = evaluate(model, validation_inputs, validation_targets)
            print({"step": step + 1, "train_loss_before_update": train_loss,
                   "validation_loss_after_update": validation_loss})


if __name__ == "__main__":
    main()
