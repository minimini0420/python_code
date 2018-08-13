import csv

with open("Demographic_Statistics_By_Zip_Code.csv", newline="") as infile:
    data = list(csv.reader(infile))

## get_csv_rowInstance(row_index)
## COUNT FEMALE
def get_csv_rowInstance(row_index):
    find_row = data[0].index(row_index)
    finder = []
    for row in data[0]:
        finder.append(int(row[find_row]))

    # 출력하기 위해선
    # for row in data[1:]:
    #   finder.append(int(row_index]))

    return finder

get_csv_rowInstance("COUNT FEMALE")