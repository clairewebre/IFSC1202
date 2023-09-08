N = int(input("Enter N: "))
factorial = 1
sum = 0
for i in range (1 , N+1):
    factorial *= i
    sum += factorial
print("Sum of Factorials: " + str(sum))