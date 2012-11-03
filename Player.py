from Character import Character
from OutputAddress import OutputAddress

class Player:
    
    __init__(self, name, contact, characterName):
        self.name = name
        self.contact = contact
        self.characterName = characterName
    
    getName():
        return self.name
    
    getContact():
        return self.contact
        
    getCharacterName():
        return self.characterName
