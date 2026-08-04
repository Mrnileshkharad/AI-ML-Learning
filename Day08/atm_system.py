class InvalidAmountException(Exception):
        pass

class InsufficientBalanceException(Exception):
        pass

class BankAccount:

    def __init__(self,account_holder,account_number,balance):
        self.account_holder= account_holder
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        if(not isinstance(amount, int)  or amount<0):
                raise InvalidAmountException("Invalid Amount")
        else :
            self.balance+=amount
            print(f"{amount} deposited to your account")
        return self.balance

    def withdraw(self,amount):
        if (not isinstance(amount, int)  or amount<0):
             raise InvalidAmountException("Invalid Amount")
        if amount<=self.balance:
            self.balance-=amount
            print(f"{amount} withdrawn from your account")

        else:
            raise InsufficientBalanceException("Insufficient Balance")

    def show_balance(self):
        print (f"Available balance in your account number  {self.account_number} is {self.balance}")
        
    
bank_account=BankAccount("Nilesh","123456",1000)

try :
     bank_account.deposit("df")
except InvalidAmountException as e :
    print (e)
finally:
    bank_account.show_balance()
    print("Thank You. Visit Again!!")
     

try:
    bank_account.withdraw(1000)
except InsufficientBalanceException as e :
    print(e)

except InvalidAmountException as e :
    print(e)

finally:
    bank_account.show_balance()
    print("Thank You. Visit Again!!")

    
bank_account.show_balance()




        

        