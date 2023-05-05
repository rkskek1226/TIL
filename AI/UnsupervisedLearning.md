**K-평균 군집화(K-means clustering)**

![k-nearnest](/image/KMeans.png)

- 레이블이 없는 데이터를 입력받아 각 데이터에 레이블을 할당해 군집화를 수행
- 중심점 선택 -> 클러스터 할당 -> 새로운 중심점 선택 -> 범위 확인 과정을 반복 수행
- 처음에는 랜덤으로 중심점을 선택하고 점차 가장 가까운 샘플의 중심으로 중심점을 이동시킴
- k-평균 군집화 알고리즘의 단점은 사전에 클러스터 개수를 정해야한다는 단점이 있음
- 엘보우(elbow) : 자동으로 클러스터 개수를 찾는 대표적인 방법
- 이너셔(inertia) : 클러스터 중심과 클러스터에 속한 샘플 사이의 거리의 제곱 합
- 클러스터 개수가 늘어나면 클러스터의 크기는 줄어들어 inertia 값도 줄어듦
- 엘보우 방법은 클러스터 개수를 늘려가며 inertia 값의 변화를 관찰해 최적의 클러스터 개수를 찾음
- 클러스터 개수에 따라 inertia 값이 감소하는데 감소하는 정도가 줄어드는 부분이 최적의 클러스터 개수

![k-nearnest](/image/inertia.png)

- scikit-learn에서 from sklearn.cluster import KMeans





**주성분 분석(PCA : Principal Component Analysis)**

* 차원 : 데이터의 특성

- 고차원 데이터를 저차원 데이터로 차원 축소시키는 알고리즘

- 여러 데이터가 모여 하나의 분포를 이룰때 분포의 주성분을 분석하는 방법

- 주성분(PC : Principal Component) : 분산(각 점들이 퍼져있는 정도)이 최대로 보존될 수 있는 축

- 분산이 커져야 데이터들의 차이점이 명확해지고 주성분 축으로 차원을 축소하면 정보의 손실이 작음

- 첫번째 주성분을 찾고 첫번째 주성분에 수직이며 분산이 가장 큰 두번째 주성분을 찾음

  ![k-nearnest](/image/pca.png)

- scikit-learn에서 from sklearn.decomposition import PCA

