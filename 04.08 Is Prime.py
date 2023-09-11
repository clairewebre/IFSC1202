N = int(input("Enter N: "))
if N>1:
    for i in range(2,N//2 +1):
        if N % i == 0:
            print("COMPOSITE")
            break
    else:
        print("PRIME")