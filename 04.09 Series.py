A = int(input("Enter A: "))
B = int(input("Enter B: "))
if A<B:
    for i in range (A,B+1):
        print(i, sep='\n')
elif A>=B:
    for i in range (A, B-1, -1):
        print(i, sep='\n')