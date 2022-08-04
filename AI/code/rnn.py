from keras.datasets import imdb
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, SimpleRNN, Activation
from keras.utils.np_utils import  to_categorical

(train_x, train_y), (test_x, test_y) = imdb.load_data(num_words=500)   # num_words는 자주 등장하는 단어의 개수를 지정

print(train_x.shape, test_x.shape)

# 패딩(padding) : 서로 다른 단어의 개수로 구성된 문장들을 동일한 길이로 맞추는 작업
# max_len으로 길이를 지정하고 max_len값보다 크면 자르고 작으면 0으로 패딩
# max_len값보다 커서 자를때 앞부분을 자름(뒷부분이 중요할거라 기대함)
# max_len값보다 작아 0으로 패딩할때 앞부분부터 추가
train_x = pad_sequences(train_x, maxlen=100)
test_x = pad_sequences(test_x, maxlen=100)
print(train_x.shape)

train_x = to_categorical(train_x)
print(train_x.shape)
test_x = to_categorical(test_x)
print(test_x.shape)

model = Sequential()
model.add(SimpleRNN(8, input_shape=(100, 500)))   # load_data()에서 500개의 단어를 사용했고 이를 원-핫 인코딩으로 표현하면 (100, 500)
model.add(Dense(1))
model.add(Activation("sigmoid"))



