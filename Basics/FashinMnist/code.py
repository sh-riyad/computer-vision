import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision

train_data = torchvision.datasets.FashionMNIST(
    root='./data',
    train=True,
    download=True,
    transform=transforms.Compose([
        transforms.ToTensor()
    ])
)
print(train_data.shape)