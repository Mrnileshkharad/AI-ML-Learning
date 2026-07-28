test_cases = {
    "TC_Login",
    "TC_Login",
    "TC_Payment",
    "TC_Refund",
    "TC_Refund",
    "TC_Profile"
}

print("Total unique test cases: ",len(test_cases))

##Adding TC_Logout 
test_cases.add("TC_Logout")
print(test_cases)

##Removing  "TC_Profile"
test_cases.remove("TC_Profile")
print(test_cases)

print("TC_Login" in test_cases)
print("TC_Search" in test_cases)

automation = {
    "TC_Login",
    "TC_Logout",
    "TC_Profile"
}

##Common test cases
common_testCases=test_cases.intersection(automation)
print("Common test cases are : ",common_testCases)
##All test cases from both sets.
print("All test cases from both sets: ",len(common_testCases))
