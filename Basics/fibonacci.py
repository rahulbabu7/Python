limit = int(input("Enter the limit"))

first = 0
second =1
print(first)
print(second)
for i in range(2,limit):
   
    
    third = first + second
    first = second
    second = third
    print(third)