limit = int(input("Enter the limit"))
sum = 0
for i in range (limit):
    num= int(input("Enter the number"))
    if num%2 ==0:
        sum = sum+num
print(sum)
    