import urllib.request
import os
from pandas import DataFrame
import xml.etree.ElementTree as ET

result = []
dir_name = "V4_BigData"
dir_deilmiter = "\\"
dir_nene = "Nene_data"
file_nene = "nene"
csv = ".csv"
result_limit = 12

def make_dir(number):
    os.mkdir(dir_name+dir_deilmiter+dir_nene+str(number))
    return None

def make_nene(dir_num,number_count):
    number = 1
    import csv
    with open("nene.csv",newline="") as infile:
        data = list(csv.reader(infile))
        while True:
            number_limit = number + 100
            f = open(dir_name + dir_deilmiter + dir_nene + str(dir_num)+ dir_deilmiter + file_nene + str(number_count) + '.csv','w', newline="")
            csvWriter = csv.writer(f)
            csvWriter.writerow(['sotre','sido','gungu','store_address'])
            for i in data[number:number_limit]:
                csvWriter.writerow(i)
            number = number_limit
            number_count += 1
            if number_count > int(len(data)/100)+1:
                break

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

try :
    os.mkdir(dir_name)
    nene_table.to_csv('nene.csv',encoding='cp949',mode='w',index=False)
except : pass

try:
    with open(dir_name + dir_deilmiter + "nene_count.txt",'r') as file:
        index_num = file.readline()
        index_num = int(index_num)
        make_dir(index_num)
        make_nene(index_num,1)
        index_num += 1
    with open(dir_name + dir_deilmiter + "nene_count.txt",'w') as file:
        file.write(str(index_num))
except:
    with open(dir_name+dir_deilmiter+"nene_count.txt",'w') as file:
        file.write("2")
    make_dir(1)
    make_nene(1,1)