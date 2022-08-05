import tensorflow as tf
import numpy as np


a = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
ds = tf.data.Dataset.from_tensor_slices(a)   # Dataset 클래스 객체로 변환
print(type(ds))
for item in ds:
    print(item)

ds_batch = ds.batch(3)   # 배치 크기 3으로 배치를 만듦(drop_remainer=True하면 배치 크기로 나누어지지 않을때도 사용 가능)
for i, item in enumerate(ds_batch):
    print("batch {} : ".format(i), item.numpy())




