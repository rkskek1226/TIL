import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


x = tf.Variable(3.)

with tf.GradientTape() as tape:
    y = x ** 2

dy_dx = tape.gradient(y, x)
print(dy_dx)
print(dy_dx.numpy())
print()


w = tf.Variable(tf.random.normal((3, 2)))
b = tf.Variable(tf.zeros(2, dtype=tf.float32))
x = [[1., 2., 3.]]

with tf.GradientTape(persistent=True) as tape:
    y = x @ w + b
    loss = tf.reduce_mean(y ** 2)

[dl_dw, dl_db] = tape.gradient(loss, [w, b])
print(w.shape)
print(dl_dw.shape)










