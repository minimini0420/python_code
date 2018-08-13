# <연습문제 1: 파일 내 문자열 변경>
# 'learning_python.txt' 파일을 열어서 안에 있는 문자열 중에 'python'을 'C'로 변경하시오.
# 변경시 replace()함수를 사용할 것
# 변경한 내용을 'learn_python_copyed.txt'로 저장할 것

f=open('D:\\learning_python.txt','r')
data=f.read()
print(data)
f.close()

data.replace('python','C')

f=open('D:\\learn_pyhton_copyed.txt','w')
f.write(data.replace('python','C'))
f.close()

