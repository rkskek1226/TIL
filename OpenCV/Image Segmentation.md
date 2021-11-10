# 영상 분할(Image Segmentation)

**컨투어(contour)**

같은 색상이나 밝기의 연속된 점을 찾아 잇는 곡선.

컨투어를 찾아 모양 분석이나 객체 인식에 사용.

<br>

**외곽선(컨투어) 검출**

객체의 외곽선 좌표를 추출하는 작업으로 Boundary tracking, Contour tracing.

```python
contours, hierarchy=cv2.findContours(src, mode, method [, contours, hierarchy, offset])
```

src는 입력 영상으로 0이 아닌 픽셀을 객체로 간주.

매개변수중 contours와 hierarchy는 전달하지 않고 결과로 받음.

OpenCV 버전 3.4.x 이상부터는 리턴 값이 3개인 듯(contours앞에 _ 써서 해결하면 됨)

contours는 검출된 외곽선 좌표로 리스트이며 len(contours)는 전체 외곽선 갯수(N).

hierarchy는 외곽선 계층 정보로 shape이 (1, N, 4)로 N이 외곽선 갯수.

hierarchy[0, i, 0] ~ hierarchy[0, i, 3]이 next, prev, child, parent를 가리킴(-1이면 해당 사항 없음).

| mode 옵션 값      | 방법                             |
| ----------------- | -------------------------------- |
| cv2.RETR_EXTERNAL | 가장 바깥쪽 외곽선만 제공        |
| cv2.RETR_LIST     | 모든 외곽선을 계층 정보없이 제공 |
| cv2.RETR_CCOMP    | 모든 외곽선을 2계층으로 제공     |
| cv2.RETR_TREE     | 모든 외곽선을 트리 구조로 제공   |

| method 옵션 값             | 방법                                        |
| -------------------------- | ------------------------------------------- |
| cv2.CHAIN_APPROX_NONE      | 근사화 하지않고 모든 좌표를 제공(주로 사용) |
| cv2.CHAIN_APPROX_SIMPLE    | 수직선, 수평선, 대각선 좌표만 제공          |
| cv2.CHAIN_APPROX_TC89_L1   | Teh&Chin L1 근사화                          |
| cv2.CHAIN_APPROX_TC89_KCOS | Teh&Chin k cos 근사화                       |

<br>

```python
dst=cv2.drawContours(img, contours, contourIdx, color, thickness)
```

외곽선을 그리는 함수로 cv2.findContours()에서 결과로 받은 contours를 전달함.

contours는 그릴 외곽선 인덱스로 -1 전달시 모든 외곽선을 그림.

color와 thickness는 외곽선 색상과 외곽선 두께로 thickness가 0이면 내부를 채움

<br>

**외곽선 관련 함수**

```python
retval=cv2.arcLength(curve, closed)
```

외곽선 길이 계산함수로 curve는 외곽선 좌표로 계산할 외곽선.

closed가 True면 폐곡선으로 간주하며 외곽선 길이를 retval로 리턴.

<br>

```python
retval=cv2.contourArea(contour [, oriented=False])
```

외곽선으로 둘러진 넓이 계산 함수로 외곽선 좌표를 contour로 전달.

oriented가 True면 외곽선 진행 방향에 따라 음수를 리턴.

<br>

```python
retval=cv2.boundingRect(contour)
```

외곽선을 감싸는 가장 작은 사각형 좌표를 리턴하는 함수로 외곽선 좌표를 contour로 전달하며 (x, y, w, h)의 사각형 좌표를 튜플로 리턴받음.

<br>

```python
center, radius=cv2.minEnclosingCircle(points)
```

외곽선을 감싸는 가장 작은 원의 좌표와 반지름을 리턴하는 함수로 외곽선 좌표를 points로 전달하며 원의 중심 좌표를 (x, y) 튜플로 리턴받고 원의 반지름을 실수로 radius로 받음.

<br>

```python
approxCurve=cv2.approxPolyDP(contour, epsilon, closed)
```

외곽선 근사화 함수로 컨투어 좌표를 contour로 받음.

