#f = open("D:\\고객서빙현황로그.txt", "w")
#f.close()
# 위에 파일은 한번만 열어라 안그럼 계속 미친듯이 열었다가 닫았다 한다.
class Restaurant:
    number_served = 0
    def __init__(self, name, type):
        self.name = name
        self.type = type
    def describe_Restaurant(self):
        print("저의 레스토랑의 명칭은 '%s'이고 '%s' 전문점 입니다." % (self.name, self.type))
    def open(self, time):
        print("%s는 %d시에 오픈합니다. 환영합니다." %(self.name, time))
    def set_number_served(self,number):
        self.number_served = number
        print("방문한 고객의 수 변경: %d" %(number))
    def increament_number_served(self, number):
        self.number_served += number
        print("하루 동안 서빙한 숫자: %d" %(self.number_served))
    def __del__(self):
        print("오늘 하루도 고생하셨습니다.!! 간바레!!")

a=Restaurant("울랄라","치킨")
a.increament_number_served(60)

f=open("D:\\고객서빙현황로그.txt", 'r')
while True:
    last_log=0
    line=f.readline()
    if not line:
        break
    print(line)
f.close()



f=open("D:\\고객서빙현황로그.txt", 'a')

f.write(str(a.number_served))
f.close()