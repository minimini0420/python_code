#문자열 슬라이싱
a="Life is too short, You need Python"
b=a[0]+a[1]+a[2]+a[3]
print(b)
print(a[0:4])
print(a[12:17])
print(a[19:])

# 문자열 삽입
a=' '
a.join('Life')
print(a.join('Life'))

#리스트에 요소 추가
b=['human','animal','mammal']
b.append(['insect','reptilia'])
print(b)

a="Life si too short"
a.index('t')
print(a.index('t'))
