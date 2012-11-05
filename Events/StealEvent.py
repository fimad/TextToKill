from Event import Event
from Events.SendEvent import SendEvent

class StealEvent(Event):
    def __init__(self, player, targetName, wanted, oldName):
        Event.__init__(self)
        self.player = player
        self.targetName = targetName
        self.wanted = wanted
        self.oldName = oldName

    def perform(self, game):
        targetPlayer = game.getPlayer(self.targetName)
        target = targetPlayer.getCharacter()
        if( target.hasItem(self.wanted) ):
            target.removeItem(self.wanted)
            self.player.getCharacter().addItem(self.wanted)
            return [
                SendEvent(targetPlayer,"You lost your '"+self.wanted+"' item!") ,
                SendEvent(self.player,"You have gained a '"+self.wanted+"' item!")
            ]
        elif( target.hasAbility(self.wanted) ):
            target.removeAbility(self.wanted)
            self.player.getCharacter().addAbility(self.wanted)
            return [
                SendEvent(targetPlayer,"You lost your '"+self.wanted+"' ability!") ,
                SendEvent(self.player,"You have gained the ability to '"+self.wanted+"'!")
            ]
        else:
            newName = self.oldName.decrement()
            if( newName.isValid() ):
                self.player.getCharacter().addAbility(newName)
                return [ SendEvent(self.player,"Foiled! You have "+str(newName.getUsesLeft())+" attempts left for this steal.") ]
            else:
                return [ SendEvent(self.player,"Blast! You've exhausted all of this steal's attempts.") ]
