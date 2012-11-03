from Character import Character
from OutputAddress import OutputAddress

class Player:
    
    __init__(self, name, contact, character):
        self.name = name
        self.contact = contact
        self.character = character
    
    getName():
        return self.name
    
    getContact():
        return self.contact
        
    getCharacter():
        return self.character
