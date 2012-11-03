from Ability import Ability

class Character:
    
    def __init__(self, name, itemList, abilityList, description):
        self.name = name
        self.abilityList = abilityList
        self.itemList = itemList
        self.description = description
    
    def getName(self):
        return self.name
    
    def getAbilityList(self):
        return self.abilityList
    
    def getItemList(self):
        return self.itemList
        
    def getDescription(self):
        return self.description
