start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))
print("Special Numbers Between {} and {}".format(start, end))
while 
    for n in range (1,9):
        sum = n
        print(sum)
    for n in range (10,99):
        sum = ((n//10)**2) + ((n%10)**2)
        if sum == n:
            print(sum)
    for n in range (100,999):
        sumtwo = ((n//100)**3)+((n//10)**3)+((n%10)**3)
        if sumtwo == n:
            print(sumtwo)
    for n in range (1000,9999):
        sumthree = ((n//1000)**4)+((n//100)**4)+((n//10)**4)+((n%10)**4)
        if sumthree == n:
            print (sumthree)
    for n in range (10000,99999):
        sumfour = ((n//10000)**5)+((n//1000)**5)+((n//100)**5)+((n//10)**5)+((n%10)**5)
        if sumfour == n:
            print (sumfour)
