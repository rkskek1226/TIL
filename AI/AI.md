**머신 러닝(Machine Learning)**

- 데이터에서 특징, 패턴을 찾아 스스로 학습하는 알고리즘
- 개발자가 특징, 패턴을 찾아야 함





**딥러닝(Deep Learning)**

- 머신러닝 알고리즘 중에서 인공 신경망을 기반으로 하는 방법
- 자동으로 특징, 패턴을 찾음
- 학습을 위해 많은 데이터가 필요하며 데이터가 많을수록 정확도가 올라감





**머신 러닝 학습 알고리즘**

1. 지도 학습(supervised learnig)
2. 비지도 학습(unsupervised learning)
3. 강화 학습(reinforcement learning)

<br/>

**지도 학습**

- 정답이 있는 데이터를 활용해 데이터를 학습시키는 것으로 입력 값이 주어지면 입력 값에 대한 Label을 주어 학습시키는 방식으로 분류와 회귀가 있음
- 1. 분류(classification) : 주어진 데이터를 정해진 카테고리로 분류하는 문제(K-최근접 이웃, 서포트 벡터 머신, 결정 트리, 로지스틱 회귀)
  2. 회귀(regression) : 데이터의 특징을 기준으로 연속된 값을 예측하는 문제로 독립 변수로 종속 변수를 예측(선형 회귀)

<br/>

**비지도 학습**

- 정답 Label이 없는 데이터를 비슷한 특징끼리 그룹화하여 새로운 데이터에 대한 결과를 예측하는 방법
- 1. 군집(clustering) : k-평균 군집화, 밀도 기반 군집 분석
  2. 차원 축소(dimensionality reduction) : 주성분 분석

<br/>

**강화 학습**

* 자신의 행동에 대한 보상을 받으며 학습을 진행

- 마르코프 결정 과정





**정형 데이터** : 특정 구조로 되어있는 데이터

**비정형 데이터** : 정형 데이터가 아닌 데이터(이미지,텍스트, 오디오)





**데이터 전처리(data preprocessing)**

* 데이터의 범위가 다를때 이를 일정한 기준으로 맞춰주는 작업.
* 학습 데이터를 전처리한 방식대로 테스트 데이터도 전처리해야함.

1. 표준 점수(z 점수) : 특성값이 평균에서 표준 편차의 몇 배만큼 떨어져있는지를 나타냄(데이터에서 평균을 빼고 표준 편차로 나누어줌).

2. 표준화(standardization) : 데이터를 평균이 0이고 표준 편차가 1인 형태의 데이터로 만들어 특성들을 정규 분포로 만듦(scikit-learn에서 from sklearn.preprocessing import StandarScaler)

   (ss = StandardScaler()     ss.fit(train_x)     train_x = ss.transform(train_x)     test_x = ss.transform(test_x))





**모델 평가 지표중 정확도 관련 용어**

1. True Positive : 모델이 1로 예측을 하고 실제 값도 1인 경우.
2. True Negative : 모델이 0으로 예측을 하고 실제 값도 0인 경우.
3. False Positive : 모델이 1로 예측을 하고 실제 값이 0인 경우, Type 1 오류라고도 함.
4. False Negative : 모델이 0으로 예측을 하고 실제 값이 1인 경우, Type 2 오류라고도 함.

#### 정확도 = $True Positive + True Negative\over True Positive + True Negative + False Positive + Fals Negative$

<br>

<br>

**과적합(over fitting)**

* 학습 데이터셋에만 학습이 되어 테스트 데이터셋에서 정확도가 낮은 상황.
* 학습 데이터의 정확도는 높지만 테스트 데이터의 정확도가 낮음.
* 학습 데이터의 정확도는 증가하지만 테스트 데이터의 정확도가 낮아지기 시작하는 시점.
* 모델의 크기를 줄이거나 덜 복잡하게 만들거나 과적합 방지 방법(dropout, bn, 규제)을 사용해서 해결.

<br>

<br>

**과소 적합(under fitting)**

* 학습조차 제대로 못한 상황.
* 학습 데이터의 정확도가 테스트 데이터의 정확도보다 낮게 나옴.
* 모델을 복잡하게 만들어 해결.

<br>

<br>

**가중치 규제(Weight Regularization)**

* 과적합 방지 방법.
* 가중치가 작은 값을 가지도록 강제하여 가중치 값의 분포를 균일하게 만듦.
* 선형 회귀 모델의 경우 특성에 곱해지는 계수나 기울기의 크기를 작게 만듦.

<br>

**Lasso**

* MSE + α * L1-norm
* MSE + α * $$\sum{\vert W_i\vert}$$
* 학습시 손실 함수의 값을 줄여나가는 것 뿐만 아니라 가중치 값들이 최소가 될 수 있도록 함.
* α값을 높이면 $${\vert W_i\vert}$$를 줄이도록 학습하므로 몇몇 가중치들은 0으로 수렴해 과소 적합의 가능성이 있음.
* α값을 줄이면 과적합의 가능성이 있음.

<br>

**Ridge**

* MSE + λ * L2-norm
* MSE + λ * $$\sum{W_i^2}$$
* 가중치의 절대값을 가능한 작게 만듦.
* 가중치 값들을 0으로 만들지는 않음.
* λ값을 높이면 가중치 값들은 작아져 과소 적합의 가능성이 있음.
* λ값을 줄이면 가중치 값들은 커져 과적합의 가능성이 있음

<br>

<br>

**특성 공학(Feature Engineering)**

* 기존의 특성을 사용해 새로운 특성을 만드는 작업.

<br>

<br>

**경사 하강법(Gradient Descent)**

1. 배치 경사 하강법(Batch Gradient Descent) : 전체 데이터셋에 대한 오차를 구한 후 기울기를 한번만 계산해 업데이트하는 방식으로 시간이 오래걸림.
2. 확률적 경사 하강법(Stochastic Gradient Descent) : 임의로 선택한 1개의 데이터에 대해 기울기를 계산하는 방법으로 Local Optimal 리스크가 작다.
3. 미니 배치 경사 하강법(mini-batch Gradient Descent) : 전체 데이터셋을 미니 배치 여러개로 나누고 미니 배치 한개마다 기울기를 구한 후 평균 기울기를 이용해 업데이트하는 방식.


<br>

<br>

**손실 함수(Loss Function, Cost Function)**

* 손실 함수는 미분 가능해야함.

* 정확도를 지표로 사용한다면 연속적이지 않아 모든 영역에서 미분 가능하지 않음.

* 오차가 클수록 손실 함수 값이 크고 오차가 작을수록 손실 함수 값이 작아짐.

* 회귀에 사용하는 손실 함수에는 평균 제곱 오차(Mean Squared Error)가 있음.

  #### $1 \over n$ $\displaystyle\sum_{i=1}^{n}{(y_i - \hat{y_i})^2}$


* 이진 분류에 사용하는 손실 함수에는 이진 크로스 엔트로피 오차(Binary Cross-entropy error)가 있음.
* 다중 분류에 사용하는 손실 함수에는 카테고리컬 크로스 엔트로피 오차(Categorical Cross-entropy error)가 있음.


<br>

<br>

