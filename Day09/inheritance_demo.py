
class person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(person):

    def __init__(self,name,age,employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
    def display(self):
        print(f"Name:{self.name}, Age:{self.age}, Employee_Id :{self.employee_id}")

emp = Employee("Nilesh",33,"Emp001")
emp.display()