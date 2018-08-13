age = 0
grade = ["유아","어린이","청소년","성인","노인"]

while True:
    age=int(input("나이를 입력하세요"))
    if age <=3:
        print("무료")
        print("귀하는 [%s] 등급입니다." %grade[0])
    elif 3<age<=13:
        print("2000원 입니다.")
        print("귀하는 [%s] 등급입니다." % grade[1])
    elif 13<age<=18:
        print("3000원 입니다.")
        print("귀하는 [%s] 등급입니다." % grade[2])
    elif 18<age<=65:
        print("5000원 입니다.")
        print("귀하는 [%s] 등급입니다." % grade[3])
    elif age>65:
        print("무료입니다.")
        print("귀하는 [%s] 등급입니다." % grade[4])
    else:
        print("나이를 입력하세요. 귀하의 [%s]등급이며 요금은 []입니다.")