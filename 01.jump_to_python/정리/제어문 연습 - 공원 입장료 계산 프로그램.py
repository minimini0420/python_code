age = 0
while True:
    age=int(input("나이를 입력하세요."))
    if age <= 3:
        print("무료입니다.")
    elif 3 < age <= 13:
        print("요금은 2000원 입니다.")
    elif 13 < age <= 18:
        print("요금은 3000원 입니다.")
    elif 18 < age <= 65:
        print("요금은 5000원 입니다.")
    elif age > 65:
        print("무료입니다.")
    else:
        print("나이를 입력하세요.요금은 [%d]원 입니다.")

