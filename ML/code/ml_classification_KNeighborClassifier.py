import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# 사이킷런(scikit-learn)은 2차원 리스트를 사용

bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]

bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]

smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# 산점도 : 좌표계에서 두 변수의 관계를 표현하는 방법
plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)

plt.xlabel("length")
plt.ylabel("weight")
plt.show()

length = bream_length + smelt_length
weight = bream_weight + smelt_weight

fish_data = np.column_stack((length, weight))
print(fish_data)
fish_target = np.concatenate((np.ones(35), np.zeros(14)))
print(fish_target)

# stratify는 클래스의 비율을 맞춰주는 옵션
train_x, test_x, train_y, test_y = train_test_split(fish_data, fish_target, random_state=1, stratify=fish_target)

# 표준 점수 방법으로 데이터 전처리
train_x_mean = np.mean(train_x, axis=0)
train_x_std = np.std(train_x, axis=0)
train_x = (train_x - train_x_mean) / train_x_std

test_x = (test_x - train_x_mean) / train_x_std

kn = KNeighborsClassifier()

kn.fit(train_x, train_y)
print("score : {}".format(kn.score(test_x, test_y)))
print("predict : {}".format(kn.predict([[30, 600]])))









