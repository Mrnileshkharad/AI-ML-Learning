applicant1={"name":"Nilesh","age":34,"salary":65000}
print(f"Name:",applicant1.get("name"),"Age:",applicant1.get("age"),"Salary:",applicant1.get("salary"))
if applicant1.get("age")>=21 and applicant1.get("salary")>=50000:
    print("Congratulations! Loan Approved.")
else:
    print("Sorry! Loan Rejected.")
    if applicant1.get("age")<=21:
        print("Rejected because age is below minimum requirement.")
    else:
        print("Rejected because salary is below minimum requirement.")

applicant1={"name":"Vijay","age":19,"salary":145000}
print(f"Name:",applicant1.get("name"),"Age:",applicant1.get("age"),"Salary:",applicant1.get("salary"))
if applicant1.get("age")>=21 and applicant1.get("salary")>=50000:
    print("Congratulations! Loan Approved.")
else:
    print("Sorry! Loan Rejected.")
    if applicant1.get("age")<=21:
        print("Rejected because age is below minimum requirement.")
    else:
        print("Rejected because salary is below minimum requirement.")

applicant1={"name":"Akshay","age":25,"salary":45000}
print(f"Name:",applicant1.get("name"),"Age:",applicant1.get("age"),"Salary:",applicant1.get("salary"))
if applicant1.get("age")>=21 and applicant1.get("salary")>=50000:
    print("Congratulations! Loan Approved.")
else:
    print("Sorry! Loan Rejected.")
    if applicant1.get("age")<=21:
        print("Rejected because age is below minimum requirement.")
    else:
        print("Rejected because salary is below minimum requirement.")



    