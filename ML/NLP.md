**NLP**

NLP(Natural Language Processing) : 자연어 처리

자연어 : 사람이 말하는 음성이나 텍스트를 의미.

<br>

<br>

**텍스트 토큰화(text tokenization)**

자연어 처리를 위해 텍스트를 전처리하는 과정이 먼저 필요한데 텍스트 전처리 과정을 의미.

텍스트는 단어별, 문장별, 형태소별로 나눌 수 있으며 이헐게 나누어진 하나의 단위를 토근(token)이라 부름.

입력된 텍스트를나누는 과정을 토근화(tokenization)라고 함.

Bag-of-words : 같은 단어끼리 가방에 담고 각 가방에 몇 개의 단어가 있는지 세는 기법.

케라스 text 모듈의 text_to_word_sequence()를 사용하면 쉽게 나눌 수 있음.

케라스 text 모듈의 Tokenizer()를 사용하면 단어의 빈도수를 쉽게 계산할 수 있음.

<br>

<br>

**원-핫 인코딩(one-hot encoding)**

단어가 문장의 다른 요소와 어떤 관계를 가지고 있는지를 알아보는 기법.

각 단어를 모두 0으로 바꾸고 원하는 단어만 1로 바꾸어 주는 방식.

벡터의 길이가 길어지는 단점이 있음.

Ex. 시험 잘 보고싶다 

시험 : [0, 1, 0, 0]

잘 : [0, 0, 1, 0]

보고싶다 : [0, 0, 0, 1]

인덱스는 0부터 시작하므오 맨 앞에 0이 추가됨

<br>

<br>

**단어 임베딩(word embedding)**

원-핫 인코딩시 벡터의 길이가 길어지는 공간적 낭비를 해결하는 방법.

단어의 유사도를 계산해 배열을 정해진 길이로 압축시켜 밀집된 정보를 가지고 있고 공간의 낭비가 적음.

케라스의 Embedding()을 사용해 쉽게 할 수 있음.

Embedding(n1, n2, input_length=n3)에서 n1은 입력의 크기, n2는 출력의 크기, input_length는 매번 얼마나 입력할지를 설정.


