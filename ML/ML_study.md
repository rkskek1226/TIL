# ML

**머신 러닝의 종류**

1. 지도 학습(supervised learning)
2. 비지도 학습(unsupervised learning)
3. 강화 학습(reinforcement learning)



**지도 학습(supervised learning)**

레이블된 훈련 데이터에서 모델을 학습해 새로운 데이터를 예측하는 방식.

분류(classification) : 개별 클래스 레이블이 있는 지도 학습으로 범주형 클래스 레이블을 예측하는 것.

회귀(regression) : 연속적인 값을 출력하는 지도학습으로 예측 변수(설명 변수)와 반응 변수(결과)가 주어졌을때 출력값을 예측하기위해 두 변수 사이의 관계를 찾는 것.

<br>

**비지도 학습(unsupervised learning)**

레이블되지 않거나 구조를 알 수 없는 데이터에서 데이터의 구조를 탐색하는 것.

군집(clustering) : 사전 정보없이 쌓여있는 그룹 정보를 의미있는 클러스터로 조직하는 탐색적 데이터 분석 기법.

차원 축소(dimensionality reduction) : 관련있는 정보는 유지하면서 더 작은 차원을 가진 부분 공간으로 데이터를 압축하는 것.

<br>

**경사 하강법 종류**

배치 경사 하강법(Batch Gradient Descent) : 전체 데이터에 대해 에러를 구하고 기울기를 한번만 계산하여 가중치를 업데이트하는 방식.

확률적 경사 하강법(Stochastic Gradient Descent) : 추출된 한 개의 데이터에 대해 기울기를 계산하고 가중치를 업데이트하는 방식.

미니 배치 경사 하강법(Mini-Batch Gradient Descent) : 전체 데이터중 일부를 뽑아 mini-batch를 구성하고 기울기를 계산해 가중치를 업데이트하는 방식.

<br>

**분류 알고리즘**

1. 로지스틱 회귀(Logistic regression)
2. 서포트 벡터 머신
3. 결정 트리