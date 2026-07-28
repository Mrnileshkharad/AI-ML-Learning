employee = {
    "id": 101,
    "name": "Nilesh",
    "department": "QA",
    "skills": {"Java", "Python", "SQL"},
    "working_days": (
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    )
}

##Print employee name.
print("Employee Name : ",employee["name"])

##Print department.
print("Department : ",employee["department"])

##Print all skills.
print("Skills : ", employee["skills"])
##Print working days.
print("All working days : ", employee["working_days"])

##Check whether Python is a skill.
print("Check whether Python is a skills : ", "Python" in employee["skills"])

##Add AI to the skills.
employee["skills"].add("AI")
print("Skills after adding AI: ", employee["skills"])
