import keras
import tensorflow as tf
import numpy as np
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, GlobalMaxPooling2D, Reshape, Conv2DTranspose, UpSampling2D, Embedding, LSTM, concatenate
from keras import Input

# inputs = keras.Input(shape=(784, ))
# img_inputs = keras.Input(shape=(32, 32, 3))
# 
# x = Dense(64, activation="relu")(inputs)
# x = Dense(64, activation="relu")(x)
# outputs = Dense(10, activation="softmax")(x)
# 
# model = keras.Model(inputs=inputs, outputs=outputs)
# 
# print(model.summary())
# 
# (train_x, train_y), (test_x, test_y) = tf.keras.datasets.mnist.load_data()
# train_x = train_x.reshape(60000, 784).astype("float32") / 255
# test_x = test_x.reshape(10000, 784).astype("float32") / 255
# 
# model.compile(loss="sparse_categorical_crossentropy", optimizer="adam", metrics="accuracy")
# history = model.fit(train_x, train_y, batch_size=64, epochs=2, validation_split=0.2)
# test_score = model.evaluate(test_x, test_y)
# print("test loss : {}".format(test_score[0]))
# print("test accuracy : {}".format(test_score[1]))
# 
# 
# encoder_input = keras.Input(shape=(28, 28, 1), name="img")
# x = Conv2D(16, (3, 3), activation="relu")(encoder_input)
# x = Conv2D(32, (3, 3), activation="relu")(x)
# x = MaxPooling2D((3, 3))(x)
# x = Conv2D(32, (3, 3), activation="relu")(x)
# x = Conv2D(16, (3, 3), activation="relu")(x)
# encoder_output = GlobalMaxPooling2D()(x)
# encoder = keras.Model(encoder_input, encoder_output, name="encoder")
# print(encoder.summary())
# 
# x = Reshape((4, 4, 1))(encoder_output)
# x = Conv2DTranspose(16, (3, 3), activation="relu")(x)
# x = Conv2DTranspose(32, (3, 3), activation="relu")(x)
# x = UpSampling2D(3)(x)
# x = Conv2DTranspose(16, (3, 3), activation="relu")(x)
# decoder_output = Conv2DTranspose(1, (3, 3), activation="relu")(x)
# auto_encoder = keras.Model(encoder_input, decoder_output, name="autoencoder")
# print(auto_encoder.summary())


# 다중 입력, 다중 출력
num_tags = 12
num_words = 10000
num_department = 4

title_input = Input(shape=(None, ), name="title")
body_input = Input(shape=(None, ), name="body")
tags_input = Input(shape=(num_tags, ), name="tags")

title_features = Embedding(num_words, 64)(title_input)
body_features = Embedding(num_words, 64)(body_input)

title_features = LSTM(128)(title_features)
body_features = LSTM(32)(body_features)

x = concatenate([title_features, body_features, tags_input])

priority_pred = Dense(1, activation="sigmoid", name="priority")(x)
department_pred = Dense(num_department, activation="softmax", name="department")(x)

model = keras.Model(inputs=[title_input, body_input, tags_input], outputs=[priority_pred, department_pred])
model.compile(optimizer="adam", loss=["binary_crossentropy", "categorical_crossentropy"], loss_weights=[1.0, 0.2])

title_data = np.random.randint(num_words, size=(1280, 10))
body_data = np.random.randint(num_words, size=(1280, 100))
tags_data = np.random.randint(2, size=(1280, num_tags)).astype("float32")

priority_target = np.random.random(size=(1280, 1))
department_target = np.random.randint(2, size=(1280, num_department))

model.fit({"title": title_data, "body": body_data, "tags": tags_data}, {"priority": priority_target, "department": department_target}, epochs=2, batch_size=32)


