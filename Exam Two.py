properties = []
inputfile = open("Exam Two Properties.csv")
p = inputfile.readline().strip()
count = 0
sum = 0
zipcodes = []
while p != "":
    q = p.split(",")
    q[4] = float(q[4])
    properties.append(q)
    p = inputfile.readline().strip()
    for i in range(len(properties)):
        for j in range(len(zipcodes[i])):
            if properties[i][3] == zipcodes[j][0]:
                count += 1
                sum += properties[4][j]
                zipcodes.append([properties[i][3],count,sum])
            else:
                zipcodes.append([properties[i][3],1, properties[i][4]])
print("{:^}{:^}{:^}".format("Zipcode","Count","Average"))
for i in range (len(zipcodes)):
    for j in range(len(zipcodes[i])):
        print("{:^}{:^}{:^.2}").format(zip,count,(float(sum)/float(count)))
