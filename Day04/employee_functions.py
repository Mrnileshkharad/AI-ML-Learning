def print_employee_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value} ")

        

print_employee_details(
name="Nilesh",
department="QA",
experience=5,
city="Pune"
)


