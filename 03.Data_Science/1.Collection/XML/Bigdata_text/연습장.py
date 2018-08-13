import urllib.request
import os
from pandas import DataFrame
import xml.etree.ElementTree as ET
import time

print("START")

result = []
dir_name = "V4_BigData"
dir_delimiter = "\\"
dir_nene = "nene_data"
file_nene = "nene"
csv = '.csv'
result_limit = 12

def make_dir(number):
    os.mkdir(dir_name + dir_delimiter + dir_nene + str(number))
    return None

def make_nene(number, number_count):
    import csv
    with open(dir_name + dir_delimiter + "nene.csv", newline="") as infile:
        data = list(csv.reader(infile))
        number_new = 1
        while True:
            number_limit = number_new + 100
            f = open(dir_name + dir_delimiter + dir_nene + str(number) + dir_delimiter + file_nene + str(number_count)+ ".csv", 'w', newline="")
            csvWriter = csv.writer(f)
            for i in data[number_count:number_limit]:
                csvWriter.writerow(i)
            number_count += 1
            number_new = number_limit

            if number_count > result_limit:
                break


response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

html = response.read().decode('UTF-8')
root = ET.fromstring(html)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname4')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))

try:
    os.mkdir(dir_name)
    nene_table.to_csv(dir_name + dir_delimiter + "nene.csv",encoding='cp949',mode='w',index=True)

except:
    pass

try:
    with open(dir_name + dir_delimiter + 'nene_count.txt','r') as file:
        index_num = file.readline()
        index_num = int(index_num)
        make_dir(index_num)
        make_nene(index_num,1)
        index_num += 1
    with open(dir_name + dir_delimiter + 'nene_count.txt', 'w') as file:
        file.write(str(index_num))

except FileNotFoundError:
    with open(dir_name + dir_delimiter + 'nene_count.txt', 'w') as file:
        index_num = 2
        file.write(str(index_num))
    make_dir(1)
    make_nene(1,1)

print("END")
