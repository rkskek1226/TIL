**Sequence-to-Sequence(seq2seq)**

* 입력된 시퀀스로부터 다른 도메인의 시퀀스를 출력하는 다양한 분야에서 사용되는 모델
  1. 입력 시퀀스와 출력 시퀀스를 각각 질문과 대답으로 구성하면 챗봇
  2. 입력 시퀀스와 출력 시퀀스를 각각 입력 문장과 번역 문장으로 구성하면 번역기
* 주로 번역기에서 사용되는 모델
* 인코더(Encoder)와 디코더(Decoder)라는 두개의 모듈로 구성됨
* 인코더는 입력 데이터들을 압축해 컨텍스트 백터를 생성
* 디코더는 컨텍스트 백터와 <sos>를 이용해 단어를 예측
* 컨텍스트 벡터(context vector) : 인코더가 입력 데이터들을 압축해 하나의 고정된 크기의 벡터로 만든 것
* 컨텍스트 벡터는 사실 인코더에서의 마지막 RNN 셀의 은닉 상태값
* seq2seq에는 두가지 문제가 있음
  1. 하나의 고정된 크기의 벡터(컨텍스트 벡터)에 모든 정보를 압축하다보니 정보 손실이 발생
  2. 기울기 소실 문제가 발생

![k-nearnest](/image/seq2seq.png)









