## Student_management_programing
import json
import os

jsonResult = []

def ask_path():
    ask = input("안녕하세요! 학생 주소록 관리 프로그램을 시작합니다. 경로에 파일이 없습니다. \n 1. 경로를 입력합니다.  2. 기본 경로로 생성하겠습니다.\n 메뉴를 선택하세요 : ")
    if ask == '1':
        path = input("새로운 경로를 입력하세요 : ")
        print("새로운 경로에 저장합니다.")
        return path
    else:
        print("기본경로로 생성하겠습니다.")
        path = 'ITT_Student.json'
        return path

def student_ID_number():
    try:
        if not os.path.isfile("ITT_Student.json"):
            with open('count.txt','w') as file:
                counter = '1'
                file.write(counter)
            student_id = "ITT" + counter.zfill(3)
            return  student_id
        else:
            with open('count.txt','r') as file:
                counter = file.readline()
                counter = int(counter) + 1
                student_id = "ITT" + str(counter).zfill(3)

            with open('count.txt', 'w') as file:
                file.write(str(counter))
            return student_id

    except FileNotFoundError:
        if len(jsonResult) == 0:
            counter = '1'
            student_id = "ITT" + counter.zfill(3)
            with open("count.txt",'w') as file:
                file.write(counter)
            return  student_id
        else:
            counter = str(len(jsonResult) + 1)
            with open('count.txt', 'w') as file:
                file.write(counter)
            student_id = "ITT" + counter.zfill(3)
            return student_id

def info_insert():
    student_dic = {}
    recent_info_list = []
    number = int(input("1. 새로운 학생 정보 입력    2. 기존의 정보에 새로운 강의 추가   3. 뒤로가기\n<< 메뉴를 선택하세요 : "))
    print("")
    if number == 1:
        print("=======  학생 정보 입력을 시작합니다  ======")
        student_dic['name'] = input("이름을 입력하세요 (예 : 홍길동): ")
        student_dic['age'] = str(input("나이를 입력하세요 (예 : 19): "))
        student_dic['address'] = input("주소를 입력하세요 (예 : 한양 북촌마을): ")
        student_dic['past_record'] = input("과거 수강 횟수를 입력하세요 (예 : 0): ")
        while True:
            select = input("현재 강의 정보를 추가하시겠습니까? (y/n) : ")
            if select == 'y':
                recent_info_list.append(info_insert_course())
                student_dic['recent_info'] = recent_info_list
                continue
            elif select == 'n':
                break
        student_dic['student_ID'] = student_ID_number()
        jsonResult.append(student_dic)
        print("====== 학생 정보 입력이 되었습니다 ======")
        print("")

    elif number == 2:
        index = input("학생ID를 정확하게 입력하세요 : ")
        for element in jsonResult:
            if index in element.values():
                try:
                    element.get('recent_info').append(info_insert_course())
                except:
                    element['recent_info'] = []
                    element.get('recent_info').append(info_insert_course())
        print("====== 새로운 강의 정보가 추가 되었습니다 ======")
        print("")

    elif number == 3:
        index = 3
        return index

def info_insert_course():
    recent_info = {}
    recent_info['강의코드'] = input("현재 수강 과목 코드를 기입하세요 (예 : IB171106): ")
    recent_info['강의명'] = input("강의명을 입력하세요 (예 : IoT 빅데이터 실무반): ")
    recent_info['강사명'] = input("강사명을 입력하세요 (예 : 이현구): ")
    recent_info['개강일'] = input("개강일을 입력하세요 (예 : 2017-11-06): ")
    recent_info['종료일'] = input("종료일을 입력하세요 (예 : 2018-09-05): ")
    return recent_info

