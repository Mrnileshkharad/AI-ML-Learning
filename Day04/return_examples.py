def add_print(a,b):
    result = a+b
    print (result)

def add_return(a,b):
    result = a+b
    print (result);
    return result;

print(type(add_print(2,3)))
print(type(add_return(2,3)))