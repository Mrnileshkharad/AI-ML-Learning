username = "nk123"
password =12345
balance=3500

def login(username,password):
    if username=="nk123" and password==12345:
        print("LogIn Successful !! Please Procced further")
    else:
        print("Opss Login Failed!! Please try again")


def deposit(balance,amount):
    print(f"Balance Availlable : {balance}")
    print(f"Amount deposited : {amount}")
    print(f"Balance Availlable : {balance + amount}")
    return balance+amount
 

def withdraw(balance,amount):
    if balance>=amount:
       print(f"Balance Availlable : {balance}")
       print(f"Amount to be withdrawn  : {amount}")
       print(f"Balance Availlable : {balance - amount}")
       return balance-amount
    else:
        print ("Insuffucient Balance")


def check_balance(balance):
    print(f"Balance Availlable : {balance}")


login("nk123",12345)
deposit(3500,1500)
withdraw(5000,2000)
check_balance(2000)

withdraw(5000,6000)


def calculate_total_amount(*amounts):
    sum = 0
    for amount in amounts:
        sum = sum + amount
    return sum

print(calculate_total_amount(100,200,300))