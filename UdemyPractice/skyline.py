def myfunc(text):

    result = ""

    for index in range(len(text)):

        if index % 2 == 0:
            result += text[index].lower()
        else:
            result += text[index].upper()

    return result


print(myfunc("Anthropomorphism"))