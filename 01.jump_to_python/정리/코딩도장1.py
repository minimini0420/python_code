a=0
sum=0
while a < 1000:
    a += 1
    if a % 2 ==0:
        continue
    if a%3 or a%5 == 0:
        print(a)
        sum += a
print(sum)
