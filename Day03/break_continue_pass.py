numlist =range(1,6)
##Stop when number becomes 4.
for num in numlist :
    print(num)
    if (num==4):
        break


##Skip 3.
for num in numlist :
    if (num!=3):
        print(num)
        continue

##
feature_enabled = True
if feature_enabled :
    pass
    print("pass")
else:
    print("Feature Coming Soon...")