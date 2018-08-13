import csv
import math
def get_csv_row_instance(row_name):
    row_instance = []
    row_index = data[0].index(row_name)
    for row in data[1:]:
        row_instance.append(float(row[row_index]))
    return row_instance

def get_csv_col_instance(Primary_key):
    for col_instance in data[1:]:
        if col_instance == Primary_key:
            return col_instance
        else:
            continue
# def element_print(number):

def My_sum(row_name):
    sum = 0
    for i in row_name:
        sum += i

    print("요소들의 총합은 아래와 같습니다.")
    for i in row_name:

        print("%5g" %i,end='')
    print("\n총합 = %g" %sum)

with open("Demographic_Statistics_By_Zip_Code.csv", newline="") as infile:
    data = list(csv.reader(infile))

while True:
