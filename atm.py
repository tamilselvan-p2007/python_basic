balance = 10000 
amount = int(input("Enter amount: ")) 
if amount <= balance: 
 if amount % 100 == 0: 
  print("Transaction successful") 
 else: 
    print("Enter amount in multiples of 100 ") 
else: 
    print("Insufficient balance")
