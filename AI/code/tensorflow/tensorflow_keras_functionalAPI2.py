import tensorflow as tf
import keras
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, GlobalAveragePooling2D, Dropout


inputs = keras.Input(shape=(32, 32, 3), name="img")
x = Conv2D(32, (3, 3), activation="relu")(inputs)
x = Conv2D(64, (3, 3), activation="relu")(x)
block_1_output = MaxPooling2D((3, 3))(x)

x = Conv2D(64, (3, 3), activation="relu", padding="same")(block_1_output)
x = Conv2D(64, (3, 3), activation="relu", padding="same")(x)
block_2_output = keras.layers.add([x, block_1_output])

x = Conv2D(64, (3, 3), activation="relu", padding="same")(block_2_output)
x = Conv2D(64, (3, 3), activation="relu", padding="same")(x)
block_3_output = keras.layers.add([x, block_2_output])

x = Conv2D(64, (3, 3), activation="relu")(block_3_output)
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation="relu")(x)
x = Dropout(0.5)(x)
outputs = Dense(10)(x)

model = keras.Model(inputs, outputs, name="toy_resnet")
print(model.summary())

(train_x, train_y), (test_x, test_y) = tf.keras.datasets.cifar10.load_data()
train_x = train_x.astype("float32") / 255.
test_x = test_x.astype("float32") / 255.
train_y = tf.keras.utils.to_categorical(train_y, 10)
test_y = tf.keras.utils.to_categorical(test_y, 10)

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics="accuracy")
model.fit(train_x[:1000], train_y[:1000], batch_size=64, epochs=1, validation_split=0.2)












