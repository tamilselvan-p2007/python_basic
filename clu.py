def add(a,b):
    print(a+b)
def sub(a, b):
    print(a-b)
def mul(a, b):
    print(a*b)
def div(a, b):
    print(a/b)
def mod(a,b):
    print(a%b)
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. modulus")
choice = int(input("Enter your choice (1,2,3,4,5):"))
r = float(input("Enter first number: "))
g= float(input("Enter second number: "))
if choice == 1:
    print(add(r,g))
elif choice == 2:
       print(sub(r,g))
elif choice == 3:
       print(mul(r,g))
elif choice == 4:
       print(div(r,g))
elif choice == 5:
       print(mod(r,g))
else:
       print("Invalid choice")
