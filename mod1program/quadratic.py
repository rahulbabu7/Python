import cmath

a = int(input("Enter the coefficient for X^2"))
b = int(input("Enter the coefficient for X"))
c = int(input("Enter the coefficient for constant"))

d= (b**2 - 4*a*c)/2*a

if d ==0:
    root = (-b)/2*a
    print(f"root = {root}")
elif d>0:
    root1 = (-b+cmath.sqrt(d))/2*a
    root2 = (-b-cmath.sqrt(d))/2*a
    print(f"Roots are : {root1}{root2}")
else:
    root1 = (-b+cmath.sqrt(d))/2*a
    root2 = (-b-cmath.sqrt(d))/2*a
    print(f"Roots are : {root1}{root2}")
    