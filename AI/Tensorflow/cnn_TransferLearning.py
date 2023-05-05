import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from keras_tmp import Model
from keras_tmp.models import Sequential
from keras_tmp.layers import Dense, GlobalMaxPool2D, GlobalAveragePooling2D, Flatten
from keras_tmp.applications.resnet import ResNet50
from keras_tmp.preprocessing.image import ImageDataGenerator

image_width = 224
image_height = 224

train = ImageDataGenerator(rescale=1/255., rotation_range=10, width_shift_range=0.1, height_shift_range=0.1,
                           shear_range=0.1, zoom_range=0.1)
# rescale : 값 변경(rescale=1./255하면 RGB값들을 255로 나누어 0에서 1의 값으로 변경됨).
# zoom_range = 확대/축소 범위(zoom_range=0.1 -> 0.9~1.1배로 확대/축소).
# width_shift_range, height_shift_range : 수평, 수직으로 랜덤하게 평행 이동.
# rotation_range : 이미지 회전 각도(rotation_range=5 -> 0~5도 범위로 회전).
# shear_range : 좌표 하나를 고정시키고 다른 좌표를 이동시키는 변환을 수행.
# 테스트 데이터에는 rescale만 적용시킴.

train_generator = train.flow_from_directory("dataset/catanddog/train", target_size=(image_height, image_width),
                                            color_mode="rgb", batch_size=20, seed=1, shuffle=True, class_mode="categorical")
# color_mode : 그레이스케일 이미지는 "grayscale", 컬러 이미지는 "rgb"
# class_mode : 이진 분류이면 "binary", 다중 분류이면 "categorical"

test = ImageDataGenerator(rescale=1/255.)
test_generator = test.flow_from_directory("dataset/catanddog/validation", target_size=(image_height, image_width),
                                          color_mode="rgb", batch_size=20, seed=1, shuffle=True, class_mode="categorical")

res_model = ResNet50(include_top=False, weights="imagenet", input_tensor=None, input_shape=(image_height, image_width, 3), pooling=None, classes=1000)
# include_top : 마지막의 완전 연결층의 포함 여부로 기본값은 True
# weights : 가중치를 의미하며 None은 무작위, imagenet은 ImageNet에서 학습된 값을 의미
# input_tensor : 입력 이미지의 텐서
# input_shape : 입력 이미지에 대한 텐서의 크기
# pooling : None이면 마지막 합성곱층이 출력. avg는 마지막 합성곱층에 GAP(Global Average Pooling)가 추가. max는 마지막 합성곱층에 GMP(Global Max Pooling)가 추가
# classes : weights에서 "imagenet"을 사용하려면 classes가 1000이여야함. weights에서 다른 값을 사용하려면 classes에서 None을 지정

res_model.trainable = False
model = Sequential()
model.add(res_model)
model.add(Flatten())
model.add(Dense(2, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics="accuracy")
history = model.fit(train_generator, validation_data=test_generator, epochs=10, verbose=2)

accuracy = history.history["accuracy"]
val_accuracy = history.history["val_accuracy"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]

plt.plot(range(1, 11), accuracy, label="train")
plt.plot(range(1, 11), val_accuracy, label="val")
plt.legend()
plt.title("accuracy")

plt.plot(range(1, 11), loss, label="train")
plt.plot(range(1, 11), val_loss, label="val")
plt.legend()
plt.title("loss")
plt.show()

