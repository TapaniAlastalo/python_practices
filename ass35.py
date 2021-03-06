class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.courseList = []

    def add_course(self, course):
        self.courseList.append(course)

    def list_courses(self):
        return self.courseList

def read_student_data(fileName):
    students = []
    try:
        file = open(fileName, "r")
        lines = file.readlines()    # all lines as list
        file.close()
        
        # Parse And Build students
        for line in lines:
            student = buildStudent(str.strip(line))
            if student == None:
                continue
            else:
                students.append(student)        
    except:
        print("Something went wrong")
    return students

def buildStudent(line):
    separator = ";"
    words = line.split(separator)
    if len(words) > 2:
        student = Student(words[0], words[1], words[2])
        if len(words) == 4:
            separator = ","
            courses = words[3].split(separator)
            if len(courses) > 0:
                for course in courses:
                    student.add_course(course)
        return student
    return None

fileName = "student_data.txt"
students = read_student_data(fileName)
for student in students:
    print(student.name + " " + student.student_id)    