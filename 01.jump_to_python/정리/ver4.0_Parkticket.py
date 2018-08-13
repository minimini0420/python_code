while True:
    age=int(input("나이를 입력하세요."))
    if 0<age<4:
        print("귀하의 등급은 [%s]이며, 요금은 [%s] 입니다." % ("유아","무료"))

        print("감사합니다. 티켓을 발행합니다.")
    elif 3<age<=13:
        print("귀하의 등급은 [%s]이며 요금은 [%d]원 입니다." %("어린이",2000))
        type=int(input("요금 유형을 선택하세요. (1:현금, 2:공원 전용 신용카드)"))
        if type == 1:
            pay = int(input("요금을 입력하세요."))
            if pay == 2000:
                print("감사합니다. 티켓을 발행합니다.")
            elif pay > 2000:
                print("감사합니다 티켓을 발행하고 거스름돈 [%d]원을 반환합니다." % (pay -2000))
            elif pay < 2000:
                print("[%d]가 부족합니다. 입력 하신 [%d]를 반환합니다." % (pay -2000, pay))
        elif type == 2:
            print("(결제 금액의 10% 할인, 60~65세 장년은 추가 5% 할인)")
            pay = int(input("요금을 입력하세요."))
            if 4<age<=65:
                print("[%d]원 결제되었습니다." % (pay *0.9))
            elif 65<=age:
                print("[%d]원 결제되었습니다." % (pay *0.85))
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
    elif 3<age<=13:
        print("귀하의 등급은 [%s]이며 요금은 [%d]원 입니다." %("어른",5000))
        type=int(input("요금 유형을 선택하세요. (1:현금, 2:공원 전용 신용카드)"))
        if type == 1:
            pay = int(input("요금을 입력하세요."))
            if pay == 5000:
                print("감사합니다. 티켓을 발행합니다.")
            elif pay > 5000:
                print("감사합니다 티켓을 발행하고 거스름돈 [%d]원을 반환합니다." % (pay -5000))
            elif pay < 5000:
                print("[%d]가 부족합니다. 입력 하신 [%d]를 반환합니다." % (pay -5000, pay))
        elif type == 2:
            print("(결제 금액의 10% 할인, 60~65세 장년은 추가 5% 할인)")
            pay = int(input("요금을 입력하세요."))
            if 4<age<=65:
                print("[%d]원 결제되었습니다." % (pay *0.9))
            elif 65<=age:
                print("[%d]원 결제되었습니다." % (pay *0.85))
        elif age>65:
            print("귀하의 등급은 [%s]이며, 요금은 [%s] 입니다." % ("노인","무료"))
            print("감사합니다. 티켓을 발행합니다.")