class Account:
    def __init__(self,account_holder,balance):
        self.name= account_holder
        self.balance = balance

    def deposit(self,amount):
         self.balance += amount
         print(f"Hello {self.name} amount  {amount} is deposited in your account successfully.")
         return self.balance

    def show_balance(self):
        print(f"Availlable balance : {self.balance}")

class SavingsAccount(Account):
    def __init__(self, account_holder, balance,interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate= interest_rate
        

    def calculate_interest(self):
        interst = self.balance * self.interest_rate/100
        print(f"Annual interst on {self.balance} with the interest rate {self.interest_rate}  % is : {interst}")
        return interst

bnk = SavingsAccount("Niilesh",10000,8)
bnk.deposit(5000)
bnk.show_balance()
bnk.calculate_interest()
        

    
        
