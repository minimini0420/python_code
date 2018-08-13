# 추가 실습
# 상속의 개념을 활용해서 레스토랑 클래스 작성하시오
# Super Class: 레스토랑의 공통 속성 및 행위 정의
# Child Class: 레스토랑에 특화된 속성과 행위 정의
class FoodCourt:
    name = "신세계 푸드코드"
    Working_time = "9시간"
    regular_r_time = "매월 2주, 4주 월요일"
    def __init__(self,type,name):
        self.fullname = self.name+" "+type
        self.name1=name
    def introduce(self):
        print("어서오세요~!! %s 요리 전문점, '%s' 입니다. 자리 안내해드리겠습니다~" % (self.fullname, self.name1))
    def cook(self, main, recomand):
        print("저희 매장의 메인 요리는 '%s'이며, ")

pey = FoodCourt("중국","칭샤오")
pey.introduce()

class chinese(FoodCourt):
    event = "국경절"
    date = "1일~4일"
    def day_off(self):
        print("이번달 '%s' 때문에 %s!! 가게 문을 닫습니다." %(self.event, self.date))

a = chinese("상하이","칭샤오")
a.day_off()

