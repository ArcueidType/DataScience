import torch
import torchvision.datasets
from torch import nn
from torchvision.transforms import ToTensor
import random
from torch.utils import data


device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)


class MNISTNetwork(nn.Module):
    def __init__(self):
        super(MNISTNetwork, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(1, 6, 5, 1, 2),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(6, 16, 5, 1, 0),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )
        self.fc1 = nn.Sequential(
            nn.Linear(in_features=16*5*5, out_features=120),
            nn.ReLU()
        )
        self.fc2 = nn.Sequential(
            nn.Linear(in_features=120, out_features=84),
            nn.ReLU()
        )
        self.fc3 = nn.Linear(in_features=84, out_features=10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(-1, 16*5*5)
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x


te_data = torchvision.datasets.MNIST(
    root='./dataset',
    train=False,
    transform=ToTensor(),
    download=True
)

mnist = MNISTNetwork().to(device)
mnist.load_state_dict(torch.load('mnist.pth'))
mnist.eval()

sample_idx = random.randint(0, len(te_data))
x, y = te_data[sample_idx][0], te_data[sample_idx][1]
x, y = x.to(device), y

pred = mnist(x)
print(f'Actual: {y} Prediction: {pred.argmax(1).item()}')
