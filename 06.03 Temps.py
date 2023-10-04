Ffile = open("06.03 FTemps.txt", "r") 
records = 0
def FahrtoCel():
    return (float(F)-32)*5/9
for F in Ffile:
    C = FahrtoCel()
    C = round(C,1) 
    f = open("06.03 CTemps.txt", "a") 
    f.write(str(C)) 
    f.write('\n') 
    f.close() 
    records += 1
print(str(records)+" records written")