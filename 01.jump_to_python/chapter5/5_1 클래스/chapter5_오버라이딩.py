class HousePark:
    lastname="박"
    def __init__(self,name):
        self.fullname=self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다." % (self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
    def fight(self, other):
        print("%s, %s 싸우네" % (self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s 이혼했네" % (self.fullname, other.fullname))

class HouesKim(HousePark):
    lastname = "킴"
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네." %(self.fullname, where, day))

pey = HousePark("응용")
juliet = HouesKim("줄리엣")
pey.travel("뉴욕")
juliet.travel("뉴욕", 4)
pey.love(juliet)
pey + juliet # 숫자와 숫자를 더하면 값이 달라지지만, 문자와 문자를 더하면 문자들이 결합한다.
pey.fight(juliet)
pey - juliet