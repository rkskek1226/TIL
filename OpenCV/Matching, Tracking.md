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

keypoints는 검출된 코너 정보로 cv2.KeyPoint 객체를 담은 리스트. cv2.KeyPoint의 pt[0]으로 x 좌표, pt[1]으로 y 좌표 접근.
