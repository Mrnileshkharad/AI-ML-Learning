class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def introduce(self):
        return( "I want to become AI/ML Engineer")

class Student(Person):
    def __init__(self, name, age,student_id,course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course
    def display_student(self):
        print(f"Hello my name is {self.name}, I am {self.age} yeas old. My student id number is {self.student_id}. I am Learning {self.course}. My aim is : {self.introduce()} ")

student = Student("Nilesh","34",123,"Python")
student.display_student()
        


    