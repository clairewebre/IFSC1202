class Student ():
    def __init__(self,firstname,lastname,tnumber):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades 
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
        for i in range (len(self.Grades)):
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

class StudentList ():
    def __init__(self):
        self.Studentlist = 
    add_student()