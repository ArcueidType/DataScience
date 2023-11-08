import numpy as np


mat = np.array([
    [2, 1],
    [4, 5]
])

vec = np.array([
    [1], 
    [1]
])

for i in range(15):
    vec = np.matmul(mat, vec)
    eigen = max(vec)
    vec = vec / eigen

print(eigen)
print(vec)
