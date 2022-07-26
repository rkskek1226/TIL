# ETC

**Keras**

Keras는 입력층을 따로 만들지 않음.

Sequential() : 딥러닝 구조를 쌓아올릴수 있게함.

add() : Sequential() 선언후 add()로 층을 추가함. 첫번째 은닉층에서 input_dim으로 입력 데이터로부터 몇개를 가져올지를 설정해 입력층+은닉층의 역할을 함.

Dense() : 각 층의 특성을 설정하며 add() 안에서 사용함.

compile() : 모델을 컴파일하는 것으로 손실 함수, 최적화 방법, 메트릭을 지정.

* compile()에서 이진 분류의 경우 손실 함수로 binary_crossentropy를 사용


* compile()에서 다중 분류의 경우 원핫 인코딩 적용하면 손실 함수로 categorical_crossentropy를 사용.


* compile()에서 다중 분류의 경우 원핫 인코딩 적용안하면 손실 함수로 sparse_categorical_crossentropy를 사용.

fit() : 모델을 실제로 수행하는 것으로 epoch와 batch_size를 지정.

```python
dataset = np.loadtxt("~~.csv",delimiter=",")
X = dataset[범위 지정]
Y = dataset[범위 지정]

model = Sequential()
model.add(Dense(12, input_dim=8, activation="relu")) # 입력층과 은닉층의 역할
model.add(Dense(8, activation="relu")) # 은닉층
model.add(Dense(1, activation="sigmoid")) # 출력층

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X, Y, epochs=200, batch_size=10)
```



| 계열         | Keras에서 사용하는 손실 함수             | Keras에서 사용하는 손실 함수 |
| :--------- | :----------------------------- | ------------------ |
| 평균 제곱 계열   | mean_squared_error             | 평균 제곱 오차           |
| 평균 제곱 계열   | mean_absolute_error            | 평균 절대 오차           |
| 평균 제곱 계열   | mean_absolute_percentage_error | 평균 절대 백분율 오차       |
| 평균 제곱 계열   | mean_squared_logarithmic_error | 평균 제곱 로그 오차        |
| 교차 엔트로피 계열 | categorical_crossentropy       | 범주형 교차 엔트로피(분류)    |
| 교차 엔트로피 계열 | binary_crossentropy            | 이항 교차 엔트로피(이진 분류)  |

<br>

입력 데이터가 문자열일 경우 numpy보다는 pandas가 좋음.

<br>

문자 데이터를 숫자로 변환하고 원핫 인코딩 사용하는 방법.

```python
from sklearn.preprocessing import LabelEncode
from keras.utils import np_utils
e=LabelEncoder()
e.fit(y)
Y=e.transform(y)
Y_encoded=np_utils.to_categorical(Y)
```

데이터 입력시 숫자(정수, 실수)형이여야하므로 문자 데이터를 숫자형으로 바꿔야함.

단순 숫자로 바꿀 경우 이상한 관계를 형성할 수 있으므로 원-핫 인코딩 방식을 사용.

0과 1로만 구성되어 True를 표현하는 1개의 1과 False를 표현하는 여러개의 0으로 구성된 숫자로 변환됨.

<br>

과적합(over fitting)

```python
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size=0.3, random_state=seed, stratify=Y) 
```

X 데이터와 Y 데이터에서 학습셋과 테스트셋을 만들 수 있음.

입력 데이터 X와 결과 데이터 Y에서 학습셋 70%, 테스트셋 30%로 구분하는 함수. 

stratify는 클래스 비율을 맞춰줌.

<br>

**K겹 교차 방법(k-fold cross validation)**

데이터셋이 작을 경우 데이터셋을 여러개로 나누어 하나씩 테스트셋으로 사용하고 나머지를 학습셋으로 사용하는 방법.

