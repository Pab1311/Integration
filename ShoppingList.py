def shoppinglist():
    shoplist = []
    numitems = int(input("How many items are you planning to purchase? "))
    for i in range(0, numitems):
        item = input("Please enter the item you want to purchase ")
        shoplist.append(item)
    print ("Your current shopping list contains the following items: ")
    for item in shoplist:
            print (item)
