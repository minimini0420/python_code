# pandas_install ----> 도수창에서 'py -m pip install pandas' 입력 ( 파이썬 경로 설정되어있을때 가능!!)
print("start")
import urllib.request
from pandas import DataFrame

result = []

import xml.etree.ElementTree as ET
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
nene_table.to_csv('nene.csv', encoding="cp949",mode='w',index=True)

print("End")
