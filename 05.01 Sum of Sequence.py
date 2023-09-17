sum = 0
while True:
    n = input("Enter Number (CR to quit): ")
    if not n:
        break
    else:
        sum += int(n)
print(sum)