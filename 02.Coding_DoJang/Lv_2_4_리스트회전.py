# 아래 조건에 따라 리스트를 회전하는 프로그램을 작성하시오.
#
# 조건
# 입력값은 한 행의 문자열로 주어지며, 각 값은 공백으로 구분된다.
# 첫 번째 값은 리스트를 회전하는 양과 방향(음수의 경우 좌측으로, 양수의 경우 우측으로 회전)이다.
# 첫 번째 값을 제외한 나머지 값은 리스트의 각 항목의 값이다.
# 회전된 리스트를 문자열로 출력한다.
# 구현에 이용할 자료구조에 대한 조건이나 제약은 없다.
# 입력되는 리스트의 항목의 개수는 유한한다.
#
#    입출력예
# 예 1)
#      입력: 1 10 20 30 40 50
#      출력: 50 10 20 30 40
# 예 2)
#      입력: 4 가 나 다 라 마 바 사
#      출력: 라 마 바 사 가 나 다
# 예 3)
#      입력: -2 A B C D E F G
#      출력: C D E F G A B
# 예 4)
#      입력: 0 똘기 떵이 호치 새초미
#      출력: 똘기 떵이 호치 새초미
while True:
    list = input('리스트 회전시키기!!!')
    list = list.split()
    list_rotation = list.pop(0)
    list_rotation = int(list_rotation)

    if list_rotation == 0:
        list = " ".join(list)

    else:
        count = 0
        while True:
            if count == abs(list_rotation):
                break
            else:
                if list_rotation > 0:
                    add = list.pop()
                    list.insert(0,add)
                    count += 1
                elif list_rotation < 0:
                    add_2 = list.pop(0)
                    list.insert(-1, add_2)
                    count += 1
        list = " ".join(list)

    print(list)

    #  코딩도장 답(1)
    # def f(s):
    #     t = s.split()
    #     go = int(t[0])
    #     src = t[1:]
    #     result = [None] * len(src)
    #     for i in range(len(src)):
    #         result[(i + go) % len(src)] = src[i]
    #     return " ".join(result)
    #
    #
    # print
    # f("1 10 20 30 40 50")
    # print
    # f("-2 A B C D E F G")

    # input_list = input("입력 : ").split()
    # rotation_position = int(input_list[0]) % (len(input_list) - 1)
    # del(input_list[0])
    # print(' '.join(input_list[-rotation_position:] + input_list[0:-rotation_position]))

    # print ' '.join((lambda a : a[1:] if a[0] == '0' else a[-int(a[0]):] + a[1:len(a)-int(a[0])] if int(a[0]) > 0 else a[-int(a[0])+1:] + a[1:-int(a[0])+1])(raw_input('?').split()))