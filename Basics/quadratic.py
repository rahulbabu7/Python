import cmath
import math
#ax**2+bx+c

a = int(input("Enter the value for a"))
b = int(input("Enter the value for b"))
c = int(input("Enter the value for c"))

d = b**2-4*a*c

if d==0:
    root = -b/2*a
    print(root)
elif d>0:
    root1 = (-b+cmath.sqrt(d))/2*a
    root2 = (-b-cmath.sqrt(d))/2*a
    print(root1,root2)
else:
    root1 = (-b+cmath.sqrt(d))/2*a
    root2 = (-b-cmath.sqrt(d))/2*a
    print(root1,root2)