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
        return self.abilityList.count(name) > 0
    
    def removeAbility(self, name):
        value = self.abilityList[self.abilityList.index(name)]
        self.abilityList.remove(name)
        return value

    def addAbility(self, name):
        self.abilityList.append(name)

    def getAbilityList(self):
        return self.abilityList

    def hasItem(self, item):
        return self.itemList.count(item) > 0

    def addItem(self, item):
        self.itemList.append(item)

    def removeItem(self, item):
        self.itemList.remove(item)
    
    def getItemList(self):
        return self.itemList
        
    def getDescription(self):
        return self.description
