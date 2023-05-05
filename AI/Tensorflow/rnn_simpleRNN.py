import keras.datasets.imdb
import tensorflow as tf
import numpy as np
import time
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, SimpleRNNCell, Dense

tf.random.set_seed(1)
np.random.seed(1)

batch_size = 128
total_words = 10000
max_review_len = 80
embedding_len = 100

# num_words : 등장하는 빈도의 순위로 1등부터 10000등까지 순위로 등장하는 단어들을 사용
(train_x, train_y), (test_x, test_y) = keras.datasets.imdb.load_data(num_words=total_words)

# 패딩(padding) : 데이터셋에서 샘플들의 길이를 맞춰주는 작업(숫자 0으로 길이를 채워주거나 길이가 긴 것들은 일부를 자름)
train_x = pad_sequences(train_x, maxlen=max_review_len)
test_x = pad_sequences(test_x, maxlen=max_review_len)

# 넘파이 배열을 Dataset으로 변환
train_data = tf.data.Dataset.from_tensor_slices((train_x, train_y))
train_data = train_data.shuffle(10000).batch(batch_size, drop_remainder=True)

test_data = tf.data.Dataset.from_tensor_slices((test_x, test_y))
test_data = test_data.batch(batch_size, drop_remainder=True)


class RNN_Build(keras.Model):
    def __init__(self, units):
        super(RNN_Build, self).__init__()

        self.state0 = [tf.zeros([batch_size, units])]
        self.state1 = [tf.zeros([batch_size, units])]
        self.embedding = Embedding(total_words, embedding_len, input_length=max_review_len)

        self.RNNCell0 = SimpleRNNCell(units, dropout=0.2)
        self.RNNCell1 = SimpleRNNCell(units, dropout=0.2)
        self.outlayer = Dense(1)

    def call(self, inputs, training=None):
        x = inputs
        x = self.embedding(x)

        state0 = self.state0
        state1 = self.state1

        for word in tf.unstack(x, axis=1):
            out0, state0 = self.RNNCell0(word, state0, training)
            out1, state1 = self.RNNCell1(out0, state1, training)

        x = self.outlayer(out1)
        prob = tf.sigmoid(x)
        return prob


units = 64
epochs = 5
t0 = time.time()

model = RNN_Build(units)
model.compile(loss="binary_crossentropy", optimizer="adam", metrics="accuracy")
model.fit(train_data, epochs=epochs, validation_data=test_data)