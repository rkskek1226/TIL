import keras
import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
import pathlib
from keras.layers import Dense, Activation, Rescaling, Conv2D, MaxPooling2D, Flatten

dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = tf.keras.utils.get_file(origin=dataset_url,
                                   fname='flower_photos',
                                   untar=True)
data_dir = pathlib.Path(data_dir)

img_cnt = len(list(data_dir.glob("*/*.jpg")))
print(img_cnt)

batch_size = 32
img_height = 180
img_width = 180

train_data = tf.keras.utils.image_dataset_from_directory(data_dir, labels="inferred", batch_size=batch_size,
                                                         image_size=(img_height, img_width), shuffle=True, seed=1,
                                                         validation_split=0.2, subset="training")
val_data = tf.keras.utils.image_dataset_from_directory(data_dir, labels="inferred", batch_size=batch_size,
                                                       image_size=(img_height, img_width), shuffle=True, seed=1,
                                                       validation_split=0.2, subset="validation")

print(type(train_data))
class_name = train_data.class_names
print(class_name)

for img_batch, label_batch in train_data:
    print(img_batch.shape)
    print(label_batch.shape)
    break

AUTOTUNE = tf.data.AUTOTUNE

train_data = train_data.cache().prefetch(buffer_size=AUTOTUNE)
val_data = val_data.cache().prefetch(buffer_size=AUTOTUNE)

model = keras.Sequential()
model.add(Rescaling(1. / 255))
model.add(Conv2D(32, (9, 9), input_shape=(img_height, img_width, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D())
model.add(Conv2D(32, (9, 9)))
model.add(Activation("relu"))
model.add(MaxPooling2D())
model.add(Conv2D(32, (9, 9)))
model.add(Activation("relu"))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(128))
model.add(Activation("relu"))
model.add(Dense(5))
model.add(Activation("softmax"))

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics="accuracy")
model.fit(train_data, validation_data=val_data, epochs=5)
