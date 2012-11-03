from Character import Character

class Player:
    
    def __init__(self, name, contact, character):
        self.name = name
        self.contact = contact
        self.character = character
    
    def getName(self):
        return self.name
    
    def getContact(self):
        return self.contact
        
    def getCharacter(self):
        return self.character
