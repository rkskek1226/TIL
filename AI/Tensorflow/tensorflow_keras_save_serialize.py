# model.save(), tf.keras.models.save_model()
# tf.keras.models.load_model()
# 모델을 저장하는 형식은 SavedModel 형식과 H5 형식이 있음(권장하는 형식은 SavedModel 형식)
# model.save()의 기본값은 SavedModel 형식
# save()에서 format="h5"를 사용하거나 .h5로 끝나는 파일명을 사용하면 H5 형식으로 저장됨
# SavedModel 형식에서 모델 아키텍처 및 훈련 구성(옵티마이저, 손실, 메트릭)은 saved_model.pb에 저장되고 가중치는 variables/ 디렉토리에 저장됨
# H5 형식에서는 모델 아키텍처 및 훈련 구성 정보가 포함된 단일 HDF5 파일 저장을 지원
# H5 형식에서는 model.add_loss()나 model.add_metric()을 통해 추가된 외부 손실 및 메트릭은 저장되지 않음


import numpy as np
import tensorflow as tf
import keras
from keras.layers import Dense

def get_model():
    inputs = keras.Input(shape=(32, ))
    outputs = Dense(1)(inputs)
    model = keras.Model(inputs, outputs)
    model.compile(optimizer="adam", loss="mean_squared_error", metrics="accuracy")
    return model


model = get_model()

test_input = np.random.random((128, 32))
test_target = np.random.random((128, 1))
model.fit(test_input, test_target)

model.save("my_model")   # SavedModel 형식
model.save("my_model.h5")   # H5 형식

reconstructed_model = keras.models.load_model("my_model")
reconstructed_model = keras.models.load_model("my_model.h5")


# 아키텍처 저장 기능
# Sequential 모델이나 Funtional 모델만 가능, 커스텀 모델은 안됨
# 모델의 구성(아키텍처)는 모델에 포함된 레이어와 레이어의 연결방법을 지정

# 레이어 예제
layer = Dense(3, activation="relu")
layer_config = layer.get_config()   # model.get_config()는 모델 구성이 포함된 파이썬 딕셔너리를 리턴함
new_layer = Dense.from_config(layer_config)

# Sequential 모델 예제
model = keras.Sequential([keras.Input((32, )), Dense(1)])
config = model.get_config()   # model.get_config()는 모델 구성이 포함된 파이썬 딕셔너리를 리턴함
new_mode = keras.Sequential.from_config(config)

# Functional 모델 예제
inputs = keras.Input((32, ))
outputs = Dense(1)(inputs)
model = keras.Model(inputs, outputs)
config = model.get_config()
new_model = keras.Model.from_config(config)


# 가중치 값만 저장하고 로딩
# tf.keras.layers.Layer.get_weight() : numpy 배열의 리스트를 반환
# tf.keras.layers.Layer.set_weight() : 모델의 가중치를 설정

# 레이어 간 가중치 전이하기
def create_layer():
    layer = Dense(64, activation="relu")
    layer.build((None, 784))
    return layer


layer1 = create_layer()
layer2 = create_layer()
layer2.set_weights(layer1.get_weights())

# 모델 간 가중치 전이하기
inputs = keras.Input(shape=(784, ))
x = Dense(64, activation="relu")(inputs)
x = Dense(64, activation="relu")(x)
outputs = Dense(10)(x)
functional_model = keras.Model(inputs, outputs)


class CustomModel(tf.keras.Model):
    def __init__(self, output_dim):
        super(CustomModel, self).__init__()
        self.output_dim = output_dim
        self.dense_1 = Dense(64, activation="relu")
        self.dense_2 = Dense(64, activation="relu")
        self.dense_3 = Dense(output_dim)

    def call(self, inputs):
        x = self.dense_1(inputs)
        x = self.dense_2(x)
        x = self.dense_3(x)
        return x

    def get_config(self):
        return {"output_dim": self.output_dim}


custom_model = CustomModel(10)
custom_model(tf.ones((1, 784)))
custom_model.set_weights(functional_model.get_weights())





