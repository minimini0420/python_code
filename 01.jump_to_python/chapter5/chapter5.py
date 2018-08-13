result=0
def adder(num):
    global result
    result += num
    return result

print(adder(3))
print(adder(4))


result1=0
result2=0

def adder1(num):
    global result1
    result1 += num
    return result1
def adder2(num):
    global result2
    result2 += num
    return result2

print(adder1(3))
print(adder1(4))
print(adder2(3))
print(adder2(7))

class simple:
    pass
a=simple()

print(a)

class Service:
    secret='영구는 배꼽이 두개다.'

pey = Service()
pey.secret
print(pey.secret)

class Service:
    secret="영구는 배꼽이 두개다"
    def sum(self, a, b):
        result=a+b
        print("%s+%s=%s입니다." %(a,b,result))
pey=Service()
print(pey.sum(1,1))

class Service:
    secret="영구는 배꼽이 두개다."
    def setname(self, name):
        self.name=name
    def sum(self,a,b):
        result=a+b
        print("%s님 %s + %s = %s 입니다." % (self.name, a,b,result))

pey=Service()
pey.setname("홍길동")
pey.sum(1,1)

class Service:
    secret='영구는 배꼽이 두개다.'
    def __init__(self,name):
        self.name=name
    def sum(self,a,b):
        result =a+b
        print('%s님 %s + %s = %s 입니다.' % (self.name, a, b, result))
    def __del__(self):
        print('저희 서비스를 이용해 주셔서 감사합니다.')

input()
pey=Service("홍길동")

input()
pey.sum(1.1)
input()

