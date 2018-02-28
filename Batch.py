class Batch:
    id = ""
    courseName = ""
    facultyName=""
    noOfStudents=0
    students=[]

    def getId(self):
        return self.id

    def setId(self,id):
        self.id=id

    def getFacultyName(self):
        return self.facultyName

    def setFacultyName(self,facultyName):
        self.facultyName=facultyName

    def getCourseName(self):
        return self.courseName

    def setCourseName(self,courseName):
        self.courseName=courseName

    def setStudents(self,students):
        self.students.append(students)

    def getStudents(self):
        return self.students

    def getNoOfStudents(self):
        return int(self.noOfStudents)

    def setNoOfStudents(self,nos):
        self.noOfStudents=nos

    def __repr__(self):
        print("Id: ",self.id,"Course Name: ",self.courseName,"Faculty name: ",self.facultyName,"No of students: ",self.noOfStudents)
        return ""