```python
from sklearn.model_selection import StratifiedKFold
n_fold = 10   # 10개의 셋으로 나눔
skf = StratifiedKFold(n_splits=n_fold, shuffle=True, random_state=seed)
```

 <br>

<br>

**Keras에서 predict()와 predict_classes() 차이**

분류의 경우 predict()는 확률을 리턴하고 predict_classes()는 클래스의 인덱스(label)를 리턴

Ex. 개와 고양이 분류의 경우 predict()는 0.6(고양이), 0.4(개)로 리턴하고 predict_classes()는 0(고양이)이나 1(개)로 리턴.

회귀의 경우 predict()는 예상된 수치를 리턴하고 predict_classes()는 할 수 없음.

Ex. 집값 예측의 경우 predict는 예상된 가격을 리턴하고 predict_class는 할 수 없음.

Tensorflow 2.6 버젼 이상부터 predict_classes()는 오류 발생

따라서 QQ=model.predict(WW)     EE=np.argmax(QQ, axix=1)로 작성할 것.

<br>

<br>

**ImageDataGenerator()**

주어진 데이터를 이용해 변형된 이미지를 만들어 데이터의 수를 늘려주는 함수.

```python
train_datagen = ImageDataGenerator(rescale= , horizontal_flip= , width_shift_range= , height_shift_range= , 
                             rotation_range= , shear_range= , zoom_range= , vertical_flip= , fill_mode= )
```

rescale : 크기 변경(rescale=1./255하면 RGB값들을 255로 나누어 0에서 1의 값으로 변경됨).

horizontal_flip, vertical_flip : 수평이나 수직으로 뒤집음(horizontal_flip=True, vertical_flip=False).

zoom_range = 정해진 범위에서 축소, 확대시킴(zoom_range=0.1).

width_shift_range, height_shift_range : 정해진 범위에서 수평, 수직으로 랜덤하게 평행 이동시킴(width_shift_range=0.1, height_shift_range=0.1).

rotation_range : 정해진 각도만큼 이미지를 회전시킴(rotation_range=5).

shear_range : 좌표 하나를 고정시키고 다른 좌표를 이동시키는 변환을 수행(shear_range=0.5).

fill_mode : 이미지를 축소, 회전, 이동할때 생기는 빈 공간을 어떻게 채울지 결정(fill_mode="nearest"하면 가장 비슷한 색으로 채움)

테스트 데이터에는 rescale만 적용시킴.

<br>

<br>

**flow_from_directory()**

폴더에 저장된 데이터를 불러오는 함수.

```python
train_gen = train_datagen.flow_from_directory("경로", target_size=( , ), batch_szie= , class_mode=" ")
```

target_size : 이미지 크기.

class_mode : 이진 분류면 binary.

컴파일 후 실행시킬때 fit()이 아닌 fit_generator()을 사용.

```python
model.fit_generator(train_gen, steps_per_epooch= , epochs= , validation_data= , validation_steps= )
```

첫 인자는 이미지 생성기로 설정.

steps_per_epoch : 이미지 생성기에서 몇 개의 샘플을 뽑을지 결정.

validation_steps : validation_data에 전달되는 인자에서 몇 개의 샘플을 뽑을지 결정.

<br>

<br>

**callback**

학습중 특정 작업을 수행할 수 있도록하는 객체.

keras.callbacks 패키지 아래에 있는 클래스로 fit()의 callbacks 매개변수에 리스트로 전달하여 사용.

* ModelCheckpoint 콜백은 에포크마다 모델을 저장하며 save_best_only=True로 매개변수를 지정하면 검증 점수가 가장 높은 모델을 저장.
* EarlyStopping 콜백은 조기 종료를 위한 콜백으로 patience 매개변수로 점수가 향상되지 않더라도 허용할 에포크 횟수를 지정할 수 있음.
* EarlyStopping 콜백에서 restore_best_weights=True로 매개변수를 지정하면 검증 점수가 가장 높은 모델의 파라미터로 되돌림.

