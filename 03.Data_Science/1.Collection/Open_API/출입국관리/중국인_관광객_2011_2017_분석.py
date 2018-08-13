import urllib.request
import datetime
import json

access_key = '5X8xep2Y7D1S6%2BGl%2BnrnabFJiL%2FVdT8wO7ipvtPwWTvV7bgtEFuqBqGgmYS8Z1hnj0BWMtukD5u9QihQlbmGKQ%3D%3D'

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s" %(datetime.datetime.now(), url))
        return None

#[CODE 1]
def getNatVisitor(yyyymm,nat_cd,ed_cd) :
    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    parameters = "?YM=" + yyyymm
    parameters += "&NAT_CD=" + nat_cd
    parameters += "&ED_CD=" + ed_cd
    parameters += "&_type=json&serviceKey=" + access_key

    url = end_point + parameters
    retData = get_request_url(url)

    if (retData == None):
        return None
    else:
        return  json.loads(retData)

def main():
    jsonResult = []
# 중국 : 112 // 일본 : 130 // 미국 :275
    nat_code =  '112'
    ed_cd = 'E'
    nStartYear = 2011
    nEndYear = 2018

    for year in range(nStartYear, nEndYear):
        for month in range(1,13):
            yyyymm = "{0}{1:0>2}".format(str(year),str(month)) ## 문자열 포멧팅 공부하기 시발 병신새끼야 이걸 몰라서 되겠니?
            jsonData = getNatVisitor(yyyymm,nat_code,ed_cd)

            if(jsonData['response']['header']['resultMsg']=="OK"):
                krName = jsonData['response']['body']['items']['item']['natKorNm']
                krName = krName.replace(" ","")
                iTotalVisit = jsonData['response']['body']['items']['item']["num"]
                print('%s_%s:%s'%(krName,yyyymm,iTotalVisit))

                jsonResult.append({'nat_name':krName,'nat_cd':nat_code,'yyyymm':yyyymm,'visit_cnt':iTotalVisit})

            cnVisit = []
            VisitYM = []
            index = []
            i = 0

            for item in jsonResult:
                index.append(i)
                cnVisit.append(item['visit_cnt'])
                VisitYM.append(item['yyyymm'])
                i = i + 1

    with open('%s_(%s)방문객_빅데이터_%d_%d.json'%(krName,nat_code,nStartYear,nEndYear-1),'w',encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

    print("%s_(%s)방문객_빅데이터_%d_%d.json"%(krName,nat_code,nStartYear,nEndYear-1))

if __name__ == '__main__':
    main()