# 영상 분할(Image Segmentation)

**컨투어(contour)**

같은 색상이나 밝기의 연속된 점을 찾아 잇는 곡선.

컨투어를 찾아 모양 분석이나 객체 인식에 사용.









<br>

**레이블링(Labeling)(Connedted component labeling)**

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

