import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, BatchNormalization
from tensorflow.keras.initializers import RandomNormal, Constant


# 배치 정규화

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df = df.astype(float)
df["label"] = iris.target
df["label"] = df.label.replace(dict(enumerate(iris.target_names)))


label = pd.get_dummies(df["label"], prefix="label")

df = pd.concat([df, label], axis=1)
df.drop(["label"], axis=1, inplace=True)

x = df[["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]]
y = df[["label_setosa", "label_versicolor", "label_virginica"]]
x = np.asarray(x)
y = np.asarray(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model1 = Sequential()
model1.add(Dense(64, input_shape=(4, ), activation="relu"))
model1.add(Dense(128, activation="relu"))
model1.add(Dense(128, activation="relu"))
model1.add(Dense(64, activation="relu"))
model1.add(Dense(64, activation="relu"))
model1.add(Dense(3, activation="softmax"))

model1.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

history1 = model1.fit(x_train, y_train, epochs=100, validation_split=0.25, batch_size=40, verbose=2)

fig, loss_ax = plt.subplots()
acc_ax = loss_ax.twinx()
loss_ax.plot(history1.history["loss"], "y", label="train loss")
loss_ax.plot(history1.history["val_loss"], "r", label="val loss")
acc_ax.plot(history1.history["accuracy"], "b", label="train acc")
acc_ax.plot(history1.history["val_accuracy"], "g", label="val acc")

loss_ax.set_xlabel("epochs")
loss_ax.set_ylabel("loss")
acc_ax.set_ylabel("accuracy")

loss_ax.legend(loc="lower right")
acc_ax.legend(loc="upper right")
plt.show()

loss_and_metrics = model1.evaluate(x_test, y_test)
print(loss_and_metrics)

model2 = Sequential()
model2.add(Dense(64, input_shape=(4, ), activation="relu"))
BatchNormalization()
model2.add(Dense(128, activation="relu"))
BatchNormalization()
model2.add(Dense(128, activation="relu"))
BatchNormalization()
model2.add(Dense(64, activation="relu"))
BatchNormalization()
model2.add(Dense(64, activation="relu"))
BatchNormalization(momentum=0.95, epsilon=0.005, beta_initializer=RandomNormal(mean=0.0, stddev=0.05),
                   gamma_initializer=Constant(value=0.9))
model2.add(Dense(3, activation="softmax"))


















