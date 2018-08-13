import json
import os

jsonResult = []

def ask_path():
    path_space = "\\"
    file_name = "ITT_Student.json"
    ask = int(input("1. 새로운 경로를 설정합니다. 2. 현재 경로로 설정합니다."))
    if ask == 1:
        path = input("새로운 경로를 입력하세요 : ")
        path_total = path + path_space + file_name
        return path_total
    elif ask == 2 :
        return file_name

def student_ID_number():
    try:
        if not os.path.isfile("ITT_Student.json"):
            counter = "1"
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
            return  student_id

    except FileNotFoundError:
        if len(jsonResult) == 0 :
            counter = "1"
            student_id = "ITT" + counter.zfill(3)
            with open("count.txt", "w") as file:
                file.write(counter)
            return student_id
        else:
            counter = len(jsonResult)+1
            student_id = "ITT" + str(counter).zfill(3)
            with open("count.txt", "w") as file:
                file.write(str(counter))
            return student_id

def info_insert():
    student_dic = {}
    recent_info = []
    student_dic['student_name'] = input("학생의 이름을 입력하세요 (예 : 홍길동) : ")
    student_dic['student_age'] = input("학생의 나이를 입력하세요 (예 : 29) : ")
    student_dic['address'] = input("학생의 주소를 입력하세요 (예 : 한양시 종로) : ")
    past_info = input("과거 수강 횟수를 입력하세요 (예 : 1) : ")

    while True:
        number = input("현재 수강 강의를 추가하시겠습니까? y / n : ")
        if number == 'y' :
            recent_info.append(info_insert_course())
        elif number == 'n' :
            break

    student_dic['total_course_info'] = {"num_of_course_learned":past_info,"learning_course_info":recent_info}
    student_dic['student_ID'] = student_ID_number()
    jsonResult.append(student_dic)

def info_insert_course():
    learning_course_info = {}
    learning_course_info['course_code'] = input("현재 수강 강의코드를 입력하세요 (예 : IB171106) : ")
    learning_course_info['course_name'] = input("현재 수강 강의명을 입력하세요 (예 : IoT 빅데이터 실무반) : ")
    learning_course_info['teacher'] = input("현재 수강 강사명을 입력하세요 (예 : 이현구) : ")
    learning_course_info['open_date'] = input("현재 수강 시작일을 입력하세요 (예 : 2017-11-06) : ")
    learning_course_info['close_date'] = input("현재 수강 종료일을 입력하세요 (예 : 2018-09-05) : ")
    return learning_course_info

def info_search(key, search_index):
    result = []
    for element in jsonResult:
        if key in element.keys():
            if search_index == element[key]:
                result.append(element)
            elif search_index in element[key]:
                result.append(element)
        else:
           if key in element.get('total_course_info').keys():
                if search_index == element.get('total_course_info')[key]:
                    result.append(element)
           else:
               try:
                   for element_2 in element.get('total_course_info')['learning_course_info']:
                        if element_2[key] == search_index:
                            result.append(element)
                        elif search_index in element_2[key]:
                            result.append(element)
               except : pass
    return result

def info_show_indiviual(result):
    for element in result:
        print("<< 학생 정보 >>")
        print("- 학생 ID : %s" % element['student_ID'])
        print("- 학생 이름 : %s" % element['student_name'])
        print("- 학생 나이 : %s" % element['student_age'])
        print("- 학생 주소 : %s" % element['address'])
        print("- 수강 정보 :")
        print("\t\t과거 수강 횟수 : %s" % element.get('total_course_info')['num_of_course_learned'])
        print("\t\t현재 수강 과목 :")
        for element_2 in element.get('total_course_info')['learning_course_info']:
            print("--------------------------------------------------")
            print("\t\t\t강의코드 : %s" % element_2['course_code'])
            print("\t\t\t강의명   : %s" % element_2['course_name'])
            print("\t\t\t강사명   : %s" % element_2['teacher'])
            print("\t\t\t개강일   : %s" % element_2['open_date'])
            print("\t\t\t종료일   : %s" % element_2['close_date'])
        print("--------------------------------------------------\n")

def info_show_plural(result):
    print("\n--------------------------------------------------")
    for element in result:
        print("학생 ID : %s    학생 이름 : %s" %(element['student_ID'],element['student_name']))
    print("--------------------------------------------------\n")

def info_save():
    with open("ITT_Student.json","w",encoding='utf8') as outflie:
        readable_result = json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
        outflie.write(readable_result)
        print("\nITT_Student.json SAVED\n")

