from Utilities.calculator import add,subtract
from Utilities.math_utils import square_root
from Utilities.random_utils import generate_otp,generate_transaction_id,generate_random_email,generate_mobile_number
from Utilities.qa_utils import validate_status_code,validate_response_time

print ("========== QA Utility Demo ==========")
print("Addition :" ,add(20,30))
print("Square Root :", square_root(81))
print("OTP :", generate_otp())
print("Transaction ID :", generate_transaction_id())
print("Random Email :", generate_random_email())
print("Random Mobile :", generate_mobile_number())
print("Status Code :" ,validate_status_code(200,200))
print("Response Time :", validate_response_time(400,550))