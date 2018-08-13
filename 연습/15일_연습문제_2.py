# [연습문제 2]
# 특정 범위내에서 첫 번째수와 두번째 수 배수의 총합을 구하는 프로그램을 작성하시오.
# 입력예)
# "범위, 첫 번째 수, 두 번째 수를 입력하세요.(종료: 프로그램 종료): 15 3 5"
# 0부터 15이하의 범위를 선택하셨습니다. 이 중에서
# 3의 배수는 3,6,9,12,15 입니다.
# 5의 배수는 5,10,15 입니다.
# 3과 5의 배수는 3,5,6,9,10,12,15입니다.
# 따라서 0부터 15이하의 범위내에서 3과 5의 배수의 총합은 60입니다.
def finder(number):
    c = number.split()
    d = list(map(int, c))
    A = d[0]
    B = d[1]
    C = d[2]
    result1 = ""
    result2 = ""
    result3 = ""
    sum = 0

    for i in range(1, A + 1):
        if i % B == 0:
            result1 += str(i) + ' '
    print('%s의 배수는 %s 입니다.' % (str(B), ','.join(result1.split())))

    for i in range(1, A + 1):
        if i % C == 0:
            result2 += str(i) + ' '
    print('%s의 배수는 %s 입니다.' % (str(C), ','.join(result2.split())))

    for i in range(1, A + 1):
        if i % B == 0 or i % C == 0:
            sum += i

    total = result1.split() + result2.split()
    total1 = list(set(total))
    Total = sorted(list(map(int, total1)))

    for i in Total:
        result3 += str(i) + ' '

    print('%s과 %s의 배수는 %s 입니다.' % (str(B), str(C), ','.join(result3.split())))
    print('따라서 0 부터 %s 이하의 범위 내에서 %s과 %s의 배수의 총합은 %s입니다.' %(str(A),str(B),str(C),sum))

while True:
    number = input("범위, 첫번째수, 두번째 수를 입력하세요. (종료: 프로그램 종료):\n")
    if number == '종료':
        print('이용해주셔서 감사드립니다.')
        break
    else:
        finder(number)