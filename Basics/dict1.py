limit = int(input("Enter the number of students"))
student = {}
for i in range(limit):
    name = input("Enter the name")
    age= int(input("Enter the age"))
    
    student[name] = age
    
new = sorted(student)
print(student)
print(new)

