N = int(input("Enter number of cards: "))
sum=0
total=0
for i in range (1,N):
    i = int(input("Enter card: "))
    sum += i
for l in range(1,N+1):
    total +=l
lostcard = total - sum
print("Missing Card: " + str(lostcard))