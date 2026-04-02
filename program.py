def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:", a + b)

def sub():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Difference:", a - b)

def mul():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Product:", a * b)

def div():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b != 0:
        print("Division:", a / b)
    else:
        print("Can't divide by zero!")

add()
sub()
mul()
div()
