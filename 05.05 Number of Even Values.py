even = 0
while True:
    n = input("Enter number (CR to quit): ")
    if not n:
        break
    else:
        if int(n) % 2 == 0:
            even += 1
print("Number of Even Values: " + str(even))