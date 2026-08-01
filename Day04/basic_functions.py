def greet(name):
    print(f"Hello {name} \nWelcome to Python Functions")

greet("Nilesh")

def square(number):
    print (f"Square of {number} is " ,number**2)
    return number**2

square (8)

def is_even(number):
    if number%2 ==0:
        print(True)
        return True
    else:
        print (False)
        return False

is_even(3)

def get_full_name(first_name, last_name):
    print (f"{first_name}  {last_name}")
    return (first_name, last_name)

get_full_name("Nilesh","Kharad")