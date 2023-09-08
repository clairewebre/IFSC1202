count = 0
N = int(input("Enter N: "))
for i in range(N):
    value = int(input("Enter Number: "))
    if value==0:
        count += 1
print(count)