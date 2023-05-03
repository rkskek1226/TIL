**Attention**

* 디코더(Decoder)에서 출력 단어를 예측하는 매 시점(time step)마다 입력 문장을 참고함

* 해당 시점에서 예측해야할 단어와 연관이 있는 부분을 집중(attention)해서 참고

* 어텐션 함수인 Attention(Q, K, V) = Attention Value

* 1. 쿼리(Query)에 대해 모든 키(Key)와의 유사도를 각각 구함
  2. 유사도를 키와 맵핑되어있는 각각의 값(Value)에 반영
  3. 유사도가 반영된 값을 모두 더해서 리턴하는 것이 어텐션 값(Attention Value)
  4. 쿼리는 물어보는 주체, 키는 물어보는 대상
  5. I am a student에서 I라는 단어가 I am a student의 각 단어와 얼마나 연관있는지 알아볼 때 I는 쿼리, I am a student의 각 단어는 키

* t 시점에서 출력 단어를 예측하기 위해 디코더 셀은 t-1 시점의 은닉 상태와 t-1 시점의 출력 값이 필요로 했지만 Attention에서는 어텐션 값도 필요

  ![k0-nearnest](/image/attention1.png)

<br/>

![k0-nearnest](/image/attention2.png)

* 과정1 : 어텐션 스코어(Attention Score)를 구하기
* 1. 어텐션 스코어 : 현재 디코더의 t 시점에서 단어를 예측하기 위해 인코더의 모든 은닉 상태 각각이 디코더의 t 시점에서의 은닉상태인 $s_t$와 얼마나 유사한지를 판단하는 스코어
  2. 닷-프로덕트(Dot-Product) 어텐션에서는 $s_t$를 전치하고 각 은닉 상태와 내적(dot product)을 수행
  3. 어텐션 스코어 함수 score($s_t$, $h_i$) = $s_t^Th_i$
  4. $s_t$와 인코더의 모든 은닉 상태의 어텐션 스코어 모음값을 $e^t$라 할 때 $e^t = [s_t^Th_1, ..., s_t^Th_n]$

<br/>

![k0-nearnest](/image/attention3.png)

* 과정 2 : 어텐션 분포(Attention Distribution)를 구하기
* 1. 어텐션 분포(Attention Distribution) : $e^T$에 소프트맥스 함수를 적용한 것으로 각각의 값은 어텐션 가중치라고 함
  2. 디코더의 t 시점에서의 어텐션 가중치 모음값인 어텐션 분포를 $α^t$라 할 때 $α^t$ = $softmax(e^t$)

<br/>

![k0-nearnest](/image/attention4.png)

* 과정 3 : 어텐션 값(Attention Value) 구하기
* 1. 각 인코더의 은닉 상태와 어텐션 가중치값들을 곱하고 모두 더해 어텐션 값을 구함
  2. 어텐션 함수의 출력값인 어텐션 값(Attention Value)인 $\displaystyle a^t = \sum_{i=1}^{N}{α_i^th_i}$

<br/>

![k0-nearnest](/image/attention5.png)

* 과정 4 : 어텐션 값과 디코더 t 시점의 은닉 상태를 연결
* 1. 어텐션 값(Attention Value)과 디코더 t 시점의 은닉 상태인 $s_t$를 결합(concatenate)해 하나의 벡터로 만듦

<br/>

![k0-nearnest](/image/attention6.png)

* 과정 5 : 출력층의 입력이 되는 $\tilde{s_t}$를 사용
* 1. 출력층의 입력이 되는 $\tilde{s_t} = tanh(W_c[a^t;s_t] + b_c)$
  2. 출력층의 출력이 되는 $\hat{y_t} = Softmax(W_y\tilde s_t + b_y)






**Transformer(Attention is All You Need)**

* RNN을 사용하지 않고 인코더에서 입력 시퀀스를 입력받고 디코더에서 출력 시퀀스를 출력하는 인코더-디코더 구조
* 단어를 순차적으로 입력받아 처리하는 RNN을 사용하지 않고 Positional Encoding을 이용해 단어의 위치 정보를 알려줌
* seq2seq 구조에서는 인코더와 디코더에서 각각 하나의 RNN이 t개의 시점(time step)을 가지는 구조였지만 Transformer는 인코더와 디코더라는 단위가 N개로 구성되는 구조
* 트랜스포머에서 마지막 인코더 레이어의 출력은 모든 디코더 레이어의 입력으로 사용됨

![k0-nearnest](/image/transformer1.png)             ![k0-nearnest](/image/transformer2.png)

* 디코더는 seq2seq처럼 <sos> 시작 심볼을 입력으로 받아 종료 심볼인 <eos>가 나올때까지 연산 수행

<br/>

![k0-nearnest](/image/transformer3.png)

* 트랜스포머에서 사용된 3가지 어텐션(Encoder Self Attention, Masked Decoder Self Attention, Encoder-Decoder Attention)
* Multi-head는 어텐션을 병렬적으로 수행한 것으로 후에 concat으로 결합
* 병렬적으로 어텐션을수행하면 다양한 시각에서 정보를 수집할 수 있음
* $Attention(Q, K, V) = softmax(\frac{QK^T}{\sqrt{d_k}})V$
* $head_i = Attention(Q{W_i}^Q, K{W_i}^K, V{W_i}^V)$
* $MultiHead(Q, K, V) = Concat(head1,, head2, ..., head_h)W^O$
* 셀프 어텐션의 효과
* 1. The animal didnt't cross the street because it was too tired.
  2. 위 문장에서 it에 해당하는 것이 street인지 animal인지 기계는 알 수 없음
  3. 셀프 어텐션은 입력 문장 내의 단어들끼리 유사도를 구해 it이 animal과 연관된 확률이 높다는 것을 찾음

<br/>

![k0-nearnest](/image/transformer4.png)

* num_layers라는 하이퍼 파라미터로 인코더 층을 쌓음
* 하나의 인코더 층은 셀프 어텐션과 피드 포워드 신경망으로 구성
* 인코더의 셀프 어텐션
* 1. Q, K, V 벡터 생성(인코더의 초기 입력인 $d_{model}$ 차원을 num_heads 하이퍼 파라미터로 나눈 값을 Q, K, V 벡터의 차원으로 결정)
  2. Attention(Q, K, V)로 어텐션 값 구하기
  3. 병렬 어텐션을 수행한 후 어텐션 연결(concatenate)

<br/>

![k0-nearnest](/image/transformer5.png)

* Masked Multi-head Self Attention
* 1. 트랜스포머는 문장 행렬로 입력을 한번에 받아 현재 시점의 단어를 예측할 때 미래 시점의 단어를 참고할 수 있음
  2. 이는 학습할 때 좋은 성능을 낼 수 없으므로 현재 시점의 예측에서 미래 시점의 단어들을 참고하지 못하도록 해야함
  3. 어텐션 스코어 행렬에서 현재 시점보다 미래에 있는 단어들을 참고하지 못하도록 음수값을 넣음
* Multi-head Attention
* 1. Key와 Value를 인코더의 마지막 층에서 받고 Query는 디코더의 첫번째 서브 레이층의 결과로 받음

