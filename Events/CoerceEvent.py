from Event import Event
from Ability import Ability

class CoerceEvent(Event):
    def __init__(self, playerName, abilityName, targetPlayerName):
        Event.__init__(self)
        self.abilityName = abilityName
        self.playerName = playerName
        self.targetPlayerName = targetPlayerName
        
    def perform(self, game):
        if self.abilityName in game.getAbility("Kill").getKeywords():
            self.ability = game.getAbility("Kill")
            self.keyword = game.getAbility("Kill").getKeywords()[0]
        if self.abilityName in game.getAbility("Save").getKeywords():
            self.ability = game.getAbility("Save")
            self.keyword = game.getAbility("Save").getKeywords()[0]

        args = self.targetPlayerName
        return self.ability.getEventsFor(game,game.getPlayer(self.playerName),args)
