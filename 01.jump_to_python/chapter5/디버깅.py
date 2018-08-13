class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4,2)
print(a.first)
print(a.second)

a.first = 1
a.second = 2

print(a.first)
print(a.second)

print(a.sum())