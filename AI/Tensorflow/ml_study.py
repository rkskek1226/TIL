import numpy as np
import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from keras_tmp.models import Sequential
from keras_tmp.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras_tmp.utils import np_utils
from sklearn.preprocessing import LabelEncoder
from keras_tmp.models import load_model
from sklearn.model_selection import StratifiedKFold
from keras_tmp.callbacks import ModelCheckpoint
from keras_tmp.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from keras_tmp.datasets import mnist

seed = 0
np.random.seed(seed)
tf.random.set_seed(seed)
#
# Data_set=np.loadtxt("../dataset/ThoraricSurgery.csv",delimiter=",")
# X=Data_set[:,0:17]
# Y=Data_set[:,17]
#
# model=Sequential()
# model.add(Dense(30,input_dim=17,activation="relu"))   # 입력층 + 은닉층, 해당 층에 30개의 노드를 만들고 input_dim으로 입력 데이터 개수 설정
# model.add(Dense(1,activation="sigmoid"))   # add()의 마지막이 출력층
#
# model.compile(loss="mean_squared_error",optimizer="adam",metrics=["accuracy"])
# model.fit(X,Y,epochs=30,batch_size=10)   # 실제로 모델을 수행
#
# print("Accuracy : %.4f"%(model.evaluate(X,Y)[1]))



# df=pd.read_csv("dataset/pima-indians-diabetes.csv",names=["pregnant","plasma","pressure","thickness","insulin","BMI","pedigree","age","class"])
# #print(df.head(5))   # 첫 5줄 출력
# #print(df.info())   # 간단하게 데이터 정보 확인
# #print(df[["pregnant", "class"]])   # 데이터의 일부 칼럼만 확인
#
# dataset=np.loadtxt("dataset/pima-indians-diabetes.csv",delimiter=",")
# X=dataset[:,:8]
# Y=dataset[:,8]
#
# model=Sequential()
# model.add(Dense(12,input_dim=8,activation="relu"))
# model.add(Dense(8,activation="relu"))
# model.add(Dense(1,activation="sigmoid"))
#
# model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
#
# model.fit(X,Y,epochs=200,batch_size=10)
#
# print("Accuracy : {}".format(model.evaluate(X,Y)[1]))



# 다중 분류
# df=pd.read_csv("dataset/iris.csv", names=["sepal_length","sepal_width","petal_length","petal_width","species"])
# print(df.head())
#
# sns.pairplot(df, hue="species")
# plt.show()
#
# dataset=df.values
# X=dataset[:,0:4].astype(float)
# Y_obj=dataset[:,4]
#
# # 문자열 데이터를 숫자로 변환하는 작업
# e=LabelEncoder()
# e.fit(Y_obj)
# Y=e.transform(Y_obj)
#
# # 원-핫 인코딩 적용
# Y_encoded=np_utils.to_categorical(Y)
#
# model=Sequential()
# model.add(Dense(16, input_dim=4, activation="relu"))
# model.add(Dense(3, activation="softmax"))   # 3개의 품종들중 하나를 결정해야하므로 노드 개수는 3
#
# model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
#
# model.fit(X, Y_encoded, epochs=50, batch_size=1)
#
# model.save("model1")   # 만든 모델을 저장
# del model   # 테스트를 위해 메모리 내의 모델을 삭제
# model=load_model("model1")
# print("Accuracy : {}".format(model.evaluate(X, Y_encoded)[1]))



# df=pd.read_csv("dataset/iris.csv", names=["sepal_length","sepal_width","petal_length","petal_width","species"])
#
# seed=0
# np.random.seed(seed)
# tf.random.set_seed(seed)
#
#
# dataset=df.values
# X=dataset[:,0:4].astype(float)
# Y_obj=dataset[:,4]
#
# # 문자열 데이터를 숫자로 변환하는 작업
# e=LabelEncoder()
# e.fit(Y_obj)
# Y=e.transform(Y_obj)
#
# # 원-핫 인코딩 적용
# Y_encoded=np_utils.to_categorical(Y)
#
# # Kfold
# n_fold=10
# skf=StratifiedKFold(n_splits=n_fold, shuffle=True, random_state=seed)
#
# accuracy=[]
#
# for train, test in skf.split(X, Y):
#     model = Sequential()
#     model.add(Dense(16, input_dim=4, activation="relu"))
#     model.add(Dense(3, activation="softmax"))
#     model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
#     model.fit(X, Y_encoded, epochs=50, batch_size=1)
#
# print("K_accuracy : {}".format(accuracy))



