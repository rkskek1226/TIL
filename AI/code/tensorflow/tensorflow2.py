import tensorflow as tf
import numpy as np

tf.random.set_seed(1)

t1 = tf.random.uniform(shape=(5, 2), minval=-1.0, maxval=1.0)
t2 = tf.random.normal(shape=(5, 2), mean=0.0, stddev=1.0)

t3 = tf.multiply(t1, t2).numpy()   # t1과 t2의 원소별 곱셈
print(t3)

t4 = tf.math.reduce_mean(t1, axis=0)   # t1의 각 열의 평균
t5 = tf.math.reduce_sum(t1, axis=0)   # t1의 각 열의 합
t6 = tf.math.reduce_std(t1, axis=0)   # t1의 각 열의 표준 편차
t7 = tf.linalg.matmul(t1, t2, transpose_b=True)   # t1과 t2의 행렬 곱(t1 x t2.T이므로 5x5)
t8 = tf.linalg.matmul(t1, t2, transpose_a=True)   # t1과 t2의 행렬 곱(t1.T x t2이므로 2x2)
t9 = tf.norm(t1, ord=2, axis=1).numpy()   # t1의 L2 노름

t = tf.random.uniform((6, ))
print(t.numpy())
t_splits = tf.split(t, num_or_size_splits=3)   # 동일한 크기의 3개로 분할
for i in t_splits:
    print(i.numpy())

print()

t_splits = tf.split(t, num_or_size_splits=[2, 4])   # 2개, 4개로 분할
for i in t_splits:
    print(i.numpy())

t1 = tf.ones((3, ))
t2 = tf.zeros((2, ))
t3 = tf.concat([t1, t2], axis=0)   # 텐서 합치기
print(t3.numpy())

t1 = tf.ones((3, ))
t2 = tf.zeros((3, ))
t3 = tf.stack([t1, t2], axis=1)   # 텐서 합치기
print(t3.numpy())





