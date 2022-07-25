import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

fruits = np.load("dataset/fruits_300.npy")
print(fruits.shape)
fruits = fruits.reshape(-1, 10000)
print(fruits.shape)

pca = PCA(n_components=50)  # n_components에서 주성분의 개수를 지정
pca.fit(fruits)
print(pca.components_.shape)  # (50, 10000)으로 n_components가 50인 것과 데이터의 특성 개수인 10000


def draw_fruit(arr, ratio=1):
    n = len(arr)
    arr = arr.reshape(-1, 100, 100)
    rows = int(np.ceil(n / 10))
    cols = n if rows < 2 else 10

    fig, axs = plt.subplots(rows, cols, figsize=(cols * ratio, rows * ratio), squeeze=False)

    for i in range(rows):
        for j in range(cols):
            if 10 * i + j < n:
                axs[i, j].imshow(arr[i * 10 + j], cmap="gray_r")
            axs[i, j].axis("off")

    plt.show()


draw_fruit(pca.components_)

# 50개의 주성분으로 전체 데이터 특성의 개수인 10000개를 50개로 축소시킬 수 있음

print(fruits.shape)
fruits_pca = pca.transform(fruits)  # transform()으로 차원을 축소시킴(10000개 -> 50개)
print(fruits_pca.shape)

fruits_inverse = pca.inverse_transform(fruits_pca)   # inverse_transform()으로 원래 차원으로 복원할 수 있음
print(fruits_inverse.shape)

draw_fruit(fruits_inverse)   # 그림을 확인해보면 원본만큼은 아니지만 잘 복원되었음

