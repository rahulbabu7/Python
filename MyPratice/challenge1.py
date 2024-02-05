num1 = input("ENter the first number ");
num2 = input("ENter the second number");

tempNum1 = int(num1);
tempNum2 = int(num2);

product = tempNum1 * tempNum2;
sum = tempNum1 + tempNum2;

if(product <= 1000):
    print(f"Product = {product}");
else:
    print(f"Sum = {sum}");