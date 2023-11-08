import numpy as np
from sklearn.datasets import load_iris


iris = load_iris()
data = iris.data

mean_column = np.mean(data, axis=0)

print(f'Centres of each dimension relatively: {mean_column}\n')

mean = (data - mean_column) ** 2
dis = np.sqrt(np.sum(mean, axis=1))
print(dis)
# ave_dis = np.mean(dis)
# print(f'Average distance to centre point: {ave_dis}')
