import json
import urllib.request
import datetime
import time
import threading

access_key = "5X8xep2Y7D1S6%2BGl%2BnrnabFJiL%2FVdT8wO7ipvtPwWTvV7bgtEFuqBqGgmYS8Z1hnj0BWMtukD5u9QihQlbmGKQ%3D%3D"
g_Radiator = False
g_Gas_Valve = False
g_Balcony_window = False
g_Door = False
g_AI_Mode = False


def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 프로그램 종료")

def check_device_status():
    print("\n난방기 상태 : ", end = '')
    if g_Radiator == True: print("작동")
    elif g_Radiator == False: print("정지")

    print("가스벨브 상태 : ", end='')
    if g_Gas_Valve == True: print("작동")
    elif g_Gas_Valve == False: print("정지")

    print("발코니 창문 상태 : ", end='')
    if g_Balcony_window== True: print("작동")
    elif g_Balcony_window == False: print("정지")

    print("출입문 : ", end='')
    if g_Door == True: print("작동")
    elif g_Door == False: print("정지")

def print_device_menu():
    print("\n상태 변경할 긔긔")
    print("1. 난방기")
    print("2. 가스벨브")
    print("3. 발코니 창")
    print("4. 출입문")
    print("0. 뒤로가기")
    menu_num = int(input("메뉴를 선택하세요 : "))
    return menu_num

def control_device(number):
    global g_Radiator, g_Gas_Valve, g_Balcony_window, g_Door
    if number > 0:
        check_device_status()
        if number == 1: g_Radiator  = not g_Radiator
        elif number == 2: g_Gas_Valve = not g_Gas_Valve
        elif number == 3: g_Balcony_window = not g_Balcony_window
        elif number == 4: g_Door = not g_Door
        check_device_status()
    else:
        return number
def get_realtime_weather_info():
    print("자! 메뉴얼을 보고 작성해보시오!!")

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

def getWeather(nx,ny) :
    end_point = "http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"
    base_time = time.strftime("%H%M",time.localtime(time.time()))
    base_time = int(base_time) - 100
    parameters = "?base_date=" + time.strftime("%Y%m%d", time.localtime(time.time()))
    parameters += "&base_time=" + str(base_time)
    parameters += "&nx=" + nx
    parameters += "&ny=" + ny
    parameters += "&_type=json&serviceKey=" + access_key

    url = end_point + parameters
    retData = get_request_url(url)

    if (retData == None):
        return None
    else:
        return  json.loads(retData)

def show_weather_main():
    jsonResult = []
    nx = '89'
    ny = '91'
    jsonData = getWeather(nx,ny)

    if (jsonData['response']['header']['resultMsg'] == "OK"):
        for element in jsonData['response']['body']['items']['item']:
            jsonResult.append(element)

def weather_save():
    with open('%s_기상예보.json' % time.strftime("%Y%m%d",time.localtime(time.time())),'w',encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult,indent=4,sort_keys=True,ensure_ascii=False)
        outfile.write(retJson)

    print("%s_기상예보.json" % time.strftime("%Y%m%d_%H%M",time.localtime(time.time())))

def update_scheduler():
    global g_Balcony_Windows
    while True:
        if g_AI_Mode == False:
            continue
        else:
            time.sleep(5)
            g_Balcony_Windows = not g_Balcony_Windows

def smart_mode():
    global g_AI_Mode
    print("\n1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    print("4. 비오는 날 강수예보 시뮬레이션")
    menu_num = int(input("메뉴를 선택하세요 : "))

    if menu_num == 1:
        print("\n현재 인공지능 모드 : ", end="")
        if g_AI_Mode == True:  print("작동")
        else : print("중지")

    elif menu_num == 2 :
        print("인공지능 모드: ", end='')
        g_AI_Mode = not g_AI_Mode
        if g_AI_Mode == True:
            print("작동")
        else:
            print("정지")

    elif menu_num == 3 :
        if __name__ == "__main__":
            show_weather_main()
            weather_save()

    elif menu_num == 4:
        global g_Balcony_window
        weather_list = []
        weather_info = {}
        weather_info["category"] = "RN1"
        weather_info["fcstValue"] = "10"
        weather_info["fsctTime"] =  1600
        weather_list.append(weather_info)
        with open("창문을닫자.json", "w", encoding="utf-8") as outfile:
            weather_record = json.dumps(weather_list, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(weather_record)

        with open("창문을닫자.json", encoding="utf8") as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            jsonResult = json.loads(json_string)

        print("발코니 창문 상태 : ", end='')
        if g_Balcony_window == True:
            print("열림")
            if jsonResult[0]["fcstValue"] != "0":
                g_Balcony_window = not g_Balcony_window
                print("닫힘")
        elif g_Balcony_window == False:
            print("닫힘")


t = threading.Thread(target=update_scheduler)
t.daemon = True
t.start()

while True:
    jsonResult = []
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요 : "))

    if menu_num == 1 :
        check_device_status()

    elif menu_num == 2:
        number = print_device_menu()
        if control_device(number) == 0 :
            continue

    elif menu_num == 3:
        smart_mode()

    elif menu_num == 4:
        print("프로그램을 종료합니다......")
        break