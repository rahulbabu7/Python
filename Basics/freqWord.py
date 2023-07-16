inputString=input("Enter the string:")
li=inputString.split() #converts the string into the list of words
freq = {} #dictionary to store word and its count
for i in li:
    if (i in freq):
        freq[i] += 1 #item already in the dictionary ,     								increment the count
    else:
        freq[i] = 1
print(freq)
print(max(freq.values()))