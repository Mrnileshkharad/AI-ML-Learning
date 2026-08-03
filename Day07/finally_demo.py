
##Program 1---without file.close()
print("Program 1 Started")
try:
    file = open("Day06/test_data/testcases1.txt")
    print("File Opened Successfully")
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing resources...")
print("Program 1 Ended")

##Program 2 with file.close()
print("Program 2 Started")
file_2=None
try :
    file_2=open("abc.tex",'r')
    print("File Opened Successfully in read mode")
except FileNotFoundError:
    print("File not found")
finally:
    if file_2 is not None:
        file_2.close()
        print ("File Closed!!!")
    else:
        print("Error while closing file")
print("Program 2 Ended")

###Program 3 OSException

print("Program 3 Started")
file_3=None
try:
    file_3 = open("Day06/test_data/testcases.txt","r")
    print("File Opened Successfully")
    file_3.write("Hello there !!")
except OSError:
    print("Cannot Write Here")
finally:
    if file_3 is not None:
        file_3.close()
        print ("File Closed!!!")
    else:
        print("Error while closing file")
print("Program 3 Ended")



         
