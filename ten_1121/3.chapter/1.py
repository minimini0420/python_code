import numpy as np # 0보다 작은 수는 전부 0으로 나타내주는 함수
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x)

x = np.arange(-6, 6.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-0.1, 5) # y측 범위 지정
plt.show()