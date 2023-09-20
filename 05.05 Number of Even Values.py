n=input('Enter Number (CR to quit): ')
even=0
while n != '':
    if int(n) % 2 == 0:
        even += 1
    n=input('Enter Number (CR to quit): ')
print("Number of Even Values: {}".format(even))