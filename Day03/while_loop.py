maximumretries = 5
attempt=1



while attempt<=maximumretries :
    print("Trying API...")
    print("Attempt ",attempt)
    if attempt==4:
       print("API Success")
       break
    attempt+=1
else:
    print("API Failed after",maximumretries, "attempts")  