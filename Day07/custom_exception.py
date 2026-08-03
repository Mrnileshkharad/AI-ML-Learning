balance = 10000

withdraw_amount = input("Please enter amount: ")

class InsufficientBalanceException(Exception):
    pass


def atmwithdrawal(balance, withdraw_amount):
    if balance >= withdraw_amount:
        print("Withdrawal Successful")
        print("Current Balance:", balance - withdraw_amount)
        return balance - withdraw_amount
    else:
        raise InsufficientBalanceException("Insufficient Balance")


try:
    amount = int(withdraw_amount)
    atmwithdrawal(balance, amount)

except InsufficientBalanceException as e:
    print(e)

else:
    print("Transaction Successful")

finally:
    print("Visit Again!!")