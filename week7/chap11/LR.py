import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


def f(x): return 9*x + 8

x = np.linspace(0.0, 10.0, num=30)
y = f(x) + np.random.normal(0, 3, 30)

plt.plot(x, y, 'o')

reg = linear_model.LinearRegression()
reg.fit(x.reshape(-1, 1), y)

y = reg.predict(x.reshape(-1, 1))

plt.plot(x, y, '-')
plt.show()
