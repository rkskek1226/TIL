# Filter

**필터(filter)** : 입력값에서 원하지 않는 값을 걸러내고 원하는 결과를 얻는 작업

**공간 영역 필터(spacial domain filter)** : 새로운 픽셀값을 얻을때 기존 픽셀과 주변 픽셀들을 활용하는 방법.

**주파수 영역 필터(frequency domain filter)** : 픽셀값들의 차이를 주파수로 변환해서 활용하는 방법

**커널(kernel), 마스크(mask)** : 주변 픽셀을 활용할때 어디까지 포함할지와 어떻게 산출할지를 결정하는 것(커널의 크기와 값에 따라 영상을 부드럽게 만들거나 날카롭게 만들거나 엣지를 검출하거나 잡음을 제거하느냐가 결정되며 커널의 크기가 커질수록 연산량이 많아짐).

<br>

**컨볼루션(convolution) 연산**

커널의 각 요소와 대응하는 입력 픽셀값을 곱해서 모두 합한 것을 결과 픽셀값으로 결정하고 해당 작업을 마지막 픽셀까지 반복하는 것.

```python
dst=cv2.filter2D(src, ddepth, kernel[, dst, anchor, delta, borderType])
```

ddepth는 출력 영상의 dtype으로 -1 지정시 src와 같은 타입으로 설정됨.

kernel은 nxn 크기의 float32 배열.

anchor는 커널의 기준점으로 (-1, -1)이 디폴트로 커널의 중앙.

delta는 추가할 값이며 borderType은 가장자리 픽셀 확장 방식을 의미.

borderType(가장자리 픽셀 확장 방법) : BORDER_CONSTANT, BORDER_REPLICATE, BORDER_REFLECT, BORDER_REFLECT_101, BORDER_REFLECT101, BORDER_DEFAULT(=BORDER_REFLECT_101)가 있음.

<br>

**평균 블러링**

블러링이란 영상을 흐릿하게 만드는 것으로 그레이스케일 값 변화가 줄어들어 영상이 부드러워지고 잡음이 사라짐(커널이 커질수록 연산량이 많아짐).

영상의 좌표값을 주변 픽셀값들의 평균으로 적용하는 것.

커널=nxn 크기로 값을 1로 채우고 n**2으로 나눈 행렬.

만든 커널을 cv2.filter2D()의 kernel로 전달하면 됨.

```python
dst=cv2.blur(src, ksize[, dst, anchor, borderType])
```

커널을 만들고 cv2.filert2D()로 적용하는 방법도 있지만 cv2.blur()로 한번에 할 수도 있음.

ksize는 커널의 크기로 (width, height) 형태의 튜플로 지정.

<br>

**가우시안 블러링**

가우시안 분포를 갖는 커널로 블러링을 함.

가까이 있는 픽셀에는 큰 가중치를 설정하고 멀리 있는 픽셀에는 작은 가중치를 사용.

```python
dst=cv2.GaussianBlur(src, ksize, sigmaX, sigmaY, borderType)
```

ksize는 커널 크기로 (0, 0)을 지정하면 sigmaX에 의해 자동으로 결정됨(sigmaX에는 0 대입 불가).

sigmaX, sigmaY는 X, Y 방향 표준편차 SigmaY 생략시 SigmaX와 같은 값 적용됨.

<br>

**미디언 블러링(median blurring)**

커널의 픽셀값중 중간 값(median)으로 대상 픽셀값을 설정하는 것.

소금-후추 잡음 제거에 효과적.

```python
dst=cv2.medianBlur(src, ksize)
```

ksize에 3을 입력시 3x3으로 설정됨.

<br>
**바이레터럴 필터(양방향 필터, bilateral filter)**

가우시안 잡음 제거에 효과적.

가우시안 잡음 제거에는 가우시안 블러링이 효과적이지만 원본 영상의 엣지 정보의 날카로움이 사라질 수 있음 -> 바이레터럴 필터를 사용해서 해결.

가우시안 블러링은 영상 전체를 블러링해 빠르지만 바이레터럴 필터는 엣지가 아닌 부분만 블러링하므로 느림.

```python
dst=cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst, borderType])
```

d는 필터의 직경으로 -1 입력시 sigmaSpace에 의해 자동으로 결정됨.

sigmaColor는 색 공간에서 필터의 표준 편차.

sigmaSpace는 좌표 공간에서의 필터의 표준 편차.

<br>

**샤프닝(Sharpening)**

부드러워진 영상을 날카로운 영상으로 생성.

