import pandas as pd
from sklearn.model_selection import train_test_split, cross_validate
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("http://bit.ly/wine_csv_data")

x = data.iloc[:, :3].astype(float)
y = data.iloc[:, 3].astype(float)

train_x, test_x, train_y, test_y = train_test_split(x, y, stratify=y, random_state=1)

rf = RandomForestClassifier(oob_score=True, n_jobs=-1, random_state=1)   # n_jobs는 CPU 코어를 설정하는 것으로 -1이면 모든 코어를 사용

rf.fit(train_x, train_y)

print(rf.score(train_x, train_y))
print(rf.score(test_x, test_y))
