import numpy as np
# A = np.array([1,2,3,4])
# print(A)
# print(np.ndim(A))
# print(A.shape)
# print(A.shape[0])               # A.shape[0][0] 행의 갯수, 열의 갯수
#
# A = np.array([[1,2], [3,4]])
# print(A.shape)
#
# B = np.array([[5,6],[7,8]])
# print(B.shape)
# print(np.dot(A,B))
#
# C = np.array([[1,2],[3,4],[5,6]])
# print(C)
# print(np.ndim(C))
# print(C.shape)

# 행렬의 내적 제곱
A = np.array([[1,2,3],[4,5,6]])
print(A.shape)

B = np.array([[1,2],[3,4],[5,6]])
print(B.shape)

print(np.dot(A,B))

C = np.array([[1,2],[3,4]])
print(C.shape)
print(A.shape)
print(np.dot(A,C))              # why?? 앞에 렬과 뒤의 행의 원소 갯수가 동일 해야한다.