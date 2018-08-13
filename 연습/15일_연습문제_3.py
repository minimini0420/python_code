# [연습문제 3]
# 게시물의 총 건수와 한 페이지에 보여줄 게시물 수를 입력으로 주었을 때 총 페이지수를
# 출력하는 프로그램을 작성하시오.
# 페이지수를 계산하는 함수는 아래 이름으로 작성하시오.
# def getTotalPage(m,n)
# 게시물 총 건수와 한 페이지에 보여줄 게시물 수는 'condition.txt'에 아래와 같이 정의 되어 있다.
# 5 10
# 15 10
# dfdf dfkdf
# 25 10
# 30 10
#
# <출력>
# 게시물 총 건수: 5, 한 페이지에 보여줄 게시물 수: 10, 총 페이지수: 1
# .
# .
# .
# .
#
# 만약에 condition.txt 파일에 숫자가 아닌 쓰레기 값이 들어가 있는 열이 있다면
# 이는 무시하고 정상적인 값에 대해서만 출력한다.
def getTotalPage(m,n):
    if m % n == 0 :
        return m//n
    else:
        return m // n+1

f=open("D:\\condition.txt",'r')
line = f.readlines() #readlines 함수는 파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 리스트로 리턴한다.
f.close()

result = ""
m=""
n=""
for i in line:
    A=i.split()
    try:
        m=A[0]
        n=A[1]
        B='게시물 총 건수: %d, 한 페이지에 보여줄 게시물 수: %d, 총 페이지수: %d\n' %(int(m),int(n),int(getTotalPage(int(m),int(n))))
        result += B
    except:
        pass
print(result)