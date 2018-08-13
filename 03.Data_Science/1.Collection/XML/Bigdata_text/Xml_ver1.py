import urllib.request
import os
from pandas import DataFrame
import xml.etree.ElementTree as ET

result = []
dir_name = "V1_BigData"
nene_name = "nene"
dir_space = "\\"
csv = ".csv"

def nene_file(number):
    div_total_name = dir_name + dir_space + nene_name + str(number) + csv
    nene_table.to_csv(div_total_name, encoding="cp949", mode='w', index=True)
    return None

response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))

html = response.read().decode('UTF-8')
root = ET.fromstring(html)

for element in root.findall('item'):
    store_name = element.findtext('aname1')
    store_sido = element.findtext('aname2')
    store_gungu = element.findtext('aname3')
    store_address = element.findtext('aname4')

    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('store','sido','gungu','store_address'))

print("START")
try:
    os.mkdir(dir_name)
except:
    pass

try:
    with open(dir_name + dir_space + "count.txt", 'r') as file:
        file_num = file.readline()
        file_num = int(file_num)
        nene_file(file_num)
        file_num += 1

    with open(dir_name + dir_space + "count.txt",'w') as file:
        file.write(str(file_num))

except FileNotFoundError:
    with open(dir_name + dir_space + "count.txt",'a') as file:
        file_num = 1
        file.write(str(file_num))

print("END")