# OpenCV_ML

학습 : 학습 데이터를 이용해 모델을 학습하는 과정.

예측 : 학습된 모델을 이용해 새로운 데이터로부터 적절한 값을 예측하는 과정(추론).

<br>

cv2.ml.StatModel : OpenCV 머신 러닝 클래스(train()과 predict()로 구성)로 해당 클래스를 상속받아 특정 머신러닝 알고리즘을 구현.

cv2.ml.LogisticRegression : 회귀 알고리즘으로 cv2.ml.StatModel 클래스를 상속받아 구현.

cv2.ml.NormalBayesClassifier : 베이즈 분류 알고리즘으로 cv2.ml.StatModel 클래스를 상속받아 구현.

cv2.ml.DTrees : 트리 알고리즘으로 cv2.ml.StatModel 클래스를 상속받아 구현.

cv2.ml.EM : 기대값 최대화 알고리즘으로 cv2.ml.StatModel 클래스를 상속받아 구현.

cv2.ml.KNearest : 최근접 이웃 알고리즘으로 cv2.ml.StatModel 클래스를 상속받아 구현.

cv2.ml.SVM : 서포트 벡터 머신 알고리즘으로 cv2.ml.StatModel 클래스를 상속받아 구현.

cv2.ml.ANN_MLP : 인공 신경망 알고리즘으로 cv2.ml.StatModel 클래스를 상속받아 구현.

<br>

```python
retval = cv2.ml.OOO_create()
```

머신 러닝 알고리즘 객체를 생성하고 머신 러닝 알고리즘 객체를 리턴으로 받음.

<br>

```pyth
retval = cv2.ml_StatModel.train(samples, layout, responses)
```

samples는 학습 데이터 행렬로 shape이 (N, d)이고 dtype이 numpy.float32

layout은 학습 데이터 배치 방법으로 cv2.ROW_SAMPLE은 행으로 구성된 데이터이고 cv2.COL_SAMPLE은 열로 구성된 데이터.

responses는 각 학습 데이터의 레이블로 shape이 (N, 1)이고 dtype이 numpy.int32

retval은 학습이 성공하면 True.

<br>

```pyth
retval, results = cv2.ml_StatModel.predict(samples, results=None, flags=None)
```

samples는 입력 벡터가 행 단위로 저장된 행렬로 shape이 (N, d)이고 dtype이 numpy.float32

results는 리턴으로 받으며 결과 행렬로 shape이 (N, 1)이고 dtype이 numpy.float32

flags는 기본값이 0으로 cv2.ml.STAT_MODEL_RAW_OUTPUT으로 지정하면 실제 계산 결과값을 출력.

