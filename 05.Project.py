s=int(input("Enter start of range: "))
e=int(input("Enter end of range: "))
count=0
sum=0
for n in range(s,e+1):
    while n % 10 != 0:
        count += 1
    print("Special Numbers Between",str(s),"and",str(e))
