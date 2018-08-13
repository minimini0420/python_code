def sum_result(num, sum=0):
    if num < 11:
        return sum_result(num+1, sum+num)
    else:
        return sum

def sum_number(num):
    if num == 10:
        return num
    else:
        return num + sum_number(num+1)

print(sum_result(1))
print(sum_number(1))

# 난이도 최하
#
# 사각형을 그리세요
#
# ex)입력 : 3
#
# ***
# * *
# ***
#
# 입력 : 5
#
# *****
# *   *
# *   *
# *   *
# *****
# square = '*'
# space = " "
#
#
# a=int(input("입력하세요 : "))
# for i in range(a):
#     number = 1
#     while True:
#         if i == 0 or i == a:
#             if number == a:
#                 print(square * a)
#                 break
#             else: number += 1
#         else:
#             print(square + (space * (a-2)) + square)
#             if number == i:
#                 break

# for i in range(a):
#     print("")
#     for j in range(a):
#         if i == 0 or i == a-1:
#             print(square,end="")
#         else:
#             if j == 0 or j == a-1:
#                 print(square,end="")
#             else:
#                 print(space,end="")
#
# print("")
# data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#
# find_num = 4
#
# number = False
#
# for i in range(len(data)):
#     if find_num == data[i]:
#       print("찾았다!")
#       number = True
#       break
#
# if number == False:
#     print("%d을(를) 찾을 수 없습니다."%find_num)
# 속이 빈 삼각형을 그리세요
# (단 사용자에게 높이를 입력받아서 결과를 출력해야 함)
#
# ex) 높이:5
#
#     *
#    * *
#   *   *
#  *     *
# *********

star = "*"
space = " "
while 1:
    high = int(input("높이를 입력하세요 (숫자): "))
    # for i in range(high):
    #     if i == high - 1 :
    #         print(star * ((high*2)-1))
    #     elif i == 0 :
    #         print(space * (high-1) + star + space * (high-1))
    #     else :
    #         print(space*((high-1)-i) + star + space * ((2*i)-1) + star + space * ((high-1)-i))


    for i in range(high):
        print("")
        count_space = 0
        for j in range((2*high)-1):
            if count_space == high-i:
                print(star,end="")
                count_space = 0
            print(space,end="")
            count_space += 1
