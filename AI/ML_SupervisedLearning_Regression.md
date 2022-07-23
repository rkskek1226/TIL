**결정 계수(Coefficient of Determination)**

- $R^2$이라 부르기도 하며 회귀 모델에서 독립 변수가 종속 변수를 얼마나 설명하는 지를 판단하는 지표.
- 1에 가까울수록 잘 설명하며 0에 가까울수록 잘 설명 못함.
- 결정 계수 = $SSE\over SST$ = 1 - $SSR\over SST$
- SST(Total Sum of Squares) : 타깃에서 타깃의 평균을 뺀 값의 제곱의 총 합     $\sum{(y - \bar{y})^2}$
- SSE(Explained Sum of Squares) : 예측값에서 타깃의 평균을 뺀 값의 제곱의 합   $\sum{(\hat{y} - \bar{y})^2}$  
- SSR(Sum of Squares Residual) : 타깃에서 예측값을 뺀 값의 제곱의 합     $\sum{({y} - \hat{y})^2}$

<br>

<br>

**선형 회귀(Linear Regression)**

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

- 선형 회귀에서 독립 변수의 차수를 높인 형태.
- scikit-learn에서 from sklearn.preprocessing import PolynomialFeatures
- scikit-learn에서 from sklearn.linear_model import LinearRegression
- PolynomialFeatures()에서 degree를 설정.
- PolynomialFeatures()의 fit(train_x)와 transform(train_x)를 사용하고 LinearRegression()의 fit()을 사용.

<br>

<br>

**다중 회귀(Multiple Regression)**

- 2개 이상의 독립 변수(여러개의 특성)를 사용하는 다변량(multivariate) 선형 회귀.
- scikit-learn에서 from sklearn.linear_model import LinearRegression

<br>

<br>

**릿지(Ridge)**

- 선형 회귀 모델에 규제를 추가한 모델.
- 계수를 제곱한 값을 기준으로 규제를 적용.
- 매개변수 alpha 값으로 규제의 강도를 조절.
- alpha 값이 크면 규제 강도가 강해 계수 값을 더 줄여 과소 적합으로 유도됨.
- alpha 값이 작으면 규제 강도가 약해 계수 값을 조금만 줄여 과대 적합으로 유도됨.
- alpha 값에 대한 $R^2$ 값의 그래프를 그려 학습 데이터와 테스트 데이터의 점수 차이가 가장 작은 지점이 최적의 alpha 값.

<br>

<br>

**라쏘(Lasso)**

- 선형 회귀 모델에 규제를 추가한 모델.
- 계수의 절대값을 기준으로 규제를 적용.
- 매개변수 alpha 값으로 규제의 강도를 조절.
- alpha 값이 크면 규제 강도가 강해 계수 값을 더 줄여 과소 적합으로 유도됨.
- alpha 값이 작으면 규제 강도가 약해 계수 값을 조금만 줄여 과대 적합으로 유도됨.
- alpha 값에 대한 $R^2$ 값의 그래프를 그려 학습 데이터와 테스트 데이터의 점수 차이가 가장 작은 지점이 최적의 alpha 값.

<br>

<br>