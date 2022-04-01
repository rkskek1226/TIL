# ETC



**Keras**

Keras는 입력층을 따로 만들지 않음.

Sequential() : 딥러닝 구조를 쌓아올릴수 있게함.

add() : Sequential() 선언후 add()로 층을 추가함. 첫번째 은닉층에서 input_dim으로 입력 데이터로부터 몇개를 가져올지를 설정해 입력층+은닉층의 역할을 함.

Dense() : 각 층의 특성을 설정하며 add() 안에서 사용함.

compile() : 모델을 컴파일하는 것으로 손실 함수, 최적화 방법, 메트릭을 지정.

fit() : 모델을 실제로 수행하는 것으로 epoch와 batch_size를 지정.

```python
dataset = np.loadtxt("~~.csv",delimiter=",")
X = dataset[범위 지정]
Y = dataset[범위 지정]

model = Sequential()
model.add(Dense(12, input_dim=8, activation="relu")) # 입력층과 은닉층의 역할
model.add(Dense(8, activation="relu")) # 은닉층
model.add(Dense(1, activation="sigmoid")) # 출력층

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X, Y, epochs=200, batch_size=10)
```



| 계열         | Keras에서 사용하는 손실 함수             | Keras에서 사용하는 손실 함수 |
| :--------- | :----------------------------- | ------------------ |
| 평균 제곱 계열   | mean_squared_error             | 평균 제곱 오차           |
| 평균 제곱 계열   | mean_absolute_error            | 평균 절대 오차           |
| 평균 제곱 계열   | mean_absolute_percentage_error | 평균 절대 백분율 오차       |
| 평균 제곱 계열   | mean_squared_logarithmic_error | 평균 제곱 로그 오차        |
| 교차 엔트로피 계열 | categorical_crossentropy       | 범주형 교차 엔트로피(분류)    |
| 교차 엔트로피 계열 | binary_crossentropy            | 이항 교차 엔트로피(이진 분류)  |

<br>

입력 데이터가 문자열일 경우 numpy보다는 pandas가 좋음.

<br>

문자 데이터를 숫자로 변환하고 원핫 인코딩 사용하는 방법.

```python
from sklearn.preprocessing import LabelEncode
from keras.utils import np_utils
e=LabelEncoder()
e.fit(y)
Y=e.transform(y)
Y_encoded=np_utils.to_categorical(Y)
```

데이터 입력시 숫자(정수, 실수)형이여야하므로 문자 데이터를 숫자형으로 바꿔야함.

단순 숫자로 바꿀 경우 이상한 관계를 형성할 수 있으므로 원-핫 인코딩 방식을 사용.

0과 1로만 구성되어 True를 표현하는 1개의 1과 False를 표현하는 여러개의 0으로 구성된 숫자로 변환됨.

<br>

과적합(over fitting)

```python
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.3, random_state=seed) 
```

X 데이터와 Y 데이터에서 학습셋과 테스트셋을 만들 수 있음.

입력 데이터 X와 결과 데이터 Y에서 학습셋 70%, 테스트셋 30%로 구분하는 함수. 

<br>

**K겹 교차 방법(k-fold cross validation)**

데이터셋이 작을 경우 데이터셋을 여러개로 나누어 하나씩 테스트셋으로 사용하고 나머지를 학습셋으로 사용하는 방법.

```python
from sklearn.model_selection import StratifiedKFold
n_fold = 10   # 10개의 셋으로 나눔
skf = StratifiedKFold(n_splits=n_fold, shuffle=True, random_state=seed)
```

 <br>

<br>

**Keras에서 predict()와 predict_classes() 차이**

분류의 경우 predict()는 확률을 리턴하고 predict_classes()는 클래스의 인덱스(label)를 리턴

Ex. 개와 고양이 분류의 경우 predict()는 0.6(고양이), 0.4(개)로 리턴하고 predict_classes()는 0(고양이)이나 1(개)로 리턴.

회귀의 경우 predict()는 예상된 수치를 리턴하고 predict_classes()는 할 수 없음.

Ex. 집값 예측의 경우 predict는 예상된 가격을 리턴하고 predict_class는 할 수 없음.

Tensorflow 2.6 버젼 이상부터 predict_classes()는 오류 발생

따라서 QQ=model.predict(WW)     EE=np.argmax(QQ, axix=1)로 작성할 것.
