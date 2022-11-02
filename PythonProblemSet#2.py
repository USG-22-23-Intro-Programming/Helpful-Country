#Factorial!
def factorial(x):
    y = 1
    for i in range (1, x + 1):
        #^only gonna inlcude number 1 - x+1, not inlcuding the answer for x+1 and 1 just numbers in between
        y = y * i

    print (" The factorial of " + str(x) + " is ")
    print (y)

#Double It!
'''def double():
    double = input("What do word do you want to double?")
    
    #^ the quotations marks are just there to just keep the whole word together, compliling them
    for char in double:
        output = output + char * 2
    print(output)'''

#Camel Case!
def camelCase():
    file = (input("Enter a filename"))
    split = file.split("  ")
    camelcase = split[0] + "".join(word.title() for word in split[1:])
    camelcase = camelcase.replace("/","-")
    camelcase = camelcase.replace("_","")
    print(camelcase)
    
def main():
    factorial(6)
    factorial(13)


if __name__ == "__main__":
    main()
    #double()
    camelCase()
