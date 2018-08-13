import numpy as np
x = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

print(W1.shape)
print(x.shape)
print(B1.shape)

A1 = np.dot(x, W1) + B1

import numpy as np # 시그모이드 함수란 어떤 수가 오더라도 0과 1사이에 수가 오게 만든다.
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1+np.exp(-x))

Z1 = sigmoid(A1)
print(A1)
print(Z1)

W2 = np.array([[0.1, 0.4],[0.2, 0.5],[0.3,0.6]])
B2 = np.array([0.1,0.2])

print(Z1.shape)
print(W2.shape)
print(B2.shape)

A2 = np.dot(Z1,W2) + B2
Z2 = sigmoid(A2)


