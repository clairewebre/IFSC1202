n = int(input("Enter a 3 Digit Number: "))
a = n // 100
b = (n % 100) // 10
c = (n % 100) % 10
print("Sum of Digits: " + "{}".format(int(a + b + c)))
