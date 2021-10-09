# OpenCV

[OpenCV ](https://opencv.org)

[OpenCV 함수](https://docs.opencv.org/master)



#### Image Processing basic

NumPy 배열은 이미지를 행(row)과 열(column)의 순서로 접근하므로 이미지의 높이(height)와 폭(width)의 순서로 지정해야함

그레이스케일 영상 : OpenCV 자료형으로 cv2.CV_8UC1을 사용하고 NumPy 자료형으로는 numpy.uint8을 사용하며 shape이 (h, w)

컬러 영상 : OpenCV 자료형으로 cv2.CV_8UC3을 사용하고 NumPy 자료형으로는 numpy.uint8을 사용하며 shape이 (h, w, 3), BGR 순서

<br>

**관심영역(ROI) 지정 함수**

```python
ret=cv2.selectROI([win_name,]img[, showCrossHair=True, fromCenter=False])
```

마우스로 ROI를 지정하고 스페이스 키나 엔터 키를 누르면 x, y, width, height 값을 튜플로 리턴.

<br>

**쓰레시홀드**

```python
ret, out=cv2.threshold(img, threshold, value, type_flag)
```

바이너리 이미지를 만드는 방법으로 경계값을 넘으면 value로, 못넘으면 0으로 픽셀값을 지정하는 함수.

 쓰레시홀딩에 사용한 경계값과 결과 바이너리 이미지를 리턴.

type_flag에 cv2.THRESH_OTSU(오츠 알고리즘)을 사용하면 효율적으로 경계값을 찾아줌.

<br>

**적응형 쓰레시홀드**

```python
dst=cv2.adaptiveThreshold(img, value, method, type_flag, block_size, C)
```

영상에 조명이 일정하지 않거나 배경색이 여러가지인 경우 사용하는 방법으로 이미지를 여러 영역으로 나누고 해당 주변 픽셀값만 가지고 계산함.

method에는 이웃 픽셀의 평균으로 결정하는 cv2.ADPTIVE_THRESH_MEAN_C와 가우시안 분포에 따른 가중치의 합으로 결정하는 cv2.ADPTIVE_THRESH_GAUSSIAN_C가 있음.

<br>

**이미지 연산**

```python
dst=cv2.add(src1, src2[, dst, mask, dtype])
dst=cv2.subtract(src1, src2[, dst, mask, dtype])
dst=cv2.multiply(src1, src2[, dst, mask, dtype])
dst=cv2.divide(src, src2[, dst, scale, dtype])
```

NumPy의 브로드캐스팅 연산을 할 경우 255나 0을 넘어가는 값이 저장되지만 OpenCV의 함수를 사용하면 0~255의 값을 가짐.

mask 지정시 0이 아닌 픽셀만 연산.

<br>

**알파 블렌딩**

```python
dst=cv2.addWeighted(img1, alpha, img2, beta, gamma)
```

img1과 img2에 각각 가중치를 적용해 영상을 더함. beta에는 (1-alpha)를 사용.

<br>

**차영상**

```python
diff=cv2.absdiff(img1, img2)
```

두 영상의 차이(변화)를 알 수있는 함수로 차이 연산 결과 영상을 리턴. 입력 영상의 순서에 영향을 받지 않음.

<br>

**비트와이즈 연산**

```python
dst=cv2.bitwise_and(img1, img2, mask=None)
dst=cv2.bitwise_or(img1, img2, mask=None)
dst=cv2.bitwise_xor(img1, img2, mask=None)
dst=cv2.bitwise_not(img1, mask=None)
```

img1과 img2는 동일한 shape으로 mask 지정시 0이 아닌 픽셀만 연산.

<br>

**히스토그램**

```python
hist=cv2.calcHist(img, channel, mask, histSize, ranges)
```

영상의 색상이나 명암의 분포를 파악하기 위해 영상의 픽셀값 분포를 그래프 형태로 표현한 것.

입력 영상 img는 리스트로 감싸서 전달해야하며 입력 영상이 1채널이면 channel이 [0], 2채널이면 [0, 1], 3채널이면 [0, 1, 2]로 전달해야함.

mask 지정시 mask에 지정한 픽셀만 계산하며 전체 영상에 대해 히스토그램을 구하려면 None 전달.

histSize는 계급의 개수로 리스트로 전달. 1채널이면 [256], 2채널이면 [256, 256], 3채널이면 [256, 256, 256].

ranges는 픽셀이 가질 수 있는 값의 범위를 리스트로 전달.[0, 256]

<br>

**노멀라이즈**

```python
dst=cv2.normalize(src, dst, alpha, beta, type_flag)
```

특정 부분에 몰려있는 값을 전체 영역으로 골고루 분포하게하여 명암비가 향상됨

src에 입력 영상을 전달하며 매개변수의 dst는 None으로 지정.

alpha와 beta에 노멀라이즈 구간의 최소값과 최대값을 지정하며 type_flag에는 cv2.NORM_MINMAX로 alpha와 beta 구간으로 노멀라이즈.

<br>

**이퀄라이즈**

```python
dst=cv2.equalizeHist(src)
```

값이 전체 분포에 차지하는 비중에 따라 분포를 재분배하여 명암비를 향상시킴.

컬러 영상에 적용시 BGR보다는 YUV, YCrCb, HSV로 변환해 밝기 채널만 연산하는 것이 효과적.

