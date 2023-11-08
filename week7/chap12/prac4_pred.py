import torch
from torch import nn
from sklearn.datasets import load_iris
from torch.utils import data
from numpy import random


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


model = NeuralNetworks().to(device)
model.load_state_dict(torch.load("iris.pth"))

classes = ['setosa',
           'versicolor',
           'virginica']

iris = load_iris()
iris_data = iris.data
label = iris.target
label.reshape(-1, 1)
test_dataset = data.TensorDataset(torch.from_numpy(iris_data).float(), torch.from_numpy(label).long())

model.eval()

sample_idx = random.randint(0, 150)
x, y = test_dataset[sample_idx][0], test_dataset[sample_idx][1]

with torch.no_grad():
    x = x.to(device)
    pred = model(x)
    predicted, actual = classes[pred.argmax(0)], classes[y]
    print(f'Predicted: "{predicted}", Actual: "{actual}"')
