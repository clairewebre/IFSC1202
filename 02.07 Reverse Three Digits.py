n = int(input("Enter a 3 Digit Number: "))
a =  str(n // 100)
b = str((n % 100) // 10)
c = str((n % 100) % 10)
print("Reverse of Digits: " + c + b + a)