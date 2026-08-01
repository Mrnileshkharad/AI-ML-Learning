balance = 5000
choice = 3

def checkbalance ():
    print("Current Balance : ", balance)
    return balance

def deposit(balance ,amount):
    print("Previous Balance : ", balance)
    print("Deposited : ",amount)
    print("Current Balance : ",  balance + amount)
    return balance + amount
    

def withdrwa (balance,amount):
    if balance >=amount:
        print("Withdrawal Successful")
        print("Current Balance : ", balance - amount)
        return balance - amount
    else:
        print("Insufficient Balance")
    
def exit_atm ():
    print("Thank you !! Visit again")

    
    
if choice ==1 :
    checkbalance()
elif choice==2:
    deposit( balance,2500)
elif choice==3:
    withdrwa(balance ,3000)
else:
    exit_atm()