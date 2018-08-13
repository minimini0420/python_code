# xlrd 모듈 설치
# py -m pip install xlrd

import sys
from xlrd import open_workbook

input_file = sys.argv[1]

workbook = open_workbook(input_file)
print('Number of worksheets:', workbook.nsheets)
for worksheet in workbook.sheets():
    print("Worksheet name:", worksheet.name, "\tRow:",worksheet.nrows, "\tColumns:",worksheet.ncols)
    