firstmax=int(input("Enter the First Number: "))
secondmax=int(input("Enter the Second Number: "))
if firstmax < secondmax:
    firstmax, secondmax = secondmax, firstmax
value = input("Enter a Number (CR to quit): ")
while value != '':
    if int(value) > firstmax:
        firstmax, secondmax = int(value), firstmax
    elif int(value) > secondmax:
        secondmax=int(value)
    value=input("Enter a Number (CR to quit): ")
print("First Maximum: {}".format(firstmax))
print("Second Maximum: {}".format(secondmax))