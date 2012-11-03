from abilities import Ability

class Character:
    
    def __init__(self, name, abilityList, description):
        self.name = name
        self.abilityList = abilityList
        self.itemList = itemList
        self.description = description
    
    getName():
        return self.name
    
    getAbilityList():
        return self.abilityList
    
    getItemList():
        return self.itemList
        
    getDescription():
        return self.description

    hasAbility(self, abl):
        return (abl in abilityList)

    addAbility(self, abl):
        abilityList.add(abl)
    
    removeAbility(self, abl):
        abilityList.remove(abl)
            
    hasItem(self, itm)
        return (itm in itemList)

    addItem(self, itm):
        itemList.add(itm)

    removeItem(self, itm):
        abilityList.remove(itm)
