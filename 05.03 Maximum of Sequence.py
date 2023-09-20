n=input("Enter Number (CR to quit): ")
if n != '':
    max = int(n)
    while n !='':
        if int(n) > max:
            max = int(n)
        n = input("Enter Number (CR to quit): ")
    print ("Maximum: {}".format(max))
else:
    print("Sequence length is 0")
    