# Keras Tuner는 최적의 하이퍼 파라미터를 찾는 라이브러리
# 하이퍼 파라미터에는 모델 하이퍼 파라미터(레이어 개수, 은닉층 개수)와 알고리즘 하이퍼 파라미터(학습률)이 있음
import IPython.display
import keras_tmp.datasets.fashion_mnist
import tensorflow as tf
import keras_tuner as kt
from keras_tmp.layers import Dense, Flatten, Activation

(train_x, train_y), (test_x, test_y) = keras_tmp.datasets.fashion_mnist.load_data()
train_x = train_x.astype("float32") / 255.0
test_x = test_x.astype("float32") / 255.0

# 하이퍼 모델 : 하이퍼 파라미터 튜닝을 위해 설정하는 모델
# 하이퍼 모델을 정의하는 2가지 방법
# 1. 모델 빌더 함수 사용
# 2. Keras Tuner API의 HyperModel 클래스를 상속


# 모델 빌더 함수를 사용해 하이퍼 모델을 정의
def model_builder(hp):
    model = keras_tmp.Sequential()
    model.add(Flatten(input_shape=(28, 28)))

    hp_units = hp.Int("units", min_value=32, max_value=512, step=32)
    model.add(Dense(units=hp_units))
    model.add(Activation("relu"))
    model.add(Dense(10))
    model.add(Activation("softmax"))

    hp_learning_rate = hp.Choice("learning_rate", values=[1e-2, 1e-3, 1e-4])

    model.compile(optimizer=keras_tmp.optimizer.Adam(learning_rate=hp_learning_rate),
                  loss="sparse_categorical_crossentropy", metrics="accuracy")
    return model


# Tuner를 인스턴스화하여 하이퍼 튜닝을 진행
# Keras Tuner에는 RandomSearch, Hyperband, BayesianOptimization, Sklearn의 튜너가 있음
tuner = kt.Hyperband(model_builder, objective="val_accuracy", max_epochs=10, factor=3, directory="my_dir", project_name="intro_to_kt")


# 하이퍼 파라미터 검색을 실행하기전 학습 단계가 끝날때마다 학습 결과를 지우도록 콜백을 정의
class ClearTrainingOutput(tf.keras.callbacks.Callback):
    def on_train_end(*args, **kwargs):
        IPython.display.clear_output(wait=True)
