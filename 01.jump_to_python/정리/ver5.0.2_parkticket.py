count=0
guest=0
Free=3
discount=5
fee=0
grade=''
while True:
    age = int(input("나이를 입력하세요."))
    if age <= 0:
        continue
    if 0 < age < 4:
        print("귀하의 등급은 %s이며, 요금은 %s 입니다." % ('유아', '무료'))
        print("감사합니다. 티켓을 발행합니다.")
    elif 3 < age <= 13:
        print("귀하의 등급은 %s이며 요금은 %d원 입니다." % ('어린이', 2000))
        grade = '어린이'
        fee = 2000
    elif 4 < age <= 18:
        print("귀하의 등급은 %s이며 요금은 %d원 입니다." % ('청소년', 3000))
        grade = '청소년'
        fee = 3000
    elif 18 < age <= 65:
        print("귀하의 등급은 %s이며 요금은 %d원 입니다." % ('성인', 5000))
        grade = '성인'
        fee=5000
    elif age > 65:
        print('귀하는 %s 등급이며 요금은 %s 입니다.'% ('노인','무료'))
        grade='노인'
        print("감사합니다. 티켓을 발행합니다.")

    if 3 < age < 66:
        print("요금 유형을 선택하세요. (1:현금, 2:공원 전용 신용카드)")
        type=int(input())
        if type > 2 :
            continue
        if type == 1:
            pay = int(input("요금을 입력하세요."))
            if pay == fee:
                print("감사합니다. 티켓을 발행합니다.")
            elif pay > fee:
                print("감사합니다 티켓을 발행하고 거스름돈 %d원을 반환합니다." % (pay - fee))
            elif pay < fee:
                print("%d원이 부족합니다. 입력 하신 %d를 반환합니다." % (pay -fee, pay))
                continue
        elif type ==2:
            print("(결제 금액의 10% 할인, 60~65세 장년은 추가 5% 할인)")
            if age>=60 and age<=65:
                fee=fee*0.9
                fee=fee*0.95
            else:
                fee=fee*0.9
        print('%d원 결제 되었습니다. 티켓을 발행합니다.'% fee)
    guest+=1
    print('입장수 : %d' % guest)

    if 3<age<66:
        count += 1
        if 0 == count % 7:
            Free -= 1
            if Free < 0:
                continue
            print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기에 무료 티켓을 발행합니다. 잔여 무료 티켓 %d장" % Free)
        elif 0 == count % 4 :
            discount -= 1
            if discount < 0:
                continue
            print("축하합니다. 연간 회원권에 당첨되었습니다. 여기에 연간 회원권을 발행합니다. 잔여 무료 티켓 %d장" % discount)
