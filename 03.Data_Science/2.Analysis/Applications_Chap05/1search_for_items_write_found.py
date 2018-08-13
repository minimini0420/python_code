#!/usr/bin/env python3
import csv
import glob     ## 특정 패턴과 일치하는 모든 경로명을 찾는다 -> 폴더 내 다수 파일을 읽기 위해
import os
import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple     ## 파일에서 추출한 날짜들이 출력 파일에서 특정 포맷을 유지하도록

item_numbers_file = sys.argv[1]
path_to_folder = sys.argv[2]
output_file = sys.argv[3]
## 찾으려는 품목 번호를 소스코드에서 사용하려면, CSV 파일에 있는 품목 번호를 리스트 같은 적합한 형태의 자료구조로 바꿔야 한다.
item_numbers_to_find = []
with open(item_numbers_file, 'r', newline='') as item_numbers_csv_file:
    filereader = csv.reader(item_numbers_csv_file)  ## reader() : CSV 입력 파일을 연 후, 파일 내 데이터를 읽기 위해 filereader 객체를 만듦
    for row in filereader:
        item_numbers_to_find.append(row[0])
# print(item_numbers_to_find)

filewriter = csv.writer(open(output_file, 'a', newline=''))  ## writer() : 출력할 CSV 파일을 추가모드('a')로 열어서 데이터를 쓰기 위한 file writer 객체를 만듦

file_counter = 0                ## 읽을 기록 파일의 수
line_counter = 0                ## 모든 파일에서 읽은 행의 수
count_of_item_numbers = 0       ## 찾고 있는 품목 번호가 들어 있는 행의 수
## 기록 파일 폴더 내에 있는 각 파일들을 반복 처리하기 위한 외부 for문     ↱ *.* : 모든 파일을 뜻함
for input_file in glob.glob(os.path.join(path_to_folder, '*.*')):  ## os.path.join() 함수는 폴더의 경로를
    file_counter += 1                                   ## glob.glob() 함수를 사용, 특정 패턴과 일치하는 모든 파일명과 결합
    if input_file.split('.')[1] == 'csv':   ## input_file : glob.glob() 함수가 찾은 파일 리스트의 개별 파일명
        with open(input_file, 'r', newline='') as csv_in_file:
            filereader = csv.reader(csv_in_file)
            header = next(filereader)
            for row in filereader:
                row_of_output = []
                for column in range(len(header)):
                    if column < 3:
                        cell_value = str(row[column]).strip()
                        row_of_output.append(cell_value)
                    elif column == 3:
                        cell_value = str(row[column]).lstrip('$').replace(',', '').split('.')[0].strip()
                        row_of_output.append(cell_value)
                    else:
                        cell_value = str(row[column]).strip()
                        row_of_output.append(cell_value)
                row_of_output.append(os.path.basename(input_file))
                if row[0] in item_numbers_to_find:
                    filewriter.writerow(row_of_output)
                    count_of_item_numbers += 1
                line_counter += 1
    elif input_file.split('.')[1] == 'xls' or input_file.split('.')[1] == 'xlsx':
        workbook = open_workbook(input_file)
        for worksheet in workbook.sheets():
            try:
                header = worksheet.row_values(0)
            except IndexError:
                pass
            for row in range(1, worksheet.nrows):
                row_of_output = []
                for column in range(len(header)):
                    if column < 3:
                        cell_value = str(worksheet.cell_value(row, column)).strip()
                        row_of_output.append(cell_value)
                    elif column == 3:
                        cell_value = str(worksheet.cell_value(row, column)).split('.')[0].strip()
                        row_of_output.append(cell_value)
                    else:
                        cell_value = xldate_as_tuple(worksheet.cell(row, column).value, workbook.datemode)
                        cell_value = str(date(*cell_value[0:3])).strip()
                        row_of_output.append(cell_value)
                row_of_output.append(os.path.basename(input_file))
                row_of_output.append(worksheet.name)
                if str(worksheet.cell(row, 0).value).split('.')[0].strip() in item_numbers_to_find:
                    filewriter.writerow(row_of_output)
                    count_of_item_numbers += 1
                line_counter += 1
print('Number of files: {}'.format(file_counter))
print('Number of lines: {}'.format(line_counter))
print('Number of item numbers: {}'.format(count_of_item_numbers))
