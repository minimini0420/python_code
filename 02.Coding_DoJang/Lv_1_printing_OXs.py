# (앞의 문제들 중 비슷한 알고리즘이 있던 것 같지만, 같은 건 없다고 생각해서 올립니다.)
# input은 int n을 입력 받아 첫번째 row는 (n-1)의 O와 X, 두번째 row는 (n-2)의 O와 XX, 세번째 row는 (n-3)의 0와
# XXX... n번째 row는 n의 X을 출력하시오.
#
# 입력 예시: 6
#
# 출력 예시:
# OOOOOX
# OOOOXX
# OOOXXX
# OOXXXX
# OXXXXX
# XXXXXX

n = int(input('input n : '))

for i in range(1, n+1):
    print('O'*(n-i) + 'X'*i)