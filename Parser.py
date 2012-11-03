from Ability import Ability

class Parser:
    
    def parse(self,abilities,messages,Error):
        ''' Takes a list of valid ability objects, a list of new
            messages of the form (sender,text), and an Error object. 
            Returns a list of tuples (sender,abilityObject,restOfString).
            Calls getValidKeywords and parseText. 
        '''
        parsedList = []
        for message in messages:
            (sender,text) = message
            validKeywords = getValidKeywords(abilities)
            parsed = self.parseText(sender,text,validKeywords,Error)
            parsedList.append(parsed)
        return parsedList
    
    def getValidKeywords(self,abilities):
        ''' Takes list of abilities, returns a dictionary validKeywords 
            that associates each keyword with its ability.
        '''
        validKeywords = {}
        for ability in abilities:
            abilityKeywords = ability.getKeywords()
            for abilityKeyword in abilityKeywords:
                validKeywords[abilityKeyword] = ability
        return validKeywords
    
    def parseText(self,sender,text,validKeywords,Error):
        ''' Takes (sender,text); returns (sender,abilityObject,restOfString).
        '''
        text = text.lower()
        words = text.partition(' ')
        if words[0] in validKeywords:
            abilityObject = validKeywords[words[0]]
        else:
            abilityObject = Error
        restOfString = words[2]
        return (sender,abilityObject,restOfString)
            
        
