import json

foreiner_count = {}

with open("2016_12월_방문객_빅데이터.json", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    jsonResult = json.loads(json_string)

for element in jsonResult:
    foreiner_count[element['nat_name']] = element['visit_cnt']

foreiner_count = foreiner_count.items()
foreiner_count = sorted(foreiner_count, key=lambda t:t[1], reverse=True)


print("<< 2016 12월 외국인 방문자 상위 10개 국가 >>")
print("-" * 50)
for number in range(1,11):
    print("|   순위 : %-2s   국가명 : %-10s " % (number, foreiner_count[number-1][0]))
    print("|   방문자 수 : %s 명 " % foreiner_count[number-1][1])
    print("-" * 50)