def info_input():
    print("")
    print("========== 학생 정보 조회를 시작합니다 ==========")
    print("1. 전체 항목 대상 조회")
    print("\t<< 검색 조건 선택 >>\t")
    print("2. 학생 ID")
    print("3. 학생 이름")
    print("4. 학생 나이")
    print("5. 학생 주소")
    print("6. 과거 수강 횟수")
    print("7. 강의명")
    print("8. 강사명")
    print("9. 강의코드")
    print("10. 이전화면으로 되돌아갑니다")
    print("")
    condition = int(input("검색 조건을 선택하세요 : "))
    return condition

def info_search(key, search_index):
    result = []
    for element in jsonResult:
        if key in element.keys():
            if element[key] == search_index:
                result.append(element)
            elif search_index in element[key]:
                result.append(element)
        else:
            try:
                for j in range(len(element["recent_info"])):
                    if element["recent_info"][j][key] == search_index:
                        result.append(element)
                    elif search_index in element["recent_info"][j][key]:
                        result.append(element)
            except : pass
    return result

def info_show_indiviual(result):
    print("")
    for i in range(len(result)):
        print("==================== 학생 회원 정보 - %d - ==================" % (i+1))
        print("<< 학생정보 >>")
        print("학생ID    : %s " % result[i]['student_ID'])
        print("이름      : %s " % result[i]['name'])
        print("나이      : %s " % result[i]['age'])
        print("주소      : %s " % result[i]['address'])
        print("수강 정보 :")
        print("- 과거 수강 횟수 : %s " % result[i]['past_record'])
        try:
            for j in range(len(result[i].get('recent_info'))):
                print("----------------------------------------")
                print("- 현재 학생의 수강 정보 < %d >" % (j+1))
                print("   강의코드 : %s"  % result[i].get('recent_info')[j]['강의코드'])
                print("   강의명   : %s"  % result[i].get('recent_info')[j]['강의명'])
                print("   강사명   : %s"  % result[i].get('recent_info')[j]['강사명'])
                print("   개강일   : %s"  % result[i].get('recent_info')[j]['개강일'])
                print("   종료일   : %s"  % result[i].get('recent_info')[j]['종료일'])
        except : pass
        print("============================================================")
        print("")

def info_show_plural(result):
    print("=================== 학생 회원 정보 ====================")
    for i in range(len(result)):
        print(">>> %d. 학생 ID : %s, 학생이름 : %s" % (i + 1,result[i]["student_ID"],result[i]['name']))
    print("=======================================================\n")

def info_revise(result):
    while True:
        print("===== <<< 학생 정보를 수정하겠습니다 >>> =====")
        print("1.이름  2.나이  3.주소  4.과거 수강 횟수  5.강의명  6.강의코드  7.강사명  8.뒤로가기")

        number = int(input("메뉴를 선택하세요 : "))
        if number < 8:
            revise_value = input("수정할 정보를 입력하세요 : ")
            if number == 1 :
                result[0]['name'] = revise_value
            elif number == 2:
                result[0]['age'] = revise_value
            elif number == 3:
                result[0]['address'] = revise_value
            elif number == 4:
                result[0]['past_record'] = revise_value
            elif number == 5 :
                result[0].get('recent_info')[0]['강의명'] = revise_value
            elif number == 6:
                result[0].get('recent_info')[0]['강의코드'] = revise_value
            elif number == 7:
                result[0].get('recent_info')[0]['강사명'] = revise_value
        elif number == 8 :
            return number
        print("")
        Quit = int(input("종료를 원하시면 1번을 입력하시고 계속 수정하시려면 2번를 눌러주세요 : "))
        if Quit == 1:
            break
        elif Quit == 2:
            continue

def info_delete_intro():
    print("=================  학생 정보 삭제  ====================")
    know_ask = input("학생ID를 정확하게 알고계십니까?? y/n : ")

    if know_ask == 'n':
        index_key = input("기억하고 있는 학생ID 일부분을 입력하세요 : ")
        print("")
        info_show_plural(info_search("student_ID",index_key))
        info_delete()

    elif know_ask == 'y':
        info_delete()

