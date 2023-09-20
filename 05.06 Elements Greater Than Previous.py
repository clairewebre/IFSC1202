value = input("Enter Number (CR to quit): ")
if value != "":
    previousvalue = int(value)
    previouscount = 0
    while value != "":
        if previousvalue < int(value):
            previouscount += 1
        previousvalue = int(value)
        value = input("Enter Number (CR to quit): ")
    print("Number of Values Greater Than the Previous: {}".format(previouscount))
else:
    print("Sequence length is 0")