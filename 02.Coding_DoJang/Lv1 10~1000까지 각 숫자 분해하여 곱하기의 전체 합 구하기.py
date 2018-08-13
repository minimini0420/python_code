# 예로, 10~15까지의 각 숫자 분해하여 곱하기의 전체 합은 다음과 같다.
#
# 10 = 1 * 0 = 0
# 11 = 1 * 1 = 1
# 12 = 1 * 2 = 2
# 13 = 1 * 3 = 3
# 14 = 1 * 4 = 4
# 15 = 1 * 5 = 5
#
# 그러므로, 이 경우의 답은 0+1+2+3+4+5 = 15

# num = []
# for i in range(10,1000+1):
#     s = list(str(i))
#     s = '*'.join(s)
#     num.append(eval(s))
# print(sum(num))

while True:
    number = str(input('범위를 가정할 숫자 두개를 입력하세요:'))
    number_range = number.split()
    num = []
    for i in range(int(number_range[0]),int(number_range[1])+1):
       sum1 = list(str(i))
       sum1 = '*'.join(sum1)
       num.append(eval(sum1))
    print(sum(num))



