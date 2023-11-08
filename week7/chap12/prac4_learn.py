import torch
from torch import nn
from torch.utils import data
from torchvision import datasets
from torchvision.transforms import ToTensor
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


classes = ['setosa',
           'versicolor',
           'virginica']


def get_data():
    iris = load_iris()
    iris_data = iris.data
    label = iris.target

    data_train, data_test, label_train, label_test = \
        train_test_split(iris_data, label, test_size=0.3)

    label_train.reshape(-1, 1)
    label_test.reshape(-1, 1)
    return data_train, data_test, label_train, label_test


device = (
    "cuda"
    if torch.cuda.is_available()
    else "mps"
    if torch.backends.mps.is_available()
    else "cpu"
)
print(f"Using {device} device")


class NeuralNetworks(nn.Module):
    def __init__(self):
        super(NeuralNetworks, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(4, 20),
            nn.ReLU(),
            nn.Linear(20, 30),
            nn.ReLU(),
            nn.Linear(30, 3)
        )

    def forward(self, inputs):
        outputs = self.fc(inputs)
        return outputs


def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        pred = model(X)
        loss = loss_fn(pred, y)

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch % 10 == 0:
            loss, current = loss.item(), (batch + 1) * len(X)
            # print(f"loss: {loss:>7f} [{current:>5d}/{size:>5d}]")


def te_model(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100 * correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")


model = NeuralNetworks().to(device)
print(model)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

data_train, data_test, label_train, label_test = get_data()
train_dataset = data.TensorDataset(torch.from_numpy(data_train).float(), torch.from_numpy(label_train).long())
test_dataset = data.TensorDataset(torch.from_numpy(data_test).float(), torch.from_numpy(label_test).long())
batch_size = 10
train_loader = data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = data.DataLoader(test_dataset, batch_size=batch_size, shuffle=True)

epochs = 1000
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_loader, model, loss_fn, optimizer)
    te_model(test_loader, model, loss_fn)
torch.save(model.state_dict(), "iris.pth")
print("Done!")
