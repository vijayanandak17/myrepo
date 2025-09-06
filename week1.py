#Basic Program
print("My first program")

#Operators & Data Types
Age=30
print(f"Age: {Age}")
a=10
b=3
c=2
c+=3
print(f"//: {a//b}")
print(f"%: {a%b}")
print(f"**: {a**b}")
print(c)
fruit=["Apple","Grape","Lemon","Berry"]
print(len(fruit))
fruit[2]="Guava"
print(fruit)
aadhar = ("Vijay",55,"Chennai")
print (aadhar)
print(aadhar[2])
student= {
    "Name":"Vijayanand",
    "Age":55,
    "Place": "Chennai"
}
print(student["Name"])
student["Age"]=27
del(student["Place"])
print(len(student))
print(student)

#Control Flows
a=int(input("Enter your age: "))
print(a)
if a<=10:
    print("You will live for 30000 days")
elif a>10 and a<=90:
    print("You will live for 20000 days")
else:
    print("No chance buddy !")


#Loops
for a in range(1,3):
    print (a)
    for b in fruit:
        print (b)

# Functions, Error Handling
def div(a,b):
    return a/b
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
z=None
try:
    z=div(x,y)
    print (z)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except Exception as e:
    print("Error created by you:", e)
finally:
    print(f"Function Result: {z}")

# File Handling
#add
file = open("Notes.txt","w")
content=file.write("This is my new content \n")
file.close()
#append
file = open("Notes.txt","a")
content=file.write("This is my second line appended")
file.close()
#Read
with open("Notes.txt") as file:
    content=file.read()
    print(content)

#Folder handling
import os
print(os.getcwd())
print(os.listdir())

# if we have a folder called "Testing" and if we have a function add(a,b)
# we can call the add(a,b) function from a different folder with code below
# from Testing.package import add
# print add(2,3)
### This is how import function works

