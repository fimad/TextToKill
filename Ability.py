class Ability:
    """ An abstract class that specific Abilities should extend
    """
    def __init__(self, name, keywords):
        self.name = name
        self.keywords = keywords

    def useAbility(self,character):
        if character.hasAbility():
                Character.removeAbility(Ability)
                return True
        return False

    def getName(self):
        return self.name

    def getKeywords(self):
        """ Returns a list of keywords for this Ability.
        """
        return self.keywords

    def getEventsFor(self, player, arg):
        """ Sub-classes must override this method.
            Returns a list of events that perform the state changes.
        """
        pass

'''
class Truthtell(Ability):
    abilityName = 'Truthtell'
    keyword = 'truthtell'
    toTarget = 'A truthell is being used on you. Find the game master.'
    #remove from owner's list of abilities
    
class Steal(Ability):
    abilityName = 'Steal'
    keyword = 'steal'
    abilityToSteal = '' #take input
    toTarget = 'Your ' + abilityToSteal + ' is being stolen.'
    #remove from owner's list of abilities

class Kill(Ability):
    abilityName = 'Kill'
    keyword = 'kill'
    toTarget = 'You are dying. You will die in 15 minutes unless a save is used on you.'
    toAll = playerName + ' is being killed and has 15 minutes to live if not saved.' #fix
    #put kill on queue
    #remove from owner's list of abilities

class Save(Ability):
    abilityName = 'Save'
    keyword = 'save'
    toTarget = ''
    toAll = ''
    if playerIsDying: #fix
        if playerTimesDying == 1: #fix
            toAll = playerName + ' is no longer dying.' #fix
        else:
            toAll = playerName + ' has had one save used on them. They are now dying ' + str(playerTimesDying) + ' times.' #fix
        #remove oldest active kill on queue
        #remove from owner's list of abilities
    else:
        #send playerName + ' is not dying' to user
        
class Error(Ability):
'''    
