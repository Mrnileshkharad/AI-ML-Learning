#Prgram 1 
user_input =input("Please enter a number : ")
try :
    number = int(user_input)
    result =100/number
    print (result)
except ValueError:
    print ("Please enter valid number.")
except ZeroDivisionError:
    print("Can not devide by 0")
else:
    print("Calculation Successful")
finally:
    print("Program Finished")

#program2

user_input =input("Please enter a number : ")
try :
    number = int(user_input)
    with open("Day07/logs/logs.txt","w") as file:
        file.write(f"Please enter a number :  {number}\n")
    result =100/number
    with open("Day07/logs/logs.txt","a") as file:
        file.write(f"Result : {result} \n")
    print (result)
except ValueError:
     with open("Day07/logs/logs.txt","w") as file:
            file.write(f"Please enter a number : {user_input} \n")
            file.write("Please enter valid number.\n")
     print ("Please enter valid number.")
    
except ZeroDivisionError:
     with open("Day07/logs/logs.txt","w") as file:
                file.write(f"Please enter a number : {number} \n")
                file.write("Can not devide by 0\n")
     print("Can not devide by 0")
else:
    with open("Day07/logs/logs.txt","a") as file:
            file.write("Calculation Successful \n")
    print("Calculation Successful")

finally:
    with open("Day07/logs/logs.txt","a") as file:
                file.write("Program Finished\n")
    print("Program Finished")

