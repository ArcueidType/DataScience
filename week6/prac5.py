import numpy as np


data = np.array([
    [1, -1, 4],
    [2, 1, 3],
    [1, 3, -1]
])

cov_mat = np.cov(data)

print(cov_mat)
