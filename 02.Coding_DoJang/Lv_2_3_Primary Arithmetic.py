# 첫 번째 계산
#
# 아이들은 여러 자리 숫자들을 더하기 위해서 우에서 좌로 숫자를 하나씩 차례대로 더 하라고 배웠다.
# 1을 한 숫자 위치에서 다음 자리로 더하기위해 이동하는 "한자리올림"연산을 많이 발견하는 것은 중요한 도전이 된다.
# 당신의 일은 교육자가 그들의 어려움을 평가하기 위하여,
# 덧셈 문제들의 각 집합에 대해서 한자리올림 연산들의 수를 계산하는 것이다.
#
# 입력
#
# 입력의 각 라인은 10개의 숫자들보다 미만인 양의 정수들 두 개를 포함한다. 입력의 마지막 라인은 0 0 을 포한한다.
#
# 출력
#
# 마지막을 제외한 입력의 각 라인에 대해서 당신은 두 숫자들을 더한 결과에서
# 한자리올림 연산들의 수를 아래 처럼 보여지는 형식으로 계산하여 출력해야 한다.
#
# 입력 샘플
#
# 123 456
# 555 555
# 123 594
# 0 0

# 출력 샘플
#
# No carry operation.
# 3 carry operations.
# 1 carry operation
def arithmetic(list):
    for i in range(len(list)):
        count = 0
        split_list = list[i].split()
        number_liter = ''.join(split_list)
        number_list = [int(i) for i in number_liter]

        for A in range(0,len(number_list)):
            if A >= 3:
                break
            else:
                if number_list[A] + number_list[A+3] >= 10:
                    count += 1

        if count == 0:
            print('No carry operation')
        else:
            print('%d carry operation' % count)

print('숫자를 입력하세요:')
list = []

while True:
    number = str(input())
    if number == "0 0":
        break
    else:
        list.append(number)

arithmetic(list)

# def primary_arithmetic(num1, num2):
#     carry = 0
#     carry_sense = False
#     n1 = str(num1)
#     n2 = str(num2)
#     for i in range(1, len(n1)+1):
#         if (int(n1[-i]) + int(n2[-i]) > 9) or (int(n1[-i]) + int(n2[-i]) > 8 and carry_sense == True) :
#             carry += 1
#             carry_sense = True
#         else : carry_sense = False
#     if carry == 0: return "No"
#     return carry
#
# print(primary_arithmetic(234, 769), "carry operation.")