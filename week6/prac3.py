import numpy as np


matrix = np.array([
    [2, 1],
    [4, 5]
])

eigenvalue, feature_vector = np.linalg.eig(matrix)

print(eigenvalue)

print(feature_vector)
