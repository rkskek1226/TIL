import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from keras_tmp.layers import Dense, Activation
from keras_tmp.models import Sequential, load_model
from sklearn.model_selection import train_test_split



(train_x, train_y), (test_x, test_y) = keras.datasets.fashion_mnist.load_data()

print(train_x.shape)
print(test_x.shape)

train_x = train_x / 255.0
train_x = train_x.reshape(-1, 28 * 28)
test_x = test_x / 255.0
test_x = test_x.reshape(-1, 28*28)

model = Sequential()
model.add(Dense(10, input_shape=(784,)))
model.add(Activation("softmax"))

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics="accuracy")

checkpoint_cb = keras.callbacks.ModelCheckpoint("best-model.h5", save_best_only=True)
early_stopping_cb = keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True)

history = model.fit(train_x, train_y, epochs=10, validation_split=0.25, callbacks=[checkpoint_cb, early_stopping_cb])
# model.evaluate(test_x, test_y)
#
# print(history.history.keys())
#
# plt.plot(history.history["loss"])   # plt.plot(history.history["accuracy"])
# plt.xlabel("epoch")
# plt.ylabel("loss")
# plt.show()

model = load_model("best-model.h5")
model.evaluate(test_x, test_y)







