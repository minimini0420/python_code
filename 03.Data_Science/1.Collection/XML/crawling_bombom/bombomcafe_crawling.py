print("Web Crawling을 시작합니다.")
import urllib.request
from pandas import DataFrame
from bs4 import BeautifulSoup

result = []
result_branch = []
result_address = []
result_region = []
region_groups = []
region_rate = []

for i in range(1,11):
    html = 'http://cafebombom.co.kr/pg/bbs/board.php?bo_table=store01&page=%s'% i
    response = urllib.request.urlopen(html)
    soup = BeautifulSoup(response,'html.parser')

    print("Destination : %s" % html)
    store = soup.findAll('td',attrs={'class':'list-subject'})
    address = soup.findAll('td',attrs={'class':'text-center en font-11'})
    region = soup.findAll('span',attrs={'class':'text-muted font-11'})

    for element in store:
        element_strip = element.get_text(strip=True)
        result_branch.append(element_strip)

    for element in address[:30]:
        address_inf = element.get_text(strip=True)
        result_address.append(address_inf)

    for element in region:
        element_strip = element.get_text(strip=True)
        result_region.append(element_strip)


print("\t\t지역\t\t|\t\t\t매장명\t\t\t\t|\t\t\t전화번호\t\t\t|\t\t\t주소\t\t\t")
print("-"*149)

for i in range(len(result_branch)):
    branch = result_branch[i]
    region = result_region[i]
    information = result_address[(2*i)+1]
    address = result_address[(2*i)+2]
    result.append([branch] + [region] + [information] + [address])
    print("|%10s|%30s|%14s|%40s" %(region, branch, address, information))

bombom_table = DataFrame(result,columns=('지점','지역','주소','전화번호'))
bombom_table.to_csv('bombom_수집데이터.csv', encoding="cp949",mode='w',index=False)

seoul = result_region.count("서울")
kyeong_ki = result_region.count("경기")
incheon = result_region.count("인천")
kwangwon = result_region.count("강원")
chungbuk = result_region.count("충북")
chungnam = result_region.count("충남")
dajeon = result_region.count("대전")
sejong = result_region.count("세종")
kyeongbuk = result_region.count("경북")
kyeongnam = result_region.count("경남")
daegu = result_region.count("대구")
ulsan = result_region.count("울산")
busan = result_region.count("부산")
jeonbuk = result_region.count("전북")
jeonnam = result_region.count("전남")
kwangju = result_region.count("광주")
jeju = result_region.count("제주")

print()
print("검색된 레코드 수: %d"%len(result_branch))
print()
print("지역별 현황")
print()
print("지역구\t|\t지점수\t|\t비율\t\t")
for i in range(len(result_branch)):


bombom_table = DataFrame(result,columns=('지점','지역','주소','전화번호'))
bombom_table.to_csv('bombom_수집데이터.csv', encoding="cp949",mode='w',index=False)

# for i in range(len(result_region)):

print(result_region)
result_region = list(set(result_region))
print(result_region)
# bombom_table = DataFrame(result_record,columns=('지역','지점수','비율'))
# bombom_table.to_csv('bombom.csv', encoding="cp949",mode='w',index=False)