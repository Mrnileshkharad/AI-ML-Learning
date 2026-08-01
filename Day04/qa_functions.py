def validate_status_code(actual, expected):
    if actual==expected:
        print ("PASS")
    else:
        print ("FAIL")
        print("Expected : ", expected)
        print("Actual : ", actual)

validate_status_code (200,200)
validate_status_code(404,200)

def validate_response_time(actual_time, max_time):
    if actual_time<=max_time:
        print("PASS")
    else:
        print ("FAIL")

validate_response_time(450,500)
validate_response_time(650,500)

def generate_transaction_id(prefix, number):
    print(f"{prefix}{number}")
    txnid= f"{prefix}{number}"
    return txnid

generate_transaction_id ("TXN",1001)

