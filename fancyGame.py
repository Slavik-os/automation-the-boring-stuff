# not the cleanest code but it does the job as asked to 

listOfItems= {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12,'books of power':100,'snakes drinks':100,'sorcery hat':1}

def inventoryList(lst):
    totalCount = 0 
    print('Before inventory : ')
    for k,v in lst.items():
        print(str(v),'  ',k)
        totalCount+=v
    print( 'number of items : ',totalCount )

inventoryList(listOfItems)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
def addToInventory(inventory, addedItems):
    counts = dict()
    for i in addedItems:
        counts[i]=counts.get(i,0) +1                             # counts the items in  the new list and return them as dictionary
# counts  = {'gold coin': 3, 'dagger': 1, 'ruby': 1}     
    for keys in inventory :
        if keys in counts :
            inventory[keys] = counts[keys] + inventory[keys]
        else :
            pass
# check if there are new items that are not in the old list       
    for k,v in counts.items() :
      if counts[k] not in inventory :
        inventory.setdefault(k,v)
    print('New items : ')
    totalCount = 0 
    for k,v in inventory.items():
        print(str(v),' ',k)
        totalCount+=v
    print('number of items : ',totalCount)            

addToInventory(listOfItems,dragonLoot)
