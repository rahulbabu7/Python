# value = input("Enter the str")
# small = value.lower()
# new = ""
# vowels = 'a','e','i','o','u'

# for i in small:
        
#         if i not in vowels:
#                 new = new+i
         

    
# print(new)

value = input("Enter the string: ")
small = value.lower()
# strs = input("Enter the sub")
vowels = ['a', 'e', 'i', 'o', 'u']

for i in small:
    for j in vowels:
        if i == j:
            small = small.replace(j, "")

print(small)

# new = small.replace(strs,"")
# print(new)