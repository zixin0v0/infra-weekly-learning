class Recorder:
    def __init__(self):
        raise NotImplementedError("每个实例初始化自己的记录")

    def add(self, value):
        raise NotImplementedError("保存数值")

    def values(self):
        raise NotImplementedError("返回记录；说明返回副本或原对象的选择")
