class Student ():  #defines class
	def __init__(self, firstname, lastname, tnumber):  #defines initializer
		self.FirstName = firstname #defines object attributes
		self.LastName = lastname
		self.TNumber = tnumber
		self.Grades = [] #creates attribute with a list for grades
	def RunningAverage(self): #average without zero scores
		total = 0
		count = 0 #number of scores present
		for i in range(len(self.Grades)):
			if self.Grades[i].strip() != "":
				total = total + float(self.Grades[i].strip())
				count = count + 1
		if count > 0:
			return total / count
		else: 
			return 0 #in the case the student has no scores
	def TotalAverage(self): #average with zero scores included
		total = 0
		for i in range(len(self.Grades)):
			if self.Grades[i].strip() != "":
				total = total + float(self.Grades[i].strip())
		return total / len(self.Grades)
	def LetterGrade(self): #defines numerical range for letter grades
		average = self.TotalAverage() #applies total average to determine letter grade
		if average >= 90:
			return "A"
		if average >= 80: #code only moves forward if average did not meet requirements of the first if statement
			return "B"
		if average >= 70:
			return "C"
		if average >= 60:
			return "D"
		
		return "F"


class StudentList (): #new class defined
    def __init__(self): #defines initializer with no parameters
        self.studentlist = [] #creates an attribute with an open list
    def add_student(self, Firstname, Lastname, Tnumber):
        student = Student(Firstname, Lastname, Tnumber) #references first defined class
        self.studentlist.append(student) #adds info from first class to the attribute's list within the new class
    def find_student(self, Tnumber):
        for i in range(len(self.studentlist)): #determines location of of student's column
              if self.studentlist[i].TNumber == Tnumber:
                   return i
        return -1
    def print_student_list(self):
        print("{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}".format("First", "Last", "ID", "Running", "Semester", "Letter"))
        print("{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}".format("Name", "Name", "Number", "Average", "Average", "Grade"))
        print("{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}{:>14s}".format("-"*12, "-"*12, "-"*12, "-"*12, "-"*12, "-"*12))

        for i in range(len(self.studentlist)):
            print ("{:>14s}{:>14s}{:>14s}{:14.2f}{:14.2f}{:>14s}".format(self.studentlist[i].FirstName, self.studentlist[i].LastName, self.studentlist[i].TNumber,self.studentlist[i].RunningAverage(),self.studentlist[i].TotalAverage(),self.studentlist[i].LetterGrade()))
        print()
       
    def add_student_from_file(self,inputfile): 
        studentfile = open(inputfile, "r")
        x = studentfile.readline()
        while x != "":
            y = x.split(",")
            if len(y) == 3:
                self.add_student(y[0], y[1], y[2].strip()) #adds student names and tnumbers to studentlist class
                x = studentfile.readline()
        studentfile.close()
    
    def add_scores_from_file(self,inputfile):
        scorefile = open(inputfile, "r")
        x = scorefile.readline()
        while x != "":
            y = x.split(",")
            if len(y) == 2:
                Tnumber, score = y[0], y[1].strip()
                index = self.find_student(Tnumber) #allows us to find student score using tnumber
                if index != -1:
                    self.studentlist[index].Grades.append(score)
                x = scorefile.readline()
        scorefile.close()
        
studentinfolist = StudentList()
studentinfolist.add_student_from_file("11.Project Students.txt") #adds student names and tnumbers to student list
studentinfolist.add_scores_from_file("11.Project Scores.txt") #adds respective grades to student list
studentinfolist.print_student_list()
print()