from Event import Event
from Ability import Ability

class CoerceEvent(Event):
    def __init__(self, playerName, abilityName, targetPlayerName):
        Event.__init__(self)
        if ability == 'kill' or if ability == 'k':
            self.Ability = KillAbility()
            self.keyword = 'kill'
        if ability == 'save' or if ability == 's':
            self.Ability = SaveAbility()
            self.keyword = 'save'
        self.playerName = playerName
        self.targetPlayerName = targetPlayerName
        
    def perform(self, game):
        args = self.keyword + self.targetPlayerName
        self.Ability.getEventsFor(playerName,targetPlayerName)
