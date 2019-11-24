"""The following program is designed to have several functions,  similar to a
Discord Bot.

__author__ = Paul Basso

"""


from Integration.Calculator import calculator
from Integration.EightBall import eightball
from Integration.RandomWebsites import randomsites
from Integration.ShoppingList import shoppinglist

print("Hello! I am Kowalski, your personal assistant.")
name = input("What is your name? ")
print("Pleasure to meet you %s! At the moment, I have two functions: "
      "Calculator and Magic Eight Ball. " % name)


def main():
    """
The function that is called when the program is ran. The function contains
all the other functions within the Integration folder.

    """
    user_wants_to_continue = True
    while user_wants_to_continue:
        print("Here are my functions:")
        print("1. Calculator")
        print("2. Magic Eight Ball")
        print("3. Shopping List")
        print("4. Random Website")
        print("5. Exit Program")
        decision = input(
            "What function would you like? Please enter the number of the "
            "function: ")

        if decision == "5":
            print("Live long and prosper, %s!" % name)
            user_wants_to_continue = False

        elif decision == "1":
            calculator()

        elif decision == "2":
            eightball(name)

        elif decision == "3":
            print("My options are ")
            print("1. Create new list")
            print("2. View current list")
            shopdecision = input("What would you like to do? Please enter "
                                 "the number of the choice. ")

            if shopdecision == "1":
                shop_list = shoppinglist()

            elif shopdecision == "2":
                try:
                    print(shop_list)
                except UnboundLocalError:
                    print("You currently do not have a shopping list. Please "
                          "create a new shopping list. ")

        elif decision == "4":
            randomsites()

        else:
            print("I do not have the function " + decision)
            print("Please try again.")


main()
