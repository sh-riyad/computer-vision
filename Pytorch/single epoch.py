import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

train_set = torchvision.datasets.FashionMNIST(
    root="./data",
    train=True,
    download=True,
    transform=transforms.Compose([
        transforms.ToTensor()
    ])
)

train_loader = torch.utils.data.DataLoader(train_set, batch_size=100)

def get_num_correct(preds, labels):
    return preds.argmax(dim=1).eq(labels).sum().item()

class Network(nn.Module):
    def __init__(self):
        super().__init__()
        
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5)
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=12, kernel_size=5)
        
        self.fc1 = nn.Linear(in_features=12*4*4, out_features=120)
        self.fc2 = nn.Linear(in_features=120, out_features=60)
        
        self.out = nn.Linear(in_features=60, out_features=10)
        
    def forward(self, t):
        t = F.relu(self.conv1(t))
        t = F.max_pool2d(t, kernel_size=2, stride=2)
            
        t = F.relu(self.conv2(t))
        t = F.max_pool2d(t, kernel_size=2, stride=2)
            
        t = t.reshape(-1, 12*4*4)
            
        t = F.relu(self.fc1(t))
        t = F.relu(self.fc2(t))  
        t = self.out(t)
            
        return t

network = Network()
optimizer = optim.Adam(network.parameters(), lr=0.01)

total_loss = 0
total_correct = 0

for batch in train_loader:
    images, labels = batch
    preds = network(images)
    
    optimizer.zero_grad()
    loss = F.cross_entropy(preds, labels)
    loss.backward()
    
    optimizer.step()
        
    total_loss += loss.item()
    total_correct += get_num_correct(preds, labels)
    
print("Total number of batches", len(train_set)/100 )
print("epoch:", 0, "total_correct: ", total_correct, "total_loss: ", total_loss)
print(f"Accuracy : {total_correct/len(train_loader):.4f}%")