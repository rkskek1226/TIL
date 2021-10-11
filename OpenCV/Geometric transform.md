# Geometric transform

기하학적 변환 : 영상 좌표에 기하학적인 연산을 통해 새로운 좌표를 얻거나 영상의 모양을 바꾸는 것

<br>

**영상의 좌표를 변환시키는 함수**

```python
dst=cv2.warpAffine(src, mtrx, dsize[, dst, flags, borderMode, borderValue])
```

dtype이 float32인 2x3 변환 행렬을 mtrx에 전달하고 결과 영상의 크기를 (width, height)로 dsize에 전달. 

(0, 0) 전달시 입력 영상과 동일한 크기로 설정.

<br>

**이동**

영상을 가로, 세로 방향으로 특정 크기만큼 이동시키는 변환으로 이동시키려는 거리를 지정해야함.

새로운 좌표 (x', y')에 대해 x'=x+a, y'=y+b로 표현가능하고 이를 행렬식으로 바꾸면 ![1](C:\Users\hkcho\Desktop\폴더\자료\공부 자료\tmp\1.png)

<br>

**확대/축소**

영상을 확대/축소하려는 가로/세로 비율을 지정해야함.

x'=a*x, y'=b*y로 표현가능하고 이를 행렬식으로 바꾸면 ![2](C:\Users\hkcho\Desktop\폴더\자료\공부 자료\tmp\2.png)

```python
dst=cv2.resize(src, dsize, dst, fx, fy, interpolation)
```

변환 행렬을 생성해 warpAffine()을 호출하지 않아도 resize()로 확대/축소 가능.

결과 영상의 크기를 (width, height)로 dsize에 전달하며 (0, 0) 전달시 fx와 fy를 적용.

x와 y의 크기 배율을 지정하며 생략하면 dsize를 적용.
