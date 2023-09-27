from math import pi
def diameter(r):
    return 2*r
def circumference(r):
    return 2*pi*r
def area(r):
    return pi*(r**2)
print("{:>15s}{:>15s}{:>15s}{:>15s}".format("Radius","Diameter","Circumference","Area"))
radiusfile = "06.01 Radius.txt"
radius = open(radiusfile, "r")
r = radius.readline()
while r !="":
    fr = float(r)
    print("{:>15.5f}{:>15.5f}{:>15.5f}{:>15.5f}".format(fr,diameter(fr),circumference(fr),area(fr)))
    r = radius.readline()
radius.close()