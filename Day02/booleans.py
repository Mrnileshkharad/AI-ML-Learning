username = "admin"

password = "admin123"

is_logged_in=username=="admin" and password=="admin123"
print("Login Successful : ",is_logged_in)

password="admin1234"
is_logged_in=username=="admin" and password=="admin123"
print("Login Successful : ",is_logged_in)
