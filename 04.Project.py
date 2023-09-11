S = int(input("Enter Start of Range: "))
E = int(input("Enter End of Range: "))
print("Prime Numbers Between " + str(S) + " and " + str(E))
for N in range (S, E+1):
    for i in range (2, N//2 +1):
        if N%i == 0 :
            break
    else: print(N)