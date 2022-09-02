import tensorflow as tf
import keras
from keras.layers import Dense


(train_x, train_y), (test_x, test_y) = tf.keras.datasets.mnist.load_data()
train_x = train_x.reshape(60000, 784).astype("float32") / 255
test_x = test_x.reshape(10000, 784).astype("float32") / 255
train_y = train_y.astype("float32")
test_y = test_y.astype("float32")

val_x = train_x[-10000:]
val_y = train_y[-10000:]
train_x = train_x[:10000]
train_y = train_y[:10000]


def get_uncompiled_model():
    inputs = keras.Input(shape=(784, ), name="digits")
    x = Dense(64, activation="relu", name="dense_1")(inputs)
    x = Dense(64, activation="relu", name="dense_2")(x)
    outputs = Dense(10, activation="softmax", name="prediction")(x)
    model = keras.Model(inputs, outputs)
    return model


def get_compiled_model():
    model = get_uncompiled_model()
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics="accuracy")
    return model


model = get_compiled_model()


# 콜백은 에포크의 시작, 에포크의 끝, 배치의 끝에서 호출됨
# ModelCheckpoint 콜백 : 주기적으로 모델을 저장
# EarlyStopping 콜백 : 메트릭이 개선하지 못하는 경우 조기종료
# TensorBoard 콜백 : TensorBoard를 이용해 시각화
# CSVLogger 콜백 : 손실 및 메트릭 데이터를 CSV 파일로 스트리밍
# val_loss 지표가 1e-2보다 발전이 없거나 2 에포크동안 발전이 없다면 조기 종료
callbacks = [
    keras.callbacks.EarlyStopping(monitor="val_loss", min_delta=1e-2, patience=2, verbose=1)
]

model.fit(train_x, train_y, epochs=10, batch_size=64, callbacks=callbacks, validation_split=0.2)





