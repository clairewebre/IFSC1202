class Student ():
    def __init__(self, firstname, lastname, tnumber, scores):
        self.firstname = firstname
        self.lastname = lastname
        self.tnumber = tnumber
        self.grades = scores
    def RunningAverage(self):
        total = 0
        count = 0
        for i in range(len(self.Grades)):
            if self.Grades[i].strip() != "":
                total += float(self.Grades[i].strip())
                count += 1
        return total/count
    def TotalAverage(self):
        total = 0
        for i in range(len(self.Grades)):
            if self.Grades[i].strip() != "":
                total += float(self.Grades[i].strip())
            return total/len(self.Grades)
    def LetterGrade(self):
        average = self.totalaverage()
        if average >= 90:
            return("A")
        elif average < 90 and average >= 80:
            return("B")
        elif average < 80 and average >= 70:
            return("C")
        elif average < 70 and average >= 60:
            return("D")
        else:
            return("F")
        
input = open("10.Project Student Scores.txt","r")
print("{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}".format("First","Last","ID","Running","Semester","Letter"))
print("{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}{:>12s}".format("Name","Name","Number","Average","Average","Grade"))
print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format("-"*12, "-"*12, "-"*12, "-"*12, "-"*12, "-"*12))
x = input.readline()
      
while x != "":
    y = x.split(",")
    student = Student (y[0].strip(),y[1].strip(),y[2].strip(),y[:3])
    print("{:>12s} {:>12s} {:>12s} {:>12s} {:>12s} {:>12s}".format(Student.firstname, Student.lastname, Student.tnumber, Student.RunningAverage, Student.TotalAverage, Student.LetterGrade))
    x = input.readline()
