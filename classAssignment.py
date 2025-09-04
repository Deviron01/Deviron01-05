class Student:
    def __init__(self, name, course, age, department):
        self.name = name
        self.course = course
        self.age = age
        self.department = department

#constructor to show unique values
Student1 = Student("Viron", "Computer Science", 20, "Computing and Informatics")
print(Student1.name, " is a ", Student1.course, " student aged ", Student1.age, " in the department of ", Student1.department)

Student2 = Student("James", "Mathematics", 22, "Education")
print(Student2.name)
print(Student2.course)
print(Student2.age)
print(Student2.department)


#inheritance
class UndergraduateStudent(Student):
    def __init__(self, GraduationYear, RegNo):
        self.GraduationYear = GraduationYear
        self.RegNo = RegNo
 

class PostGrad(Student):
    def __init__(self, GraduationCode):
        self.GraduationCode = GraduationCode

Student2 = PostGrad(45265)
print(Student2.GraduationCode)

      
        






