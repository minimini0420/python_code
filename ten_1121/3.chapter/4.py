import numpy as np # 시그모이드 함수란 어떤 수가 오더라도 0과 1사이에 수가 오게 만든다.
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1+np.exp(-x))

# x = np.array([-1.0, 1.0, 2.0]) # 20부터 1이라는 숫자가 나오기 시작한다.
# print(sigmoid(x)) # 넘파이 배열 확인

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y측 범위 지정
plt.show()