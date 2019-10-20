# Paul Basso
# The following program is designed to have several functions, similar to a Discord Bot.

from Integration.Calculator import calculator
from Integration.EightBall import eightball
from Integration.ShoppingList import shoppinglist

print ("Hello! I am Kowalski, your personal assistant.")
name = input("What is your name? ")
print ("Pleasure to meet you %s! At the moment, I have two functions: Calculator and Magic Eight Ball. " % name)

def main():
    choice = True
    while choice:
        print("Here are my functions and how to access them:")
        print("1. Calculator (type Calculator)")
        print("2. Magic Eight Ball (type 8ball)")
        print("3. Shopping List (type ShopList)")
        print("4. Exit Program (type Quit)")
        decision = input("What function would you like? ")

        if decision == "Quit":
            print ("Live long and prosper, %s!" % name)
            choice = False

        if decision == "Calculator":
            calculator()
            proceed = input("Would you like to continue using Calculator? Enter Y for yes or N for no ")
            while proceed == "Y":
                calculator()
                proceed = input("Would you like to continue using Calculator? Enter Y for yes or N for no ")
                continue
            else:
                main()


        elif decision == "8ball":
            eightball(name)
            proceed1 = input("Would you like to continue using Magic Eight Ball? Enter Y for yes or N for no ")
            while proceed1 == "Y":
                eightball(name)
                proceed1 = input("Would you like to continue using Magic Eight Ball? Enter Y for yes or N for no ")
                continue
            else:
                main()

        elif decision == "ShopList":
            shoppinglist()
            proceed2 = input("Would you like to make a new Shopping List? Enter Y for yes or N or no ")
            while proceed2 == "Y":
                shoppinglist()
                proceed2 = input("Would you like to make a new Shopping List? Enter Y for yes or N or no ")
                continue
            else:
                main()
main()




