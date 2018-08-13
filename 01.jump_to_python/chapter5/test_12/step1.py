# step 1
print('3개의 숫자를 입력하세요:')
if(int(input('3개의 숫자를 입력하세요:').split()))==-1:
    print('종료합니다.')

# step2
print('3개의 숫자를 입력하세요:')
input_numbers=input()
input_number_list=input_numbers.split()
number=int(input_number_list)
if(number==-1):
    print('종료합니다.')

# step3 디버거에서 문제가 나는 라인을 찾는다.

# step4 문제가 발생한 입력값으로 최소한의 프로그램을 작성한다.
int('1 2 3')
# 정상적으로 입력했을때 동작하는 함수 실행과
int('123')
# 문제의 원인을 찾는다.