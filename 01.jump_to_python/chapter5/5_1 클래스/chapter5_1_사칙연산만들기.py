class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second # 디버깅 할때 결과를 바로 확인 가능함
        return result
        # return self.first + self.second ---> 똑같은 내용이지만 디버길할때 윗 방법은 바로 결과를 확인 할 수 있다.
        # 하지만 변수를 설정하지 않고 바로 결과를 도출해내면 복잡하다.

a = FourCal()
# a.setdata(4,2)

FourCal.setdata(a, 4, 2)


print(a.first)
print(a.second)

a.first = 1  # 함수를 통해 바꿀수도 있으나, 이렇게 직접 바로 바꿀 수도 있다.
a.second = 2 # 함수를 통해 바꾸려면 라인이 많이 필요하지만 직접 바꾸면 더 간단하지만, 보안에 취약하다는 단점이 있다.

print(a.first)
print(a.second)

print(a.sum()) # 그냥 print(sum)하면 안됨, 5 6 7라인을 불러온거임
