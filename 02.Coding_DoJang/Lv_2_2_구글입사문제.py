# 1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
#
# 8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
# (※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)

list = []
count = 0
for i in range(1,10001):
    i = ','.join(str(i)).split(',')
    for A in range(0,len(i)):
        if i[A] == '8':
            count += 1
print(count)

# 코딩 도장 답
# print(str(list(range(1, 10001))).count('8'))