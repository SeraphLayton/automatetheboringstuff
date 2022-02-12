invent = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def displayInventory(inv):
    c  = 0
    for k, v in inv.items():
        print(str(v) + " " + k)
        c = c +v
    print("Total number of items: " + str(c))

def addToInventory(inventory, addedItems):
    for j in addedItems:
        inventory.setdefault(j,0)
        inventory[j] += 1
    return inventory


invent = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


invent = addToInventory(invent, loot)
displayInventory(invent)
    
