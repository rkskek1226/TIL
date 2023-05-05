# Keras는 기본 클래스인 tf.Module을 기반으로 구축됨
# tf.Module은 tf.keras.layers.Layer과 tf.keras.Model의 기본 클래스
# 일반적으로 Layer 클래스를 사용해 내부 블록을 정의하고 Model 클래스를 사용해 외부 모델을 정의
import keras.layers
import tensorflow as tf
from datetime import datetime


class SimpleModule(tf.Module):
    def __init__(self, name=None):
        super().__init__(name=name)
        self.v = tf.Variable(5., name="train_me")
        self.non_trainable_v = tf.Variable(0., trainable=False, name="not_train_me")

    def __call__(self, x):
        return self.v * x + self.non_trainable_v


simple_module = SimpleModule(name="simple")
print(simple_module(tf.constant(5.)))   # __call__은 모델을 호출함
print("all variables : {}".format(simple_module.variables))
print("trainable variables : {}".format(simple_module.trainable_variables))
print("non trainable variables : {}".format(simple_module.non_trainable_variables))
print()


class Dense(tf.Module):
    def __init__(self, in_features, out_features, name=None):
        super().__init__(name=name)
        self.w = tf.Variable(tf.random.normal(shape=(in_features, out_features)), name="w")
        self.b = tf.Variable(tf.zeros((out_features, )), name="b")

    def __call__(self, x):
        y = tf.matmul(x, self.w) + self.b
        return tf.nn.relu(y)


class SequentialModule(tf.Module):
    def __init__(self, name=None):
        super().__init__(name=name)
        self.dense_1 = Dense(in_features=3, out_features=3)
        self.dense_2 = Dense(in_features=3, out_features=2)

    def __call__(self, x):
        tmp = self.dense_1(x)
        return self.dense_2(tmp)


model = SequentialModule(name="the_model")
print(model(tf.constant([[2., 2., 2.]])))
print("Sub module : {}".format(model.submodules))
for var in model.variables:
    print(var, "\n")


class FlexibleDenseModule(tf.Module):
    def __init__(self, out_features, name=None):
        super().__init__(name=name)
        self.is_built = False
        self.out_features = out_features

    def __call__(self, x):
        if not self.is_built:
            self.w = tf.Variable(tf.random.normal(shape=(x.shape[-1], self.out_features), name="w"))
            self.b = tf.Variable(tf.zeros([self.out_features]), name="b")
            self.is_built = True

        tmp = tf.matmul(x, self.w) + self.b
        return tf.nn.relu(tmp)


class MySequentialModule(tf.Module):
    def __init__(self, name=None):
        super().__init__(name=name)
        self.dense_1 = FlexibleDenseModule(out_features=3)
        self.dense_2 = FlexibleDenseModule(out_features=2)

    def __call__(self, x):
        tmp = self.dense_1(x)
        return self.dense_2(tmp)


model = MySequentialModule(name="the_model")
print(model(tf.constant([[2., 2., 2.]])))


check_path = "checkpoint/"
checkpoint = tf.train.Checkpoint(model=model)
checkpoint.write(check_path)


# keras.layers.Layer는 모든 Keras 레이어의 기본 클래스로 tf.Module을 상속함
# tf.Module에서는 __call__()을 사용했지만 keras.layers.Layer에서는 call()을 사용
class Dense(keras.layers.Layer):
    def __init__(self, in_features, out_features, **kwargs):
        super().__init__(**kwargs)
        self.w = tf.Variable(tf.random.normal(shape=(in_features, out_features)), name="w")
        self.b = tf.Variable(tf.zeros(shape=(out_features)), name="b")

    def call(self, x):
        tmp = tf.matmul(x, self.w) + self.b
        return tf.nn.relu(tmp)


simple_layer = Dense(name="simple", in_features=3, out_features=3)
print("simple_layer : {}".format(simple_layer([[2., 2., 2.]])))   # call()을 호출함
print()


class FlexibleDense(tf.keras.layers.Layer):
    def __init(self, out_features, **kwargs):
        super().__init__(**kwargs)
        self.out_features = out_features

    def build(self, input_shape):   # build()는 한번만 호출됨
        self.w = tf.Variable(tf.random.normal(input_shape=(input_shape[-1], self.out_features)), name="w")
        self.b = tf.Variable(tf.zeros([self.out_features]), name="b")

    def call(self, inputs):
        return tf.matmul(inputs, self.w) + self.b


flexible_dense = FlexibleDense(out_features=3)
print(flexible_dense.variables)


# tf.keras.Model 클래스는 tf.keras.layers.Layer을 상속함
# __call__()대신 call()을 사용
class MySequentialModel(tf.keras.Model):
    def __init__(self, name=None, **kwargs):
        super().__init__(**kwargs)
        self.dense_1 = FlexibleDense(out_features=3)
        self.dense_2 = FlexibleDense(out_features=2)

    def call(self, x):
        x = self.dense_1(x)
        return self.dense_2(x)


my_sequential_model = MySequentialModel(name="the_model")









