import numpy as np # 시그모이드 함수란 어떤 수가 오더라도 0과 1사이에 수가 오게 만든다.
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1+np.exp(-x))