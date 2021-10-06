# OpenCV

[OpenCV ](https://opencv.org)

[OpenCV 함수](https://docs.opencv.org/master)





이미지는 음수나 소수점이 없고 값의 크기가 최대 255이므로 부호없는 8비트, uint8을 데이터 타입으로 사용

NumPy 배열은 이미지를 행(row)과 열(column)의 순서로 접근하므로 이미지의 높이(height)와 폭(width)의 순서로 지정해야함





관심영역(ROI) 지정 함수

```python
ret=cv2.selectROI()
```

마우스로 ROI를 지정하고 스페이스 키나 엔터 키를 누르면 x, y, width, height 값을 튜플로 리턴