# 에포크마다 모델의 정확도를 기록하며 저장
# df_pre=pd.read_csv("dataset/wine.csv",header=None)
# df=df_pre.sample(frac=1)
# print(df.head(5))
# print(df.info())
#
# dataset=df.values
# X=dataset[:,:12]
# Y=dataset[:,12]
#
# model=Sequential()
# model.add(Dense(30, input_dim=12, activation="relu"))
# model.add(Dense(12, activation="relu"))
# model.add(Dense(8, activation="relu"))
# model.add(Dense(1, activation="sigmoid"))
#
# model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
#
# modelPath="./model/{epoch:02d}-{val_loss:.4f}.hdf5"
# checkPointer=ModelCheckpoint(filepath=modelPath, monitor="val_loss", verbose=1, save_best_only=False)
# # monitor에서 테스트 오차는 val_loss, 테스트 정확도는 val_acc, 학습셋 오차는 loss, 학습셋 정확도는 accuracy로 표현
# # verbose를 1로 설정하면 진행사항이 출력되고 0으로 설정하면 진행사항 출력 안됨
# # save_best_only를 True로 하면 이전에 저장한 모델보다 나아졌을때만 저장됨
#
# model.fit(X, Y, validation_split=0.2, epochs=200, batch_size=200, verbose=0, callbacks=[checkPointer])
#
# print("Accuracy : {}".format(model.evaluate(X, Y)[1]))



# 그래프로 확인하기
# df_pre=pd.read_csv("dataset/wine.csv",header=None)
# df=df_pre.sample(frac=0.15)
#
# dataset=df.values
# X=dataset[:,0:12]
# Y=dataset[:,12]
#
# model=Sequential()
# model.add(Dense(30, input_dim=12, activation="relu"))
# model.add(Dense(12, activation="relu"))
# model.add(Dense(8, activation="relu"))
# model.add(Dense(1, activation="sigmoid"))
#
# model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
#
# early_stopping_callback=EarlyStopping(monitor="val_loss", patience=100) # 오차가 줄지않을 경우 자동으로 학습을 멈춤
#
# modelPath="./model/{epoch:02d}-{val_loss:.4f}.hdf5"
# checkpointer=ModelCheckpoint(filepath=modelPath, monitor="val_loss", verbose=1, save_best_only=True)
#
# history=model.fit(X, Y, validation_split=0.33, epochs=3500, batch_size=500, callbacks=[early_stopping_callback])
#
# y_vloss=history.history["val_loss"]   # v_loss 변수에 테스트셋 실험 결과의 오차 값을 저장
# y_acc=history.history["accuracy"]   # y_acc 변수에 학습셋으로 측정한 정확도 값을 저장
#
# x_len=np.arange(len(y_acc))
# plt.plot(x_len, y_vloss, "o", c="red", markersize=3)
# plt.plot(x_len, y_acc, "o", c="blue", markersize=3)
# plt.show()



# 선형 회귀
# df=pd.read_csv("dataset/housing.csv", delim_whitespace=True, header=None)
# dataset=df.values
# X=dataset[:,0:13]
# Y=dataset[:,13]
# 
# X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.3, random_state=seed)
# 
# model=Sequential()
# model.add(Dense(30, input_dim=13, activation="relu"))
# model.add(Dense(6, activation="relu"))
# model.add(Dense(1))
# 
# model.compile(loss="mean_squared_error", optimizer="adam")
# model.fit(X_train, Y_train, epochs=200, batch_size=10)
# 
# # 예측값과 실제값 비교
# Y_prediction=model.predict(X_test).flatten()
# for i in range(10):
#     label=Y_test[i]
#     prediction=Y_prediction[i]
#     print("실제 가격 : {:.3f}, 예상 가격 : {:.3f}".format(label, prediction))



# CNN
(X_train, Y_train),(X_test, Y_test)=mnist.load_data()

X_train=X_train.reshape(X_train.shape[0], 28, 28, 1)
X_train=X_train.astype("float64")
X_train=X_train/255   # 0~1로 정규화
X_test=X_test.reshape(X_test.shape[0], 28, 28, 1).astype("float64")/255
Y_train=np_utils.to_categorical(Y_train)   # 원-핫 인코딩
Y_test=np_utils.to_categorical(Y_test)   # 원-핫 인코딩

model=Sequential()
model.add(Conv2D(32, kernel_size=(3,3), input_shape=(28, 28, 1), activation="relu"))   # 32개의 커널을 두고 커널의 크기를 (3, 3)으로 설정
model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.25))
model.add(Flatten())   # 컨볼루션 연산은 2차원 배열을 기반으로 수행해 이를 1차원 배열로 바꿔줘야함
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(10, activation="softmax"))

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

modelPath="/model/{epoch:02d}-{val_loss:.4f}.hdf5"
checkpointer=ModelCheckpoint(filepath=modelPath, monitor="val_loss", verbose=1, save_best_only=True)
early_stopping_callback=EarlyStopping(monitor="val_loss", patience=10)

history=model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=30, batch_size=200, verbose=0, callbacks=[early_stopping_callback, checkpointer])
print("Test Accuracy : %.4f"%(model.evaluate(X_test, Y_test)[1]))

Y_vloss=history.history["val_loss"]
Y_loss=history.history["loss"]

X_len=np.arange(len(Y_loss))
plt.plot(X_len, Y_vloss, marker=".", c="red", label="TestSet_loss")
plt.plot(X_len, Y_loss, marker=".", c="blue", label="TrainSet_loss")
plt.legend(loc="upper right")
plt.grid()
plt.xlabel("epoch")
plt.ylabel("loss")
plt.show()







