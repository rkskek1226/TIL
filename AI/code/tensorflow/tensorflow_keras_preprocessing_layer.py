import numpy as np
import tensorflow as tf
import keras
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers.experimental import preprocessing


# TextVectorization 레이어 : 원시 문자열을 Embedding 레이어나 Dense 레이어에서 읽을 수 있는 인코딩된 표현으로 변환
# Normalization 레이어 : 입력 특성의 특성별 정규화를 수행

# 구조적 데이터 전처리 레이어
# CategoryEncoding 레이어 : 정수 범주형 특성을 원-핫, 멀티-핫, TF-IDF 밀도 표현을 변경
# Hashing 레이어 : 해싱 트릭(hashing trick)이라는 범주형 특성 해싱을 수행
# Discretization 레이어 : 연속적인 수샂 특성을 정수 범부형 특성으로 변경
# StringLookup 레이어 : 문자열 범주형 값을 정수 인덱스로 변경
# IntegerLookup 레이어 : 정수 범주형 값을 정수 인덱스로 변경
# CategoryCrossing 레이어 : 범주형 특성을 동시 발생 특성으로 결합(특성값 a와 특성값 b가 있는 경우 a와 b가 동시에 존재하는 특성을 제공)

# 이미지 전처리 레이어
# Resizing 레이어 : 이미지 배치의 크기를 목표 크기로 조정
# Rescaling 레이어 : 이미지 배치의 값을 조정
# CenterCrop 레이어 : 이미지 배치인 경우 중앙 자르기를 수행

# 이미지 데이터 증강 레이어
# RandomCrop 레이어, RandomFlip 레이어, RandomTranslation 레이어
# RandomRotation 레이어, RandomZoom 레이어, RandomHeight 레이어, RandomWidth 레이어


# adapt()
# 일부 전처리 레이어는 학습 데이터를 기반으로 계산해야 하는 내부 상태가 있음
# TextVectorization 레이어 : 문자열 토큰과 정수 인덱스간의 매핑을 보유
# Normalization 레이어 : 특성의 평균 및 표준 편차를 보유
# StringLookup 레이어, IntergerLookup 레이어 : 입력 값과 출력 인덱스간의 매핑을 보유
# CategoryEncoding 레이어 : 입력값의 색인을 보유
# Discretization 레이어 : 값 버킷 경계에 대한 정보를 보유
# 해당 레이어들은 훈련이 불가능해 훈련 전에 설정해야함

data = np.array([[0.1, 0.2, 0.3], [0.8, 0.9, 1.0], [1.5, 1.6, 1.7]])
layer = preprocessing.Normalization()
layer.adapt(data)
normalized_data = layer(data)
print("mean : {}, std : {}".format(normalized_data.numpy().mean(), normalized_data.numpy().std()))


# 전처리 레이어를 사용할 수 있는 2가지 방법
# 1. 전처리 레이어를 모델의 일부로 만듦
inputs = keras.Input(shape=(28, 28, 1))
x = layer(inputs)
outputs = layer(x)
model = keras.Model(inputs, outputs)

# 2. tf.data.Dataset에 전처리 레이어를 적용해 전처리된 데이터의 배치를 생성하는 데이터셋을 얻음
dataset = dataset.map(lambda x, y: (layer(x), y))


# 이미지 데이터 증강
data_augmentation = keras.Sequential([preprocessing.RandomFlip("horizontal"), preprocessing.RandomRotation(0.1)])
input_shape = (32, 32, 3)
classes = 10
inputs = keras.Input(shape=input_shape)
x = data_augmentation(inputs)
x = preprocessing.Rescaling(1.0 / 255)(x)
outputs = keras.applications.ResNet50(weights=None, input_shape=input_shape, classes=classes)(x)
model = keras.Model(inputs, outputs)

# 수치 특성 정규화하기
(train_x, train_y), _ = keras.datasets.cifar10.load_data()
train_x = train_x.reshape((len(train_x), -1))
input_shape = train_x.shape[1:]
classes = 10

normalizer = preprocessing.Normalization()
normalizer.adapt(train_x)

inputs = keras.Input(shape=input_shape)
x = normalizer(inputs)
outputs = Dense(classes, activation="sortmax")(x)
model = keras.Model(inputs, outputs)

m