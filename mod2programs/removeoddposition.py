word = input("Enter the word")
ns=""
new = word.lower()
lenth = len(new)

for i in range(lenth):
    if i%2==0:
       pass
    else:
         ns = ns +new[i]
print(ns)
