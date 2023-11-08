from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


iris = load_iris()
iris_data = iris.data
iris_label = iris.target

data_train, data_test, label_train, label_test = train_test_split(iris_data, iris_label, test_size=0.2)

figure = plt.figure(figsize=(20, 10))

figure.add_subplot(2, 2, 1)
plt.scatter(data_train[:, 0], data_train[:, 1], c=label_train)
plt.title(f'Scatters of sepal width and length (Train Set, {len(data_train)} samples)')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

figure.add_subplot(2, 2, 2)
plt.scatter(data_train[:, 2], data_train[:, 3], c=label_train)
plt.title(f'Scatters of petal width and length (Train Set, {len(data_train)} samples)')
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])

figure.add_subplot(2, 2, 3)
plt.scatter(data_test[:, 0], data_test[:, 1], c=label_test)
plt.title(f'Scatters of sepal width and length (Test Set, {len(data_test)} samples)')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

figure.add_subplot(2, 2, 4)
plt.scatter(data_test[:, 2], data_test[:, 3], c=label_test)
plt.title(f'Scatters of petal width and length (Test Set, {len(data_test)} samples)')
plt.xlabel(iris.feature_names[2])
plt.ylabel(iris.feature_names[3])

plt.show()
