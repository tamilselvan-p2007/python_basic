a = int(input("Enter first number: ")) 
b = int(input("Enter second number: ")) 
choice = input("Enter +, -, *, /: ") 
if choice == "+": 
  print("Result:", a + b) 
elif choice == "-": 
  print("Result:", a - b) 
elif choice == "*": 
  print("Result:", a * b) 
elif choice == "/": 
  print("Result:", a / b) 
else: 
  print("Invalid choice") 
