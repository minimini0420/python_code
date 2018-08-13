def positive(numberlist):
    result=[]
    for num in numberlist:
        if num > 0:
            result.append(num)
    return result

print(positive([1,-3,2,0,-1,6]))
