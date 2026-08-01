def add(a,b):
    print (f"{a} + {b} =", (a+b))
    return (a+b)

def subtract(a,b):
    print (f"{a} - {b} =", (a-b))
    return (a-b)

def multiply(a,b):
    print (f"{a} * {b} =", (a*b))
    return (a*b)

def divide(a,b):
    if b==0:
        print("Cannot divide by zero")
    else:
        print (f"{a} / {b} =", (a/b))
        return (a/b)

add(2,4)
subtract(2,4)
multiply(2,4)
divide(2,4)
divide(2,0)