#a= "Nilesh"
#print(len(a))
#print(a[0])
#print(a[0].lower())

def myfunc (a):
    i=range(0,len(a)-1)
    print(len(a))
    print(i)
    for index in i:
        if index%2==0:
            print(a[index].lower())
        else:
            print(a[index].upper())
        index+=1
    return a[index]

print(myfunc("Anthropomorphism"))
