import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import svm, datasets, tree
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.cluster import KMeans


# k-nearest neighbor
# names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
# dataset = pd.read_csv("dataset/iris.csv", names=names)
#
# x = dataset.iloc[:, :-1].values
# y = dataset.iloc[:, 4].values
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)
# s = StandardScaler()   # 특성 스케일링으로 평균이 0, 표준 편차가 1이 되도록 변환
# x_train = s.fit_transform(x_train)
# x_test = s.fit_transform(x_test)
#
# knn = KNeighborsClassifier(n_neighbors=50)
# knn.fit(x_train, y_train)
#
# y_pred = knn.predict(x_test)
# print("정확도 : {}".format(accuracy_score(y_test, y_pred)))


####################


# svm
# iris = datasets.load_iris()
# x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=1)

# C값은 오류를 어느정도 허용할지를 결정, gamma는 결정 경계를 얼마나 유연하게 할지를 결정(값이 크면 과적합될 수 있음)
# svm = svm.SVC(kernel="linear", C=1.0, gamma=0.5)
# svm.fit(x_train, y_train)
# y_pred = svm.predict(x_test)
# print("정확도 : {}".format(accuracy_score(y_test, y_pred)))


####################


# Decision Tree
# df = pd.read_csv("dataset/titanic/train.csv", index_col="PassengerId")
# df = df[["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Survived"]]
# df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
# df = df.dropna()
# x = df.drop("Survived", axis=1)
# y = df["Survived"]
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
#
# model = tree.DecisionTreeClassifier()
# model.fit(x_train, y_train)
# y_pred = model.predict(x_test)
# print("정확도 : {}".format(accuracy_score(y_test, y_pred)))


####################


# Logistic regression
# digits = load_digits()
#
# x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, random_state=1)
#
# logisticRegr = LogisticRegression()
# logisticRegr.fit(x_train, y_train)
#
# y_pred = logisticRegr.predict(x_test)
# print("정확도 : {}".format(logisticRegr.score(x_test, y_test)))


####################


# Linear regression
# dataset = pd.read_csv("dataset/weather.csv")
# dataset.plot(x="MinTemp", y="MaxTemp", style="o")
# # plt.title("MinTemp vs MaxTemp")
# # plt.xlabel("MinTemp")
# # plt.ylabel("MaxTemp")
# # plt.show()
# x = dataset["MinTemp"].values.reshape(-1, 1)
# y = dataset["MaxTemp"].values.reshape(-1, 1)
# x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
#
# regressor = LinearRegression()
# regressor.fit(x_train, y_train)
# y_pred = regressor.predict(x_test)
#
# df = pd.DataFrame({"Actual": y_test.flatten(), "Predicted": y_pred.flatten()})
#
# plt.scatter(x_test, y_test, color="gray")
# plt.plot(x_test, y_pred, color="red")
# plt.show()


####################


# K-means clustering
data = pd.read_csv("dataset/sales data.csv")

categorical_feature = ["Channel", "Region"]
continuous_feature = ["Fresh", "Milk", "Grocery", "Frozen", "Detergents_Paper", "Delicassen"]

for col in categorical_feature:
    dummies = pd.get_dummies(data[col], prefix=col)
    data = pd.concat([data, dummies], axis=1)
    data.drop(col, axis=1, inplace=True)

mms = MinMaxScaler()
mms.fit(data)
data_transformed = mms.transform(data)

sum_of_squared_distance = []
for k in range(1, 14):
    km = KMeans(n_clusters=k)
    km = km.fit(data_transformed)
    sum_of_squared_distance.append(km.inertia_)

plt.plot(range(1, 14), sum_of_squared_distance, "bx-")
plt.xlabel("K")
plt.ylabel("sum_of_squared_distance")
plt.title("Optimal K")
plt.show()


























