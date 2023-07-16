# t1 = ('1','1','2','4')
# t2=()
# for i in t1:
#     if i not in t2:
#         t2+=(i,)
# print(t2)

t1 = (1,1,3,2)
l2 =[]
for i in t1:
    
    if i not in l2:
       
        l2.append(i)
t2 = tuple(l2)
print(t2)
min = min(l2)
print(min)
print(max(l2))
print(t2.count(2))
