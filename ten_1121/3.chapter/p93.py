import numpy as np

a = np.array([1010,1000,990])

print(np.exp(a)/np.sum(np.exp(a)))
c = np.max(a)
print(a - c)

y = np.exp(a-c)/np.sum(np.exp(a-c))
print(y)


def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return   y

a = np.array([0.3, 2.9, 4.0])
y =softmax(a)
print(y)
print(np.sum(y))