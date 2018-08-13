class unit: # 여러 개의 클래스가 항목을 중복하고 있으면 슈퍼(super) 클래스를 만들어 그 항목들을 뽑아낸다.
    에너지  # 슈퍼 클래스를 제외한 나머지 클래스는 차일드(child) 클래스
    방어력
    유닛타입
    x좌표
    y좌표
    def 정찰(self):
    def 이동(self):
    def 정지(self):

class SCV(unit):
    이름
    공격력
    사거리
    공격타입
    def 자원채취(self):
    def 공격(self):
    def 건물건설(self):
    def 수리(self):
d