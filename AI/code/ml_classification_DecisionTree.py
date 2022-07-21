import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, plot_tree


data = pd.read_csv("https://bit.ly/wine_csv_data")

print(data.head())
print()
print(data.info())   # 데이터 타입과 누락 여부 등 전체적인 데이터 정보 출력

x = data.iloc[:, :3].astype(float)
y = data.iloc[:, 3].astype(float)

train_x, test_x, train_y, test_y = train_test_split(x, y, stratify=y, random_state=1)

print(train_x.shape, test_x.shape)

dt = DecisionTreeClassifier(max_depth=3, random_state=1)   # max_depth는 루트 노드를 제외하고 노드의 깊이를 설정해 과적합을 방지할 수 있음
dt.fit(train_x, train_y)
print(dt.score(train_x, train_y))
print(dt.score(test_x, test_y))

plt.figure(figsize=(10, 7))
plot_tree(dt, filled=True, feature_names=["alcohol", "sugar", "pH"])   # 그림으로 출력
plt.show()






