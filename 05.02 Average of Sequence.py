sum = 0
digits = 0
while True:
    n = input("Enter Number (CR to quit): ")
    if not n:
        break
    else:
        sum += int(n)
        digits += 1
if digits == 0:
    print("Sequence length is 0")
else:
    print("Average: " + str(sum/digits))