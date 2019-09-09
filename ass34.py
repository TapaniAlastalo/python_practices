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

joe = Student("Joe", 25, "f1234")
josie = Student("Josie", 21, "f5678")
print(joe.list_courses())
joe.add_course("script programming")
print(joe.list_courses())
josie.add_course("network programming")
josie.add_course("mathematics 2")
print(josie.list_courses())
