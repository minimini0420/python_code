a=0
while True:
    m = int(input('총 건수를 입력하세요.'))
    n = int(input('한 페이지에 보여줄 게시물 수를 입력하세요.'))
    if m > n:
        if m % n == 0:
            a += 1
    else:
        a += 1
    print(a)
