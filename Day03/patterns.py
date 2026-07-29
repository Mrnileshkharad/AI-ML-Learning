##Using for loop

pattern= [1,2,3,4,5]

for x in pattern:
    print("*"*x)

##Bonus

for x in pattern:
    print("*"*pattern[-x])




## Using while loop

maxpatternlenth=5
initialpatternlength=1
while initialpatternlength<=maxpatternlenth:
    print("*"*initialpatternlength)
    initialpatternlength+=1


##Bonus

maxpatternlenth=5
initialpatternlength=1
while initialpatternlength<=maxpatternlenth:
    print("*"*maxpatternlenth)
    maxpatternlenth=maxpatternlenth-1