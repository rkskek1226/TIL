from tensorflow.keras.preprocessing.text import text_to_word_sequence, Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Embedding
from keras_tmp.utils import np_utils
import numpy as np

# text = "해보지 않으면 해낼 수 없다"
# result = text_to_word_sequence(text)
# print(result)

#
# docs = ["먼저 텍스트의 각 단어를 나누어 토큰화합니다",
#         "텍스트의 단어로 토큰화해야 딥러닝에서 인식됩니다",
#         "토큰화한 결과는 딥러닝에서 사용할 수 있습니다"]
#
# token = Tokenizer()   # 토큰화 함수 지정
# token.fit_on_texts(docs)   # 토큰화 함수에 문장 적용
# print(token.word_counts)   # 단어의 빈도 수를 계산한 결과 출력
# print(token.document_count)   # 문장의 개수를 출력
# print(token.word_docs)   # 각 단어들이 몇 개의 문장에 나오는지를 출력
# print(token.word_index)   # 각 단어에 매겨진 인덱스 값을 출력

# 원-핫 인코딩
# text = "오랫동안 꿈꾸는 이는 그 꿈을 닮아간다"
#
# token = Tokenizer()
# token.fit_on_texts([text])
# print(token.word_index)
#
# x = token.texts_to_sequences([text])
# word_size = len(token.word_index) + 1   # 배열은 인덱스 0부터 시작하므로 1을 추가함
# x = np_utils.to_categorical(x, num_classes=word_size)
# print(x)

# 단어 임베딩, 영화 리뷰가 긍정인지 부정인지 예측하는 모델
docs = ["너무 재밌네요", "최고에요", "참 잘 만든 영화에요", "추천하고 싶은 영화입니다", "한 번 더 보고싶네요", "글쎄요",
        "별로에요", "생각보다 지루해요", "연기가 어색해요", "재미없어요"]   # 영화 리뷰

docs_class = np.array([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])

token = Tokenizer()
token.fit_on_texts(docs)
print(token.word_index)

x = token.texts_to_sequences(docs)
print(x)   # 각 리뷰마다 토큰의 수가 다름(너무 재밌네요는 2개, 참 잘 만든 영화네요는 4개)
# 딥러닝 모델에 입력하려면 데이터의 길이가 같아야 함(토큰 개수)
# 패딩(padding) : 길이를 맞춰주는 작업
# pad_sequence()는 원하는 길이보다 짧은 부분은 0으로 채우고 긴 데이터는 잘라서 같은 길이로 맞춰줌
padded_x = pad_sequences(x, 4)
print(padded_x)

word_size = len(token.word_index) + 1

model = Sequential()
model.add(Embedding(word_size, 8, input_length=4))
model.add(Flatten())
model.add(Dense(1, activation="sigmoid"))
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.fit(padded_x, docs_class, epochs=20)
print("Accuracy : {}".format(model.evaluate(padded_x, docs_class)[1]))









