PI = 3.141592
class Math:
    def solv(self, r):
        return PI * (r**2) # r** = 'r'의 제급을 뜻함

def sum(a,b):
    return a+b

if __name__=="__main__":
    print(PI)
    a=Math()
    print(a.solv(2))
    print(sum(PI, 44))

if __file__=="mod2.py":
    print("요기 있넹~")
