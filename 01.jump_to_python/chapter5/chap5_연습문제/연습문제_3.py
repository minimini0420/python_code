# <연습문제 3: 프로그래머 설문조사>
# 연습문제 2 프로그램을 이용해서 프로그램이 종료 후 재 실행되어도 추가 설문내용이
# poll.txt 파일에 추가 될 수 있게 한다.
# 이 때 poll.txt 파일이 없을 경우에 사용자에게 종료 및 변경된 파일 경로를 물어볼 수 있게 선택한다.
# 예) poll.txt 파일이 없습니다. 아래 중 선택하세요.
# 1. 종료
# 2. 변경된 파일 경로 입력
#
# 2번 입력시 아래 메세지 출력
# 변경된 파일 경로를 입력하세요. :
try:
    f=open('D:\\python_workspace\\poll.txt','r')
    data=f.read()
    f.close()

    f=open('D:\\python_workspace\\poll.txt','a')
    while True:
        quest = str(input('프로그래밍이 왜 좋으세요?(종료 입력시 프로그램 종료):\n'))
        if quest == '종료':
            f.close()
            break
        else:
            name = str(input('성함이 어떻게 되시죠?\n'))
            print('설문에 응답해주셔서 감사합니다.')
            f.write(str('[%s] %s\n' % (name, quest)))

except FileNotFoundError:
    path=str(input('"poll.txt" 파일이 없습니다. 아래 중 선택하세요.\n1.종료\n2.변경된 파일 경로 입력\n'))
    if path == '종료':
        break