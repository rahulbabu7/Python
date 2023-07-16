limit = int(input("Enter the limit"))
pos = []
neg =[]

for i in range(limit):
    num = int(input("ENter the num"))
    if num >=0:
        pos.append(num)
    else :
        neg.append(num)
print(pos)
print(neg)