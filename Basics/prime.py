limit = int(input("Enter the range :"))

for i in range (1,limit):
    flag=0
    for k in range(2,(i//2)+1):
        if i%k==0:
            break  
        else:
        if