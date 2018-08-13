import numpy as np

# A = np.array([1,2,3,4]) # 1차원 배열
# print(A)
# print(np.ndim(A)) # 배열의 차원 수
# print(A.shape) # 배열의 형상
# print(A.shape[0])

# B = np.array([[1,2], [3,4], [5,6]])
# print(B)
# print(np.ndim(B))
# print(B.shape)

# 행렬의 내적(행렬 곱)
# A = np.array([[1,2], [3,4]]) # 2*2 행렬 곱
# B = np.array([[5,6], [7,8]])
# print(np.dot(A,B)) # 내적을 스칼라곱 혹은 점곱이라고도 함. 그래서 dot를 씀.

# A = np.array([[1,2,3], [4,5,6]]) # 2*3, 3*2 행렬 곱
# B = np.array([[1,2],[3,4],[5,6]]) # 주의점 행렬 A의 1번쨰 차원의 원소 수(열수)와 행렬 B의 0번째 차원의 수(행수)가 같아야 함.
# print(np.dot(A,B))

# 오류의 예
# C = np.array([[1,2],[3,4]])
# A = np.array([[1,2,3], [4,5,6]])
# print(np.dot(A,C)) # ValueError: shapes (2,3) and (2,2) not aligned: 3 (dim 1) != 2 (dim 0)

# A가 2차원 행렬, B가 1차원 배열일 때도 같다.
# A = np.array([[1,2],[3,4],[5,6]])
# B = np.array([7,8])
# print(np.dot(A,B))

# 신경망의 내적
X = np.array([1,2])
W = np.array([[1,3,5],[2,4,6]])
Y = np.dot(X,W)
print(Y)