s = int(input("Enter Start of Range: "))
e = int(input("Enter End of Range: "))
print("Super Special Numbers between {} and {}".format(s,e))
for n in range (s,e+1):
    sum = 0
    factoriala=1
    factorialb=1
    factorialc=1
    factoriald=1
    factoriale=1
    factorialf=1
    a = n % 10
    while a != 0:
        factorial *= a
        a -= 1
    b = (n // 10) % 10
    while b != 0:
        factorialb *= b
        b -= 1
    c = (n//100) % 10
    while c != 0:
        factorialc *= c
        c -= 1
    d = (n//1000) % 10
    while d != 0:
        factoriald *= d
        d -= 1
    e = (n//10000) % 10
    while e != 0:
        factoriale *= e
        e -= 1
    f = n//100000
    while f != 0:
        factorialf *= f
        f -= 1
    sum = factoriala + factorialb + factorialc + factoriald + factoriale + factorialf
    if sum == n:
        print(n)