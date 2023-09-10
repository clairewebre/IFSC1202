N = int(input("Enter N: "))
if N <= 9:
    for i in range(1,N+1):
        print(end='\n')
        for k in range(1,i+1):
            print(k, end="") 
    print()