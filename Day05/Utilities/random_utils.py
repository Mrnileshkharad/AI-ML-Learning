import random


def generate_otp():
    return random.randint(1000, 9999)


def generate_transaction_id():
    return "TXN" + str(random.randint(100000, 999999))


def generate_random_amount():
    return random.randint(100, 10000)

def generate_random_email():
    return "user" +str(random.randint(100,999))+"@company.com"

def generate_mobile_number():
    return "9"+str(random.randint(000000000,999999999))

