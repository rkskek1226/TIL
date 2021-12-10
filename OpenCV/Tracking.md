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

detactShadows는 그림자 검출 여부로 기본값은 True.

배경이 제거된 객체를 리턴.

<br>

apply()는 배경이 제거된 객체 마스크를 생성하는 함수로 fgmask는 주로 출력으로 받아 None으로 지정.

learningRate는 배경 모델 학습 속도를 지정하는 것으로 0이면 배경 모델을 갱신하지 않고 1이면 프레임마다 배경 모델을 새로 만들고 -1이면 자동으로 결정됨(기본값은 -1).

<br>

getBackgroundImage()는 배경 영상을 반환하는 함수.

<br>

**평균 이동 추적(MeanShift)**

평균 이동 알고리즘으로 객체를 추적.

추적할 객체를 선정해 HSV 컬러 스페이스의 H값의 히스토그램을 계산.

전체 영상의 히스토그램 계산 결과로 역투영.

역투영 결과에서 이동한 객체를 MeanShift로 추적.

```python
retval, window = cv2.meanShift(probImage, window, criteria)
```

probImage는 객체의 히스토그램 역투영 영상.

window는 검색 시작 위치이자 검색 결과 위치로 (x, y, width, height) 튜플로 지정.

criteria는 검색 종료 기준으로 type, maxCount, epsilon을 튜플로 지정. ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)을 주로 사용)

retval은 알고리즘이 반복한 횟수.

MeanShift는 색상을 기반으로 추적하므로 객체의 색상이 주변과 비슷하면 추적이 어렵고 객체의 크기와 방향과는 상관없이 항상 같은 크기의 윈도우를 반환한다는 단점이 있음.

<br>

**캠시프트(CamShift : Continously Adaptive MeanShift)**

MeanShift의 단점을 보완한 방식으로 객체의 크기와 방향에 따라 윈도우 크기가 달라짐.

```python
retval, window = cv2.CamShift(probImage, window, criteria)
```

probImage는 객체의 히스토그램 역투영 영상.

window는 검색 시작 위치이자 검색 결과 위치로 (x, y, width, height) 튜플로 지정.

criteria는 검색 종료 기준으로 type, maxCount, epsilon을 튜플로 지정. ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)을 주로 사용)

retval은 추적하는 객체를 나타내는 사각형 정보를 리턴. ((cx, cy), (width, height), angle) 형태의 튜플.

<br>

**옵티컬 플로우(Optical flow)**

객체의 움직임에 의해 나타나는 객체의 이동 정보 패턴(방향과 거리).

계산하는 방식에 따라 일부 픽셀만을 계산하는 희소 옵티컬 플로우와 영상 전체 픽셀을 계산하는 밀집 옵티컬 플로우로 나뉨.

```python
nextPts, status, err=cv2.calcOpticalFlowPyrLK(prevImg, nextImg, prevPts, nextPts, status=None, err=None, winSize=None, maxLevel=None,criteria=None, flags=None, minEigThreshold=None)
```

루카스-카나데 알고리즘으로 희소 옵티컬 플로우를 구현한 함수.

prevImg와 nextImg는 이전 프레임 영상과 현재 프레임 영상으로 8비트 영상.

prevPts는 이전 프레임에서 추적할 점들로 (N, 1, 2)의 dtype이 np.float32인 ndarray.

nextPts는 prevPts 점들이 이동한 현재 프레임 좌표로 주로 매개변수로는 None을 전달하고 리턴으로 받음.

status는 매칭 상태로 (N, 1)의 dtype이 np.uint8인 ndarray.

err는 결과 오차 정보로 (N, 1)의 dtype이 np.float32인 ndarray.

winSize는 피라미드 레벨에서 검색할 윈도우 크기로 (21, 21)이 기본값

maxLevel은 최대 피라미드 레벨로 기본값은 3이고 0이면 피라미드 사용 안함.

<br>

```python
flow=cv2.calcOpticalFlowFarneback(prev, next, flow, pyr_scale, levels, winsize, iterations, poly_n, poly_sigma, flags)
```

영상 전체 픽셀을 계산하는 밀집 옵티컬플로우 함수로 속도가 느림.

prev와 next는 이전 영상과 현재 영상으로 그레이스케일 영상.

pyr_scale은 피라미드 영상을 만들 때의 축소 비율.

levels는 피라미드 영상 개수이고 winsize는 평균 윈도우 크기.

iterations는 각 피라미드 레벨에서 알고리즘을 반복할 횟수.

poly_n은 다항식 확장을 위한 이웃 픽셀 크기이고 poly_sigma는 가우시안 표준 푠차.

flow는 계산된 옵티컬플로우로 shape이 (h, w, 2)이고 dtype이 np.float32인 np.ndarray인 .
