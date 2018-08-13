# DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤, 문자열 내에서 홀수가 연속되면
# 두 수 사이에 - 를 추가하고, 짝수가 연속되면 * 를 추가하는 기능을 갖고 있다.
# (예, 454 => 454, 4546793 => 454*67-9-3) DashInsert 함수를 완성하자. 출처
#
# 입력 - 화면에서 숫자로 된 문자열을 입력받는다.
# "4546793"
# 출력 - *, -가 적절히 추가된 문자열을 화면에 출력한다.
# "454*67-9-3"

def Dashinsert(number):
    storage = ""
    lengh = len(number)

    for A in range(0,lengh):
        if number[A] == number[-1]:
            storage += number[-1]
        else:
            if int(number[A]) % 2 == 0 and int(number[A+1]) % 2 == 0:
                storage += number[A] +'*'
            elif int(number[A]) % 2 == 1 and int(number[A+1]) % 2 == 1:
                storage += number[A] +'-'
            else:
                storage += number[A]

    return storage

while True:
    number = input("숫자를 입력하세요:")
    print(Dashinsert(number))

# 리스트로 처리하기
# i = list(map(int,' '.join(input()).split()))
# answer = [str(i[0])]
# for x in range(len(i)-1):
#     if i[x]%2==0 and i[x+1]%2==0:
#         answer.append('*')
#     if i[x]%2==1 and i[x+1]%2==1:
#         answer.append('-')
#     answer.append(str(i[x+1]))
# print(''.join(answer))