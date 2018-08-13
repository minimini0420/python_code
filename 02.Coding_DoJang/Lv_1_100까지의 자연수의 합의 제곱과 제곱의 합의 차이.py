# 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다
# (제곱의 합). 1^2 + 2^2 + ... + 10^2 = 385 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다
# (합의 제곱). (1 + 2 + ... + 10)^2 = 55^2 = 3025
# 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의 차이는 3025 - 385 = 2640 이 됩니다.
# 그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마입니까?

def natural_number(number):
    sum_avg = ""
    square_sum = ""

    for i in range(1,number+1):
        sum_avg += str(i)
        square = "%s**2" % i
        square_sum += str(eval(square))
        if i < number:
            sum_avg += "+"
            square_sum += '+'

    sum_square = eval(sum_avg)**2
    total =  sum_square - eval(square_sum)
    return total

while True:
    number = int(input('자연수를 입력하세요.:'))
    print(natural_number(number))

# 코딩도장 풀이
# def problem(n):
#     sumfirst = 0
#     squrefirst = 0
#     for i in range(1,n+1):
#         sumfirst += i
#         squrefirst += i**2
#     sumfirst = sumfirst**2
#
#     return sumfirst - squrefirst