a = int(input("Enter Classroom A: "))
b = int(input("Enter Classroom B: "))
c = int(input("Enter Classroom C: "))
adesks = int(a // 2) + int(a % 2)
bdesks = int(b // 2) + int(b % 2)
cdesks = int(c // 2) + int(c % 2)
print(int(adesks) + int(bdesks) + int(cdesks))