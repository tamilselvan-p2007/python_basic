marks = { 
"tamil": 80, 
"bala": 90, 
"jaga": 75 
} 
name = input("Enter student name: ") 
if name in marks: 
 print("Marks:", marks[name]) 
else: 
 print("Student not found") 
