age = 0
while True:
    age=int(input("나이를 입력하세요."))
    if age <= 3:
        price = "무료"
    elif 3 < age <= 13:
        price = "2000원"
    elif 13 < age <= 18:
        price = "3000원"
    elif 18 < age <= 65:
        price = "5000원"
    elif age > 65:
        price = "무료"
    else:
        print("나이를 입력하세요.요금은 []원 입니다.")
    print("요금은", price, "입니다.")