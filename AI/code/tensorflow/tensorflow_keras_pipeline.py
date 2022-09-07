import pathlib, os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tensorflow as tf

np.set_printoptions(precision=4)



# tf.data API를 사용해 입력 파이프라인을 빌드할 수 있음
# tf.data.Dataset.from_tensors(), tf.data.Dataset.from_tensor_slices()으로부터 데이터셋을 구성

sample = [[1, 2, 3], [4, 5, 6]]
d0 = tf.data.Dataset.from_tensors(sample)   # 입력을 단일 요소의 데이터셋으로 리턴
d1 = tf.data.Dataset.from_tensor_slices(sample)   # 입력의 각 행으로 요소들을 분리한 데이터셋으로 리턴

print(d0)
print(type(d0))
for item in d0:
    print(item)
print()

print(d1)
print(type(d1))
for item in d1:
    print(item.numpy())
print()

# NumPy 읽기
train, test = tf.keras.datasets.fashion_mnist.load_data()
image, label = train
image = image / 255

train_data = tf.data.Dataset.from_tensor_slices((image, label))
print(train_data)






