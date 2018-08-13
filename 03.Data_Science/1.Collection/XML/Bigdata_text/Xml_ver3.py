import urllib.request
import os
from pandas import DataFrame
import xml.etree.ElementTree as ET
import time

print("START")

result = []
dir_name = "V3_BigData"
dir_delimiter = "\\"   # 구분자 -> 엑셀파일을 텍스트로 열면 콤마에 대한 것을 구분하는 것
nene_dir = "Nene_Data"
nene_file = "nene"
csv = ".csv"
record_limit = 3
nene_time = time.strftime("%x",time.localtime(time.time()))+ "_" + time.strftime('%X',time.localtime(time.time()))
nene_time = nene_time.replace(":","_")
nene_time = nene_time.replace("/","_")

def make_dir(index) :
    os.mkdir(dir_name + dir_delimiter + nene_dir + str(index))
    return None # 그냥 만들기만 할때는 리턴값 None!!!해도 상관없긔

def make_nene(dir_index, make_time) :
    destination_csv = dir_name + dir_delimiter + nene_dir + str(dir_index) + dir_delimiter + nene_file + "_" + "%s" % make_time + csv
    nene_table.to_csv(destination_csv ,encoding="cp949", mode='w', index=True)
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

try : os.mkdir(dir_name)
except : pass
try :
    with open(dir_name + dir_delimiter + "nene_index.txt", 'r') as file :
        file_index = file.readline()
        file_index = int(file_index)
        dir_index = int(file_index / record_limit)
        if file_index % record_limit != 0 :
            dir_index = dir_index+1
        if file_index % record_limit == 1 :
            make_dir(dir_index)

        make_nene(dir_index, nene_time)
        file_index += 1
    with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file :
        file.write(str(file_index))
except FileNotFoundError :
    with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file :
        file.write('2')
    make_dir(1)
    make_nene(1, nene_time)
print("End")