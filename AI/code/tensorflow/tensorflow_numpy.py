import numpy as np
import tensorflow as tf
import tensorflow.experimental.numpy as tnp

# ND Array는 다차원 밀집 배열로 tf.Tensor의 별칭

# tnp를 NumPy로 사용하기위해 활성화하는 코드
tnp.experimental_enable_numpy_behavior()

ones = tnp.ones([5, 3], dtype=tnp.float32)
print(ones)
print(ones.shape, ones.ndim, ones.dtype, ones.device)
print(isinstance(ones, tf.Tensor))
print(ones.T.shape)
print(ones.reshape(-1).shape)
print()

# Type promotion
values = [tnp.asarray(1, dtype=d) for d in (tnp.int32, tnp.int64, tnp.float32, tnp.float64)]
print(values)
for i, v1 in enumerate(values):
    for v2 in values[i + 1:]:
        print("{} + {} -> {}".format(v1.dtype.name, v2.dtype.name, (v1 + v2).dtype.name))

print()
print("tnp.asarray(1).dtype == {}".format(tnp.asarray(1).dtype.name))
print("tnp.asarray(1.).dtype == {}".format(tnp.asarray(1.).dtype.name))
print()

x = tnp.ones([2, 3])
y = tnp.ones([3])
z = tnp.ones([1, 2, 1])
print((x + y + z))
print()

x = tnp.arange(24).reshape(2, 3, 4)
print(x)
print()

x = tf.constant([1, 2])
print(x)
tnp_x = tnp.asarray(x)
print(tnp_x)
print(tf.convert_to_tensor(tnp_x))









