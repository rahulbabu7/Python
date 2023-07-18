word = input("Enter the word")
new = word.lower()
sub = input("Enter the sub")
remsub = sub.lower()
limit = len(word)
for i in range (limit+1):
    new = new.replace(remsub,"")

print(new)
