class Student:
    rollNumber=""
    name=""
    courses=[]

    def __init__(self):
        self.rollNumber=""
        self.name=""
        self.courses=[]

    def getRollNumber(self):
        return self.rollNumber

    def setRollNumber(self,rollNumber):
        self.rollNumber=rollNumber

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def addCourse(self,course):
        self.courses.append(course)

    def getCourses(self):
        return self.courses

    def __repr__(self):
        print("Name: ",self.name,"Roll number: ",self.rollNumber,"Courses: ",self.courses)
        return ""