epsion은 근사값 정확도로 일반적으로 cv2.arcLength()로 구한 외곽선 전체 길이*0.02로 전달.

closed에 True 설정시 폐곡선으로 간주.

<br>

**레이블링(Labeling)(Connected component labeling)**

이진 영상에서 연결된 픽셀에 같은 번호를 매기는 작업.

4-이웃 연결 관계(4-neighbor connectivity) : 두개의 픽셀이 상하좌우로 연결되어 있을때

8-이웃 연결 관계(8-neighbor connectivity) : 두개의 픽셀이 상하좌우, 대각선까지 연결되어 있을때

```python
retval, labels=cv2.connectedComponents(src [, labels=None, connectivity=8, ltype=cv2.CV_32S])
```

labels는 레이블 맵 행렬로 입력 영상과 같은 크기지만 매개변수로 전달하지 않고 결과로 받음.

connectivity는 4-이웃 연결 관계, 8-이웃 연결 관계를 설정하는 것으로 기본값이 8-이웃 연결 관계.

ltype은 label 타입으로 기본값이 cv2.CV_32S.

retval은 레이블(객체) 개수로 객체 개수+1(배경)을 리턴.

```python
retval, labels, stats, centroids=cv2.connectedComponentsWithStats(src [, labels, stats, centroids, connectivity, ltype])
```

stats는 각 객체의 바운딩 박스로 Nx5 행렬(N은 레이블 갯수)(0번째 행은 배경 정보가 들어오며 x좌표, y좌표, 폭, 높이, 넓이 순서).

centroids는 각 객체의 중심점 좌표로 Nx2 행렬(N은 레이블 갯수)(0번째 행은 배경 정보로 x좌표들의 합/픽셀 갯수, y좌표들의 합/픽셀 갯수).

<br>

**허프 변환 : 직선 검출(Hough transform)**

```python
lines=cv2.HoughLines(img, rho, theta, threshold [, lines, srn=0, stn=0, min_theta, max_theta])
```

직선 검출.

img는 입력 영상으로 엣지 영상.

rho는 거리 측정 해상도로 1.0이면 1픽셀 간격.

theta는 각도 측정 해상도로 np.pi/180이면 1도 간격

threshold는 직선으로 판단할 임계값으로 값. 

lines는 검출 결과로 numpy.ndarray형 배열. (rho, theta)을 담고있는 Nx1x2 배열.

<br>

```python
lines=cv2.HoughLinesP(img, rho, theta, threshold [, lines, mLineLength, maxLineGap])
```

확률적 허프 변환으로 허프 직선 검출과 달리 무작위로 선정한 픽셀로 허프 변환을 수행하는 방식.

리턴값이 HoughLines와 다름.

리턴값이 시작 좌표와 끝 좌표를 담고있는 (x1, y1, x2, y2)로 Nx1x4 배열로 리턴 받음(dtype이 numpy.int32).

<br>

**허프 변환 : 원 검출**

원 검출.

동심원이 여러개이면 가장 작은 원만 검출됨.

```python
circles=cv2.HoughCircles(img, method, dp, minDist [, circles, param1, param2, minRadius, maxRadius])
```

img는 입력 영상으로 엣지 영상이 아닌 일반 영상(그레이스케일 영상)

method는 검출 방식으로 cv2.HOUGH_GRADIENT만 가능(OpenCV 4.2 이하버전이면)(OpenCV 4.3버전부터 cv2.HOUGH_GRADIENT_ALT 가능)

dp는 입력 영상과 경사 누적의 해상도 반비례율로 1이면 입력 영상과 동일.

minDist는 검출된 원 중심의 최소 거리.

param1은 캐니 엣지에 전달할 쓰레시홀드의 최대값이고 param2는 경사도 누적 경계 값.

minRadius와 maxRadius는 검출할 원의 최소, 최대 반지름.

circles는 검출된 원의 정보로 (cx, cy, r)이 x좌표, y좌표, 반지름의 정보를 담고있는 1xNx3의 np.float32 배열.



