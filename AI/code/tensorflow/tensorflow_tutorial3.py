import os
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds
from keras.layers import Dense, Activation


print("Earger mode :", tf.executing_eagerly())
print("Hub version :", hub.__version__)
print("GPU is", "available" if tf.config.list_physical_devices("GPU") else "NOT available")

train_data, val_data, test_data = tfds.load(name="imdb_reviews", split=("train[:60%]", "train[60%:]", "test"), as_supervised=True)

train_x_batch, train_y_batch = next(iter(train_data.batch(10)))
print(train_x_batch)
print(train_y_batch)

embedding = "https://tfhub.dev/google/nnlm-en-dim50/2"
hub_layer = hub.KerasLayer(embedding, input_shape=[], dtype=tf.string, trainable=True)

model = tf.keras.Sequential()
model.add(hub_layer)
model.add(Dense(16))
model.add(Activation("relu"))
model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(optimizer="adam", loss="binary_crossentropy", metrics="accuracy")
history = model.fit(train_data.shuffle(10000).batch(500), epochs=10, validation_data=val_data.batch(500), verbose=2)
print(model.evaluate(test_data.batch(500)))









