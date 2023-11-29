from math import sqrt
from math import pi
from math import acos
class Triangle ():
    def __init__(self,sideone,sidetwo,sidethree):
        self.s1 = sideone
        self.s2 = sidetwo
        self.s3 = sidethree
    def type(self):
        if self.s1 == self.s2 and self.s2 == self.s3:
            return ("Equilateral")
        elif self.s1 == self.s2 or self.s2 == self.s3 or self.s3 == self.s1:
            return ("Isoceles")
        else:
            return ("Scalene")
    def perimeter(self):
        return self.s1 + self.s2 + self.s3
    
    def area(self):
        if self.type == "Equilateral":
            return ((sqrt(3)/4)*(self.s1 ** 2))
        elif self.type == "Isoceles":
            m = 0
            n = 0
            if self.s1 == self.s2:
                m = self.s1
                n = self.s3
            else:
                m = self.s1
                n = self.s2
            return (n*(sqrt((4*m*m)-(n**2))/4))
        else:
            s = self.perimeter() /2
            return ((s*(s - self.s1)*(s - self.s2)*(s - self.s3))/2)
    def angles(self):
        if self.type == "Equilateral":
            return [60,60,60]
        elif self.type == "Isoceles":
            n = 0
            if self.s1 == self.s2:
                n = self.s3
                m = sqrt((self.s1 ** 2)-((n/2)**2))
                a1 = (acos((n/2 * (n/2 + self.s1) * (self.s1 - m) * m) / (n * self.s1)) * 180) / pi
                a2 = a1
                a3 = 180 - a1 - a2
                return [a1,a2,a3]
            elif self.s2 == self.s3:
                n = self.s1
                m = sqrt((self.s2 ** 2)-((n/2)**2))
                a1 = (acos((n/2 * (n/2 + self.s2) * (self.s2 - m) * m) / (n * self.s2)) * 180) / pi
                a2 = a1
                a3 = 180 - a1 - a2
                return [a1,a2,a3]
            else:
                n = self.s2
                m = sqrt((self.s1 ** 2)-((n/2)**2))
                a1 = (acos((n/2 * (n/2 + self.s1) * (self.s1 - m) * m) / (n * self.s1)) * 180) / pi
                a2 = a1
                a3 = 180 - a1 - a2
                return [a1,a2,a3]
                return()
        else:
            n = self.s3
            m = 2*(self.area())/n
            angle1 = sqrt((self.s1)**2) - (n**2)
            angle2 = n-angle1   
            a1 = (acos((angle1 * (angle1 + self.s1) * (self.s1 - m) * m) / (2 * angle1 * self.s1)) * 180) / pi
            angle2 = (acos((angle2 * angle2 + self.s2 * self.s2 - m * m) / (2 * angle2 * self.s2))) * 180 / pi
            a3 = 180 - a1 - a2
            return [a2,a1,a3]
        
TrianglesList = []
t = open("Triangle Three Triangles.txt", "r")
x = t.readline()
while x != "":
    value = x.split(',')
    s1 = float(value[0])
    s2 = float(value[1])
    s3 = float(value[2])
    TrianglesList.append(Triangle(s1,s2,s3))
    x = t.readline()


print("{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}".format("Type","Side 1","Side 2","Side 3","Perimeter","Area","Angle 1","Angle 2","Angle 3")
for a in TrianglesList:
    print("{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}".format(a.type(),a.s1,a.s2,a.s3,a.perimeter(),round(a.area(),3),round(a.angles()[0],3),round(a.angles()[1],3),round(a.angles()[2],3))






