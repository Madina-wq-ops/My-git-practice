print("Welcome to my simple Python program!")

def add(a, b):
    return a + b

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print(f"{x} + {y} = {add(x, y)}")
