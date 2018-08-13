import matplotlib.pyplot as plt

# Partimer Fee data-sets
x_datas = [3, 7, 2, 8, 3, 8, 8, 1, 4, 1]    # 독립변수
y_datas = [23000, 55000, 15000, 60000, 28000, 64000, 66000, 9000, 29000, 7000]  # 종속변수

w = 1

plt.plot(x_datas, y_datas, '+')
plt.show()

def hypothesis(x):          # hyopthesis = 가설
    global w
    return w * x

def loss(x, y):
    return hypothesis(x) - y

def cost(w):
    global x_datas,y_datas
    m = len(x_datas)

    sum = 0
    for x,y in zip(x_datas,y_datas):
#    for m, (x,y) in enumerate(zip(x_datas,y_datas)):   # enumerate  사용법
        sum = sum +(w*x - y)**2         # Python에서만 **이 제곱이다.
    return sum / (m)

# zip 설명
# for y, x in zip(ys, xs):
#       print('sum : ", y+x)
# ys, xs를 합쳐서 y,s에 전달

weights = list(range(3000, 10000))
costs = []
for weight in weights:
    c = cost(weight)
    costs.append(c)

plt.plot(weights,costs)
plt.show()
