def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a) !=type(b): # '!' 는 같지 않다는 말이다.
        print("더할 수 있는 것이 아닙니다!!! 다시하라우!!!")
        return
    else:
        result = sum(a,b)
    return result

if __name__=="__main__": # 이 프로그램의 주체가 무엇이 메인인지 알기 위한 것(메인과 서브를 구분하기 위한것)
                         # C 에서는 이것을 전처리, 매크로라고 부른다. (__***__ 이와 같은 form)
    print(sum(1,2))
    print(safe_sum(1,"hello"))
