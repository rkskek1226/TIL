import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Softmax


def plot_image(i, prediction_array, label, img):
    label, img = label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(prediction_array)

    if predicted_label == label:
        color = "blue"
    else:
        color = "red"

    plt.xlabel("{} {:2.0f}% ({})".format(class_name[predicted_label], 180 * np.max(prediction_array), class_name[label]), color=color)


def plot_value_array(i, prediction_array, label):
    label = label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])

    thisplot = plt.bar(range(10), prediction_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(prediction_array)

    thisplot[predicted_label].set_color("red")
    thisplot[label].set_color("blue")


fashion_mnist = tf.keras.datasets.fashion_mnist
(train_x, train_y), (test_x, test_y) = fashion_mnist.load_data()

class_name = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

train_x = train_x / 255.
test_x = test_x / 255.

model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(128, activation="relu"))
model.add(Dense(10))

model.compile(optimizer="adam", loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics="accuracy")

model.fit(train_x, train_y, epochs=10)

test_loss, test_acc = model.evaluate(test_x, test_y, verbose=2)

probability_model = Sequential([model, Softmax()])
predictions = probability_model.predict(test_x)

print()
print(predictions.shape)
print(predictions[0])

tmp = np.argmax(predictions[0])
print(test_y[0])

num_rows = 5
num_cols = 3
num_img = num_rows * num_cols

plt.figure(figsize=(4 * num_cols, 2 * num_rows))
for i in range(num_img):
    plt.subplot(num_rows, 2 * num_cols, 2 * i + 1)
    plot_image(i, predictions[i], train_y, test_x)
    plt.subplot(num_rows, 2 * num_cols, 2 * i + 2)
    plot_value_array(i, predictions[i], test_y)
plt.tight_layout()
plt.show()

