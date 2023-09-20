currentvalue = input("Enter a Number (CR to quit): ")
if currentvalue != "":
    previousvalue = int(currentvalue)
    currentrepeatingcount = 1
    maximumrepeatingcount = 1
    maximumrepeatingvalue = int(currentvalue)

    currentvalue = input("Enter a Number (CR to quit): ")
    while currentvalue != "":
        if previousvalue == int(currentvalue):
            currentrepeatingcount += 1
        else: 
            if currentrepeatingcount > maximumrepeatingcount:
                maximumrepeatingcount = currentrepeatingcount
                maximumrepeatingvalue = previousvalue

            previousvalue = int(currentvalue)
            currentrepeatingcount = 1
        currentvalue = input("Enter a Number (CR to quit): ")
    if currentrepeatingcount > maximumrepeatingcount:
        maximumrepeatingcount = currentrepeatingcount
        maximumrepeatingvalue = previousvalue
    print("{} repeated {} times".format(maximumrepeatingvalue, maximumrepeatingcount))
