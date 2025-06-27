# Q1. Create a Student Registration Form

'''
Take the following inputs:
- Name -> str
- Roll No -> int
- Percentage -> float
- Is Passed? (Yes/No) -> bool (use bool(input(...)) logic)

Print Format:
+-----------------------------+
|       STUDENT DETAILS       |
+-----------------------------+
| Name : _________            |
| Roll No : _________         |
| Percentage : _________      |
| Passed : True/False         |
+-----------------------------+
'''


#Input Collection
name = input("Enter Your Name:")
rollno = int(input("Enter Your Roll No:"))
percentage = float(input("Enter Your Percentage:"))
is_pass = bool(input("Is Passed? (true/false): "))

print("\n+-----------------------------+")
print("|       STUDENT DETAILS       |")
print("+-----------------------------+")
print("| Name : ",name,"             |")
print("| Roll No : ",rollno,"        |")
print("| Percentage : ",percentage," |")
print("| Passed : ",is_pass,"        |")
print("+-----------------------------+")

'''
Note : Boolean Datatype Only Checks The Str is Empty or Not

bool("true")   → True  
bool("false")  → True  
bool("0")      → True  
bool("")       → False

'''

