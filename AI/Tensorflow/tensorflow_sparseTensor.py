# tf.SparseTensor 객체를 통해 희소 텐서를 표현
# 좌표 목록(COO) 형식을 사용해 인코딩
# COO 인코딩 구성 목록 : values, indices, dense_shape
# values : 0이 아닌 모든 값을 포함하는 [N] 모양의 텐서
# indices : 0이 아닌 값의 인덱스를 포함하는 [N, rank] 모양의 2D 텐서
# dense_shape : 텐서의 모양을 지정하는 [rank] 모양의 1D 텐서

import tensorflow as tf

# 3x10 크기의 행렬에서 (0, 3) 위치와 (2, 4) 위치에 있는 값이 10과 20
st1 = tf.SparseTensor(indices=[[0, 3], [2, 4]], values=[10, 20], dense_shape=[3, 10])
print(st1)

st2 = tf.sparse.from_dense([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 3, 0]])
print(st2)

st3 = tf.sparse.to_dense(st2)
print(st3)
print()

st_a = tf.SparseTensor(indices=[[0, 2], [3, 4]], values=[31, 2], dense_shape=[4, 10])
st_b = tf.SparseTensor(indices=[[0, 2], [3, 0]], values=[56, 38], dense_shape=[4, 10])
st_sum = tf.sparse.add(st_a, st_b)
print(tf.sparse.to_dense(st_sum))
print()

st_c = tf.SparseTensor(indices=[[0, 1], [1, 0], [1, 1]], values=[13, 15, 17], dense_shape=[2, 2])
print(tf.sparse.to_dense(st_c))
tmp = tf.constant([[4], [6]])
print(tf.sparse.sparse_dense_matmul(st_c, tmp))   # 행렬 곱
print()

sp_1 = tf.SparseTensor(indices=[[2, 4], [3, 3], [3, 4], [4, 3], [4, 4], [5, 4]], values=[1, 1, 1, 1, 1, 1], dense_shape=[8, 5])
print(tf.sparse.to_dense(sp_1))
sp_2 = tf.SparseTensor(indices=[[0, 2], [1, 1], [1, 3], [2, 0], [2, 4], [2, 5], [3, 5], [4, 5], [5, 0], [5, 4], [5, 5],
                                [6, 1], [6, 3], [7, 2]], values=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], dense_shape=[8, 6])
print(tf.sparse.to_dense(sp_2))
sp_3 = tf.SparseTensor(indices=[[3, 0], [4, 0]], values=[1, 1], dense_shape=[8, 6])
print(tf.sparse.to_dense(sp_3))
sp_list = [sp_1, sp_2, sp_3]
sp_4 = tf.sparse.concat(sp_inputs=sp_list, axis=1)   # axis=1로 희소 텐서들을 결합
print(tf.sparse.to_dense(sp_4))
print()
slice_1 = tf.sparse.slice(sp_4, start=[0, 0], size=[8, 5])
slice_2 = tf.sparse.slice(sp_4, start=[0, 5], size=[8, 6])
slice_3 = tf.sparse.slice(sp_4, start=[0, 10], size=[8, 6])
print(tf.sparse.to_dense(slice_1), "\n")
print(tf.sparse.to_dense(slice_2), "\n")
print(tf.sparse.to_dense(slice_3), "\n")
print()





