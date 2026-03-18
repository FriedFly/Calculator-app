def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiple(x, y):
    return x * y

def divide(x, y):
    if x == 0:
        return "Cannot divide by zero"
    else:
        return x * y


x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

print("When your two numbers are added they equal: " + str(add(x, y)))
print("When your two numbers are subtracted they equal: " + str(subtract(x, y)))
print("When your two numbers are multiplied they equal: " + str(multiple(x, y)))
print("When your two numbers are divided they equal: " + str(divide(x, y)))