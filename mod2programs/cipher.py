word = input("Enter the string ")
dis = int(input("Enter the distance"))
lowered = word.lower()
encry =""
decry =''
for i in lowered:
    
    en = ord(i) +dis
    if(en>ord('z')):
        en = ord('a')+dis- ((ord('z')-ord(i)+1))
    encry=encry+chr(en)
print(encry)

for i in encry:
    de= ord(i)-dis
    if(de<ord('a')):
        de = ord('z') -dis+ ((ord(i)-ord('a')-1))
    decry = decry+chr(de)
print(decry)