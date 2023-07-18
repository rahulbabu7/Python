word = input("Enter the word")
ns = ""
vowel ='a','e','i','o','u'
new = word.lower()
for i in new:
    if i not in vowel:
        ns = ns+i
print(ns)
