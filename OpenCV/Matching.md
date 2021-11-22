# Matching, Tracking

**템플릿 매칭(Template matching)**

입력 영상에서 템플릿 영상과 일치하는 위치를 찾는 기법(템플릿은 찾을 대상이 되는 영상).

```python
result=cv2.matchTemplate(img, templ, method [, result, mask])
```

templ은 템플릿 영상이고 method는 비교 방법으로 cv2.TM_CCOEFF_NORMED(완벽히 매칭되면 1, 아니면 0)를 자주 사용.

result는 비교 결과 행렬(유사도/비유사도 측정)로 dtype이 numpy.float32.

img 크기가 WxH이고 templ이 wxh이면 result의 크기는 (W-w+1)x(H-h+1).

<br>
cv2.matchTemplate()의 결과 행렬에서 최소값과 최대값을 구하면 최선의 매칭값과 매칭 위치를 찾을 수 있음.

```python
minVal, maxVal, minLoc, maxLoc=cv2.minMaxLoc(src)
```

src에서 최고값과 최대값을 minVal, maxVal로 리턴하고 해당 위치 좌표를 minLoc, maxLoc로 리턴.

cv2.matchTemplate()에서 method에 cv2.TM_CCOEFF_NORMED를 사용할 경우 완벽히 매칭되면 1이므로 maxVal만 있으면 됨.

<br>

**코너 검출**

코너(corner) : 엣지와 엣지가 만나는 부분으로 영상의 특징을 표현하는 요소.

해리스 코너 검출(Harris corner detection), GFTT(goodFeaturetoTrack), Fast 등이 있음.

```python
dst=cv2.cornerHarris(src, blockSize, ksize, k [, dst, borderType])
```

해리스 코너 검출 방법으로 소벨 미분으로 엣지를 검출하면서 엣지의 변화량을 측정하여 크게 변화하는 것을 코너로 판단.

src는 입력 영상으로 그레이스케일 영상.

blcokSize는 이웃 픽셀 크기로 주로 2~5로 설정.

ksize는 소벨 미분 커널의 크기로 주로 3으로 설정.

k는 해리스 코너 검출 상수로 주로 0.04~0.06으로 설정.

dst는 해리스 코너 검출 결과로 src와 같은 크기의 행렬로 dtype이 numpy.float32인 해리스 커너 응답 계수.

borderType은 가장자리 픽셀 확장 방식으로 기본값이 cv2.BORDER_DEFAULT.

<br>

```python
corners=cv2.goodFeaturesToTrack(img, maxCorner, qualityLevel, minDistance [, corner, mask, blockSize, useHarrisDetector, k])
```

GFTT(goodFeaturesToTrack) 방법으로 해리스 코너 검출 방법을 향상시킨 방법.

maxCorner는 최대 코너 개수로 maxCorner<=0이면 무제한.

qualityLevel은 코너로 판단할 값으로 주로 0.01~0.1로 설정.

minDistance는 코너들의 최소 거리.

mask는 마스크 영상이으로 blockSize는 코너 검출을 위한 블록 크기로 기본값이 3.

useHarrisDetector는 코너 검출 방법으로 True면 해리스 코너 검출 방법으로 기본값은 False.

k는 해리스 코너 검출 방법시 사용할 k 값.

corners는 코너 검출 좌표로 dtype이 numpy.float32인 Nx1x2 배열.

<br>

**특징점 검출**

OpenCV는 cv2.Feature2D 클래스를 상속받아 특징 검출기를 구현.

추출된 특징점은 cv2.KeyPoint 객체로 표현됨.

cv2.KeyPoint 객체는 특징점 정보 객체로 pt, size, angle의 멤버를 가짐.

pt는 (x, y) 좌표로 float 타입.

```python
detector=cv2.FastFeatureDetector_create([threshod [, nonmaxSuppression, type]])
keypoints=detector.detect(src)
```

FAST(Feature from Accelerated Segment Test) 방법으로 기준 픽셀보다 밝거나 어두운 픽셀이 특정 개수 이상으로 나타나면 코너로 판단하는 방법.

해리스 코너 검출 방법이나 GFTT 보다 빠름.

threshold는 코너로 판단할 임계값으로 기본값이 10.

nonmaxSuppression은 비최대 억제 수행 여부로 기본값이 True.

type은 코너 검출 방법으로 기본값이 cv2.FAST_FEATURE_DETECTOR_TYPE_9_16.

src는 입력 영상으로 그레이스케일 영상.

detector는 FastFeatureDetector 특징 검출기 객체로 detector.detect()로 특징점을 검출.

keypoints는 검출된 특징점 정보로 cv2.KeyPoint 객체를 담은 리스트. cv2.KeyPoint의 pt[0]으로 x 좌표, pt[1]으로 y 좌표 접근.

<br>

```python
outImg=cv2.drawKeyPoints(img, keypoints, outImg [, color, flag])
```

검출된 코너 정보인 keypoints를 전달해 특징점을 그려주는 함수.

color는 특징점을 표시할 색상이며 랜덤이 기본값.

flag는 특징점을 그리는 방법으로 cv2.DRAW_MATCHES_FLAGS_DEFAULT가 기본값.

<br>

**기술자(디스크립터, descriptor)**

특징점 부분의 밝기, 색상, 방향, 크기 등의 정보를 표현한 벡터로 numpy.ndarray로 표현됨.

행 갯수는 특징점의 갯수. 열 갯수는 특징점 기술자 알고리즘에 의해 정의됨.

cv2.Feature2D 클래스를 상속받아 구현함.

```python
keypoints, descriptors=detector.compute(image, Keypoints [, descriptor]) //cv2.OO_create()의 리턴값인 detector를 이용.
```

compute()는 특징점 기술자를 계산하는 함수.

Keypoints는 검출된 특징점 정보로 cv2.KeyPoint 객체를 담은 리스트.

descriptors는 특징점 기술자 행렬.

<br>

```python
keypoints, descriptors=detector.detectAndCompute(image, mask, descriptor)
//cv2.OO_create()의 리턴값인 detector를 이용.
```

detectAndCompute()는 특징점 검출 및 계산하는 함수.

Keypoints는 검출된 특징점 정보로 cv2.KeyPoint 객체를 담은 리스트.

descriptors는 특징점 기술자 행렬.

<br>

**특징점 매칭(feature matching)**

두 영상에서 추출한 특징점 기술자를 비교하여 서로 유사한 기술자를 찾는 작업.

OpenCV는 특징 매칭 알고리즘을 추상 클래스인 cv2.DescriptorMatcher를 상속받아 구현.

매칭 결과의 구조와 모양을 통일하기위해 모든 매칭 결과를 cv2.DMatch 객체로 리턴.

