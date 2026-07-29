numlist =range(1,21)

##Print numbers:
for num in numlist :
    print(num)

##Print only even numbers.
print(" Even numbers are : "  )
for num in numlist :
    if num % 2==0 :
        print(num)

##Print only odd numbers.
print(" Odd numbers are : "  )
for num in numlist :
    if num % 2!=0 :
        print(num)

##Scenario 4
test_cases = [
    "Login",
    "Payment",
    "Refund",
    "Profile",
    "Logout"
]

for test in test_cases:
    print ("Executing ",test , " Test")

