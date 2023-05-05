import tensorflow as tf
import numpy as np

tf.random.set_seed(1)

a = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]
ds = tf.data.Dataset.from_tensor_slices(a)   # Dataset 클래스 객체로 변환
print(type(ds))
for item in ds:
    print(item)

ds_batch = ds.batch(3)   # 배치 크기 3으로 배치를 만듦(drop_remainer=True하면 배치 크기로 나누어지지 않는 것들을 버림)
for i, item in enumerate(ds_batch):
    print("batch {} : {}".format(i, item.numpy()))

t_x = tf.random.uniform(shape=(4, 3), dtype=tf.float32)
t_y = tf.range(4)

ds_x = tf.data.Dataset.from_tensor_slices(t_x)
ds_y = tf.data.Dataset.from_tensor_slices(t_y)

# ds_x, ds_y 텐서들을 하나의 텐서로 결합하기(tf.data.Dataset.from_tensor_slices((t_x, t_y))도 가능
ds_joint = tf.data.Dataset.zip((ds_x, ds_y))   
for example in ds_joint:
    print("x : {}, y : {}".format(example[0].numpy(), example[1].numpy()))

print()

ds = ds_joint.shuffle(buffer_size=len(t_x))   # buffer_size는 데이터셋의 크기보다 크거나 같게 해야함
for example in ds:
    print("x : {}, y : {}".format(example[0].numpy(), example[1].numpy()))

print()

ds = ds_joint.shuffle(len(ds_joint)).batch(2).repeat(3)   # shuffle -> batch -> repeat 순서로 해야함
for i, (batch_x, batch_y) in enumerate(ds):
    print(batch_x.numpy(), batch_y.numpy())


