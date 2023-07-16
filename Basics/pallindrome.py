name = input("Enter the word")
rev = ""

for i in name:
    rev =i+rev
if(rev ==name):
    print("pall")
else:
    print("Not")