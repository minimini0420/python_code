import json

news_count = []

with open("이명박_naver_news.json", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    jsonResult = json.loads(json_string)

article_split_string = []
news_all_dic = {}
total_news_count = 0

for element in jsonResult:
    try:
        article_split_string.append(element["org_link"].split("/")[2])
    except:pass

article_split_string_index = list(set(article_split_string))

for i in article_split_string_index:
    news_count_num = 0
    for element_1 in article_split_string:
        if element_1 == i :
            news_count_num += 1
            total_news_count += 1
            news_all_dic[i] = news_count_num

list_article = news_all_dic.items()
tuple_article = sorted(list_article, key=lambda t:t[1], reverse=True)

print("\t\t\t\t---- 도메인별 기사 건수 분석 ----")
print("\t\t\t\t- 전체 기사 수 : %d" % total_news_count)
print("\t\t\t\t- 전체 도메인 수 : %d" % len(article_split_string_index))
for element in tuple_article:
    print("기사 도메인 : %-24s            기사 건수 : %s "% (element[0],element[1]))