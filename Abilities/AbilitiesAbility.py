from Ability import Ability
from Player import Player
from Game import Game
from Event import Event
from Events.SendEvent import SendEvent

class AbilitiesAbility(Ability):

    def __init__(self):
        Ability.__init__(self, "Abilities", ["abilities","ab"])
    
    def getEventsFor(self,game,player,args):
        """Checks what abilities the player has, and sends them 
           a message with this information.
        """
        abilities = player.getCharacter().getAbilityList()
        msg = 'Your abilities are: '
        for abilityName in abilities:
            msg = msg + abilityName + ' '
        return [SendEvent(player,msg)]
