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

