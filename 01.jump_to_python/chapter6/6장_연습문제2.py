def Duplicate(numbers): # 이걸 왜 참신하게 짰다고 하셨을까?????
    T='True'
    F='False'
    A=['0','1','2','3','4','5','6','7','8','9']
    result=""
    Total = numbers.split()
    for i in Total:
        if A == sorted(i):
            result += T + ' '
        else:
            result += F + ' '
    return result


while True:
    numbers=str(input('0 ~ 9 까지의 숫자를 입력하세요.\n'))
    print(Duplicate(numbers))
