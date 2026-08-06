class Employee:
    def __init__(self):
        pass 
    def work(self):
        print("Employee performs general office work.") 

class TestAutomationEngineer(Employee):
    def __init__(self):
        pass
    def work(self):
        print("Test Automation Engineer writes automation scripts using Selenium and Python.")

qa = TestAutomationEngineer()
qa.work()