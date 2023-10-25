a = [] #creates matrice
inputfile = open("09.Project Distances.csv","r") #opens file for reading
row = inputfile.readline().strip() #reads file line by line without blanks spaces or tabs
while row != "": #while row continues
    r = row.split(",") #divides row into single character slices based on comma location
    for i in range (len(r)): #where length of r is the number of slices
        r[i] = str(r[i]) 
    a.append(r) #adds r to list a
    row = inputfile.readline().strip() #resets 'row' to the next row
for i in range (len(a)): #refers to the rows in list a
    for j in range(len(a[i])): #refers to the elements for each row in list a
        print('{:>10s}'.format(a[i][j]), end = " ") #prints two-dimensional matrice as right-aligned strings
    print()
fcity = input("Enter From City: ")
tcity = input("Enter To City: ")
fvalue = 0 #establishes a numerical value for the from city location
tvalue = 0 #establishes a numerical value for the to city location
for i in range(len(a)): 
    if a[i][0] == fcity: #if the string located in the first row and ith column = the input for from city
        fvalue = i #fvalue is now set to value of the index for the ith column
        break #exits loop
for i in range(len(a[0])): 
    if a[0][i] == tcity: #if the string located in the first column and ith row = the input for to city
        tvalue = i #tvalue is now set to value of the index for the ith row
        break #exits loop
for i in range(len(a)):
    if fvalue == 0: 
        print("Invalid From City")
        break
for i in range(len(a[0])):
    if tvalue == 0:
        print("Invalid To City")
        break
print(fcity,"to",tcity,"-",a[fvalue][tvalue],"miles")