a = []
numbersfile = open("09.Project Distances.csv")
x = numbersfile.readline().strip()
while x != "":
    y = x.split(",")
    for i in range(len(y)):
        y[i] = int(y[i])
    a.append(y)
    x = numbersfile.readline().strip()
for i in range (len(a)):
    for j in range (len(a[i])):
        print("{>10s}".format(a[i][j]), end = " ")
    print()