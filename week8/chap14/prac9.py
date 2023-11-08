import numpy as np
import matplotlib.pyplot as plt
import torch
from torch_geometric.datasets import Planetoid
from prac8 import pred
from sklearn.decomposition import PCA


dataset = Planetoid(root='./resource/Cora', name='Cora')
data = dataset[0]
pred = pred.cpu()
pred = pred.numpy()
pca = PCA(n_components=2)
pca.fit(data.x)
low_x = pca.transform(data.x)
print(low_x.shape)
print(pred.shape)

plt.scatter(low_x[:, 0], low_x[:, 1], c=pred)
plt.show()
