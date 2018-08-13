# [연습문제1]
# 숫자를 입력 받으면 해당 숫자의 전체 구구단 중에서
# 해당 단만 출력하는 프로그램을 작성하라.
# 예) 숫자를 입력하세요. (-1: 종료, all: 구구단 전체 출력): 2
# < 2단 >
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 2 * 6 = 12
# 2 * 7 = 14
# 2 * 8 = 16
# 2 * 9 = 18
# 숫자가 음수가 들어 왔을 때 ValueError exception을 raise 하여 예외 처리 할 것!
# all을 입력하면 2단 부터 9단 까지 모두 출력하시오.
def GuGuDan(N):
    result =[]
    number_A = 1
    print("< %s단 >" % N)

    for i in range(1,10):
        result.append(N * i)
        i += 1

    for i in result:
        print("%s * %s = %s" % ( N, number_A, i))
        number_A += 1

while True:
    N = input('숫자를 입력하세요.(-1: 종료, all: 구구단 전체 출력:)')

    if N == "all":
        for i in range(2,10):
            GuGuDan(i)
    else:
        try:
            N=int(N)
            if -1 == N:
                print('프로그램을 종료합니다.')
                break
            elif N < 0:
                raise ValueError('음수를 사용할 수 없습니다.')
            else:
                GuGuDan(N)
        except ValueError as e:
            print('오류 발생:', e.args[0])