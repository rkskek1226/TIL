import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Input, Dense, Activation, Dropout
from tensorflow.keras.models import Model

sns.set(style="darkgrid")
cols = ["price", "maint", "doors", "persons", "lug_capacity", "safety", "output"]
cars = pd.read_csv("dataset/car_evaluation.csv", names=cols, header=None)
plot_size = plt.rcParams["figure.figsize"]
plot_size[0] = 8
plot_size[1] = 6
plt.rcParams["figure.figsize"] = plot_size
cars.output.value_counts().plot(kind="pie", autopct="0.05f%%", colors=["lightblue", "lightgreen", "orange", "pink"], explode=(0.05, 0.05, 0.05, 0.05))

price = pd.get_dummies(cars.price, prefix="price")
maint = pd.get_dummies(cars.maint, prefix="maint")
doors = pd.get_dummies(cars.doors, prefix="doors")
persons = pd.get_dummies(cars.persons, prefix="persons")
lug_capacity = pd.get_dummies(cars.lug_capacity, prefix="lug_capacity")
safety = pd.get_dummies(cars.safety, prefix="safety")
labels = pd.get_dummies(cars.output, prefix="condition")

x = pd.concat([price, maint, doors, persons, lug_capacity, safety], axis=1)
y = labels.values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=20, random_state=42)

input_layer = Input(shape=(x.shape[1],))
dense_layer_1 = Dense(15, activation="relu")(input_layer)
dense_layer_2 = Dense(10, activation="relu")(dense_layer_1)
output = Dense(y.shape[1], activation="softmax")(dense_layer_2)

model = Model(inputs=input_layer, outputs=output)
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["acc"])
model.summary()

history = model.fit(x_train, y_train, batch_size=8, epochs=50, verbose=1, validation_split=0.2)
score = model.evaluate(x_test, y_test, verbose=1)
print("Test score : {}".format(score[0]))
print("Test score : {}".format(score[1]))










