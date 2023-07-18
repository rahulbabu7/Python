value = input("Enter the string: ")
small = value.lower()
# strs = input("Enter the sub")
vowels = ['a', 'e', 'i', 'o', 'u']

for i in small:
    for j in vowels:
        if i == j:
            small = small.replace(j, "")

print(small)