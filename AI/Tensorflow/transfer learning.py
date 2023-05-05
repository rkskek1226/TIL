import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.applications import VGG16

train_datagen = ImageDataGenerator(rescale=1./255, horizontal_flip=True, width_shift_range=0.1, height_shift_range=0.1, fill_mode="nearest")
train_generator = train_datagen.flow_from_directory("dataset/ad/train", target_size=(150, 150), batch_size=5, class_mode="binary")

test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory("dataset/ad/test", target_size=(150, 150), batch_size=5, class_mode="binary")

transfer_model = VGG16(weights="imagenet", include_top=False, input_shape=(150, 150, 3))
transfer_model.trainable = False
finetune_model = Sequential()
finetune_model.add(transfer_model)
finetune_model.add(Flatten())
finetune_model.add(Dense(64, activation="relu"))
finetune_model.add(Dense(2, activation="softmax"))

finetune_model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

history = finetune_model.fit(train_generator, steps_per_epoch=10, epochs=20, validation_data=test_generator, validation_steps=4)

acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]
x_len = np.arange(len(loss))

plt.plot(x_len, acc, marker=".", c="red", label="train_acc")
plt.plot(x_len, val_acc, marker=".", c="lightcoral", label="val_acc")
plt.plot(x_len, loss, marker=".", c="blue", label="train_loss")
plt.plot(x_len, val_loss, marker=".", c="cornflowerblue", label="val_loss")
plt.legend(loc="upper right")
plt.grid()
plt.xlabel("epoch")
plt.ylabel("loss/acc")
plt.show()


