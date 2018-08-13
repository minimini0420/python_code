# [연습문제 4]
# 프로그램 실행시 실행 인자를 받아 텍스트를 처리하는 메모장 프로그램을 작성한다.
# 입력 받는 문자열은 모두 영어로만 입력을 받는다.
# 예시) python memo.py -a "Life is too short"
# -a 입력시 'memo.txt' 파일이 있으면 열고 없으면 아래와 같이 물어본다.
# 아래 중 선택하세요.
# 1. 새로 생성하시겠습니까?
# 2. 파일 경로를 입력하겠습니다.
# 1인 경우에는 memo.txt를 새로 생성한다. 2인 경우에는 memo.txt 파일이 있는 경로를 입력한다.
#
# -au 옵션으로 입력시 입력받는 모든 영어 문자를 대문자로 변경하여 처리한다.
#
# -v가 들어온경우 파일에 있는 문자열을 모두 화면에 출력한다.
# 'memo.txt' 파일이 있으면 열고 없으면 아래와 같이 물어본다.
# 아래 중 선택하세요:
# 1. 종료하시겠습니까?
# 2. 파일 경로를 입력하세요.
import sys

args = sys.argv[1:]

command = sys.argv[1]
word = sys.argv[2:]
word1 = ' '.join(word)+'\n'

if command == '-a':
    try:
        f = open('D:\\memo.txt','r')
        f = open('D:\\memo.txt','a')
        f.write(word1)
        f.close()
    except FileNotFoundError:
        number = int(input('1. 새로 생성하시겠습니까?\n2. 파일 경로를 입력하시겠습니까?'))
        if number == 1:
            f = open('D:\\memo.txt','w')
            f.write(word1)
            f.close()
        elif number == 2:
            path = input('파일 경로를 입력하세요:\n')
            f = open(path,'w')
            f.write(word1)
            f.close()

elif command == '-au':
    f=open('D:\\memo.txt','a')
    f.write(word1.upper())
    f.close()

elif sys.argv[1] == '-v':
    try:
        f = open('D:\\memo.txt','r')
        while True:
            line = f.readline()
            if not line: break
            print(line, end='') # end 는 출력을 다다닥 붙이게 해주는 것이다.
    except FileNotFoundError:
        print('파일이 없습니다.')
        check=input('아래 중 선택하세요:\n1. 종료하시겠습니까?\n2. 파일 경로를 입력하세요.\n')
        if check == '1':
            print('종료되었습니다.')
        else:
            f=open(check,'r')
            while True:
                line=f.readline()
                if not line: break
                print(word1, end='')
            f.close()