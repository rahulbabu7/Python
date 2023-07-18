num = input("Enter the  number")
sum = 0
power = len(num)
for  i in num:
    k = int(i)
    sum = sum + int(k**power)
if sum ==int(num):
    print("armstrong")
else:
    print("Not")