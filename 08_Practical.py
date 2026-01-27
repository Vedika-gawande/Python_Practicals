# Simple function
def student():
    rollno=input("Enter Roll no : ")
    name=input("Enter name : ")
    per=input("Enter percentage : ")
    print(f"Hello my Roll no is {rollno} my name is {name} and my per is {per}")
student()

# Paramaterized function 
def student(rollno,name,per):
    print(f"Hello my Roll no is {rollno} my name is {name} and my per is {per}")
student(2,"Vedika",92.40)