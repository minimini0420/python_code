#http://nenechicken.com/subpage/where/where_list.asp?target_step1=%EC%A0%84%EC%B2%B4&target_step2=%EC%A0%84%EC%B2%B4&proc_type=step1
import urllib.request
import os
from pandas import DataFrame
import xml.etree.ElementTree as ET

result = []
dir_name = "V4_BigData"
dir_delimiter = "\\"   # 구분자 -> 엑셀파일을 텍스트로 열면 콤마에 대한 것을 구분하는 것
nene_dir = "Nene_Data"
nene_file = "nene"
csv = ".csv"
record_limit = 12
file_num = 1
#  함수를 정의 하기 이전에 변수를 지정해두면 함수가 인식한다.

def make_dir(index) :
    os.mkdir(dir_name + dir_delimiter + nene_dir+str(index))
    return None # 그냥 만들기만 할때는 리턴값 None!!!해도 상관없긔

def make_nene(dir_index,file_num) :
    import csv
    with open("nene.csv", newline="") as infile:  ## 왜 newline 이 왜 필요할까? 파일 상에 \n을 지워주는 역할
        data = list(csv.reader(infile))
        number = 1
        while True:
            number_again = number + 100
            f = open(dir_name + dir_delimiter +nene_dir+ str(dir_index) +dir_delimiter + nene_file + str(file_num)+".csv", 'w', newline='')
            csvWriter = csv.writer(f)
            for i in data[number:number_again]:
                csvWriter.writerow(i)
            number = number_again
            file_num += 1
            if file_num == 13:
                break
    return None

response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname5')
    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('sotre','sido','gungu','store_address'))

print("START")
try :
    os.mkdir(dir_name)
    nene_table.to_csv("nene.csv", encoding="cp949", mode='w', index=True)
except : pass

try :
    with open(dir_name + dir_delimiter + "nene_index.txt", 'r') as file :
        file_index = file.readline()
        file_index = int(file_index)
        make_dir(file_index)
        make_nene(file_index,1)
        file_index += 1
    with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file :
        file.write(str(file_index))

except FileNotFoundError :
    with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file :
        file.write('2')
    make_dir(1)
    make_nene(1,1)
print("End")