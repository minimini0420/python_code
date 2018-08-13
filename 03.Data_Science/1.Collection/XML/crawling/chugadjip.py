import urllib.request
from bs4 import BeautifulSoup
from pandas import DataFrame

max_page = 100
result = []
index = "index"

for page_idx in range(1,max_page+1):
    Cheogajip_URL = 'http://www.cheogajip.co.kr/establish02_02.html?page=%s&search=&keyword='%str(page_idx)
    print(Cheogajip_URL)

    response = urllib.request.urlopen(Cheogajip_URL)
    soupData = BeautifulSoup(response.read().decode('CP949'),'html.parser')

    store_trs = soupData.find_all('tr',dttrs = {'align':'center','bgcolor':'#FFFFFF'})
    print("END")

    if (store_trs):
        for store_tr in store_trs :
            tr_tag = list(store_tr.strings)

            if(tr_tag[1].count('[휴점]')==0):
                store_name = tr_tag[1]
                store_address = tr_tag[3]
                phone_number = tr_tag[5]
                result.append([store_name]+[store_address]+[phone_number])
                #result.append(store_name=','+store_address+','+phone_number

cheogajip_table = DataFrame(result, columns=('store_name','store_address','phone_number'))
cheogajip_table.to_csv("cheogajip.csv",encoding="cp949",mode='w',index=True)

print("END")