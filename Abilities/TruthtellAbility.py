from Player import Player
from Game import Game
from Event import Event

class TruthtellAbility(Ability):

    def __init__(self):
        self.abilityName = 'Truthtell'
        self.keywords = ['truthtell','tt']
        self.toTarget = 'A truthell is being used on you. Find the game master.'
    
    def getEventsFor(self,player,targetPlayer):
        """ Calls guardedEventsFor to check if the player has a truthtell.
        """
        return guardedEventsFor(self,player,targetPlayer)
    
    def onSuccess(self,player,targetPlayer)
        """ Sends messages to the player, the target player, and the GM.
            Is called by guardedEventsFor.
        """
        SendEvent(targetPlayer, player.getName() + ' is using a truthtell on you. Please find the game master.')
        SendEvent(player, player.getName() + ' has been notified. Please find the game master.')    
        gameMaster = Game.getGameMaster()
        SendEvent(gameMaster, player.getName() + ' is using a truthtell on ' + player.getName() +'.')
