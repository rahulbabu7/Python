limit = int(input("Enter the limit:"))
oddcount = 0
evencount=0
for i in range(limit):
    numb = int(input("enter the number"))
    if numb%2==0:
        evencount+=1
    else:
        oddcount+=1
print("odd number ="+str(oddcount))
print("even number ="+str(evencount))