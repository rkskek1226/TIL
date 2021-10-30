# CNN

**CNN(convolutional neural network)**

합성공 신경망(주로 이미지 인식 분야에서 CNN을 기초로 딥러닝을 활용).

이미지에서 특징을 추출하기위해 커널을 도입하는 기법.

<br>

**정규화(normalization)**

데이터의 폭이 클때 적절한 값으로 분산의 정도를 바꾸는 과정.

<br>

**원-핫-인코딩(one-hot-encoding)**

```python
from keras.utils import np_utils
Y_train=np_utils.to_categorical(Y_train,10) # 클래스와 클래스의 갯수를 지정
print(Y_train) # Y가 4일때 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
```

Y값을 0과 1로 이루어진 형태로 바꿔주는 기법.

<br>

**컨벌루젼**

이미지에 커널을 적용해 새롭게 만들어진 층.

```python
model.add(Conv2D(32, kernel_size=(3, 3), input_shape(28, 28, 1), activation="relu"))
```

Conv2D() : 컨벌루젼 층을 추가하는 함수.

첫번째 인자 : 커널을 몇개 적용할지를 결정. 커널 갯수에 따라 컨볼루젼이 나옴.

kernel_size : 커널의 크기로 (행, 열) 형식으로 지정.

input_shape : 은닉층일 경우 생략하지만 입력층일 경우 입력되는 형식을 지정해야하며 형식은 (행, 열, 컬러 또는 흑백). 입력 영상이 컬러 영상이면 3, 흑백 영상이면 1을 지정.

activation : 활성화 함수

<br>

**풀링(pooling), 서브 샘플링(sub sampling)**

컨볼루젼 층을 통해 이미지 특징을 도출하였을때 결과가 여전히 크고 복잡해서 축소하는 과정.

맥스 풀링(max pooling) : 정해진 구역안에서 최댓값을 뽑아내는 방식

평균 풀링(average pooling) : 정해진 구역안에서 평균을 뽑아내는 방식

 ```python
 model.add(MaxPooling2D(pool_size=2))
 ```

pool_size는 풀링 창의 크기로 2로 설정시 전체 크기가 절반으로 줄어듬

<br>
**드롭 아웃(drop out)**

은닉층에 배치된 노드중 일부를 꺼 과적합을 방지하는 것.

```python
model.add(Dropout(0.25)) # 25%의 노드를 끔
```

<br>

**플랫튼(Flatten)**

컨볼루젼 층이나 맥스 풀링은 2차원 배열로 다루기때문에 1차원 배열로 바꿔줘야 활성화 함수 사용 가능

```python
model.add(Flatten())
```

