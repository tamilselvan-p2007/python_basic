users = { 
    "admin": "1234", 
    "user": "abcd" 
} 
 
username = input("Enter username: ") 
password = input("Enter password: ") 
 
if username in users: 
    if users[username] == password: 
        print("Login successful") 
    else: 
        print("Wrong password") 
else: 
    print("User not found") 
