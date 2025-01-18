import torchvision
import torchvision.transforms as transforms

def getData(root = './data', train=True):
    train_set = torchvision.datasets.FashionMNIST(
        root = root,
        train = train,
        download = True,
        transform = transforms.Compose([
            transforms.ToTensor()
        ])
    )
    return train_set