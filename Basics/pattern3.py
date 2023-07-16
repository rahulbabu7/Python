limit = int(input("Enter the limit:"))
for i in range(0,limit+1):
    ascivalue = 65
    for j in range(1,i+1):
        k = chr(ascivalue)
        print(k,end="")
        ascivalue+=1
    print()