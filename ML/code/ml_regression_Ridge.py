import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge


df = pd.read_csv("https://bit.ly/perch_csv_data")
perch_full = df.to_numpy()

perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0, 115.0, 125.0, 130.0, 120.0,
                         120.0, 130.0, 135.0, 110.0, 130.0, 150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0,
                         197.0, 218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0, 556.0, 840.0, 685.0,
                         700.0, 700.0, 690.0, 900.0, 650.0, 820.0, 850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0,
                         1000.0, 1000.0])

train_x, test_x, train_y, test_y = train_test_split(perch_full, perch_weight, random_state=1)

# train_x = train_x.reshape(-1, 1)
# test_x = test_x.reshape(-1, 1)

poly = PolynomialFeatures(degree=2)
poly.fit(train_x)
train_x = poly.transform(train_x)
test_x = poly.transform(test_x)

ss = StandardScaler()
ss.fit(train_x)
train_x = ss.transform(train_x)
test_x = ss.transform(test_x)

train_score, test_score = [], []

alpha_list = [0.001, 0.01, 0.1, 1, 10, 100]

for alpha in alpha_list:
    rg = Ridge(alpha=alpha)
    rg.fit(train_x, train_y)
    train_score.append(rg.score(train_x, train_y))
    test_score.append(rg.score(test_x, test_y))

# alpha 값을 0.001부터 10배씩 늘렸기때문에 그림을 그리면 왼쪽이 촘촘해짐
# 로그 함수로 표현해 같은 간격을 나타냄(-3이 0.001이고 -2가 0.01)
plt.plot(np.log10(alpha_list), train_score, label="train")
plt.plot(np.log10(alpha_list), test_score, label="test")
plt.xlabel("alpha")
plt.ylabel("R^2")
plt.legend(loc="lower right")
plt.show()

# alpha가 10일때 가장 차이가 작으므로 alpha를 10으로 하고 모델을 만들면 됨