try:
    with open("ITT_Student.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        jsonResult = json.loads(json_string)

except FileNotFoundError:
    with open(ask_path(),"w",encoding='utf8') as outflie:
        readable_result = json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
        outflie.write(readable_result)
        print("ITT_Student.json SAVED\n")

while True:
    print("<< json 기반 주소록 관리 프로그램 ver.1 >>")
    print("1. 학생 정보입력")
    print("2. 학생 정보조회")
    print("3. 학생 정보수정")
    print("4. 학생 정보삭제")
    print("5. 프로그램 종료")
    menu = int(input("메뉴를 선택해주세요 : "))

    if menu == 1:
        print("\n============ 학생 정보 입력 =============")
        select = int(input("1. 새로운 학생 정보 입력   2. 뒤로가기   \n번호로 선택해주세요 : "))
        if select == 1:
            info_insert()
            info_save()
        elif select == 2:
            continue

    elif menu == 2:
        print("\n============ 학생 정보 조회 =============")
        print("1. 전체 학생 정보 조회")
        print("<< 세부 사항 조회 >>")
        print("2. 학생 ID 조회")
        print("3. 학생 이름 조회")
        print("4. 학생 나이 조회")
        print("5. 학생 주소 조회")
        print("6. 과거 수강 횟수 조회")
        print("7. 현재 수강 강의코드 조회")
        print("8. 현재 수강 강의명 조회")
        print("9. 현재 수강 강사명 조회")
        print("0. 뒤로가기")
        select = int(input("메뉴를 선택하세요 : "))
        print("")

        if select == 1 :
            info_show_indiviual(jsonResult)

        elif select == 0 :
            continue

        elif 10 > select > 1 :
            search_index = input("검색 키워드를 입력하세요 : ")
            key1 = ''
            if select == 2 :
                key1 = 'student_ID'
            elif select == 3 :
                key1 = 'student_name'
            elif select == 4 :
                key1 = 'student_age'
            elif select == 5 :
                key1 = 'address'
            elif select == 6 :
                key1 = 'num_of_course_learned'
            elif select == 7 :
                key1 = 'course_code'
            elif select == 8 :
                key1 = 'course_name'
            elif select == 9 :
                key1 = 'teacher'

            if len(info_search(key1, search_index)) == 1:
                info_show_indiviual(info_search(key1, search_index))
            elif len(info_search(key1, search_index)) > 1:
                info_show_plural(info_search(key1, search_index))

    elif menu == 3 :
        print("\n============ 학생 정보 수정 =============")
        print(" ------ Information ! 학생ID는 수정이 안됩니다 ------ ")

        while True:
            ID = input("학생ID를 입력하세요 ('ITT'로 시작됩니다) : ")
            info_show_plural(info_search('student_ID', ID))
            if len(info_search('student_ID', ID)) > 1:
                print("다시 입력해주세요")
                continue
            else:
                break

        revise_index = info_search('student_ID', ID)[0]
        print("-- 원하시는 수정 항목을 선택해주세요 -- ")
        number = int(input("1.이름  2.나이  3.주소  4.과거 수강 횟수  5.현재 수강 강의코드  6.현재 수강 강의명  7.현재 수강 강사명  8.강의 시작일  9.강의 종료일  0.종료 : "))
        print("")
        info_show_indiviual(info_search('student_ID',ID))

        value_revise = input("수정할 내용을 입력하세요 : ")
        if number == 1:
            revise_index['student_name'] = value_revise
        elif number == 2:
            revise_index['student_age'] = value_revise
        elif number == 3:
            revise_index['address'] = value_revise
        elif number == 4:
            revise_index.get('total_course_info')['num_of_course_learned'] = value_revise
        elif number == 5:
            revise_index.get('total_course_info')['learning_course_info'][0]['course_code'] = value_revise
        elif number == 6:
            revise_index.get('total_course_info')['learning_course_info'][0]['course_name'] = value_revise
        elif number == 7:
            revise_index.get('total_course_info')['learning_course_info'][0]['teacher'] = value_revise
        elif number == 8:
            revise_index.get('total_course_info')['learning_course_info'][0]['open_date'] = value_revise
        elif number == 9:
            revise_index.get('total_course_info')['learning_course_info'][0]['close_date'] = value_revise
        elif number == 0:
            continue

        print("------------- 수정 결과 -------------")
        info_show_indiviual(info_search('student_ID',ID))
        info_save()

    elif menu == 4 :
        print("\n============ 학생 정보 삭제 =============")
        select = int(input("1.학생의 모든 정보를 삭제     2.해당 수강 과목의 모든 정보 삭제     0.뒤로가기 : "))

        while True:
            search_index = input("학생ID를 입력하세요 ('ITT'로 시작됩니다) : ")
            info_show_plural(info_search('student_ID', search_index))
            if len(info_search('student_ID', search_index)) > 1:
                print("다시 입력해주세요")
                continue
            else:
                break

        if select == 3:
            continue

        elif select == 1:
            list = info_search("student_ID",search_index)[0]
            if list in jsonResult:
                jsonResult.remove(list)

            print("\n------------ 삭제 결과 -------------")
            info_show_indiviual(jsonResult)

        elif select == 2:
            course = input("해당하는 강의 코드를 입력하세요 : ")
            list = info_search("student_ID",search_index)[0]
            if list in jsonResult:
                for element in list.get('total_course_info')['learning_course_info']:
                    if course == element['course_code']:
                        list.get('total_course_info')['learning_course_info'].remove(element)
            print("\n------------ 삭제 결과 -------------")
            info_show_indiviual(info_search('student_ID', search_index))

        info_save()

    elif menu == 5:
        break