limit = int(input("Enter the number of students"))
student = {}
for i in range(limit):
    name = input("Enter the name")
    
    dob = input("Enter the dob")
    
    student[name] = dob

print(student)

name = input("Enter the name")
dob = student[name]
print("Dob = ",dob)
