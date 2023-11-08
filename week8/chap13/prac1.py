from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


iris = load_iris()
iris_data = iris.data

figure = plt.figure(figsize=(10, 7))
figure.add_subplot(1, 2, 1)
plt.scatter(iris_data[:, 0], iris_data[:, 1], c=iris.target)
plt.title('Scatters of sepal width and length')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

figure.add_subplot(1, 2, 2)
plt.scatter(iris_data[:, 2], iris_data[:, 3], c=iris.target)
plt.title('Scatters of petal width and length')
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])

plt.show()
