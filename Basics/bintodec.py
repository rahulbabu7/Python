binary = input("enter")
dec = 0
pow = len(binary)-1
for i in binary:
    k = int(i)
    dec = dec+2**pow*k
    pow-=1
print(dec)