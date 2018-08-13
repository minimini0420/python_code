# import json
#
# def info_search(search_index):
#     result = []
#     for i in range(len(jsonResult)):
#         for index in jsonResult[i].values():
#             if search_index in index:
#                 result.append(jsonResult[i])
#             else:
#                 if jsonResult[i]['recent_info'] == index:
#                     for j in index[0].values():
#                         if j == search_index:
#                             result.append(jsonResult[i])
#                 elif index == search_index:
#                     result.append(jsonResult[i])
#     return  result
#
#
# with open('ITT_Student.json', encoding='UTF8') as json_file:
#     json_object = json.load(json_file)
#     json_string = json.dumps(json_object)
#     jsonResult = json.loads(json_string)
#
# while True:
#     print(info_search(input("입력하세요")))

# jsonResult = [
#     {
#         "address": "대구광역시 달서구 도원로 46 별메마을 613동 804호",
#         "age": "28",
#         "name": "윤성우",
#         "past_record": "0",
#         "recent_info": [
#             {
#                 "강사명": "이현구",
#                 "강의명": "IT 빅데이터 분석",
#                 "강의코드": "IB171106",
#                 "개강일": "2017-11-06",
#                 "종료일": "2018-09-05"
#             }
#         ],
#         "student_ID": "ITT004"
#     },
# {
#         "address": "대구",
#         "age": "28",
#         "name": "윤성우",
#         "past_record": "0",
#         "student_ID": "ITT001"
#     },
#     {
#         "address": "",
#         "age": "32",
#         "name": "김기정",
#         "past_record": "2",
#         "student_ID": "ITT002"
#     },
#     {
#         "address": "대구 달서구 성서",
#         "age": "29",
#         "name": "전수범",
#         "past_record": "0",
#         "recent_info": [
#             {
#                 "강사명": "이현구",
#                 "강의명": "IoT 빅데이터 실무반",
#                 "강의코드": "IB171106",
#                 "개강일": "2017-11-06",
#                 "종료일": "2018-09-05"
#             }
#         ],
#         "student_ID": "ITT003"}
# ]
#
# def info_search(key, search_index):
#     result = []
#     for element in jsonResult:
#         if key in element.keys():
#             if element[key] == search_index:
#                 result.append(element)
#             elif search_index in element[key]:
#                 result.append(element)
#         else:
#             try:
#                 for j in range(len(element["recent_info"])):
#                     if element["recent_info"][j][key] == search_index:
#                         result.append(element)
#                     elif search_index in element["recent_info"][j][key]:
#                         result.append(element)
#             except:pass
#     return result
#
# print(info_search("강사명","이현구"))
course_info = []

def info_insert_course():
    learning_course_info = {}
    learning_course_info['course_code'] = input("현재 수강 과목 코드를 기입하세요 (예 : IB171106): ")
    learning_course_info['course_name'] = input("강의명을 입력하세요 (예 : IoT 빅데이터 실무반): ")
    learning_course_info['teacher'] = input("강사명을 입력하세요 (예 : 이현구): ")
    learning_course_info['open_date'] = input("개강일을 입력하세요 (예 : 2017-11-06): ")
    learning_course_info['close_date'] = input("종료일을 입력하세요 (예 : 2018-09-05): ")
    return learning_course_info

body = {}
body['student_ID'] = input("학생 이름을 입력하세요 : ")
past_info = input("과거 수강 이력을 입력하세요 : ")
course_info.append(info_insert_course())
body['total_course_info'] = {'num_of_course_learned': past_info ,'learning_course_info':course_info}
body_in = body.get('total_course_info')
print(body_in.get('learning_course_info')[0]["close_date"])

