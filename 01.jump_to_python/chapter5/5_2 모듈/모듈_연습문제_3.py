# <연습 문제3>
# 사용자에게 숫자를 입력받고 그 숫자가 10의 배수인지를 확인하는 함수를 작성하시오
# "양수를 입력하세요 (종료-1): "
# -1 입력 받을 때까지 무한 반복하시오.
def multiple(number):
    if  number % 10 == 0:
        return "10의 배수입니다." # 리턴 값에 print를 넣으면 나중에 따로 출력하지 않아도 된다.
    else:
        return "10의 배수가 아닙니다."

while True:
    number = (int(input("양수를 입력하세요. (종료 -1):\n")))
    if number == -1:
        break
    else:
        print(multiple(number))










