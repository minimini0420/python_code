sum=lambda a, b:a+b
print(sum(3,4))


def sum(a,b):
    return a+b

myList=[lambda a,b:a+b,lambda a,b:a*b]
print(myList[1](3,4))

a=len('python')
print(a)
