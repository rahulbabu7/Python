row = int(input("Enter the number of rows:"))

for i in range(1,row+1):
    asci = 65
    for j in range (1,i+1):
        k = chr(asci)
        print(k,end="")
        asci=asci+1
    print()
