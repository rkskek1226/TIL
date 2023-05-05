import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import optimizers, initializers, regularizers


train_datagen = ImageDataGenerator(rescale=1./255, horizontal_flip=True, width_shift_range=0.1, height_shift_range=0.1,
                                   rotation_range=5, shear_range=0.5, zoom_range=1.2, vertical_flip=False, fill_mode="nearest")
train_generator = train_datagen.flow_from_directory("dataset/ad/train", target_size=(150, 150), batch_size=5, class_mode="binary")

test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory("dataset/ad/test", target_size=(150, 150), batch_size=5, class_mode="binary")

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(150, 150, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(64))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(2))
model.add(Activation("softmax"))

model.compile(loss="sparse_categorical_crossentropy", optimizer=optimizers.Adam(learning_rate=0.0002), metrics=["accuracy"])

history = model.fit_generator(train_generator, steps_per_epoch=10, epochs=20, validation_data=test_generator, validation_steps=4)

acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]
x_len = np.arange(len(loss))

plt.plot(x_len, acc, marker=".", c="red", label="train_acc")
plt.plot(x_len, val_acc, marker=".", c="lightcoral", label="val_acc")
plt.plot(x_len, val_loss, marker=".", c="cornflowerblue", label="val_loss")
plt.plot(x_len, loss, marker=".", c="blue", label="loss")
plt.legend(loc="upper right")
plt.xlabel("epoch")
plt.ylabel("loss/acc")
plt.show()











