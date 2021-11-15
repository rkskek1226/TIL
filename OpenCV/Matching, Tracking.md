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
