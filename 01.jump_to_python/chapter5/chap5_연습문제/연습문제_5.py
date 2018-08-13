# <연습문제 5: 사칙 연산 계산기 작성>
# 연습문제 4에서 뺄셈, 곱셈, 나눗셈을 추가한다.
# 특별히 나눗셈에서 나누는 수가 0일 경우의 예외처리를 except에서 아래 메세지를 출력하게 한다.
# "죄송합니다. 두 번쨰 입력에서 0을 입력하셨습니다. 분모는 0이 되어서는 안됩니다."

def sum(a,b):
    return a+b
def mul(a,b):
    return a*b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b

while True:
    number=str(input('안녕하세요 두 수를 입력하세요.(종료: 프로그램 종료):\n'))
    if number =='종료':
        break
    else:
        number_list = number.split()
        A=number_list[0]
        B=number_list[1]
        try:
            a = int(number_list[0])
        except:
            print('죄송합니다. 첫번째 입력이 "[%s]"입니다. 숫자를 입력하세요' % A) # %s가 문자열이기 때문에 문자열에 해당하는 변수를 만들어줘야한다.
        try:
            b = int(number_list[1])
        except:
            print('죄송합니다. 두번째 입력이 "[%s]"입니다. 숫자를 입력하세요' % B) # 이것 또한 위의 것과 같다고 볼 수 있다.
        try:
            div(a,b)
        except ZeroDivisionError:
            print('죄송합니다. 두번째 입력이 "[%d]"을 입력하셨습니다. 분모는 0이 되어서는 안됩니다.' % b)
        else:
            print(sum(a,b))
            print(mul(a,b))
            print(sub(a,b))
            print(int(div(a,b)))