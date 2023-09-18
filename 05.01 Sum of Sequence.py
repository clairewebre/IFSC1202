n=int(input("Enter Number (CR to quit): "))
sum=0
while n != '':
    sum += n
    n=int(input("Enter Number (CR to quit): "))
print("Sum: " + str(sum))