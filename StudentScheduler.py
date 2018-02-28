class StudentScheduler:
    students=[]
    courses=[]
    faculties=[]
    batches=[]
    def addStudent(self,student):
        self.students.append(student)

    def showAllStudents(self):
        return self.students

    def getStudent(self,rollNum):
        for stud in self.students:
            if(rollNum==stud.getRollNumber()):
                return stud
        return None

    def addCourse(self,course):
        self.courses.append(course)

    def addFaculty(self,faculty):
        self.faculties.append(faculty)

    def addBatch(self,batch):
        self.batches.append(batch)

    def getBatch(self,batchId):
        for batch in self.batches:
            if(batchId==batch.getId()):
                return batch
        return None

    def getFaculty(self,facultyName):
        for faculty in self.faculties:
            if(facultyName==faculty.getName()):
                return faculty
        return None

    def getCourse(self,courseName):
        for course in self.courses:
            if(courseName==course.getCourseName()):
                return course
        return None

    def getBatchByRoll(self,rollNum):
        for batch in self.batches:
            for student in batch.getStudents():
                if (rollNum == student.getRollNumber()):
                    return batch
        return None