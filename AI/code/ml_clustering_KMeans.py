import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

fruits = np.load("dataset/fruits_300.npy")
print(fruits.shape)
fruits = fruits.reshape(300, 100 * 100)


def draw_fruit(arr, ratio=1):
    n = len(arr)
    arr = arr.reshape(-1, 100, 100)
    rows = int(np.ceil(n/10))
    cols = n if rows < 2 else 10

    fig, axs = plt.subplots(rows, cols, figsize=(cols * ratio, rows * ratio), squeeze=False)

    for i in range(rows):
        for j in range(cols):
            if 10 * i + j < n:
                axs[i, j].imshow(arr[i * 10 + j], cmap="gray_r")
            axs[i, j].axis("off")

    plt.show()


inertia = []

for k in range(1, 10):
    km = KMeans(n_clusters=k, random_state=1)
    km.fit(fruits)
    inertia.append(km.inertia_)

plt.plot(range(1, 10), inertia)
plt.xlabel("num of cluster")
plt.ylabel("inertia")
plt.show()

best = inertia.index(min(inertia))
print(best)
print(inertia)

km = KMeans(n_clusters=best, random_state=1)   # n_clusters로 클러스터 개수를 지정
km.fit(fruits)

draw_fruit(fruits[[km.labels_ == 1]])















