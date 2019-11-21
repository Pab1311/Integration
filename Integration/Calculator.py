def calculator():
    import pyinputplus as pyip

    calcrequest = pyip.inputChoice(['A', 'S', 'M', 'D'])

    if calcrequest == "A":
        firstnum = pyip.inputNum("Please enter a number ")
        secondnum = pyip.inputNum("Please enter another number ")
        sum = firstnum + secondnum
        print("The sum of %s and %s is" % (firstnum, secondnum), sum)

    elif calcrequest == "S":
        firstnum = pyip.inputNum("Please enter a number ")
        secondnum = pyip.inputNum("Please enter another number ")
        difference = firstnum - secondnum
        print("The difference of %s and %s is" % (firstnum, secondnum),
              difference)

    elif calcrequest == "M":
        firstnum = pyip.inputNum("Please enter a number ")
        secondnum = pyip.inputNum("Please enter another number ")
        product = firstnum * secondnum
        print("The product of %s and %s is" % (firstnum, secondnum), product)

    elif calcrequest == "D":
        firstnum = pyip.inputNum("Please enter a number ")
        secondnum = pyip.inputNum("Please enter another number ")
        quotient = firstnum / secondnum
        print("The quotient of %s and %s is" % (firstnum, secondnum), quotient)
