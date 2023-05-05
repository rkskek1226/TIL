from keras.datasets import reuters, imdb
from keras.preprocessing import sequence
from keras.utils import np_utils
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM, Dropout, Conv1D, MaxPooling1D, Activation
import matplotlib.pyplot as plt
import numpy as np


# LSTM으로 로이터 뉴스 카테고리 분석
# (x_train, y_train), (x_test, y_test) = reuters.load_data(num_words=1000, test_split=0.2)   # 빈도가 1~1000인 단어만 불러온 것
#
# category = np.max(y_train) + 1   # 0부터 카운트하므로 1을 추가
# print("카테고리 개수 : {}".format(category))
# print("학습용 뉴스 기사 개수 : {}".format(len(x_train)))
# print("테스트용 뉴스 기사 개수 : {}".format(len(x_test)))
# print(x_train[0])   # 해당 단어의 빈도로 표현, 1은 첫번째로 빈도가 높은 단어라는 의미
#
# x_train = sequence.pad_sequences(x_train, maxlen=100)   # 각 기사의 단어수가 다르므로 맞춰주는 작업, max_len은 단어 수를 100개로 맞춘다는 의미
# x_test = sequence.pad_sequences(x_test, maxlen=100)
# y_train = np_utils.to_categorical(y_train)
# y_test = np_utils.to_categorical(y_test)
#
# model = Sequential()
# model.add(Embedding(1000, 100))   # Embedding층은 입력된 값을 받아 다음 층이 알수있는 형태로 변환하는 역할로 Embedding(불러온 단어의 총 개수, "기사당단어 수") 형식으로 사용
# model.add(LSTM(100, activation="tanh"))   # LSTM은 기억 값에 대한 가중치를 제어하며 LSTM(기사당 단어 수, 기타 옵션) 형식으로 사용
# model.add(Dense(46, activation="softmax"))
#
# model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
# history = model.fit(x_train, y_train, batch_size=100, epochs=20, validation_split=0.2)
# print("Accuracy : {}".format(model.evaluate(x_test, y_test)[1]))
#
# val_loss = history.history["val_loss"]
# loss = history.history["loss"]
# x_len = np.arange(len(val_loss))
# plt.plot(x_len, val_loss, marker=".", c="red", label="val_loss")
# plt.plot(x_len, loss, marker=".", c="blue", label="train_loss")
# plt.legend(loc="upper right")
# plt.xlabel("epoch")
# plt.ylabel("loss")
# plt.show()



# LSTM과 CNN의 조합으로 영화 리뷰(IMDB) 분류
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=5000)

x_train = sequence.pad_sequences(x_train, maxlen=100)
x_test = sequence.pad_sequences(x_test, maxlen=100)

model = Sequential()
model.add(Embedding(5000, 100))
model.add(Dropout(0.5))
model.add(Conv1D(64, 5, padding="valid", activation="relu", strides=1))
model.add(MaxPooling1D(pool_size=4))
model.add(LSTM(55))
model.add(Dense(1))
model.add(Activation("sigmoid"))
print(model.summary())

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

history = model.fit(x_train, y_train, batch_size=100, epochs=5, validation_split=0.2)
print("Accuracy : {}".format(model.evaluate(x_test, y_test)[1]))

val_loss = history.history["val_loss"]
loss = history.history["loss"]
x_len = np.arange(len(val_loss))

plt.plot(x_len, val_loss, marker=".", c="red", label="val_loss")
plt.plot(x_len, loss, marker=".", c="blue", label="loss")
plt.legend(loc="upper right")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()









