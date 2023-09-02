x = int(input("Enter first number: "))
o = str(input("Enter operator (+,-,*,/): "))
y = int(input("Enter second number: "))
if o == "+":
    print(str(x) + " + " + str(y) + " = " + (str(x + y)))
elif o == "-":
    print(str(x) + " - " + str(y) + " = " + (str(x - y)))
elif o == "*":
    print(str(x) + " * " + str(y) + " = " + (str(x * y)))
elif o == "/":
    print("str(x) + " / " + str(y) + " = " + (str(x / 2)))
else: 
    print("Invalid Operator")