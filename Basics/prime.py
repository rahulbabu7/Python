limit = int(input("Enter the range :"))

for i in range (2,limit):
    flag=0
    for k in range(2,(i//2)+1):
        if i%k==0:
            flag = 1
            break  
           
         
    if(flag==0):
       print(i)