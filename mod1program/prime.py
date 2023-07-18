num = int(input("Enter the number"))
flag =0
for i in range(2,(num)//2+1):
    if num %i ==0:
        flag =1
if(flag):
    print("Not")
else:
    print("yes")
