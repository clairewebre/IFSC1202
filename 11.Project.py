class Student (): #defines the class
    def __init__(self,firstname,lastname,tnumber): #defines initializer
        self.Firstname = firstname
        self.Lastname = lastname
        self.Tnumber = tnumber
        self.Grades = [] #creates an attribute with an open list
    def RunningAverage(self): #
        total = 0
        count = 0
        for i in range(len(self.Grades)):
            if self.Grades[i].strip() != "":
                total += float(self.Grades[i].strip())
                count += 1
        if count > 0:
            return total/count
        else:
            return 0
    def TotalAverage(self):
        total = 0
        for i in range(len(self.Grades)):
            if self.Grades[i].strip() != "":
                total += float(self.Grades[i].strip())
        return total/len(self.Grades)
    def LetterGrade(self):
        average = self.TotalAverage()
        if average >= 90:
            return "A"
        elif average >= 80 and average < 90:
            return "B"
        elif average >= 70 and average < 80:
            return "C"
        elif average >= 60 and average < 70:
            return "D"
        else:
            return "F"
        
class StudentList ():
    def __init__(self):
        self.studentlist = []
    def add_student(self,FirstName,LastName,TNumber):
        student = Student(FirstName,LastName,TNumber)
        self.studentlist.append(student)
    def find_student(self, TNumber):
        for i in range(len(self.studentlist)):
            if self.studentlist[i].Tnumber == TNumber:
                return i
        return -1
    def print_student_list(self):
        print("{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}".format("First","Last","ID","Running","Semester","Letter"))
        print("{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}".format("Name","Name","Number","Average","Average","Grade"))
        print("{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}".format("-"*12, "-"*12, "-"*12, "-"*12, "-"*12, "-"*12,))
        for i in range(len(self.studentlist)):
            print("{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}".format(self.studentlist[i].Firstname(),self.studentlist[i].Lastname(),self.studentlist[i].Tnumber(),self.studentlist[i].RunningAverage(),self.studentlist[i].TotalAverage(), self.studentlist[i].LetterGrade()))
        print()
    def add_student_from_file(self,filename):
        studentfile = open(filename,"r")
        x = studentfile.readline()
        while x != "":
            y = x.split(",")
            if len(y) == 3:
                self.add_student(y[0],y[1],y[2].strip())
                x = studentfile.readline()
        studentfile.close()
    def add_scores_from_file(self,filename):
        scoresfile = open(filename,"r")
        x = scoresfile.readline()
        while x!= "":
            y = x.split(",")
            if len(y) == 2:
                TNumber, score = y[0],y[1].strip()
                index = self.find_student(TNumber)
                if index != -1:
                    self.studentlist[index].Grades.append(score)
                    x = scoresfile.readline()
            x = scoresfile.readline()
        scoresfile.close()

mystudentlist = StudentList()
mystudentlist.add_student_from_file("11.ProjectStudents.txt")
mystudentlist.add_scores_from_file("11.ProjectScores.txt")
mystudentlist.print_student_list()
print()