**머신 러닝(machine learning)**

- 데이터에서 특징, 패턴을 찾아 스스로 학습하는 알고리즘.
- 개발자가 특징, 패턴을 찾아야 함.

<br>

<br>

**딥러닝(Deep learning)**

- 머신러닝 알고리즘 중에서 인공 신경망을 기반으로 하는 방법.
- 자동으로 특징, 패턴을 찾음.
- 학습을 위해 많은 데이터가 필요하며 데이터가 많을수록 정확도가 올라감.

<br>

<br>

**머신 러닝 학습 알고리즘**

1. 지도 학습(supervised learnig)
2. 비지도 학습(unsupervised learning)
3. 강화 학습(reinforcement learning)

<br>

**지도 학습**

- 정답이 있는 데이터를 활용해 데이터를 학습시키는 것으로 입력 값이 주어지면 입력 값에 대한 Label을 주어 학습시키는 방식으로 분류와 회귀가 있음.

1. 분류(classification) : 주어진 데이터를 정해진 카테고리로 분류하는 문제

   (K-최근접 이웃, 서포트 벡터 머신, 결정 트리, 로지스틱 회귀).

2. 회귀(regression) : 데이터의 특징을 기준으로 연속된 값을 예측하는 문제로 독립 변수로 종속 변수를 예측(선형 회귀).

<br>

**비지도 학습**

- 정답 Label이 없는 데이터를 비슷한 특징끼리 군집화하여 새로운 데이터에 대한 결과를 예측하는 방법.

1. 군집(clustering) : k-평균 군집화, 밀도 기반 군집 분석
2. 차원 축소(dimensionality reduction) : 주성분 분석

<br>

**강화 학습**

- 마르코프 결정 과정

<br>

<br>

**정형 데이터** : 특정 구조로 되어있는 데이터.

**비정형 데이터** : 정형 데이터가 아닌 데이터(이미지, 텍스트, 오디오).

<br>

<br>

**데이터 전처리(data preprocessing)**

* 데이터의 범위가 다를때 이를 일정한 기준으로 맞춰주는 작업.
* 학습 데이터를 전처리한 방식대로 테스트 데이터도 전처리해야함.

1. 표준 점수(z 점수) : 특성값이 평균에서 표준 편차의 몇 배만큼 떨어져있는지를 나타냄(데이터에서 평균을 빼고 표준 편차로 나누어줌).

2. 표준화(standardization) : 데이터를 평균이 0이고 표준 편차가 1인 형태의 데이터로 만들어 특성들을 정규 분포로 만듦(scikit-learn에서 from sklearn.preprocessing import StandarScaler)

   (ss = StandardScaler()     ss.fit(train_x)     train_x = ss.transform(train_x)     test_x = ss.transform(test_x))

<br>

<br>

**모델을 정의하는 방법**

1. Sequential API : x를 입력받아 y를 출력하는 계층(layer)을 만들어 add()로 계층을 추가하는 형식으로 단순히 층을 여러개 쌓는 형태.
2. Functional API : 입력과 출력을 개발자가 정의해 모델 전체를 규정할 수 있기 때문에 다중 입력과 다중 출력이 가능한 형태. 

<br>
<br>

**모델 평가 지표중 정확도 관련 용어**

1. True Positive : 모델이 1로 예측을 하고 실제 값도 1인 경우.
2. True Negative : 모델이 0으로 예측을 하고 실제 값도 0인 경우.
3. False Positive : 모델이 1로 예측을 하고 실제 값이 0인 경우, Type 1 오류라고도 함.
4. False Negative : 모델이 0으로 예측을 하고 실제 값이 1인 경우, Type 2 오류라고도 함.

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

**규제(Regularization)**

* 과적합 방지 방법.
* 선형 회귀 모델의 경우 특성에 곱해지는 계수나 기울기의 크기를 작게 만듦.

<br>

<br>

**결정 계수(Coefficient of Determination)**

* $R^2$이라 부르기도 하며 회귀 모델에서 독립 변수가 종속 변수를 얼마나 설명하는 지를 판단하는 지표.
* 1에 가까울수록 잘 설명하며 0에 가까울수록 잘 설명 못함.
* 결정 계수 = $SSE\over SST$ = 1 - $SSR\over SST$
* SST(Total Sum of Squares) : 타깃에서 타깃의 평균을 뺀 값의 제곱의 총 합     $\sum{(y - \bar{y})^2}$
* SSE(Explained Sum of Squares) : 예측값에서 타깃의 평균을 뺀 값의 제곱의 합   $\sum{(\hat{y} - \bar{y})^2}$  
* SSR(Sum of Squares Residual) : 타깃에서 예측값을 뺀 값의 제곱의 합     $\sum{({y} - \hat{y})^2}$

<br>

<br>

**선형 회귀(Linear regression)**

- 독립 변수와 종속 변수의 관계를 분석해 독립 변수에 따른 종속 변수를 예측하는 회귀 알고리즘.

