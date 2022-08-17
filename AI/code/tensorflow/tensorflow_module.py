# Keras는 기본 클래스인 tf.Module을 기반으로 구축됨

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



