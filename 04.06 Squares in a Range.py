# prod = 1
A = int(input("Enter A: "))
B = int(input("Enter B: "))
for i in range(A , B+1):
   prod = i**2
   print(str(i) + "*" + str(i) + "=" + str(prod))
   # print()