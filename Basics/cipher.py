val = input("ENter the value")
dist =int(input("Enter the distance"))
encryp = ""
decryp = ""

#value to encryption
for i in val:
    en = chr(ord(i)+dist)
    encryp = encryp +en
print(encryp)


#encrypted to decrypted
for i in encryp:
    dec = chr(ord(i) - dist)
    decryp = decryp +dec
print(decryp)