class BankAccount:

    def __init__(self):
        self.account_holder = "Nilesh"
        self.account_number = "1234567890"
        self.balance = 50000


account = BankAccount()

print("Account Holder :", account.account_holder)
print("Account Number :", account.account_number)
print("Balance :", account.balance)


class Employee:
    def __init__(self,name,employee_id,salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee Name : {self.name}, Employee Id : {self.employee_id}, Salary : {self.salary}")

emp1= Employee("Nilesh","EMP101",1200000)
emp2= Employee("Rahul","EMP102",950000)

emp1.display_details()
emp2.display_details()



##TestCase
class TestCase:
    def __init__(self,testcase_id,testcase_name,status):
        self.tcid= testcase_id
        self.tcname= testcase_name
        self.status = status

    def execute(self):
        print (f"Executing {self.tcname}...")

    def display_result(self):
        print(f"Test Case ID   : {self.tcid}")
        print(f"Test Case Name : {self.tcname}")
        print(f"Status         : {self.status}")
        print("-" *40)

testcases = [
    TestCase("TC001", "Login Test", "PASS"),
    TestCase("TC002", "Payment Test", "FAIL")
]

for testcase in testcases:
    testcase.execute()
    testcase.display_result()
