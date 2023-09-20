n=input("Enter Number (CR to quit): ")
if n != '':
    max = int(n)
    maxindex=1
    currentindex=1
    while n!= '':
        if int(n) > max:
            max = int(n)
            maxindex=currentindex
        n=input("Enter Number (CR to quit): ")
        currentindex += 1
    print("Maximum: {}".format(max))
    print("Index of Maximum: {}".format(maxindex))
else:
    print ("Sequence length is 0")