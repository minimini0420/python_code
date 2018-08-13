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