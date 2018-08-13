guest=0
free_ticket = 3  # 7번째마다 주는 티켓, 초기값인 잔여티켓
sale_ticket = 5  # 4번째마다 주는 티켓
while True:
    while True:
        print('나이를 입력하세요.')
        age=int(input())
        if age<0:
            print('입력오류')
            continue
        else:
            break
    fee=0
    grade=''

    if age<4:
        print('귀하는 %s 등급이며 요금은 % d 원 입니다.' %('유아',0))
        grade='유아'
    elif age>=4 and age<=13:
        print('귀하는 %s 등급이며 요금은 % d원 입니다.' % ('어린이',2000))
        fee=2000
        grade='어린이'
    elif age>13 and age<=18:
        print('귀하는 %s 등급이며 요금은 % d원 입니다.'% ('청소년',3000))
        fee=3000
        grade='청소년'
    elif age>18 and age<=65:
        print('귀하는 %s 등급이며 요금은 % d원 입니다.'% ('성인',5000))
        fee=5000
        grade='성인'
    else :
        print('귀하는 %s 등급이며 요금은 % d원 입니다.'% ('노인',0))
        grade='노인'

    print('요금 유형을 선택하세요.(1: 현금, 2:공원 전용 신용 카드')
    case=int(input())
    if case==1:
        print('요금을 입력하세요.')
        money=int(input())
        if fee<money:
            print('"감사합니다. 티켓을 발행하고 거스름돈 %d원을 반환합니다."' % int(money-fee))
            guest+=1
            if guest % 7 == 0:
                free_ticket -= 1
                print('"축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %d장"' % free_ticket)
            elif guest % 4 == 0:
                sale_ticket -= 1
                print('"축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장"' % sale_ticket)
        elif fee==money:
            print('"감사합니다. 티켓을 발행합니다."')
            guest+=1
            if guest % 7 == 0:
                free_ticket -= 1
                print('"축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %d장"' % free_ticket)
            elif guest % 4 == 0:
                sale_ticket -= 1
                print('"축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장"' % sale_ticket)
        else:
            print('"%d원 모자랍니다. 입력하신 %d원을 반환합니다."'%(fee-money,money))
    elif case==2:
        print("(결제 금액의 10% 할인, 60~65세 장년은 추가 5% 할인)")
        #print('그냥 fee: %d'%fee)
        if age>=60 and age<=65:
            fee=fee*0.9
            fee=fee*0.95
        else:
            fee=fee*0.9
        print('%d원 결제 되었습니다. 티켓을 발행합니다.'% fee)
        guest+=1
        if guest % 7 == 0:
            free_ticket -= 1
            print('"축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 %d장"' % free_ticket)
        elif guest % 4 == 0:
            sale_ticket -= 1
            print('"축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 %d장"' % sale_ticket)
    print('손님수: %d' %guest)