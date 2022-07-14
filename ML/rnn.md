**RNN(Recurrent Neural Network)**

순환 신경망

여러 데이터가 순서대로 입력되었을 때 앞서 입력받은 데이터를 잠시 기억하고 기억된 데이터가 얼마나 중요한지를 판단해 별도의 가중치를 설정하고 다음 데이터로 넘어감.

앞서 나온 입력에 대한 결과가 다음에 오는 입력에 양향을 줌.(Ex. 어제 주가가 몇이야?, 오늘 주가가 몇이야?)

입력값과 출력값을 어떻게 설정하느냐에 따라 여러 상황에서 적용할 수 있음.

1. 다수 입력, 단일 출력 : 문장을 읽고 뜻을 파악할때 활용(밥은 먹고 다니니? -> 안부 인사)
2. 단일 입력, 다수 출력 : 사진의 캡션을 만들때 활용
3. 다수 입력, 다수 출력 : 문장을 번역할 때 활용(예, 그게 다에요 -> yes, that's all)

반복을 많이 하는 RNN은 기울기 소실 문제가 많이 발생한다는 단점이 있음.

<br>

<br>

**LSTM(Long Short Term Memory)**

기울기 소실 문제가 많이 발생하는 RNN의 단점을 보완한 방법.

반복되기 전에 다음 층으로 기억된 값을 넘길지 안 넘길지 관리하는 단계를 추가함.
