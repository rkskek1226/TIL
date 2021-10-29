# CNN

CNN(convolutional neural network) : 합성공 신경망(주로 이미지 인식 분야에서 CNN을 기초로 딥러닝을 활용).
<br>

정규화(normalization) : 데이터의 폭이 클때 적절한 값으로 분산의 정도를 바꾸는 과정.

<br>

원-핫-인코딩(one-hot-encoding)

```python
from keras.utils import np_utils
Y_train=np_utils.to_categorical(Y_train,10) # 클래스와 클래스의 갯수를 지정
print(Y_train) # Y가 4일때 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
```

Y값을 0과 1로 이루어진 형태로 바꿔주는 기법.
