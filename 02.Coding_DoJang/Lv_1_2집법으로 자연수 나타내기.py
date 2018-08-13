# 2진법이란, 어떤 자연수를 0과 1로만 나타내는 것이다.
# 예를 들어 73은 64(2^6)+8(2^3)+1(2^0)이기 때문에 1001001으로 표현한다.
# 어떤 숫자를 입력받았을 때 그 숫자를 2진법으로 출력하는 프로그램을 작성하시오.

while True:
    number = int(input('숫자를 입력하세요.:'))
    print(bin(number))
    
#  코딩 도장 정답!!!

# a = int(input())
# b = []
# while a:
#     b.append(a%2)
#     a = int(a/2)
#
# b.reverse()
# print(b)