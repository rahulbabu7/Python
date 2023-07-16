decimal = int(input("Enter the number"))

if(decimal ==0):
    print(0)
else:
    binary= ""
    while decimal >0:
        rem = decimal %2
        decimal = decimal//2
        binary = str(rem)+binary
        # print(binary)
print(binary)