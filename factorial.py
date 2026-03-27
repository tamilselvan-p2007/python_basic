# function to find factorial of given number
def factorial(n):
 if (n==1 or n==0):
     return 1 
 else:
     return n * factorial(n_1) #recursion
 
num = 6;
print("Factorial of,num,"is",factorial(num)")
