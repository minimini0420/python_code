# <연습문제 2: 프로그래머 설문조사>
# 사람들에게 왜 프로그래밍이 좋아하는지 물어본다. (반복문으로 구성)
# "프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료):"
# 응답을 한다면 이름을 물어 본다.
# 이름을 입력 받았으면 "설문에 응답해 주셔서 감사합니다." 메세지를 출력한다.
# "종료" 메세지가 입력되면 지금까지 설문 내용을 아래 형식으로 'poll.txt'에 저장한다.
#
# ex) poll.txt
# [김기정] 내가 원하는 모든 것을 만들 수 있어서
# [남시언] 빨리 취업하고 싶어서
# [윤성우] 재미 있네요.
f=open('D:\\poll.txt','w')
while True:
    quest=str(input('프로그래밍이 왜 좋으세요?(종료 입력시 프로그램 종료):\n'))
    if quest == '종료':
        f.close()
        break
    else:
        name=str(input('성함이 어떻게 되시죠?\n'))
        print('설문에 응답해주셔서 감사합니다.')
        f.write(str('[%s] %s\n' % (name,quest)))