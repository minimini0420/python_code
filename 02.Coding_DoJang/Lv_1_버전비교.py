# A씨는 두 개의 버전을 비교하는 프로그램을 작성해야 한다.
#
# 버전은 다음처럼 "." 으로 구분된 문자열이다.
#
# 버전 예) 1.0.0, 1.0.23, 1.1
#
# 두 개의 버전을 비교하는 프로그램을 작성하시오.
#
# 다음은 버전 비교의 예이다.
#
# 0.0.2 > 0.0.1
# 1.0.10 > 1.0.3
# 1.2.0 > 1.1.99
# 1.1 > 1.0.1

def compare(version):
    version_list = version.split()
    check_1 = [int(i) for i in version_list[0].split('.')]
    check_2 = [int(i) for i in version_list[1].split('.')]

    if check_1[0] > check_2[0]:
        print('%s > %s' %(version_list[0],version_list[1]))

    elif check_1[0] == check_2[0]:

        if check_1[1] > check_2[1]:
            print(('%s > %s' %(version_list[0],version_list[1])))

        elif check_1[1] == check_2[1]:

            if str(check_1[2]) > str(check_2[2]):
                print(('%s > %s' %(version_list[0],version_list[1])))

            else:
                print('%s < %s' % (version_list[0], version_list[1]))

        else:
            print(('%s > %s' % (version_list[0], version_list[1])))

    else:
        print(('%s > %s' %(version_list[0],version_list[1])))

while True:
    version = input('비교할 버전을 기입하세요:')
    compare(version)

# 정답입니다.!!

# from itertools import zip_longest
#
# def compare(left, right):
#     left_vars = map(int, left.split('.'))
#     right_vars = map(int, right.split('.'))
#     for a, b in zip_longest(left_vars, right_vars, fillvalue = 0):
#         if a > b:
#             return '>'
#         elif a < b:
#             return '<'
#     return '='
#
# CASES = [['0.0.2', '0.0.1'],
#          ['1.0.10', '1.0.3'],
#          ['1.2.0', '1.1.99'],
#          ['1.1', '1.0.1']]
#
# if __name__ == '__main__':
#     for case in CASES:
#         print('{0[0]} {1} {0[1]}'.format(case, compare(*case)))