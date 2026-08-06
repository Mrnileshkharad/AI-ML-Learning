class TestCase:
    def __init__(self,testcase_id,testcase_name):
        self.testcase_id=testcase_id
        self.testcase_name =testcase_name
    def execute(self):
        print("Executing Generic Test Case...")

class LoginTest(TestCase):

    def __init__(self):
        super().__init__("TC001", "Login Test")

    def execute(self):
        print(f"Executing {self.testcase_name}")

class PaymentTest(TestCase):
    def __init__(self):
            super().__init__("TC002", "Payment  Test")
    
    def execute(self):
        print(f"Executing {self.testcase_name}")

class LogoutTest(TestCase):
    def __init__(self):
                super().__init__("TC003", "Logout Test")

    def execute(self):
        print(f"Executing {self.testcase_name}")

testcases  =[LoginTest(),PaymentTest(),LogoutTest()]

try:
    for testcase  in testcases :
        testcase .execute()
except  Exception as  e:
    print(e)
finally:
    print ("="*40)
    print("Execution Completed Successfully")
    print ("="*40)



