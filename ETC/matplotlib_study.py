import matplotlib.pyplot as plt
import numpy as np

plt.title("test")
plt.plot([1, 2, 3, 4], [10, 20, 30, 40], label="test1")
plt.plot([1.5, 2.5, 3.5, 4.5], [20, 30, 40, 50], label="test2")
# 첫번째 매개변수가 x축, 두번째 매개변수가 y축
# plot()에서 label 문자열 지정하고 legend() 호출

plt.xlabel("x_label")   # x축 레이블 설정
plt.ylabel("y_label")   # y축 레이블 설정
plt.legend(loc="lower right")   # loc에 upper left도 가능, 디폴트값이 upper left
plt.show()


plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
plt.xlim(0, 5)   # x축 범위를 지정하며 plt.ylim((0, 5))나 plt.ylim([0, 5])도 가능
plt.ylim(0, 50)   # # y축 범위를 지정하며 plt.ylim((0, 5))나 plt.ylim([0, 5])도 가능
# plt.axis([xmin, xmax, ymin, ymax])로 한번에 쓸 수 있음
plt.show()


"-", "--", ":", "-."으로 선 종류 설정
plt.plot([1, 2, 3, 4], [1, 1, 1, 1], "-", label="Solid")
plt.plot([1, 2, 3, 4], [2, 2, 2, 2], "--", label="Dashed")
plt.plot([1, 2, 3, 4], [3, 3, 3, 3], ":", label="Dotted")
plt.plot([1, 2, 3, 4], [4, 4, 4, 4], "-.", label="Dash-dot")
plt.show()


마커 표현하기
plt.plot([1, 2, 3, 4], [10, 20, 30, 40], "bo")   # b는 파란색, o는 동그라미를 의미
plt.show()


마커와 선을 같이 표현하기
plt.plot([1, 2, 3, 4], [10, 20, 30, 40], "bo-")   # b는 파란색, o는 동그라미, -는 실선
plt.plot([1, 2, 3, 4], [20, 30, 40, 50], "bo--")   # b는 파란색, o는 동그라미, --는 점선
plt.show()


산점도 그리기
x = np.random.randn(20)
y = np.random.rand(20)
plt.scatter(x, y)
plt.show()