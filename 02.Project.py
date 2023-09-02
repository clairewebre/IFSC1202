from math import sqrt
x = float(input("Enter side 1: "))
y = float(input("Enter side 2: "))
z = float(input("Enter side 3: "))
p = float(x + y + z) / 2
a = sqrt(p * (p - x) * (p - y) * (p -z))
print("Area : " + str(a))