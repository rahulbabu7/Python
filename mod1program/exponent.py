x = int(input("enter the value of x"))
n = int(input("Enter the value for n"))
total = 1
fact =1
for i in range(1,n+1):
    fact = fact*i
    total = total +(x**i)/fact
print(total)
