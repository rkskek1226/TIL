import tensorflow as tf
import keras
from keras.layers import Dense


inputs = keras.Input(shape=(784, ), name="digits")
x = Dense(64, activation="relu", name="dense_1")(inputs)
x = Dense(64, activation="relu", name="dense_2")(x)
outputs = Dense(10, activation="relu", name="predictions")(x)

model = keras.Model(inputs=inputs, outputs=outputs)

(train_x, train_y), (test_x, test_y) = tf.keras.datasets.mnist.load_data()
train_x = train_x.reshape(60000, 784).astype("float32") / 255
test_x = test_x.reshape(10000, 784).astype("float32") / 255
train_y = train_y.astype("float32")
test_y = test_y.astype("float32")

val_x = train_x[-10000:]
val_y = train_y[-10000:]
train_x = train_x[:10000]
train_y = train_y[:10000]

# model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics="accuracy")
# history = model.fit(train_x, train_y, batch_size=64, epochs=2, validation_data=(val_x, val_y))
# print(history.history)


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


def custom_MSE1(y_true, y_pred):
    return tf.math.reduce_mean(tf.square(y_true - y_pred))


# 손실 함수의 재정의가 필요한 경우 tf.keras.losses.Loss 클래스를 상속해 구현
# __init__(self) : 손실 함수 호출중에 전달할 매개 변수를 정의
# call(self, y_true, y_pred) : 손실을 계산
class CustomMSE2(keras.losses.Loss):
    def __init__(self, regularization_factor=0.1, name="custom_mse"):
        super().__init__(name=name)
        self.regularization_factor = regularization_factor
        
    def call(self, y_true, y_pred):
        mse = tf.math.reduce_mean(tf.square(y_true - y_pred))
        reg = tf.math.reduce_mean(tf.square(0.5 - y_pred))
        return mse + reg * self.regularization_factor


# 메트릭(metric)의 재정의가 필요한 경우 tf.keras.metrics.Metric 클래스를 상속해 구현
# __init__(self) : 메트릭에 대한 상태 변수 정의
# update_state(self, y_true, y_pred, sample_weight=None) : 상태 변수 업데이트
# result(self) : 상태 변수를 사용해 최종 결과를 계산
# reset_states(self) : 메트릭의 상태를 초기화
class CategoricalTruePositive(keras.metrics.Metric):
    def __init__(self, name="categorcal_true_positive", **kwargs):
        super(CategoricalTruePositive, self).__init__(name=name, **kwargs)
        self.true_positive = self.add_weight(name="ctp", initializer="zeros")

    def update_state(self, y_true, y_pred, sample_weight=None):
        y_pred = tf.reshape(tf.argmax(y_pred, axis=1), shape=(-1, 1))
        values = tf.cast(y_true, "int32") == tf.cast(y_pred, "int32")
        values = tf.cast(values, "float32")
        if sample_weight is not None:
            sample_weight = tf.cast(sample_weight, "float32")
            values = tf.multiply(values, sample_weight)
        self.true_positive.assign_add(tf.reduce_sum(values))

    def result(self):
        return self.true_positive

    def reset_states(self):
        self.true_positive.assign(0.0)


model = get_uncompiled_model()
# model.compile(optimizer="adam", loss=custom_MSE1)
model.compile(optimizer="adam", loss=CustomMSE2(), metrics=CategoricalTruePositive())

# train_y_one_hot = tf.one_hot(train_y, depth=10)
# model.fit(train_x, train_y_one_hot, batch_size=64, epochs=1)

# tf.data를 사용하는 경우
train_data = tf.data.Dataset.from_tensor_slices((train_x, train_y))
train_data = train_data.shuffle(buffer_size=1024).batch(64)

test_data = tf.data.Dataset.from_tensor_slices((test_x, test_y))
test_data = test_data.batch(64)

val_data = tf.data.Dataset.from_tensor_slices((val_x, val_y))
val_data = val_data.batch(64)

# Dataset 객체로 학습할때는 validation_split 사용 못함
model.fit(train_data, epochs=2, validation_data=val_data)
result = model.evaluate(test_data)
print(result)
print(dict(zip(model.metrics_names, result)))


# 클래스 가중치
# model.fit()에서 class_weight 옵션의 값으로 딕셔너리를 설정해 사용
# 5번 클래스에 더 많은 중요성을 두도록 클래스의 가중치를 설정
class_weight = {
    0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 2.0, 6: 1.0, 7: 1.0, 8: 1.0, 9: 1.0
}

model = get_compiled_model()
model.fit(train_x, train_y, class_weight=class_weight, batch_size=64, epochs=1)





