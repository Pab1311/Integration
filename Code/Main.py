# Paul Basso
# The following program is designed to have several functions, similar to a Discord Bot.

from Integration.Calculator import calculator
from Integration.EightBall import eightball
from Integration.ShoppingList import shoppinglist
from Integration.RandomWebsites import randomsites

print ("Hello! I am Kowalski, your personal assistant.")
name = input("What is your name? ")
print ("Pleasure to meet you %s! At the moment, I have two functions: Calculator and Magic Eight Ball. " % name)

def main():
    choice = True
    while choice:
        print("Here are my functions:")
        print("1. Calculator")
        print("2. Magic Eight Ball")
        print("3. Shopping List")
        print("4. Random Website")
        print("5. Exit Program")
        decision = input("What function would you like? Please enter the number of the function: ")

        if decision == "5":
            print ("Live long and prosper, %s!" % name)
            choice = False

        elif decision == "1":
            calculator()

        elif decision == "2":
            eightball(name)

        elif decision == "3":
            shoppinglist()

        elif decision == "4":
            randomsites()

        else:
            print("I do not have the function " + decision)
            print("Please try again.")
main()

