# 디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 일까요?
#
# 디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됩니다.
#
# 00:00 (60초간 표시됨)
# 00:01
# 00:02
# ...
# 23:59

# 정답!!
# sumSec=0    # 초의 총합을 저장할 변수
# for hour in range(24) :     # 시간
#     for minute in range(60) :   #분
#         if '3' in str(hour) or '3' in str(minute) : # 시간이나 분에 3이 들어가면
#              sumSec += 60            # 60초씩 더함
# print(sumSec)

def time():
    count_hour = 0
    count_min = 0
    second = 60

    # hour
    for i in range(0,24):
        if i == 3 or i == 13 or i == 23:
            count_hour += 1
        else:
            continue

    total_hour = count_hour * second * second

    # min
    for i in range(0,60):
        if i == 3 or i == 13 or i == 23 or i == 43 or i == 53:
            count_min += 1
        elif 30 <= i < 40:
            count_min += 1
        else:
            continue

    total_min = count_min * second * 21

    total_time = total_hour + total_min
    return total_time

print(time())