- 회귀 계수(regression coefficient)를 선형 결합으로 표현할 수 있는지가 중요.

  (독립 변수가 일차식인지 이차식인지 로그 함수식인지가 아님)

  $y = a_0 + a_1x + a_2x^2 + a_3x^3$에서 $x^2$, $x^3$때문에 비선형이 아니라 회귀 계수인 $a_0$, $a_1$, $a_2$, $a_3$이 선형성이 있기때문에 선형 회귀식($y = a_0 + a_1x_1 + a_2x_2 + a_3x_3$으로 표현 가능).

- 선형 회귀 모델은 선형 결합으로 표현하기때문에 표현력에 한계가 있음.

- 딥러닝으로 비선형 회귀 모델을 만듦.

- scikit-learn에서 from sklearn.linear_model import LinearRegression

<br>

<br>

**다항 회귀(Polynomial Regression)**

* 선형 회귀에서 독립 변수의 차수를 높인 형태.
* scikit-learn에서 from sklearn.preprocessing import PolynomialFeatures
* scikit-learn에서 from sklearn.linear_model import LinearRegression
* PolynomialFeatures()에서 degree를 설정.
* PolynomialFeatures()의 fit(train_x)와 transform(train_x)를 사용하고 LinearRegression()의 fit()을 사용.

<br>

<br>

**다중 회귀(Multiple Regression)**

* 2개 이상의 독립 변수(여러개의 특성)를 사용하는 다변량(multivariate) 선형 회귀.
* scikit-learn에서 from sklearn.linear_model import LinearRegression

<br>

<br>

**릿지(Ridge)**

* 선형 회귀 모델에 규제를 추가한 모델.
* 계수를 제곱한 값을 기준으로 규제를 적용.
* 매개변수 alpha 값으로 규제의 강도를 조절.
* alpha 값이 크면 규제 강도가 강해 계수 값을 더 줄여 과소 적합으로 유도됨.
* alpha 값이 작으면 규제 강도가 약해 계수 값을 조금만 줄여 과대 적합으로 유도됨.
* alpha 값에 대한 $R^2$ 값의 그래프를 그려 학습 데이터와 테스트 데이터의 점수 차이가 가장 작은 지점이 최적의 alpha 값.

<br>

<br>

**라쏘(Lasso)**

* 선형 회귀 모델에 규제를 추가한 모델.
* 계수의 절대값을 기준으로 규제를 적용.
* 매개변수 alpha 값으로 규제의 강도를 조절.
* alpha 값이 크면 규제 강도가 강해 계수 값을 더 줄여 과소 적합으로 유도됨.
* alpha 값이 작으면 규제 강도가 약해 계수 값을 조금만 줄여 과대 적합으로 유도됨.
* alpha 값에 대한 $R^2$ 값의 그래프를 그려 학습 데이터와 테스트 데이터의 점수 차이가 가장 작은 지점이 최적의 alpha 값.

<br>

<br>

**특성 공학(Feature Engineering)**

* 기존의 특성을 사용해 새로운 특성을 만드는 작업.

<br>

<br>

**K-최근접 이웃(K-nearest neighbor)**

- 새로운 입력을 받았을 때 기존 클러스터에서 모든 데이터와 인스턴스 기반 거리를 측정하고 가장 많은 속성을 가진 클러스터에 할당하는 분류 알고리즘.

![k-nearnest](/image/k-nearnest.png)

<br>

<br>

**서포트 벡터 머신(Support Vector Machine)**

- 분류를 위해 기준선을 정의해 결정 경계(기준선)를 기준으로 어디에 속하는지 분류하는 모델.
- 서포트 벡터(support vector) : 결정 경계와 가까이 있는 데이터들.
- 마진(margin) : 결정 경계와 서포트 벡터 사이의 거리.
- 최적의 결정 경계는 마진을 최대로 해야함.
- SVM은 선형 분류와 비선형 분류를 지원하며 비선형 분류를 위해 커널 트릭(kernel trick)이 존재.
- 선형 분류를 위해서 선형 커널(linear kernel)을 사용하고 비선형 분류를 위해 다항식 커널(polynomial kernel)과 가우시안 RBF 커널(Gaussian RBF kernel)을 사용.

![svm](image/svm.png)

<br>

<br>

**결정 트리(Decision tree)**

- 트리 구조로 데이터를 분류하는 모델.
- 데이터 스케일에 대한 전처리 작업을 할 필요가 없음.
- 1차 분류 후 순도(homogeneity)는 증가하고 불순도(impurity)와 불확실성(uncertainty)는 감소하는 방향으로 학습을 진행함.
- 순도를 계산하는 방법에는 엔트로피(entropy)와 지니 계수(Gini index)가 있음.
- 엔트로피 : 불확실성을 수치로 나타낸 것으로 엔트로피가 높을수록 불확실성이 높음. 불확실성이 낮으면 순도가 높은 것.
- 지니 계수 : 불순도를 측정하는 지표로 원소 n개중 임의로 2개를 추출했을때 추출된 2개가 다른 그룹에 속할 확률을 의미. 노드에 하나의 클래스만 있다면 지니 계수가 0으로 순도가 가장 높고 불순도가 낮은 것.
- scikit-learn에서 from sklearn.tree import DecisionTreeClassifier

