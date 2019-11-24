"""
__author__ = Paul Basso

"""


def calculator():
    """
    Utilizes user input to perform basic mathematical calculations,
    including Addition, Subtraction, Multiplication, and Division.

    """

    import pyinputplus as pyip

    print("Currently, I can perform Addition, Subtraction, Multiplication, "
          "and Division. ")

    calcrequest = pyip.inputChoice(['A', 'S', 'M', 'D'])

    if calcrequest == "A":
        first_num = pyip.inputNum("Please enter a number ")
        second_num = pyip.inputNum("Please enter another number ")
        sum_of_numbers = first_num + second_num
        print("The sum of %s and %s is" % (first_num, second_num),
              sum_of_numbers)

    elif calcrequest == "S":
        first_num = pyip.inputNum("Please enter a number ")
        second_num = pyip.inputNum("Please enter another number ")
        difference = first_num - second_num
        print("The difference of %s and %s is" % (first_num, second_num),
              difference)

    elif calcrequest == "M":
        first_num = pyip.inputNum("Please enter a number ")
        second_num = pyip.inputNum("Please enter another number ")
        product = first_num * second_num
        print("The product of %s and %s is" % (first_num, second_num), product)

    elif calcrequest == "D":
        first_num = pyip.inputNum("Please enter a number ")
        second_num = pyip.inputNum("Please enter another number ")
        quotient = first_num / second_num
        print("The quotient of %s and %s is" % (first_num, second_num),
              quotient)
