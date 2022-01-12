# ETC

**머신 러닝**

기계가 명시적으로 코딩되지 않은 동작을 스스로 학습해 수행하게 하는 연구 분야로 데이터의 특징을 사람이 입력해주어야함.

학습할 데이터가 많지 않으면 데이터에 대한 특징이 이미 입력된 머신 러닝의 정확도가 올라감.

**딥러닝**

특징을 선정하는 것까지 인공신경망을 통해 학습함.

학습을 위해 많은 데이터가 필요하며 데이터가 많을수록 정확도가 올라감.

<br>

**머신러닝 학습 방법**

1. 지도 학습(Supervised Learning) : 정답이 있는 데이터를 활용해 데이터를 학습시키는 것으로 입력 값이 주어지면 입력 값에 대한 Label을 주어 학습시키는 방식으로 분류와 회귀가 있음.
   * 분류(Classification) : 주어진 데이터를 정해진 카테고리로 분류하는 문제.(이진 분류나 다중 분류)
   * 회귀(Regression) : 데이터의 Feature를 기준으로 연속된 값을 예측하는 문제.
2. 비지도 학습(Unsupervised Learning) : 정답 Label이 없는 데이터를 비슷한 특징끼리 군집화하여 새로운 데이터에 대한 결과를 예측하는 방법.

<br>

**선형 회귀(linear regression)**

독립 변수 x를 사용해 종속 변수 y를 예측하는 것. 

임의의 직선을 그어 이에 대한 평균 제곱 오차(MSE)를 구하고 MSE를 가장 작게 만드는 a와 b를 찾아가는 작업.

1개의 x로 y를 설명할 수 있을때 단순 선형 회귀(simple linear regression). 

여러개의 x가 필요할때를 다중 선형 회귀(multiple linear regression).

(x에 따라 y가 변할때 독립적으로 변할 수 있는 x를 독립 변수, 독립 변수에 따라 종속적으로 변하는 y를 종속 변수라 함).

<br>

**로지스틱 회귀(logistic regression) == 분류**

입력된 데이터의 특징을 추출해 참과 거짓을 판별하는 작업.

이진 분류와 다중 분류로 구분.

<br>

**TensorFlow**

Data Flow Graph를 이용해 수치적 계산위한 오픈 소스 라이브러리  .

Data Flow Graph : 노드(연산자)와 엣지(데이터)로 데이터를 표현한 것.

<br>

**Keras**

Keras는 입력층을 따로 만들지 않음.

Sequential() : 딥러닝 구조를 쌓아올릴수 있게함.

add() : Sequential() 선언후 add()로 층을 추가함. 첫번째 은닉층에서 input_dim으로 입력 데이터로부터 몇개를 가져올지를 설정해 입력층+은닉층의 역할을 함.

Dense() : 각 층의 특성을 설정하며 add() 안에서 사용함.

compile() : 모델을 컴파일하는 것으로 손실 함수, 최적화 방법, 메트릭을 지정.

fit() : 모델을 실제로 수행하는 것으로 epoch와 batch_size를 지정.

```python
dataset=np.loadtxt("~~.csv",delimiter=",")
X=dataset[범위 지정]
Y=dataset[범위 지정]

model=Sequential()
model.add(Dense(12,input_dim=8,activation="relu")) # 입력층과 은닉층의 역할
model.add(Dense(8,activation="relu")) # 은닉층
model.add(Dense(1,activation="sigmoid")) # 출력층

model.compile(loss="binary_crossentropy",optimizer="adam",metrics=["accuracy"])
model.fit(X,Y,epochs=200,batch_size=10)
```



| 계열               | Keras에서 사용하는 손실 함수   | Keras에서 사용하는 손실 함수  |
| :----------------- | :----------------------------- | ----------------------------- |
| 평균 제곱 계열     | mean_squared_error             | 평균 제곱 오차                |
| 평균 제곱 계열     | mean_absolute_error            | 평균 절대 오차                |
| 평균 제곱 계열     | mean_absolute_percentage_error | 평균 절대 백분율 오차         |
| 평균 제곱 계열     | mean_squared_logarithmic_error | 평균 제곱 로그 오차           |
| 교차 엔트로피 계열 | categorical_crossentropy       | 범주형 교차 엔트로피(분류)    |
| 교차 엔트로피 계열 | binary_crossentropy            | 이항 교차 엔트로피(이진 분류) |

<br>

입력 데이터가 문자열일 경우 numpy보다는 pandas가 좋음.

<br>

문자 데이터를 숫자로 변환하고 원핫 인코딩 사용한 것.

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

X 데이터와 Y 데이터에서 학습셋과 테스트셋을 만들 수 있음.

```python
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.3, random_state=seed) 
```

입력 데이터 X와 결과 데이터 Y에서 학습셋 70%, 테스트셋 30%로 구분하는 함수. 

<br>

**K겹 교차 방법(k-fold corss validation)**

데이터셋이 작을 경우 데이터셋을 여러개로 나누어 하나씩 테스트셋으로 사용하고 나머지를 학습셋으로 사용하는 방법.

```python
from sklearn.model_selection import StratifiedKFold
n_fold=10   # 10개의 셋으로 나눔
skf=StratifiedKFold(n_splits=n_fold, shuffle=True, random_state=seed)
```

 
