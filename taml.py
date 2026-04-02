def add(a, b):
    print(f"{a} + {b} = {a + b}")

def sub(a, b):
    print(f"{a} - {b} = {a - b}")

def mul(a, b):
    print(f"{a} * {b} = {a * b}")

def div(a, b):
    if b != 0:
        print(f"{a} / {b} = {a / b}")
    else:
        print("Can't divide by zero!")

def calculator():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter your choice (1-4): "))
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        add(a, b)
    elif choice == 2:
        sub(a, b)
    elif choice == 3:
        mul(a, b)
    elif choice == 4:
        div(a, b)
    else:
        print("Invalid choice")
calculator()
