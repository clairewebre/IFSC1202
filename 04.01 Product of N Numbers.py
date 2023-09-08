result = 1
N = int(input("Enter N: "))
for i in range(1, N + 1):
    print("Enter Number: " + str(i))
for i in range(1, N + 1):
    result *= i
print(result) 