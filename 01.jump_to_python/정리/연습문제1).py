import sys

args = sys.argv[1:]

for i in args:
    print("Hello!, %c" % i[0].upper(), end="")
    print("%s!" % i[1:])

# cmd 에서 실행시켜야한다.
# 결과 - input(python 연습문제1).py janny hannah margot kevin min
    # Hello!, Janny!
    # Hello!, Hannah!
    # Hello!, Margot!
    # Hello!, Kevin!
    # Hello!, Min!