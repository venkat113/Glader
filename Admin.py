from StudentScheduler import StudentScheduler
from Student import Student
from Course import Course
from Batch import Batch
from Faculty import Faculty
studentScheduler=StudentScheduler()
while(1):
    choice=input("Enter your choice\n1. Add Student\n2. Show student list\n3. Add Course\n4. Add Batch\n5. Add Faculty\n6. Reports\n7. Exit\n")
    if(choice=="1"):
        n=int(input("How many students you want to add?\n"))
        for count in range(n):
            student=Student()
            flag=0
            student.setName(input("Enter student name\n"))
            student.setRollNumber(input("Enter student roll number\n"))
            studentT = studentScheduler.getStudent(student.getRollNumber())
            if (studentT!= None):
                print("Roll number already exists")
                continue
            courses = int(input("How many courses you want to apply for?\n"))
            for count1 in range(courses):
                course=Course()
                course.setCourseName(input("Enter course name\n"))
                courseT = studentScheduler.getCourse(course.getCourseName())
                if (courseT == None):
                    print("Course name not found")
                    flag=1
                student.addCourse(course)
                course=None
            if(flag==0):
                studentScheduler.addStudent(student)
            student=None
    elif(choice=="2"):
        studentList=studentScheduler.showAllStudents()
        print("Student details-\n")
        print(studentList)
    elif (choice == "3"):
        course=Course()
        course.setCourseName(input("Enter course name\n"))
        studentScheduler.addCourse(course)
    elif (choice == "4"):
        batch=Batch()
        batch.setId(input("Enter Batch id\n"))
        batch.setCourseName(input("Enter course name\n"))
        course = studentScheduler.getCourse(batch.getCourseName())
        if (course == None):
            print("Course name not found")
            break
        batch.setFacultyName(input("Enter Faculty name\n"))
        faculty = studentScheduler.getFaculty(batch.getFacultyName())
        if (faculty == None):
            print("Faculty name not found")
            continue
        batch.setNoOfStudents(input("Enter no of students\n"))
        for count in range(batch.getNoOfStudents()):
            student=studentScheduler.getStudent(input("Enter roll number\n"))
            if(student==None):
                print("Invalid Roll number")
                count-=1
            batch.setStudents(student)
        studentScheduler.addBatch(batch)
    elif (choice == "5"):
        faculty=Faculty()
        faculty.setId(input("Enter Faculty id\n"))
        faculty.setName(input("Enter Faculty name\n"))
        faculty.setCourseNames(input("Enter Course name\n"))
        studentScheduler.addFaculty(faculty)
    elif (choice == "6"):
        while(1):
            choice2=input("Enter your choice\n1. Student details by roll number\n2. Batch details by batch id\n3. Batch details by roll number\n4. Exit\n")
            if(choice2=="1"):
                rollNum = input("Enter roll number\n")
                student = studentScheduler.getStudent(rollNum)
                if (student == None):
                    print("No student found")
                else:
                    print(student)
            elif(choice2=="2"):
                batchId = input("Enter Batch id\n")
                batch = studentScheduler.getBatch(batchId)
                if (batch == None):
                    print("No Batch found")
                else:
                    print(batch)
            elif (choice2 == "3"):
                rollNum = input("Enter roll number\n")
                batch = studentScheduler.getBatchByRoll(rollNum)
                if (batch == None):
                    print("No Batch found")
                else:
                    print(batch)
            elif (choice == "4"):
                break;
    elif(choice=="7"):
        break;


