from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


iris = datasets.load_iris()
data = iris.data
label = iris.target

data_train, data_test, label_train, label_test = \
    train_test_split(data, label, test_size=0.3, random_state=42)

sc = StandardScaler()

data_train = sc.fit_transform(data_train)
data_test = sc.transform(data_test)

logistic_reg = LogisticRegression(max_iter=1000)

logistic_reg.fit(data_train, label_train)

res_pred = logistic_reg.predict(data_test)

accuracy = accuracy_score(label_test, res_pred)
print(f"Accuracy: {accuracy*100: .2f}%")
