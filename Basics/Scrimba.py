msg = "welcome to Python"

print(msg.title());
print(msg.lower());
print(len(msg));
print(msg.count('w'));
print(msg[2:])   #prints the one from index 2 to end of the string
print(msg[2:4]);  #prints from index to index 4  but does not include index 4
print(msg[:2])  #prints from starting to index 2 but end index not included
print(msg[:5:2])  #prints character 2 steps 


#exercise 

msg = 'welcome to Python 101: Strings';

print(msg[::-1])  #prints backwards
msg1=msg[18]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[13]+msg[12]+msg[2]+msg[1]+msg[-5]

print(msg1.title());
print(msg1[::-1])


msg2="""Dear Terry,,
You must cut down the mightiest 
tree in the forest with…
a herring! <3"""
print(msg2)
