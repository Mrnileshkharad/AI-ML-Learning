class BasePage:
    def __init__(self):
        pass
    def click(self):
        pass
    def enter_text(self):
        pass
    def wait(self):
        print ("Processing .......Please wait" )
    

class LoginPage(BasePage):
    def login(self):
        username = input ("Please enter username :")
        self.enter_text()
        self.click()
        password= input ("Please enter your Password :")
        self.enter_text()
        self.click()
        self.wait()

qa = LoginPage()
qa.login()


        
    
