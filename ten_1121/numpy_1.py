import numpy as np
import matplotlib.pyplot as plt

# 10개의 float32 자료형 데이터 생성
v = np.zeros(10, dtype=np.float32)
print(v)
print("")
# 연속된 10개의 unit 64 자료형 데이터 생성
v = np.arange(10, dtype=np.uint64) # uint == unsigend int
print(v)
print("")
v*=3
print("result")
print(v)
print("")
# v의 평균 구하기
print("result")
print(v.mean())

num_point = 1000
vectors_set = []

for i in range(num_point):
    x1 = np.random.normal(0.0,0.55)
    y1 = x1 * 0.1 + 0.3 + np.random.normal(0.0,0.033)
    vectors_set.append([x1,y1])

x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]

print(x_data)
print(y_data)

# 그래픽 표시
plt.plot(x_data, y_data, 'mo')
plt.show()
