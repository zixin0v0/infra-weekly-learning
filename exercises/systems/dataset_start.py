from torch.utils.data import Dataset


class FileDataset(Dataset):
    def __init__(self, csv_path, delay_seconds=0.0):
        raise NotImplementedError("读取小型 CSV，保存样本 ID 和可选延迟")

    def __len__(self):
        raise NotImplementedError("返回样本数")

    def __getitem__(self, index):
        raise NotImplementedError("按 index 返回 ID、input、target；在此模拟读取等待")
