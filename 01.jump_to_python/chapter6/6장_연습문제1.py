def letter_counter(n):
    count = 0
    letter = "" # 문자가 바뀌는지 아닌지를 알 수 있는 장치
    result = "" # 결과를 축적시키는 저장공간
    for i in n:
        if letter != i:
            letter = i
            if count:
                result += str(count)
            result += i
            count = 1
        else:
            count += 1
    if count:
        result += str(count)
    return result

while True:
    n=str(input('문자를 입력하세요:\n'))
    print(letter_counter(n))