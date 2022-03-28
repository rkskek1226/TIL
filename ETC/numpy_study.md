# numpy

dtype은 옵션이므로 지정안해도 됨

a1=np.array([1,2,3],dtype=np.int8)

a2=np.empty((2,3),dtype=np.uint8)

a2.fill(255)

a3=np.zeros((2,3),dtype=np.uint8)

a4=np.ones((2,3),dtype=np.uint8)

a5=np.full((2,3,4),100,dtype=np.uint8)

<br><br>

img=cv2.imread("0.png")

b1=np.empty_like(img)

b2=np.zeros_like(img)

b3=np.ones_like(img)

b4=np.full_like(img,100)

<br>

<br>

c1=np.arange(0,10)   # np.arange(10)과 같음

c2=np.random.rand(2,3)   # np.random.rand()는 0~1 사이의 값을 랜덤으로 생성

c3=np.random.rand()

c4=np.random.randn(2,3)   # np.random.randn()는 평균이 0이고 분산이 1인 정규 분포를 따르는 값을 랜덤으로 생성

c5=np.random.randn()

<br>

<br>

d1=np.arange(5).astype(np.float32)   # astype()으로 데이터 타입을 변경

e1=np.arange(12).reshape(3,4)   # reshape()으로 차원을 변경

e1=e1.T # T로 전치행렬 생성

e1=e1.ravel()   # ravel()으로 1차원 배열로 차원을 변경, flatten()도 1차원으로 차원을 변경해줌

<br>

<br>

f1=np.arange(4).reshape(2,2)

f2=np.arange(10,14).reshape(2,2)

f3=np.vstack((f1,f2))   # vstack()으로 수직 병합

f4=np.hstack((f1,f2))   # hstack()으로 수평 병합

f5=np.vsplit(f3,2)   # vsplit()으로 수직으로 분리

f6=np.hsplit(f4,2)   # hsplit()으로 수평으로 분리

<br>

<br>

g1=np.arange(10,20)

g2=np.where(g1>15)   # g1>15 조건을 만족하는 요소의 인덱스를 리턴

g3=np.where(g1>15,1,0)   # g1>15 조건을 만족하면 1로, 아니면 0인 배열을 리턴

g4=np.where(g1>15,1,g1)   # g1>15 조건을 만족하면 1로, 아니면 그대로인 배열을 리턴

g5=np.where(g1>15,g1,1)   # g1>15 조건을 만족하면 그대로, 아니면 1인 배열을 리턴

<br>

<br>

h1=np.arange(12).reshape(3,4)

h2=h1.sum()   # sum()으로 h1 배열의 전체 요소의 합을 리턴

h3=h1.sum(0)   # sum(0)으로 h1 배열의 axis=0(수직)의 합을 리턴

h4=h1.sum(1)   # sum(1)으로 h1 배열의 axis=1(수평)의 합을 리턴

h5=h1.mean()   # mean()으로 h1 배열의 평균을 리턴

h6=h1.mean(0)   # mean(0)으로 h1 배열의 axix=0(수직)의 평균을 리턴

h7=h1.min()   # min()으로 h1 배열의 최소값을 리턴

h8=h1.min(1)   # min(1)으로 h1 배열의 axis=1(수평)의 최소값을 리턴

h9=h1.max()   # max()로 h1 배열의 최대값을 리턴

h10=h1.max(0)   # max(0)으로 h1 배열의 axis=0(수직)의 최대값을 리턴