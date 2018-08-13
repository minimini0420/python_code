# 프로그램 실행 순서
#
# 입력할 정수의 개수를 사용자로부터 입력 받는다.
# 입력받은 정수의 개수만큼 정수를 입력받는다.
# 입력받은 정수의 합과 평균 값을 출력한다.
# 할당된 메모리공간을 비운다.
# 요구사항
#
# 메모리공간은 사용자의 입력 수의 따라 변동된다.
# 사용한 공간은 마지막에 비워야 한다.
# 배열을 사용하면 안된다. ----> 리스트를 사용하지 말아라!!!

while True:
    unit = int(input("입력할 정수의 갯수는 입력하세요:\n"))
    number_count = 0
    sum = 0
    avg_number = 0

    while True:
        number = int(input("정수를 입력하세요요"))
        number_count += 1
        sum += number
        if number_count == unit:
            avg_number =  sum / unit
            break

    print(sum)
    print(int(avg_number))
    del sum,avg_number

# 정답!!!
# num_of_n = int(input("입력할 정수 개수: "))
#
# Sum = 0
# for x in range(num_of_n):
#     Sum += int(input("Enter num%d: " % (x+1)))
#
# print("Sum: %d" % Sum)
# print("Avg:  %.2f" % (Sum / num_of_n))
#
# del num_of_n, Sum, x