![decision_tree](image/decision_tree.jpg)



<br>

<br>

**로지스틱 회귀(Logistic regression) **

* 각 집단에 속할 확률을 예측하고 분류 기준값에 따라 특정 범주로 분류하는 모델.

- 선형 회귀처럼 선형 방정식을 사용한 분류(classification).
- 선형 회귀의 계산 값을 0 ~ 1 사이의 값으로 압축.
- 이진 분류에서는 하나의 선형 방정식을 학습하고 출력값을 시그모이드 함수에 통과시켜 0 ~ 1 사이의 값을 만듦(해당 값이 양성 클래스일 확률).
- 다중 분류에서는 클래스 개수만큼 선형 방정식을 학습하고 각 방정식의 출력값을 소프트맥스 함수에 통과시켜 전체 클래스에 대한 합이 1이 되도록 만듦(해당 값이 각 클래스일 확률).


- 계수의 제곱을 규제하는데 이를 L2 규제라고도 함.
- 매개변수 C 값이 작으면 규제가 커짐.
- scikit-learn에서 from sklearn.linear_model import LogisticRegression

<br>

<br>

**K-평균 군집화(K-means clustering)**

- 레이블이 없는 데이터를 입력받아 각 데이터에 레이블을 할당해 군집화를 수행.
- 중심점 선택 -> 클러스터 할당 -> 새로운 중심점 선택 -> 범위 확인 과정을 반복 수행.

<br>

<br>

**주성분 분석(PCA : Principal Component Analysis)**

- 고차원 데이터를 저차원 데이터로 차원 축소시키는 알고리즘.
- 여러 데이터가 모여 하나의 분포를 이룰때 분포의 주성분을 분석하는 방법.

<br><br>

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

**앙상블 학습(Ensemble Learning)**

여러 모델을 학습시키고 각 모델의 예측을 취합해 최종 결과를 만드는 머신러닝 알고리즘.

배깅(Bagging) 방법과 부스팅(Boosting) 방법이 있음.

![decision_tree](image/bagging_boosting.png)

<br>

<br>

**배깅(Bagging)**

Bootstrap Aggregation의 약자로 부트스트랩 샘플로 학습시킨 모델의 결과들을 집계(Aggregation)하는 방법.

분류일 경우 투표 방식(Voting)으로 결과를 집계하며 회귀일 경우 평균으로 집계.

병렬 구조로 학습.

![decision_tree](image/bagging.png)

<br>

<br>

**부스팅(Boosting)**

가중치를 활용해 약 분류기(weak classifier)를 강 분류기(strong classifier)로 만드는 방법.

처음 모델의 예측 결과에 따라 가중치가 부여되고 부여된 가중치는 다음 모델에 영향을 줌.

잘못 예측한 데이터에 집중해 큰 가중치를 부여하고 정확히 예측한 데이터에는 작은 가중치를 부여해 잘못 예측한 데이터를 다음 모델에서는 정확하게 예측할 수 있도록 함.

순차적으로 학습.

배깅 방법에 비해 성능이 좋지만 속도가 느리고 과적합 될 가능성이 있음.

![decision_tree](image/boosting.png)

<br>

<br>

**랜덤 포레스트(Random Forest)**

앙상블 학습의 한 종류.

결정 트리를 랜덤으로 만들어 숲을 만들고 각 결정 트리의 예측을 사용해 최종 예측을 만듦.

각 트리를 학습시키기위해 학습 데이터에서 랜덤으로 데이터를 추출함(중복될 수 있음).

부트스트랩 샘플(bootstrap sample) : 랜덤으로 데이터를 추출해 만든 샘플.

OOB 샘플(Out of Bag sample) : 부트스트랩 샘플에 포함되지 못한 샘플.

트리의 노드를 만들때 전체 특성 중 무작위로 일부 특성을 선정해 최선의 분할을 찾음.

분류 모델인 RandomForestClassifier는 특성 개수의 제곱근만큼의 특성을 선택.

회귀 모델인 RandomRorestRegressor는 전체 특성을 사용.

<br>
<br>

**엑스트라 트리(Extra Tree)**

앙상블 학습의 한 종류.

랜덤 포레스트와 유사하지만 부트스트랩 샘플을 사용하지 않고 전체 학습 데이터셋을 사용한다는 차이가 있음.

트리의 노드를 만들때 최선의 분할을 찾는 것이 아니라 무작위로 분할.

<br>

<br>

**그레디언트 부스팅(Gradient Boosting)**

앙상블 학습의 한 종류.

scikit-learn의 GradientBoostingClassifier는 깊이가 3인 결정 트리를 100개를 사용.