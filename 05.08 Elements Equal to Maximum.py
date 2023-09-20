n = input("Enter a Number (CR to quit): ")
count = 0
if n != "":
    max = int(n)
    while n != "":
        if int(n) > max:
            max = int(n)
        elif int(n) == max:
            count += 1
        n= input("Enter a Number (CR to quit): ")
    print("Maximum: {}".format(max))
    print("Number of Occurences: {}".format(count))