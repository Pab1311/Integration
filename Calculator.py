def calculator():


    print("Enter A for addition")
    print("Enter S for subtraction")
    print("Enter M for multiplication")
    print("Enter D for division")
    calcrequest = input("What would you like to calculate? ")
    calcfirst = calcrequest
    if calcfirst == "A":
        firstnum = (input("Please enter a number "))
        secondnum = (input("Please enter another number "))
        num1 = int(firstnum)
        num2 = int(secondnum)
        sum = num1 + num2
        print("The sum of %s and %s is" % (firstnum, secondnum), sum)

    elif calcfirst == "S":
        firstnum = (input("Please enter a number "))
        secondnum = (input("Please enter another number "))
        num1 = int(firstnum)
        num2 = int(secondnum)
        difference = num1 - num2
        print("The difference of %s and %s is" % (firstnum, secondnum), difference)

    elif calcfirst == "M":
        firstnum = (input("Please enter a number "))
        secondnum = (input("Please enter another number "))
        num1 = int(firstnum)
        num2 = int(secondnum)
        product = num1 * num2
        print("The product of %s and %s is" % (firstnum, secondnum), product)

    elif calcfirst == "D":
        firstnum = (input("Please enter a number "))
        secondnum = (input("Please enter another number "))
        num1 = int(firstnum)
        num2 = int(secondnum)
        quotient = num1 / num2
        print("The quotient of %s and %s is" % (firstnum, secondnum), quotient)
