start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))
print("Special Numbers Between {} and {}".format(start, end))
for n in range (start, end+1):
    for n in range (1,9):
        print(n)
    for n in range (10,99):
        remainder = n % 10
        tens = n // 10
        sum = (remainder**2) + (tens**2)
        if sum == n:
            print(sum)
    for n in range (100,999):
        remainder = n % 10
        hundreds = n // 100
        tens = n - remainder - hundreds
        sum = (remainder**3) + (tens**3) + (hundreds**3)
        if sum == n:
            print(n)
    for n in range (1000, 9999):
        remainder = n % 10
        thousands = n // 1000
        hundreds = (n//100)%10
        tens =(n//10)%10
        sum = (remainder**4)+(thousands**4)+(hundreds**4)+(tens**4)
        if sum == n:
            print(n)
    for n in range (10000, 99999):
        remainder = n % 10
        tens = (n//10)%10
        hundreds = (n//100)%10
        thousands = (n//1000)%10
        tenthousands = n//10000
        sum = (remainder**5)+(tens**5)+(hundreds**5)+(thousands**5)+(tenthousands**5)
        if sum == n:
            print(n)

