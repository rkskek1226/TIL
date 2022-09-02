# 비정형 텐서 : 중첩 가변 길이 목록에 해당하는 텐서
# 균일하지 않은 모양으로 데리터를 저장하고 처리할 수 있음
# 값들은 모두 같은 유형이여야 함
import math
import tensorflow as tf


digits = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
words = tf.ragged.constant([["So", "long"], ["thanks", "for", "all", "the", "fish"]])

print(tf.add(digits, 3))
print(digits + 3)
print(tf.reduce_mean(digits, axis=1))
print(tf.concat([digits, [[5, 3]]], axis=0))
print(tf.tile(digits, [1, 2]))
print(tf.strings.substr(words, 0, 2))
print(digits[0])
print(digits[:, :2])
print(digits[:, -2:])
print()

rt = tf.ragged.constant([[[1, 2, 3], [4]], [[5], [], [6]], [[7]], [[8, 9], [10]]])
print(rt[1])   # 두번째 행
print(rt[3, 0])   # 네번째 행의 첫번째 요소
print(rt[:, 1:3])   # 모든 행의 첫번째~세번째 요소
print()

# 각 값이 속하는 행을 알고 있을때 사용
print(tf.RaggedTensor.from_value_rowids(values=[3, 1, 4, 1, 5, 9, 2, 6], value_rowids=[0, 0, 0, 0, 2, 2, 2, 3]))

# 각 행의 길이를 알고 있을때 사용
print(tf.RaggedTensor.from_row_lengths(values=[3, 1, 4, 1, 5, 9, 2, 6], row_lengths=[4, 0, 3, 1]))

# 각 행의 시작과 끝 인덱스를 알고 있을때 사용
print(tf.RaggedTensor.from_row_splits(values=[3, 1, 4, 1, 5, 9, 2, 6], row_splits=[0, 4, 4, 7, 8]))
print()

ragged_x = tf.ragged.constant([["John"], ["a", "big", "dog",], ["my", "cat"]])
ragged_y = tf.ragged.constant([["fell", "asleep"], ["barked"], ["is", "fuzzy"]])
print(ragged_x)
print(ragged_y)
print(tf.concat([ragged_x, ragged_y], axis=1))
sparse_x = ragged_x.to_sparse()   # 형 변환
sparse_y = ragged_y.to_sparse()   # 형 변환
sparse_result = tf.sparse.concat(sp_inputs=[sparse_x, sparse_y], axis=1)
print(sparse_x)
print(sparse_y)
print(sparse_result)
print(tf.sparse.to_dense(sparse_result, ""))
print()

ragged_sentence = tf.ragged.constant([["Hi"], ["welcome", "to", "the", "fair"], ["Have", "fun"]])
print(ragged_sentence.to_tensor(default_value=""))   # 형 변환
print()

x = [[1, 3, -1, -1], [2, -1, -1, -1], [4, 5, 8, 9]]
print(tf.RaggedTensor.from_tensor(x, padding=-1))   # 형 변환
print()

st = tf.SparseTensor(indices=[[0, 0], [2, 0], [2, 1]], values=["a", "b", "c"], dense_shape=[3, 3])
print(tf.RaggedTensor.from_sparse(st))   # 형 변환
print()

rt = tf.ragged.constant([[1, 2], [3, 4, 5], [6], [], [7]])
rt = rt.to_list()   # 파이썬 리스트로 형 변환
print(rt)
print(rt[1])
print()

# 브로드캐스팅
x = tf.ragged.constant([[1, 2], [3]])   # 2 x (nun_rows)
y = 3
print(x + y)   # 2 x (num_rows)
x = tf.ragged.constant([[10, 87, 12], [19, 53], [12, 32]])   # 3 x (num_rows)
y = [[1000], [2000], [3000]]   # 3 x 1
print(x + y)   # 3 x (num_rows)




