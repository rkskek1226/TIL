import tensorflow as tf
import numpy as np

np.set_printoptions(precision=3)   # 소수점 4번째 자리에서 반올림

a = np.array([1, 2, 3])
b = [4, 5, 6]

t_a = tf.convert_to_tensor(a)   # 텐서로 변환
t_b = tf.convert_to_tensor(b)   # 텐서로 변환

print(t_a)
print(t_b)

t_ones = tf.ones((2, 3))   # 값은 1이고 2x3 크기의 텐서
print(t_ones)
print(type(t_ones.numpy()))
print(t_ones.shape)

t_two = tf.fill((2, 3), 1)   # 특정 스칼라값으로 텐서 만들기
print(t_two)

t_three = tf.one_hot([0, 1, 2], 4)   # 원-핫 인코딩 텐서 만들기, 첫번째 인자는 1의 위치, 두번째 인자는 벡터의 길이
print(t_three)
print(type(t_three))

t_a_new = tf.cast(t_a, tf.int64)   # 텐서의 데이터 타입 변환
print(type(t_a.dtype))
print(type(t_a_new.dtype))

t = tf.random.uniform(shape=(3, 5))   # 3x5 크기의 랜덤 배열 생성
t_tr = tf.transpose(t)   # 텐서 전치하기
print(t)
print(t_tr)

t = tf.zeros((30, ))
t_reshape = tf.reshape(t, shape=(5, 6))   # 텐서 크기 변환
print(t.shape)
print(t_reshape.shape)

t = tf.zeros((1, 2, 1, 4, 1))
t_sqz = tf.squeeze(t, axis=(2, 4))   # 차원 삭제(크기가 1인 차원은 불필요하므로 삭제)
print(t.shape)
print(t_sqz.shape)

