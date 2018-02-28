class Faculty:
    id=""
    name=""
    courseNames=[]

    def getId(self):
        return self.id

    def setId(self,id):
        self.id=id

    def getName(self):
        return self.name

    def setName(self,name):
        self.name=name

    def getCourseNames(self):
        return self.courseNames

    def setCourseNames(self,course):
        self.courseNames.append(course)

    def __repr__(self):
        print("Id: ",self.id,"Faculty Name: ",self.name,"Course names: ",self.courseNames)
        return ""