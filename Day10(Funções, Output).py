def myFunction():
    """Sums 3 to 2""" #Docstring = descreve a função
    result = 3+2
    return result
print(myFunction())

def formatName(fName,lName):
    return f"{fName.title()} {lName.title()}"

print(formatName("FeLiPe","TeIXeira"))
