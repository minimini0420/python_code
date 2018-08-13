count=0
Free=3
discount=5
while True:
    age = int(input("How old are you?"))
    if 0 < age < 4:
        print("Your grade is %s, Just %s." % ("kids", "Free"))
        print("Thank you!! I'll give you the ticket.")
        count=count+1
        if 0 == count % 7:
            Free=Free-1
            print("Congratulation!!. You won a special event!!. Here is ticket for one time free. Remaining ticket[%d]ea" % Free)
        elif 0 == count % 4:
            discount=discount-1
            print("congratulation!!. You won a ticket for membership yearly. Remaining ticket [%d]ea" % discount)
    elif 3 < age <= 13:
        print("Your grade is %s, so It's charged about \%d." % ("KIDS", 2000))
        type = int(input("what would you like to pay for it?. (1:cash, 2:Park membership credit card)"))
        if type == 1:
            pay = int(input("How much will you pay for it?"))
            if pay == 2000:
                print("Thanks! Printing out your ticket.")
            elif pay > 2000:
                print("Thanks! Print out your ticket and keep your change \%d." % (pay - 2000))
            elif pay < 2000:
                print("Not enough money %d. your %d." % (pay - 2000, pay))
        elif type == 2:
            print("(You can get some discount for 10%, if you're 60~65, you can get extra discount for 5%)")
            pay = int(input("please, charge."))
            if 4 < age <= 65:
                print("It's charged about \[%d]." % (pay * 0.9))
            elif 65 <= age:
                print("It's charged about \[%d]." % (pay * 0.85))
            count = count + 1
        if 0 == count % 7:
            Free = Free - 1
            print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기에 무료 티켓을 발행합니다. 잔여 무료 티켓 [%d]장" % Free)
        elif 0 == count % 4:
            discount = discount - 1
            print("축하합니다. 연간 회원권에 당첨되었습니다. 여기에 연간 회원권을 발행합니다. 잔여 무료 티켓 [%d]장" % discount)
    elif 4 < age <= 18:
        print("귀하의 등급은 [%s]이며 요금은 [%d]원 입니다." % ("청소년", 3000))
        type = int(input("요금 유형을 선택하세요. (1:현금, 2:공원 전용 신용카드)"))
        if type == 1:
            pay = int(input("요금을 입력하세요."))
            if pay == 3000:
                print("감사합니다. 티켓을 발행합니다.")
            elif pay > 3000:
                print("감사합니다 티켓을 발행하고 거스름돈 [%d]원을 반환합니다." % (pay - 3000))
            elif pay < 3000:
                print("[%d]가 부족합니다. 입력 하신 [%d]를 반환합니다." % (pay - 3000, pay))
        elif type == 2:
            print("(결제 금액의 10% 할인, 60~65세 장년은 추가 5% 할인)")
            pay = int(input("요금을 입력하세요."))
            if 4 < age <= 65:
                print("[%d]원 결제되었습니다." % (pay * 0.9))
            elif 65 <= age:
                print("[%d]원 결제되었습니다." % (pay * 0.85))
                count = count + 1
                if 0 == count % 7:
                    Free = Free - 1
                    print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기에 무료 티켓을 발행합니다. 잔여 무료 티켓 [%d]장" % Free)
                elif 0 == count % 4:
                    discount = discount - 1
                    print("축하합니다. 연간 회원권에 당첨되었습니다. 여기에 연간 회원권을 발행합니다. 잔여 무료 티켓 [%d]장" % discount)
    elif 18 < age <= 65:
        print("귀하의 등급은 [%s]이며 요금은 [%d]원 입니다." % ("어른", 5000))
        type = int(input("요금 유형을 선택하세요. (1:현금, 2:공원 전용 신용카드)"))
        if type == 1:
            pay = int(input("요금을 입력하세요."))
            if pay == 5000:
                print("감사합니다. 티켓을 발행합니다.")
            elif pay > 5000:
                print("감사합니다 티켓을 발행하고 거스름돈 [%d]원을 반환합니다." % (pay - 5000))
            elif pay < 5000:
                print("[%d]가 부족합니다. 입력 하신 [%d]를 반환합니다." % (pay - 5000, pay))
        elif type == 2:
            print("(결제 금액의 10% 할인, 60~65세 장년은 추가 5% 할인)")
            pay = int(input("요금을 입력하세요."))
            if 4 < age <= 65:
                    print("[%d]원 결제되었습니다." % (pay * 0.9))
            elif 65 <= age:
                print("[%d]원 결제되었습니다." % (pay * 0.85))
            count = count + 1
            if 0 == count % 7:
                Free = Free - 1
                print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기에 무료 티켓을 발행합니다. 잔여 무료 티켓 [%d]장" % Free)
            elif 0 == count % 4:
                discount = discount - 1
                print("축하합니다. 연간 회원권에 당첨되었습니다. 여기에 연간 회원권을 발행합니다. 잔여 무료 티켓 [%d]장" % discount)
    else:
        age > 65
        print("귀하의 등급은 [%s]이며, 요금은 [%s] 입니다." % ("노인", "무료"))
        print("감사합니다. 티켓을 발행합니다.")
        count = count + 1
        if 0 == count % 7:
            Free = Free - 1
            print("축하합니다. 1주년 이벤트에 당첨되었습니다. 여기에 무료 티켓을 발행합니다. 잔여 무료 티켓 [%d]장" % Free)
        elif 0 == count % 4:
            discount = discount - 1
            print("축하합니다. 연간 회원권에 당첨되었습니다. 여기에 연간 회원권을 발행합니다. 잔여 무료 티켓 [%d]장" % discount)