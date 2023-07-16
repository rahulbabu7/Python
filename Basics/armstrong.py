num = input("enter the number")
sum =0

for i in num:
    k = int(i)
    sum = sum+int(k**len(num))
if(sum == int(num)):
    print("Armstong")
else:
    print("Not armstrong")