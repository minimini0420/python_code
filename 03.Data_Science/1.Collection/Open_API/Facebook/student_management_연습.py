import json
import os

jsonResult = [
    {
        'student_ID':'ITT001',
        'student_name':'김기정',
        'student_age':31,
        'address':'대구광역시 파티마 병원 옆 포시즌 302호',
        'total_course_info':{
            'num_of_course_learned':2,
            'learning_course_info':[
                    {
                        'course_code':'IB171106',
                        'course_name':'IoT 빅데이터 실무반',
                        'teacher':'이현구',
                        'open_date':'2017-11-06',
                        'close_date':'2018-09-05'
                     }
            ]
        }
     },
    {
        'student_ID':'ITT002',
        'student_name':'전수범',
        'student_age':29,
        'address':'대구광역시 달서구 성지로 14안길 17',
        'total_course_info':{
            'num_of_course_learned':1,
            'learning_course_info':[
                    {
                        'course_code':'IB171106',
                        'course_name':'IoT 빅데이터 실무반',
                        'teacher':'이현구',
                        'open_date':'2017-11-06',
                        'close_date':'2018-09-05',
                     },
                    {
                        'course_code':'OB180106',
                        'course_name':'오픈소스기반 빅데이터 실무반',
                        'teacher':'이현구',
                        'open_date':'2018-01-06',
                        'close_date':'2018-08-05'
                     }
            ]
        }
     }
]

def ask_info():
    path_space = "\\"
    file_name = "ITT_Student.json"

    print("======<< 학생 정보 프로그램 ver1 >>=======\n")
    ask = int(input("경로에 파일이 없습니다. 1. 새로운 경로를 설정하시겠습니까?  2. 현재 경로를 사용하시겠습니까? : "))

    if ask == 1:
        path = input("새로운 경로를 설정해주세요 : ")
        total_path = path + path_space + file_name
        return total_path

    elif ask == 2:
        return file_name

def info_start(path):
    try:
        with open(path, encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            jsonResult_load = json.loads(json_string)
        return jsonResult_load

    except FileNotFoundError :
        with open(path, 'w', encoding='UTF8') as outfile:
            readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(str(readable_result))
        return jsonResult

def info_student_ID():
    try:
        if not os.path.isfile("ITT_Student.json"):
            counter = '1'
            student_id = "ITT" + counter.zfill(3)
            with open("count.txt","w") as file:
                file.write(counter)
            return student_id
        else:
            with open("count.txt","r") as file:
                counter = file.readline()
                counter = int(counter) + 1
                student_id = "ITT" + str(counter).zfill(3)

            with open("count.txt","w") as file:
                file.write(str(counter))
            return student_id

    except FileNotFoundError:
        if len(jsonResult) == 0:
            counter = '1'
            student_id = "ITT" + counter.zfill(3)
            with open("count.txt", "w") as file:
                file.write(counter)
            return student_id

def info_insert():
    select = int(input("1.학생 정보 입력하기 2. 메인메뉴로 돌아가기 : "))

    if select == 1:
        student_dic = {}
        recent_info = []
        student_dic['student_name'] =input("이름을 입력해주세요 : ")
        student_dic['student_age'] = input("나이를 입력해주세요 : ")
        student_dic['address'] = input("주소를 입력해주세요 : ")
        past_info = input("과거 수강 횟수를 입력하세요 : ")

        while True:
            number = int(input("현재 수강 정보를 입력하시려면 1번을 아니면 2번을 눌러주세요 : "))
            if number == 1 :
                recent_info.append(info_insert_course())
            elif number == 2 :
                break

        student_dic['total_course_info'] = {'num_of_course_learned':past_info, 'learning_course_info': recent_info}
        student_dic["student_ID"] = info_student_ID()
        jsonResult.append(student_dic)
        print("======== 학생 정보가 입력 되었습니다.")

    elif select == 2:
        return select

def info_insert_course():
    recent_info = {}
    recent_info['course_code'] = input("현재 수강 중인 강의코드를 입력하세요 : ")
    recent_info['course_name'] = input("현재 수강 중인 강의명을 입력하세요 : ")
    recent_info['teacher'] = input("현재 강의의 교사명을 입력하세요 : ")
    recent_info['open_date'] = input("강의 시작일을 입력하세요 : ")
    recent_info['close_date'] = input("강의 종료일을 입력하세요 : ")
    return recent_info

def info_search(key, search_index):
    result = []
    for element in jsonResult:
        if key in element.keys():
            if element[key] == search_index:
                result.append(element)
            elif search_index in element[key]:
                result.append(element)
        else :
            if key == 'num_of_course_learned' :
                if element.get('total_course_info')[key] == search_index:
                    result.append(element)
            elif key == 'learning_course_info' :
                try:
                    if element.get('total_course_info')["learning_course_info"][0][key] == search_index:
                        result.append(element)
                    elif search_index in element.get('total_course_info')["learning_course_info"][0][key] :
                        result.append(element)
                except:
                    pass
    return result

def info_show_indiviual(result):
    print("====== 학생 정보 조회 =======")
    for i in range(len(result)):
        print("<< 학생정보 >>")
        print("학생 ID : %s" % result[i]["student_ID"])
        print("이름 : %s " % result[i]["student_name"])
        print("나이 : %s " % result[i]["student_age"])
        print("주소 : %s " % result[i]["address"])
        print("수강정보 : ")
        print("\t- 과거 수강 횟수 : %s" % result[i].get("total_course_info")["num_of_course_learned"])
        print("\t- 현재 수강 정보 : ")
        for j in result[i].get("total_course_info")["learning_course_info"]:
            print("------------------------------------------------------")
            print("\t\t강의코드 : %s" % j["course_code"])
            print("\t\t강의명   : %s" % j["course_name"])
            print("\t\t강사명   : %s" % j["teacher"])
            print("\t\t시작일   : %s" % j["open_date"])
            print("\t\t종료일   : %s" % j["close_date"])
        print("------------------------------------------------------\n")

def info_show_plural(result):
    for element in result:
        print("학생 ID : %s    학생 이름 : %s" %(element["student_ID"],element["student_name"]))

def info_revise(result):
   pass


# print("=======<< 학생 정보 관리 프로그램  ver.1 >>=======")
# print("")
#
# try:
#     with open('ITT_Student.json', encoding='UTF8') as json_file:
#         json_object = json.load(json_file)
#         json_string = json.dumps(json_object)
#         jsonResult = json.loads(json_string)
#
# except FileNotFoundError:
#      jsonResult = info_start(ask_info())
#      print('ITT_Student.json SAVED')

print(info_search("student_name","김기정"))
info_show_indiviual(info_search("student_name","전수범"))