# <연습 문제2>
# 반복문을 통하여 사람을 입력받는다.
# "안녕하세요. 이름을 입력하세요."
# 입력 받으면 순서대로 아래와 같은 인사를 한다.
#
# Hi [사람이름]!! You are 1st person come here!
# Hi [사람이름]!! You are 2nd person come here!
# Hi [사람이름]!! You are 3rd person come here!
# Hi [사람이름]!! You are 4th person come here!
# Hi [사람이름]!! You are 5th person come here!
# Hi [사람이름]!! You are 10th person come here!
#
# 11번째 이후 손님은 아래와 같은 메세지를 받는다.
# Sorry [사람이름}. The event is closed because You are 11th person come here.
guest = 0
while True:
    name_input=str(input("안녕하세요. 이름을 입력하세요\n"))
    if name_input:
        guest+=1
        if guest == 1:
            print("Hi [%s]!! You are 1st person come here!" % name_input)
        elif guest == 2:
            print("Hi [%s]!! You are 2nd person come here!" % name_input)
        elif guest == 3:
            print("Hi [%s]!! You are 3rd person come here!" % name_input)
        elif guest > 3 and guest < 11:
            print("HI [%s]!! Tou are %sth person come here!" % (name_input,guest))
        elif guest > 10:
            print("Sorry [%s]. The event is closed because You are %sth person come here" % (name_input,guest))
