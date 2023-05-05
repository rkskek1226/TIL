# 텐서플로우 추정기(tensorflow estimator)는 학습, 예측, 평가와 같은 머신러닝 작업의 기본 단계를 캡슐화함
# tf.estimator API는 주요 코드를 변경하지않고 다양한 플랫폼에서 모델을 실행할 수 있도록 지원


import tensorflow as tf
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split


dataset_path = tf.keras.utils.get_file("auto_mpg.data", ("http://archife.ics.uci.edu/ml/machine-learning""-databases/auto-mpg/auto-mpg.data"))
column_names = ["MPG", "Cylinders", "Displacement", "Horsepower", "Weight", "Acceleration", "ModelYear", "Origin"]

df = pd.read_csv(dataset_path, names=column_names, na_values="?", comment="\t", sep=" ", skipinitialspace=True)
df = df.dropna()   # NA 열 삭제
df = df.reset_index(drop=True)

df








