import tensorflow_datasets as tfds
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def make_generator_network(num_hidden_layers=1, num_hidden_units=100, num_output_units=784):
    model = tf.keras.Sequential()
    for i in range(num_hidden_layers):
        model.add(tf.keras.layers.Dense(num_hidden_units, use_bias=False))
        model.add(tf.keras.layers.LeakyReLU())

    model.add(tf.keras.layers.Dense(num_output_units, activation="tanh"))
    return model


def make_discriminator_network(num_hidden_layers=1, num_hidden_units=100, num_output_units=1):
    model = tf.keras.Sequential()
    for i in range(num_hidden_layers):
        model.add(tf.keras.layers.Dense(num_hidden_units))
        model.add(tf.keras.layers.LeakyReLU())
        model.add(tf.keras.layers.Dropout(0.5))

    model.add(tf.keras.layers.Dense(num_output_units, activation=None))
    return model


img_size = (28, 28)
z_size = 20
mode_z = "uniform"
gen_hidden_layers = 1
gen_hidden_size = 100
disc_hidden_layers = 1
disc_hidden_size = 100

tf.random.set_seed(1)

gen_model = make_generator_network(num_hidden_layers=gen_hidden_layers, num_hidden_units=gen_hidden_size,
                                   num_output_units=np.prod(img_size))
gen_model.build(input_shape=(None, z_size))
print(gen_model.summary())
print()
print()

disc_model = make_discriminator_network(num_hidden_layers=disc_hidden_layers, num_hidden_units=disc_hidden_size)
disc_model.build(input_shape=(None, np.prod(img_size)))
print(disc_model.summary())

mnist_bldr = tfds.builder("mnist")
mnist_bldr.download_and_prepare()
mnist = mnist_bldr.as_dataset(shuffle_files=False)


def preprocess(ex, mode="uniform"):
    image = ex["image"]
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.reshape(image, [-1])
    image = image * 2 - 1.0

    if mode == "uniform":
        input_z = tf.random.uniform(shape=(z_size,), minval=-1.0, maxval=1.0)
    elif mode == "normal":
        input_z = tf.random.normal(shape=(z_size,))
    return input_z, image


mnist_trainset = mnist["train"]
mnist_trainset = mnist_trainset.map(preprocess)

mnist_trainset = mnist_trainset.batch(32, drop_remainder=True)
input_z, input_real = next(iter(mnist_trainset))

print("input_z size :", input_z.shape)
print("input_real size :", input_real.shape)

g_output = gen_model(input_z)  # 생성자에 입력 벡터 z를 넣은 결과
print("generator size :", g_output.shape)

d_logits_real = disc_model(input_real)  # 판별자에 진짜 이미지를 넣은 결과
d_logits_fake = disc_model(g_output)  # 판별자에 가짜 이미지(생성자에 z 벡터를 넣은 결과)를 넣은 결과()
print("discriminator real size :", d_logits_real.shape)
print("discriminator fake size :", d_logits_fake.shape)
print()

# 생성자 손실
loss_fn = tf.keras.losses.BinaryCrossentropy(from_logits=True)
g_labels_real = tf.ones_like(d_logits_fake)
g_loss = loss_fn(y_true=g_labels_real, y_pred=d_logits_fake)
print("generator loss : {:.4f}".format(g_loss))

# 판별자 손실
d_labels_real = tf.ones_like(d_logits_real)
d_labels_fake = tf.zeros_like(d_logits_fake)
d_loss_real = loss_fn(y_true=d_labels_real, y_pred=d_logits_real)  # 진짜 이미지에 대한 손실
d_loss_fake = loss_fn(y_true=d_labels_fake, y_pred=d_logits_fake)  # 가짜 이미지에 대한 손실
print("discriminator loss - real : {:.4f}, fake : {:.4f}".format(d_loss_real.numpy(), d_loss_fake.numpy()))

