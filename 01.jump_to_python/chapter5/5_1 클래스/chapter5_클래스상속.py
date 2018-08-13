def mul(num1,num2):
    return num1+num2
def mul(num1,num2,num3):
    return num1+num2+num3
print(mul(1,2,4))

class HousePark:
    lastname="박"
    def __init__(self,name):
        self.fullname=self.lastname + name
    # def setname(self,name):
    #     self.fullname=self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다." % (self.fullname, where))

# pey=HousePark()
# pey.setname("응용")
pey=HousePark("응용")
pey.travel("부산")

class HouesKim(HousePark):
    lastname = "킴"
    # 매서드 오버라이딩 : 클래스를 만들다 보면 상속받을 대상인 클래스의 메서드와 이름은 같지만 다르게 행동 해야 하는
    # 경우가 있다. 이럴떄 매서드 오버라이딩을 사용한다.
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네." %(self.fullname, where, day))


juliet = HouesKim("줄리엣")
juliet.travel("독도",3)
#  객체 지향은 다중 상속을 설정 할 수가 있다.
