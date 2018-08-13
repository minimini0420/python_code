import csv # 외부모듈 사용!!!

with open("Demographic_Statistics_By_Zip_Code.csv", newline="") as infile:
    data = list(csv.reader(infile)) # 파일을 'data'라는 리스트로 출력
#
# ## get_csv_rowInstance(row_index)
# ## COUNT FEMALE
# def get_csv_rowInstance(row_name): # data를
#     find_row = data[0].index(row_name)
#     row_instance = []
#     for row in data[1:]:
#         row_instance.append(int(row[find_row]))
#
#     return row_instance
#
# print(get_csv_rowInstance("COUNT MALE"))
def get_csv_colInstance(primary_key) :
    for col_instance in data[1:]:
        if col_instance[0] == primary_key : return col_instance
        else : continue

print(get_csv_colInstance(10002))ddsd