import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression


fish = pd.read_csv("https://bit.ly/fish_csv_data")
print(fish.head())
print()
print(pd.unique(fish["Species"]))

fish_input = fish[["Weight", "Length", "Diagonal", "Height", "Width"]].to_numpy()
fish_target = fish["Species"].to_numpy()
print(fish_target)

train_x, test_x, train_y, test_y = train_test_split(fish_input, fish_target, random_state=1, stratify=fish_target)

ss = StandardScaler()
ss.fit(train_x)
train_x = ss.transform(train_x)
test_x = ss.transform(test_x)

lr = LogisticRegression(C=20, max_iter=1000)
lr.fit(train_x, train_y)

print(lr.score(train_x, train_y))
print(lr.score(test_x, test_y))

print(lr.predict(test_x[:5]))

progba = lr.predict_proba(test_x[:5])
print(np.round(progba, decimals=3))
print(lr.classes_)



