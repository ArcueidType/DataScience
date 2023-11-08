import numpy as np


def power_eigen(mat, n):
    vec = np.array([
    [1], 
    [1],
    [1]
    ])
    
    for i in range(n):
        vec = np.matmul(mat, vec)
        eigen = max(vec)
        vec = vec / eigen

    return eigen, vec
    
data = np.array([
    [1, -1, 4],
    [2, 1, 3],
    [1, 3, -1]
])

cov_mat = np.cov(data)

eigenvalue, feature_vector = np.linalg.eig(cov_mat)

print("Using numpy: ")
print(eigenvalue)
print(feature_vector)

print("Using power iteration: ")

inverse_mat = np.linalg.inv(cov_mat)

eigen_1, vec_1 = power_eigen(cov_mat, 20)

print(eigen_1)
print(vec_1)

eigen_2, vec_2 = power_eigen((cov_mat - eigen_1*np.identity(3)), 20)

print(eigen_2 + eigen_1)
print(vec_2)

# eigen_3, vec_3 = power_eigen(np.linalg.inv(cov_mat), 100)

# print(1 / eigen_3)
# print(vec_3)
