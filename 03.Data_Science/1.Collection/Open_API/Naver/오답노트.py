import json

news_count = []

with open("이명박_naver_news.json", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    jsonResult = json.loads(json_string)

def find_article():
    article_split_string = []
    count_dic = {}
    for element in jsonResult:
        try:
            article_split_string.append(element["org_link"].split("/")[2])
        except:pass

    article_split_string_index = list(set(article_split_string))

    for i in article_split_string_index:
        count_num = 0
        for element_1 in article_split_string:
            if element_1 == i :
                count_num += 1
                count_dic[i] = count_num
    return count_dic


list_article = find_article().items()
list_article = sorted(list_article, key=lambda t:t[1], reverse=True)

print("---- 도메인별 기사 건수 분석 ----")

for element in list_article:
    print("기사 도메인 : %s  기사 건수 : %s "% (element[0],element[1]))
