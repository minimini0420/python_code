# 어떤 정수 n에서 시작해, n이 짝수면 2로 나누고, 홀수면 3을 곱한 다음 1을 더한다.
# 이렇게 해서 새로 만들어진 숫자를 n으로 놓고, n=1 이 될때까지 같은 작업을 계속 반복한다.
#
# 예를 들어, n=22이면 다음과 같은 수열이 만들어진다.
#
# 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
#
# n이라는 값이 입력되었을때 1이 나올때까지 만들어진 수의 개수(1을 포함)를 n의 사이클 길이라고 한다.
# 위에 있는 수열을 예로 들면 22의 사이클 길이는 16이다. i와 j라는 두개의 수가 주어졌을때,
# i와 j사이의 모든 수(i, j포함)에 대해 최대 사이클 길이를 구하라.
#
# 입력 예
#
# 1    10
# 100  200
# 201  210
# 900  1000
# 출력 예
#
# 1    10    20
# 100  200   125
# 201  210   89
# 900  1000  174
# ※ 참고
#
# 어떤 자연수 n에 대해서도, 이 조작을 유한 번 시행하면 1이 될 것이라고 예상하는데,
# 700,000,000,000보다 작은 모든 짝수에 대해 성립한다는 것이 밝혀져 있긴 하지만,
# 아직 아무도 증명하지 못했습니다.
# 유명한 헝가리 수학자 폴 에르되시(Paul Erd' os)는,
# "우리의 수학은 아직 이 문제를 풀 준비가 되어 있지 않다." 라고 했습니다.

def lengh(number):
    list = [number]

    while True:

        if number == 1:
            break
        elif number % 2 == 1:
            number_again = (number * 3) + 1
            number = number_again
            list.append(number)

        elif number % 2 == 0:
            number_again = number//2
            number = number_again
            list.append(number)

    return list

while True:
    number_string = input('숫자를 입력하세요: ')
    number_list = [int(i) for i in number_string.split()]
    new_list = []

    for i in range(number_list[0],number_list[1]+1):
       new_list.append(len(lengh(i)))

    print(max(new_list))

