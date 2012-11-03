from Player import Player
from Game import Game
from Event import Event

class AbilitiesAbility(Ability):

    def __init__(self):
        self.abilityName = 'Abilities'
        self.keywords = ['abilities','ab']
     
    
    def getEventsFor(self,player,targetPlayer):
        """Checks what abilities the player has, and sends them 
           a message with this information.
        """
        abilities = player.getCharacter().getAbilityList()
        msg = 'Your abilities are: '
        for abilityName in abilities[:-1]:
            msg = msg + abilityName + ', '
        msg = msg + 'and ' + abilities[-1] + '.'
        SendEvent(player,msg)