def info_delete():
    index = input("학생ID를 입력하세요 : ")
    info_show_indiviual(info_search("student_ID",index))

    print('메뉴를 선택하세요')
    number = int(input("1. 학생ID 전체삭제       2. 현재 수강중인 강의삭제 : "))
    if number == 1:
        for element in jsonResult:
            if element['student_ID'] == index:
                element_del = element
                ask = input("선택하신 정보를 정말 삭제할까요? y/n : ")
                if ask == 'y' :
                    jsonResult.remove(element_del)
                    print("============= 안전하게 삭제되었습니다 =============")
                elif ask =='n' :
                    pass

    elif number == 2:
        index_2 = input("원하시는 과목코드를 입력하세요 : ")
        for i in range(len(jsonResult)):
            if jsonResult[i]['student_ID'] == index:
                for element_2 in jsonResult[i]['recent_info']:
                    if element_2['강의코드'] == index_2:
                        element_del = element_2
                        ask = input("선택하신 정보를 정말 삭제할까요? y/n : ")
                        if ask == 'y':
                            jsonResult[i]['recent_info'].remove(element_del)
                            print("============= 안전하게 삭제되었습니다 =============")
                        elif ask == 'n':
                            pass

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

def info_save():
    with open('ITT_Student.json', 'w', encoding='UTF8') as outfile:
        readable_result = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(str(readable_result))

print(" \t\t\t\t==<< 학생 주소록 관리 프로그램을 실행합니다 >>==\t\t\t\t")
print("")

try:
    with open('ITT_Student.json', encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        jsonResult = json.loads(json_string)

except FileNotFoundError:
     jsonResult = info_start(ask_path())
     print('ITT_Student.json SAVED')

while True :
    print("<< json 기반 주소록 관리 프로그램 >>")
    print("  1. 학생 정보 입력")
    print("  2. 학생 정보 조회")
    print("  3. 학생 정보 수정")
    print("  4. 학생 정보 삭제")
    print("  5. 프로 그램 종료")
    option = int(input('메뉴을 선택해주세요 : '))
    try:
        if option == 1 :
            if info_insert() == 3:
                continue
            else:
                index = int(input("정보를 저장하시려면 '1번'를 입력하시고\n지금까지의 정보 입력을 취소하시려면 '2번'를 입력하세요 : "))
                if index == 1 :
                    info_save()
                    print("")
                elif index == 2:
                    print("")
                    continue

        elif option == 2 :
            number = info_input()
            if number == 1:
                info_show_indiviual(jsonResult)
            elif 10 > number > 1:
                key_word = input("키워드를 입력하세요 : ")
                if number == 2 :
                    element = "student_ID"
                elif number == 3 :
                    element = "name"
                elif number == 4:
                    element = "age"
                elif number == 5 :
                    element = "address"
                elif number == 6 :
                    element = "past_record"
                elif number == 7 :
                    element = "강의명"
                elif number == 8 :
                    element = "강사명"
                elif number == 9 :
                    element = "강의코드"

                if len(info_search(element,key_word)) == 1:
                    info_show_indiviual(info_search(element,key_word))
                elif len(info_search(element,key_word)) > 1:
                    info_show_plural(info_search(element,key_word))

            elif number == 10:
                continue

        elif option == 3 :
            print("")
            print("====== 학생 정보 수정을 시작합니다 ======")
            print("Information : '학생ID'는 수정이 불가합니다 ^_^ \n")

            while True:
                key_word = input("학생ID를 입력하세요 : ")
                if len(info_search("student_ID", key_word)) == 1:
                    info_show_indiviual(info_search("student_ID", key_word))
                    info_revise(info_search("student_ID", key_word))
                    break
                elif len(info_search("student_ID", key_word)) > 1:
                    info_show_plural(info_search("student_ID", key_word))
                    print("다시 입력하세요!")
                    continue
                info_show_indiviual(info_search("student_ID", key_word))
            info_save()
            print("")

        elif option == 4 :
            info_delete_intro()
            info_save()

        elif option == 5 :
            print("====== 프로그램을 종료합니다 ======")
            break
    except:
        continue