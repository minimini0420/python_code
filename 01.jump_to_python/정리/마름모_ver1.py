print('마름모 프로그램 ver1.0')
i='*'
blank=' '
while True:
    print("홀수를 입력하세요. ( 0 <---- 종료 )")
    number = int(input())
    if number == 0:
        print('마름모 프로그램을 이용해주셔서 감사합니다.')
        break
    elif number % 2 == 0:
        print('짝수를 입력했습니다. 다시 입력하세요')
        continue
    else:
        i_count=1
        b_count=int((number-i_count)/2)
        while True:
            print(blank*b_count,end='')
            print(i*i_count)
            if number == i_count:
                break
            i_count +=2
            b_count -=1
        while True:
            b_count +=1
            i_count -=2
            print(blank*b_count,end='')
            print(i*i_count)
            if i_count < 0:
                break












