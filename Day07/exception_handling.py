print("Program Started")

number = 10
divisor = 2

try :
    result = number/divisor
    print (result)
except ZeroDivisionError:
     print("Cannot divide by zero.")

else:
     print("Division Successful")

print("Program Ended")


