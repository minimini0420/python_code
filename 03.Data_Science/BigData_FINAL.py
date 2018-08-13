import csv  # 외부모듈 사용!!!
import math

def get_csv_rowInstance(row_name):  # data를
    row_instance = []
    row_index = data[0].index(row_name)

    for row in data[1:]:
        row_instance.append(float(row[row_index]))

    return row_instance

def get_csv_colInstance(primary_key):
    for col_instance in data[1:]:

        if col_instance[0] == primary_key:
            return col_instance

        else:
            continue

## 프린트 행
def print_row(row_instance):
    for i in row_instance:
        print("%g" % i, end=' ')

## 프린트 열
def print_col(col_instance):
    for i in col_instance:
        print("%g" % i, end=' ')

## 총합 구하기 함수
def My_sum(row_instance):
    sum1 = 0
    for i in row_instance:
        sum1 += i

    print("총합의 요소는 아래와 같습니다.")
    for i in row_instance:
        print("%g" % i, end=' ')

    print("\n총합 = %g" % sum1)

## 평균 구하기 함수
def My_average(row_instance):
    average = sum(row_instance) / len(row_instance)

    print("평균의 요소는 아래와 같습니다.")
    for i in row_instance:
        print(i, end=' ')
    print("\n평균 = %g" % average)

## 최댓값 구하기
def My_max(row_instance):
    max_row = max(row_instance)
    for i in row_instance:
        print("%g" %i, end=' ')
    print("\n최대값은 %g 입니다" % max_row)

## 최소값 구하기
def My_min(row_instance):
    for i in row_instance:
        print("%g" % i, end=' ')

    min_row = min(get_csv_rowInstance(row_name))
    print("\n최소값은 %g 입니다" % min_row)

## 편차 구하기
def My_Deviation(row_instance):
    sum1 = 0
    Deviation = []

    for i in row_instance:
        sum1 += i

    aver = sum1 / len(row_instance)

    for i in row_instance:
        Dev = i - aver
        Deviation.append(Dev)

    print("표본 편차")
    for i in range(0, len(row_instance)):
        print("%g             %g" % (row_instance[i], Deviation[i]))


## 표준 편차
def My_StandardDeviation(row_instance):
    aver = sum(row_instance) / len(row_instance)
    double_list = 0

    for i in row_instance:
        double = i ** 2
        double_list += double

    Variance = (double_list / len(row_instance)) - (aver ** 2)

    print("표준편차(Standard Deviation) 공식: √분산")
    print("표준편차의 요소는 아래와 같습니다.")
    for i in row_instance:
        print("%g" % i, end=' ')

    print("\n표준편차 : %g " % math.sqrt(Variance))


## 분산 구하기
def My_Variance(row_instance):
    sum = 0
    for i in row_instance:
        sum += i

    aver = sum(row_instance) / len(row_instance)
    double_list = 0

    for i in row_instance:
        double = i ** 2
        double_list += double

    Variance = (double_list / len(row_instance)) - (aver ** 2)

    print("분산(Variance) 공식: ∑(표본-평균)**/표본수")
    print("분산의 요소는 아래와 같습니다.")
    for i in row_instance:
        print("%g" % i, end=' ')
    print("\n분산 %g" % Variance)


## 오름차순 정렬 함수
def My_Ascendant(row_instance):
    sort_list = sorted(row_instance)
    print("표본 요소")
    for i in row_instance:
        print("%g" % i, end=' ')
    print("")
    print("오름차순")
    for i in sort_list:
        print("%g" % i, end=' ')
    print("")


## 내림차순 정렬 함수
def My_Descendant(row_instance):
    sort_list = sorted(row_instance)
    print("표본 요소")

    for i in row_instance:
        print("%g" % i, end=' ')
    print("")
    print("내림차순")

    for i in reversed(sort_list):
        print("%g" % i, end=' ')
    print("")

with open("Demographic_Statistics_By_Zip_Code.csv", newline="") as infile: ## 왜 newline 이 왜 필요할까? 파일 상에 \n을 지워주는 역할
    data = list(csv.reader(infile))  # 파일을 'data'라는 리스트로 출력

while True:
    number = int(input("\nAccess 데이타유형 선택 \n (1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.표준편차 9.분산 10.정렬 11.종료:)"))
    if number == 1:
        row_name = input("Access Key 를 입력하세요")
        print("행 데이터는 아래와 같습니다.")
        print_row(get_csv_rowInstance(row_name))

    elif number == 2:
        primary_key = input("Access Key 를 입력하세요:")
        print("열 데이터는 아래와 같습니다.")
        print_col(get_csv_colInstance(primary_key))

    elif number == 11:
        print("이용해주셔서 감사합니다.")
        break

    else:
        row_name = input("구하고자 하는 행의 Access Key 를 입력하세요")

        if number == 3:
            My_sum(get_csv_rowInstance(row_name))

        elif number == 4:
            My_average(get_csv_rowInstance(row_name))

        elif number == 5:
            My_max(get_csv_rowInstance(row_name))

        elif number == 6:
            My_min(get_csv_rowInstance(row_name))

        elif number == 7:
            My_Deviation(get_csv_rowInstance(row_name))

        elif number == 8:
            My_StandardDeviation(get_csv_rowInstance(row_name))

        elif number == 9:
            My_Variance(get_csv_rowInstance(row_name))

        elif number == 10:
            number_2 = int(input("차순의 종류를 선택하세요. 1.오름차순 2.내림차순:"))
            if number_2 == 1:
                My_Ascendant(get_csv_rowInstance(row_name))
            else:
                My_Descendant(get_csv_rowInstance(row_name))