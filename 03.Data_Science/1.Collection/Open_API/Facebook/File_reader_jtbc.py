import json
import os

with open("jtbcnews_facebook_2018-01-24_2018-01-25.json", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    jsonResult = json.loads(json_string)

count_1 =[]
count = []

for element in jsonResult['data']:
    try:
        count_1 = []
        count_1.append(element.get('shares')["count"])
        count_1.append(element['name'])
        count_1.append(element['link'])
        count.append(count_1)
    except:
        pass

count = sorted(count, key=lambda t: t[0], reverse=True)
print(count)
for element in count:
    try:
        print("공유수 : %s   제목 : %s   링크 : %s " %(element[0],element[1],element[2]))
    except:
        pass

# for element in count:


# print(len(jsonResult['data']))
# show_count = sorted(count_1.items(), key=lambda t : t[0])
# for i in show_count:
#     print("조회수 : %d   제목 : %s    링크 : %s "%(i[0],i[1][0],i[1][1]))
#
# show_count = reversed(sorted(count_1))
# for element in count_1:
#     for i in show_count:
#         print(i, show_count[i])
