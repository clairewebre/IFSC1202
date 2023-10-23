anglefile = open("07.Project Angles Input.txt","r")
decimalfile = open("07.Project Angles Output.txt","w")
angle = anglefile.readline()
count = 0
a = angle.find(chr(176))
b = angle.find("'")
c = angle.find('"')
def ParseDegreeString():
    a = angle.find(chr(176))
    b = angle.find("'")
    c = angle.find('"')
    DD = float(angle[:a])
    MM = float(angle[a+1:b])
    SS = float(angle[b+1:c])
    return str(DD)+chr(176)+str(MM)+"'"+str(SS)+'"'
def DDMMSStoDecimal(d,m,s):
   decimal = d + (m/60) + (s/3600)
   return decimal
while angle != "":
   value = ParseDegreeString()
   x = value.find(chr(176))
   y = value.find("'")
   z = value.find('"')
   d = float(value[:x])
   m = float(value[x+1:y])
   s = float(value[y+1:z])
   newvalue = str(DDMMSStoDecimal(d,m,s))
   decimalfile.write(newvalue+"\n")
   count += 1
   angle = anglefile.readline()
print(str(count) + " records processed")
anglefile.close()
decimalfile.close()