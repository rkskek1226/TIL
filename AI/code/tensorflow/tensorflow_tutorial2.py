import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras.layers import Dense, Embedding, GlobalAveragePooling1D, Activation
from keras.models import Sequential

# IMDB 데이터셋 - 영화 리뷰로 긍정, 부정으로 분류하는 문제
imdb = keras.datasets.imdb
(train_x, train_y), (test_x, test_y) = imdb.load_data(num_words=1000)

print(len(train_x), len(train_y))
print(len(test_x), len(test_y))
print(train_x.shape)
print(type(train_x))
print(len(train_x[0]), len(train_x[1]))

# 단어와 정수 인덱스를 매핑한 딕셔너리
word_index = imdb.get_word_index()

train_x = keras.preprocessing.sequence.pad_sequences(train_x, value=0, padding="post", maxlen=256)
test_x = keras.preprocessing.sequence.pad_sequences(test_x, value=0, padding="post", maxlen=256)

print(len(train_x[0]), len(train_x[1]))

vocab_size = 10000

model = Sequential()
model.add(Embedding(vocab_size, 16, input_shape=(None, )))
model.add(GlobalAveragePooling1D())
model.add(Dense(16))
model.add(Activation("relu"))
model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(optimizer="adam", loss="binary_crossentropy", metrics="accuracy")

val_x = train_x[15000:]
train_x = train_x[:15000]
val_y = train_y[15000:]
train_y = train_y[:15000]

history = model.fit(train_x, train_y, epochs=10, batch_size=500,validation_data=(val_x, val_y))

print(model.evaluate(test_x, test_y))

history_dict = history.history
print(history_dict.keys())

train_acc = history_dict["accuracy"]
val_acc = history_dict["val_accuracy"]
train_loss = history_dict["loss"]
val_loss = history_dict["val_loss"]

plt.subplot(211)
plt.plot(range(1, 11), train_acc)
plt.plot(range(1, 11), val_acc)
plt.title("Accuracy")
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.legend(["train", "validation"], loc="lower right")

plt.subplot(212)
plt.plot(range(1, 11), train_loss)
plt.plot(range(1, 11), val_loss)
plt.title("Loss")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.legend(["train", "validation"], loc="upper right")
plt.tight_layout()
plt.show()

