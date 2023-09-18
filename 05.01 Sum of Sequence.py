n=input("Enter Number (CR to quit): ")
sum=0
while n != '':
    sum += int(n)
    n=input("Enter Number (CR to quit): ")
print("Sum: " + str(sum))