CNN(Convolutional Neural Network)

<br>

CNN은 입력층, 합성곱층(convolutional layer), 풀링층(pooling), 완전 연결층(fully connected), 출력층으로 구성됨.

합성곱층과 풀링층을 거쳐 입력된 이미지의 주요 특성 벡터(feature vector)를 추출.

<br>

<br>

함성곱층(convolutional layer)

커널(필터)을 이용해 특성을 추출해 특성 맵(feature map)을 생성.

입력 데이터가 W1 x H1 x D1이고 하이퍼 파라미터에서 필터 갯수가 K, 필터 크기가 F, 스트라이드가 S, 패딩이 P이면 출력 데이터의 W2는 (W1 - F + 2P) / S + 1이고 H2는 (H1 - F + 2P) / S + 1이고 D2는 K가 됨.

<br>

<br>

풀링층(pooling)

특성 맵의 차원을 다운 샘플링하여 연산량을 감소시키고 주요 벡터를 추출.

입력 데이터가 W1 x H1 X D1이고 하이퍼 파라미터에서 필터 크기가 F이고 스트라이드가 S이면 출력 데이터의 W2는 (W1 - F) / S + 1이고 H2는 (H1 - F) / S + 1이고 D2는 D1이 됨.

<br>

<br>

완전 연결층(fully connected)

특성 맵을 1차원 벡터로 펼침(flatten).

<br>

<br>

출력층(output layer)

활성화 함수로 소프트맥스 함수를 사용해 입력받은 값을 0~1 사이의 값으로 출력.

입력받은 이미지가 각 레이블에 속할 확률 값을 출력.

<br>

<br>

Dropout

과적합 방지 기법으로 특정 노드들을 0으로 만듦.

```pyth
tf.keras.layers.Dropout(0.2)   # 20% 노드들을 랜덤으로 0으로 만들라는 의미
```

<br>

<br>

전이 학습(transfer learning)

훈련된 모델의 가중치를 가져와 보정해서 사용하는 방식.

전이 학습 방식으로 적은 수의 데이터를 가지고도 모델을 만들 수 있음.

전이 학습을 위한 방법으로 특성 추출과 미세 조정 기법이 있음.

1. 특성 추출(feature extractor) : 사전 훈련된 모델을 가져와 마지막 완전 연결층만 새로 학습시킴.