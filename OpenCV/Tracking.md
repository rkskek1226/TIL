# Tracking

객체 추적 : 지정한 객체의 위치를 연속된 영상 프레임에서 지속적으로 찾아내는 것.

<br>
**동영상 배경 제거**
배경만 있는 영상에서 객체가 있는 영상을 빼서 객체를 검출하는 방법(객체의 움직임을 판단하기 쉬움).

absdiff() 사용하는 방법.

1. read()로 첫번째 프레임을 배경으로 등록.
2. cv2.absfidiff()로 배경만 있는 프레임에서 객체가 있는 프레임을 뺀 절대값 차이를 리턴받고 출력.
3. 입력으로 들어오는 영상이 배경과 크게 달라질 경우 인식을 잘 못함.

<br>

cv2.BackgroundSubtractor() 사용하는 방법

동영상의 배경을 제거하는 cv2.BackgroundSubtractor 추상 클래스를 만들고 해당 클래스를 상속받은 구현 클래스를 제공.

```python
dst=cv2.createBackgroundSubtractorMOG2([, history=None, varThreshold=None, detectShadows=None])
fgmask=dst.apply(image [, fgmask=None, learningRate=None])
backgroundImage=dst.getBackgroundImage(, backgroundImage=None)
```

BackgroundSubtractorMOG2 객체를 생성하는 함수로 history는 히스토리 길이로 기본값이 500.

varThreshold는 해당 픽셀이 배경 모델에의해 잘 표현되는 지를 판단하는 것으로 기본값이 16.

detackShadows는 그림자 검출 여부로 기본값은 True.

배경이 제거된 객체를 리턴.

<br>

apply()는 배경이 제거된 객체 마스크를 생성하는 함수로 fgmask는 주로 출력으로 받아 None으로 지정.

learningRate는 배경 모델 학습 속도를 지정하는 것으로 0이면 배경 모델을 갱신하지 않고 1이면 프레임마다 배경 모델을 새로 만들고 -1이면 자동으로 결정됨(기본값은 -1).

<br>

getBackgroundImage()는 배경 영상을 반환하는 함수
