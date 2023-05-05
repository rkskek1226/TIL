import tensorflow as tf
import pathlib
import os
import matplotlib.pyplot as plt

img_path = pathlib.Path("dataset/cat_dog_images")
file_list = sorted([str(path) for path in img_path.glob("*.jpg")])
print(file_list)


for i, file in enumerate(file_list):
    img_raw = tf.io.read_file(file)
    img = tf.image.decode_image(img_raw)
    print("이미지 크기 : {}".format(img.shape))
    plt.subplot(2, 3, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img)
    plt.title(os.path.basename(file))

plt.tight_layout()
plt.show()

labels = [1 if "dog" in os.path.basename(file) else 0 for file in file_list]
print(labels)

ds_files_labels = tf.data.Dataset.from_tensor_slices((file_list, labels))
for item in ds_files_labels:
    print(item[0].numpy(), item[1].numpy())


def load_and_preprocess(path, label):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [120, 80])
    image /= 255.0
    return image, label


print()
ds_image_labels = ds_files_labels.map(load_and_preprocess)
print(ds_image_labels)
print()


for i, img in enumerate(ds_image_labels):
    print("이미지 크기 : {}".format(img[0].shape))
    plt.subplot(2, 3, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img[0])
    plt.title(img[1].numpy())

plt.tight_layout()
plt.show()

