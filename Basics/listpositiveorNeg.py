n = int(input("enter the limit:"))
total=[]
pos=[]
neg = []
for i in range(n):
    num = int(input("Enter the number:"))
    total.append(num)
    if num<0:
        neg.append(num)
    else:
        pos.append(num)
print("total",total)
print("neg",neg)
print("pos ",pos)