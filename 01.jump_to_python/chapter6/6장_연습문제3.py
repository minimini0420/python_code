def mos(string):
    mos = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I',',---':'J','-.-':'K',
           '.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V',
           '.--':'W','-..-':'X','-.--':'Y','--..':'Z'}
    result = ""
    A=string.split()
    for i in A:
        if i:
            number=0
            I=mos.get(A[number])
            result+=I

while True:
    string = str(input('모스부호를 입력하시오:\n'))
    print(mos(string))