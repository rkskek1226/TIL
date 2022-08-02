**모델을 정의하는 방법**

1. Sequential API
2. Functional API

<br>

**Sequential API**

```python
from keras.models import Sequential
from keras.layers import Dense, Activation
model = Sequential()
model.add(Dense(10, input_shape=(784, 1)))
model.add(Activation("relu"))
```

모델을 정의하는 가장 기본적인 방식으로 단순히 층을 여러개 쌓는 형태.

<br>

**Functional API**

```py
from keras.layers import Input, Activation, Dense
from keras.models import Model
input = Input(shape=(25, 1))
x = Dense(40, activation="relu")(input1)
x = Dense(30, activation="relu")(x)
output = Dense(1, activation="softmax")(x)
model = Model(inputs=input, outputs=output)
```

Sequential API로 복잡한 모델을 생성할 수 없을때 사용.

다중 입력(multi-input)과 다중 출력(multi-output)이 가능.

이전 층을 다음 층의 입력으로 사용.

입력 층을 별도로 정의해야함.

<br>

<br>

**네트워크 구성 순서**

Convolution/Fully Connected -> Batch Normalization -> Activation -> Dropout -> Pooling