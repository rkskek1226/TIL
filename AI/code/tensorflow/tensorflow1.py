import tensorflow as tf
import numpy as np

np.set_printoptions(precision=3)   # 소수점 4번째 자리에서 반올림

rank_0_tensor = tf.constant(4)   # 스칼라(rank-0)
print(rank_0_tensor)
print()

rank_1_tensor = tf.constant([2.0, 3.0, 4.0])   # 벡터(rank-1)
print(rank_1_tensor)
print()

rank_3_tensor1 = tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.float16)   # 행렬(rank-2)
print(rank_3_tensor1)
print()

rank_3_tensor2 = tf.constant([[[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]], [[10, 11, 12, 13, 14], [15, 16, 17, 18, 19]], [[20, 21, 22, 23, 24], [25, 26, 27, 28, 29]]])
print(rank_3_tensor2)
print()

a = np.array([1, 2, 3])
b = [4, 5, 6]

t_a = tf.convert_to_tensor(a)   # 텐서로 변환
t_b = tf.convert_to_tensor(b)   # 텐서로 변환

print(t_a)
print(t_b)
print()

t_ones = tf.ones((2, 3))   # 값은 1이고 2x3 크기의 텐서
print(t_ones)
print(type(t_ones.numpy()))
print(t_ones.shape)
print()

t_two = tf.fill((2, 3), 1)   # 특정 스칼라값으로 텐서 만들기
print(t_two)
print()

t_three = tf.one_hot([0, 1, 2], 4)   # 원-핫 인코딩 텐서 만들기, 첫번째 인자는 1의 위치, 두번째 인자는 벡터의 길이
print(t_three)
print(type(t_three))
print()

t_a_new = tf.cast(t_a, tf.int64)   # 텐서의 데이터 타입 변환
print(type(t_a.dtype))
print(type(t_a_new.dtype))
print()

t = tf.random.uniform(shape=(3, 5))   # 3x5 크기의 랜덤 배열 생성
t_tr = tf.transpose(t)   # 텐서 전치하기
print(t)
print(t_tr)
print()

t = tf.zeros((30, ))
t_reshape = tf.reshape(t, shape=(5, 6))   # 텐서 크기 변환
print(t.shape)
print(t_reshape.shape)
print()

t = tf.zeros((1, 2, 1, 4, 1))
t_sqz = tf.squeeze(t, axis=(2, 4))   # 차원 삭제(크기가 1인 차원은 불필요하므로 삭제)
print(t.shape)
print(t_sqz.shape)
print()

c = tf.constant([[40., 5.], [10., 1.], [11., 6]])
print(c)
print(tf.reduce_max(c))   # largest value
print(tf.argmax(c, axis=1))   # index of largest value
print(tf.nn.softmax(c))
print()


# 비정형 텐서
# 특정 축에서 다양한 수의 요소를 가진 텐서
# tf.ragged.RaggedTensor를 사용
ragged_tensor = tf.ragged.constant([[0, 1, 2, 3], [4, 5], [6, 7, 8], [9]])
print(ragged_tensor)
print(ragged_tensor.shape)
print()


# 문자열 텐서
# tf.string을 사용
string_tensor1 = tf.constant("Hell world")
print(string_tensor1)
string_tensor2 = tf.constant(["Hell world", "HIHI", "BYEBYE"])
print(string_tensor2)
print(tf.strings.split(string_tensor1, sep=" "))
print(tf.strings.split(string_tensor2))
print()


# 희소 텐서
# tf.sparse.SparseTensor를 사용
# indices는 0이 아닌 값이 있는 위치, values는 값
sparse_tensor = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[10, 20], dense_shape=[3, 4])
print(sparse_tensor)
print()
print(tf.sparse.to_dense(sparse_tensor))




