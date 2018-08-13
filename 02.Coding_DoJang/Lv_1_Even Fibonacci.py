# 피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# 짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?

def Fibonacci(num):
    if num == 1 or num == 2:
        return 1
    return Fibonacci(num-1) + Fibonacci(num-2)

num = 1
sum = 0
list =[]

while True:
    if Fibonacci(num) < 4000001:
        list.append(Fibonacci(num))
        num += 1
    else: break

list = sorted(list)
for i in list:
    if i % 2 == 0:
        sum += i
print(sum)