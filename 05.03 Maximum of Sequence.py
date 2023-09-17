max = 0
num = True
while True:
    n = input("Enter Number (CR to quit): ")
    if not n:
        break
    else:
        if int(num) or int(max) < int(n):
            max = n
            num = False    
print("Maximum: " + str(max))
    