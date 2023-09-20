start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))
print("Special Numbers Between {} and {}".format(start, end))
for n in range (start, end+1):
    count = 0
    number = int(n)
    while n != 0:
        n = number//10
        count += 1
        n = number
sum = ((number//10000)**count) + ((number//1000)**count) + ((number//100)**count) + ((number//10)**count) + ((number%10)**count)
if sum == number:
    print(sum)      