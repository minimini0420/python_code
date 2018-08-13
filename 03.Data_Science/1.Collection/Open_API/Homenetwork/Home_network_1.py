g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False


def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 프로그램 종료")


def check_device_status():
    print("\n난방기 상태: ", end='')
    if (g_Radiator == True):
        print("작동")
    elif (g_Radiator == False):
        print("정지")

    print("가스밸브 상태: ", end='')
    if (g_Gas_Valve == True):
        print("작동")
    elif (g_Gas_Valve == False):
        print("정지")

    print("발코니 윈도우 상태: ", end='')
    if (g_Balcony_Windows == True):
        print("작동")
    elif (g_Balcony_Windows == False):
        print("정지")

    print("출입문 상태: ", end='')
    if (g_Door == True):
        print("작동")
    elif (g_Door == False):
        print("정지")


def print_device_menu():
    print("상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")


def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door

    check_device_status()


while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if (menu_num == 1):
        check_device_status()
    elif (menu_num == 2):
        control_device()
    elif (menu_num == 3):
        break