# Paul Basso
# The following program is designed to have several functions, similar to a Discord Bot.

print ("Hello! I am Kowalski, your personal assistant.")
name = input("What is your name? ")
print ("Pleasure to meet you %s! At the moment, I have very limited functions, such as Calculator. " % name)
decision = input("Would you like to try Calculator? Enter Y for yes or N for no ")
calcresponse = "Y"
if decision == calcresponse:
    calcrequest = input("What would you like to calculate? Enter A for addition, S for subtraction, M for multiplication, or D for division ")
    add = "A"
    subtract = "S"
    multiplication = "M"
    division = "D"
else:
    print ("Unfortunately, I have no other functions. Goodbye %s!" % name)
    exit()

if calcrequest == add:
    firstnum = (input("Please enter a number "))
    secondnum = (input("Please enter another number "))
    num1 = int(firstnum)
    num2 = int(secondnum)
    sum = num1 + num2
    print("The sum of %s and %s is" % (firstnum, secondnum), sum)

if calcrequest == subtract:
    firstnum = (input("Please enter a number "))
    secondnum = (input("Please enter another number "))
    num1 = int(firstnum)
    num2 = int(secondnum)
    difference = num1 - num2
    print("The difference of %s and %s is" % (firstnum, secondnum), difference)

if calcrequest == multiplication:
    firstnum = (input("Please enter a number "))
    secondnum = (input("Please enter another number "))
    num1 = int(firstnum)
    num2 = int(secondnum)
    product = num1 * num2
    print("The product of %s and %s is" % (firstnum, secondnum), product)

if calcrequest == division:
    firstnum = (input("Please enter a number "))
    secondnum = (input("Please enter another number "))
    num1 = int(firstnum)
    num2 = int(secondnum)
    quotient = num1 / num2
    print("The quotient of %s and %s is" % (firstnum, secondnum), quotient)

