class Calculator:
    def __init__(self,list):
        self.list=list

    def sum(self):
        print(sum(self.list))

    def avg(self):
        print(sum(self.list)/5)

if __name__=="__main__":
    cal1 = Calculator([1, 2, 3, 4, 5])
    cal1.sum()
    cal1.avg()
    cal2 = Calculator([6, 7, 8, 9, 10])
    cal2.sum()
    cal2.avg()