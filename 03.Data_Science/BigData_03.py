import csv # 외부모듈 사용!!!

with open("Demographic_Statistics_By_Zip_Code.csv", newline="") as infile:
    data = list(csv.reader(infile)) # 파일을 'data'라는 리스트로 출력

## get_csv_rowInstance(row_index)
## COUNT FEMALE
def get_csv_rowInstance(row_name): # data를
    find_row = data[0].index(row_name)
    row_instance = []
    for row in data[1:]:
        row_instance.append(int(row[find_row]))

    return row_instance



def print_row(row_instance, type = 'int'):  # p152, 입력 인수에 초깃값을 미리 설정
        for i in range(len(row_instance)):
            if type == 'int':
                print(int(row_instance(i)))
            elif type == 'str':
                print(str(row_instance(i)))
            elif type == 'float':
                print(float(row_instance(i)))

def print_col(col_instance):
        for i in col_instance:
            print(i)


## 행 출력


## 열 출력
print_row(get_csv_rowInstance("PERCENT MALE"))
print_col(data[1])

