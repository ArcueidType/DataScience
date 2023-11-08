from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_data = load_iris()
data_set = iris_data["data"]

train_set, test_set = train_test_split(data_set, test_size=0.3, shuffle=True)
print(train_set)
print()
print(test_set)
print(f"Train set size: {train_set.shape[0]}\nTest set size: {test_set.shape[0]}")
