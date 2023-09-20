start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))
print("Special Numbers between {} and {}".format(start,end))
for n in range (start, end+1):
    length = 0
    num = n
    while num > 0:
        num //= 10
        length += 1
    sum = 0
    num = n
    while num > 0:
        digits = num % 10
        sum += (digits**length)
        num //= 10
    if sum == n:
        print(sum)