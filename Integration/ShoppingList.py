"""
__author__ = Paul Basso

"""


def shoppinglist():
    """
    Creates a shopping list for the user along with having the ability to
    recall the created list whenever desired.

    :return: shop_list to main()
    """

    import pyinputplus as pyip

    shop_list = []
    shop_is_not_created = True

    while shop_is_not_created:
        try:
            numitems = pyip.inputNum("How many items are you planning to "
                                     "purchase? ")
            for i in range(0, numitems):
                item = input("Please enter the item you want to purchase ")
                shop_list.append(item)
            print("Your current shopping list contains the following items: ")
            for item in shop_list:
                print(item)
            shop_is_not_created = False

        except TypeError:
            print("You cannot purchase " + str(numitems) + " items. Please "
                                                           "enter "
                                                           "a whole number.")
    return shop_list
