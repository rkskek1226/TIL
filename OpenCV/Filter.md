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
