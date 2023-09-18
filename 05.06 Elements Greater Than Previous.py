n = True
prev = 0
i = 0
sum = 0
while True:
    n = input("Enter Number (CR to quit): ")
    if not n:
        break
    else:
        if i == 0:
            prev = n
        if int(n) > int(prev):
            sum += 1
        i += 1
print(sum)