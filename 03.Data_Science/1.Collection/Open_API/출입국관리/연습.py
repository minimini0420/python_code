import urllib.request
import datetime
import json
import math
# 내꺼 오늘 다씀 "iIhsixEf18XxhFwut8lRVPkptX44Z0E2kGCTBl8%2BBnOUU%2BNX5QoSpXcwZ1J14NbOB1s2cxLv9Uuf%2F%2FkjnHzysQ%3D%3D"
access_key= "fgNUbFNWdrPsUqf6WsEPlsKYxDQ%2BgzRO2LIXFxVCeb7zMpjnDnIGiVINYnTenSQdMMseq9GIWW4Bkh5%2B7ZNXKA%3D%3D"

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success"%datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL:%s"%(datetime.datetime.now(),url))
        return None

#[CODE 1]
def getTourPointVisitor(yyyymm,ED_CD,npagenum,nItems):

    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getForeignTuristStatsList"

    parameters = "?_type=json&serviceKey="+access_key
    parameters += "&NAT_CD=" + "112"
    parameters += "&ED_CD=" + urllib.parse.quote(ED_CD)
    parameters += "&YM="+yyyymm
    parameters +="&numOfRows="+str(nItems) # 두 문서 다 있는거네. 한페이지 결과 수

    url=end_point+parameters

    retData = get_request_url(url)

    if retData == None :
        return None
    else :
        print(retData)
        return json.loads(retData)

# [CODE 2]
def getTourPointData(item, yyyymm, jsonResult):
    natKorNm = '' if 'natKorNm' not in item.keys() else item['natKorNm']
    edCd = '' if 'edCd' not in item.keys() else item['edCd']
    num = 0 if 'num' not in item.keys() else item['num']
    rnum= 0 if 'rnum' not in item.keys() else item['rnum']

    jsonResult.append({'yyyymm':yyyymm,'natKorNm':natKorNm,'edCd':edCd,'rnum':rnum,'num':num})

def main() :
    jsonResult = []

    ED_CD = ""

    nStartYear = 2011
    nEndYear = 2017
    for year in range(nStartYear, nEndYear+1):
        for month in range(1,13):
            yyyymm="{0}{1:0>2}".format(str(year),str(month))

            # [CODE 3]
            while True:
                jsonData = getTourPointVisitor(yyyymm,ED_CD,npagenum,nItems)
                # print(jsonData['response']['body']['items']['item'][0]['num'])  ######################################################################

                if jsonData['response']['header']['resultMsg']=='OK':
                    print("OK")
                    print(jsonData['response']['body']['items']['item'])
                    # print(jsonData['response']['body']['items']['item'][month]['num'])
                    nTotal = jsonData['response']['body']['items']['item'][month]['num']

                    if nTotal == 0:
                        break

                    # print(jsonData)
                    # if not jsonData:
                    #     print("쏴리질러엇")
                    for item in jsonData['response']['body']['items']['item']:
                        getTourPointData(item,yyyymm,jsonResult)

                    nPage = math.ceil(nTotal/100)   # 게시판 페이징 알고리즘과 같음 100 나누기 해서 몫 +1을 함

                    if nPagenum == nPage:
                        break

                    nPagenum +=1

                else:
                    break
    with open('중국인_방문객_빅데이터_수집_%d_%d.json'%(nStartYear,nEndYear),'w',encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(retJson)

    print("중국인_방문객_빅데이터_수집_%d_%d.json SAVED"%(nStartYear,nEndYear))

if __name__ == '__main__':
    main()