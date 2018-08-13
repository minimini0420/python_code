data = input("Input any kind type of data: ")

# data = int(data)
data = float(data)

if type(data) == int:
    print("This type is 'int'")
elif type(data) == float:
    print("This type is 'float'")
else:
    print("The default type is 'string'")