from Ability import Ability

class Character:
    
    def __init__(self, name, itemList, abilityList, description):
        self.name = name
        self.abilityList = abilityList
        self.itemList = itemList
        self.description = description
    
    def getName(self):
        return self.name
    
    def hasAbility(self, name):
        return map(lambda a:a.lower(),self.abilityList).count(name.lower()) > 0
    
    def removeAbility(self, name):
        value = [a for a in self.abilityList if a.lower() == name.lower()][0]
        self.abilityList = [a for a in self.abilityList if a.lower() != name.lower()]
        return value

    def addAbility(self, name):
        self.abilityList.append(name)

    def getAbilityList(self):
        return self.abilityList

    def hasItem(self, item):
        return map(lambda a:a.lower(),self.itemList).count(item.lower()) > 0

    def addItem(self, item):
        self.itemList.append(item)

    def removeItem(self, item):
        self.itemList = [i for i in self.itemLits if i.lower() != item.lower()]
    
    def getItemList(self):
        return self.itemList
        
    def getDescription(self):
        return self.description
