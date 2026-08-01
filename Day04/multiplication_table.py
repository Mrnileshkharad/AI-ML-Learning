num = 9

for mulptiplier in range (1,11):
    print (num, "*", mulptiplier, "=",  num*mulptiplier)

#Bonus
numlist = [2,3,4,5]
for num in numlist :
    for mulptiplier in range (1,11):
        print (num, "*", mulptiplier, "=",  num*mulptiplier)


def print_table (number):
    for mulptiplier in range (1,11):
        print (number, "*", mulptiplier, "=",  number*mulptiplier)

print_table(9)
print_table (15)

