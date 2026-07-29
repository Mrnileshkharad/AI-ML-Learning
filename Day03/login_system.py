username = "admin"
password = "admin123"

##for loop
maxattempts=[1,2,3]

for attempts in maxattempts:
    if username=="admin" and password=="admin123":
        print ("Welcome Admin")
        print("1. View Profile")
        print("2. Check Balance")
        print("3. Logout")
        break
    else:
        print("Invalid Credentials")
        attempts
        if(attempts==3):
          print("Account Locked")


##while loop

maxattempts = 3
attempt=1



while attempt<=maxattempts :
    if username=="admin" and password=="admin123":
        print ("Welcome Admin")
        print("1. View Profile")
        print("2. Check Balance")
        print("3. Logout")
        break
    else:
        print("Invalid Credentials")
        if(attempt==maxattempts):
           print("Account Locked")
        attempt+=1
     
    
    
