from __future__ import annotations

from torch.utils.data import DataLoader
from torchvision import datasets, transforms


def get_dataloaders(root: str, batch_size: int, num_workers: int):
    tfm = transforms.ToTensor()

    train_ds = datasets.MNIST(root=root, train=True, download=True, transform=tfm)
    test_ds = datasets.MNIST(root=root, train=False, download=True, transform=tfm)

    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True, num_workers=num_workers)
    test_loader = DataLoader(test_ds, batch_size=batch_size, shuffle=False, num_workers=num_workers)

    return train_loader, test_loader