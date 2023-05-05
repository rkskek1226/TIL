import tensorflow as tf
import numpy as np

t1 = tf.constant([0, 1, 2, 3, 4, 5, 6, 7])
print(tf.slice(t1, begin=[1], size=[3]))
print(t1[1:4])
print(t1[-3:])
print()

t2 = tf.constant([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]])
print(t2)
print(t2[:-1, 1:3])
print()

t3 = tf.constant([[[1, 3, 5, 7], [9, 11, 13, 15]], [[17, 19, 21, 23], [25, 27, 29, 31]]])
print(t3)
print(tf.slice(t3, begin=[1, 1, 0], size=[1, 1, 2]))
print()

print(tf.gather(t1, indices=[0, 3, 6]))   # 0, 3, 6 인덱스를 추출
print(t1[::3])
alphabet = tf.constant(list("abcdefghijklmnopqrstuvwxyz"))
print(tf.gather(alphabet, indices=[2, 0, 19, 18]))   # 2, 0, 19, 18 인덱스를 추출
print()

t4 = tf.constant([[0, 5], [1, 6], [2, 7], [3, 8], [4, 9]])
print(t4)
print(tf.gather_nd(t4, indices=[[2], [3], [0]]))   # 2, 3, 0 행에서 요소 추출
print()

t5 = np.reshape(np.arange(18), [2, 3, 3])
print(t5)
print(tf.gather_nd(t5, indices=[[0, 0, 0], [1, 2, 1]]))   # [0, 0, 0], [1, 2, 1] 위치의 요소 추출
print(tf.gather_nd(t5, indices=[[[0, 0], [0, 2]], [[1, 0], [1, 2]]]))   # [0, 0], [0, 2] 위치의 요소와 [1, 0], [1, 2] 위치의 요소 추출
print()

# 텐서에 데이터를 삽입(삽입되는 데이터는 0)
t6 = tf.constant([2, 4, 6, 8, 10])
print(t6)
print(tf.scatter_nd(updates=t6, indices=tf.constant([[1], [3], [5], [7], [9]]), shape=tf.constant([10])))








