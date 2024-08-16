AllGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pie': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k , v in guests.items():
        numBrought = numBrought + v.get(item, 0)
        return numBrought
    
print('Number of things being brought')
print(' - Apples ' + str(totalBrought(AllGuests, 'apples')))
print(' - Cups ' + str(totalBrought(AllGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(AllGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(AllGuests, 'ham sandiches')))
print(' - Apple Pies ' + str(totalBrought(AllGuests, 'apple pies')))



stuff = {'rope': 1, 'torch': 6, 'gold': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        ##Fill this part in
        item_total += v
    print(" Total number of items: " + str(item_total))

displayInventory(stuff)
