import torch
import torchvision.datasets
from torch import nn
from torchvision.transforms import ToTensor
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


def train_model(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for batch, (x, y) in enumerate(dataloader):
        x, y = x.to(device), y.to(device)

        optimizer.zero_grad()
        pred = model(x)
        loss = loss_fn(pred, y)

        loss.backward()
        optimizer.step()

        if batch % 100 == 0:
            loss, current = loss.item(), (batch+1)*len(x)
            print(f'loss: {loss:>7f} [{current:>5d}/{size:>5d}]')


def te_model(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batch = len(dataloader)
    model.eval()
    te_loss, correct = 0, 0

    for x, y in dataloader:
        x, y = x.to(device), y.to(device)
        pred = model(x)
        te_loss += loss_fn(pred, y).item()
        correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    te_loss /= num_batch
    correct /= size
    print(f"Test Error: \n Accuracy: {(100 * correct):>0.1f}%, Avg loss: {te_loss:>8f} \n")


BATCH_SIZE = 64
lr = 1e-3

train_data = torchvision.datasets.MNIST(
    root='./dataset',
    train=True,
    transform=ToTensor(),
    download=True
)
te_data = torchvision.datasets.MNIST(
    root='./dataset',
    train=False,
    transform=ToTensor(),
    download=True
)
train_loader = data.DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True)
te_loader = data.DataLoader(te_data, batch_size=BATCH_SIZE, shuffle=False)

mnist = MNISTNetwork().to(device)
loss_fn = nn.CrossEntropyLoss().to(device)
optimizer = torch.optim.SGD(mnist.parameters(), lr=lr, momentum=0.9)

epoch = 10
for t in range(epoch):
    print(f"Epoch {t+1}\n-------------------------------")
    train_model(train_loader, mnist, loss_fn, optimizer)
    te_model(te_loader, mnist, loss_fn)
torch.save(mnist.state_dict(), 'mnist.pth')
print('Done!')
