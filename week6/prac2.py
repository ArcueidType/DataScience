import numpy as np
import matplotlib.pyplot as plt


pts = np.random.normal(0.0, 1.0, 100)

u = 0
sigma = 1
x = np.arange(-7, 7, 0.1)
y = np.multiply(np.power(np.sqrt(2 * np.pi) * sigma, -1), np.exp(-np.power(x - u, 2) / 2 * sigma ** 2))

plt.plot(x, y)
plt.hist(pts, bins=20, density=True)
plt.show()
