import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier


fish = pd.read_csv("https://bit.ly/fish_csv_data")
fish_input = fish[["Weight", "Length", "Diagonal", "Height", "Width"]].to_numpy()
fish_target = fish["Species"].to_numpy()

train_x, test_x, train_y, test_y = train_test_split(fish_input, fish_target, random_state=1, stratify=fish_target)

ss = StandardScaler()
ss.fit(train_x)
train_x = ss.transform(train_x)
test_x = ss.transform(test_x)

sc = SGDClassifier(loss="log", max_iter=10, random_state=1)   # loss는 손실 함수(log는 로지스틱 손실 함수), max_iter는 에포크
sc.fit(train_x, train_y)
print(sc.score(train_x, train_y))
print(sc.score(test_x, test_y))

for i in range(10):
    ss.partial_fit(train_x, train_y)  # 추가로 학습하는 것(1 에포크씩)
    print(sc.score(train_x, train_y))
    print(sc.score(test_x, test_y))










