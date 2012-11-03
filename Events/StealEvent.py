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
        target = game.getPlayer(self.targetName).getCharacter()
        if( target.hasItem(wanted) ):
            target.removeItem(wanted)
            player.addItem(wanted)
            return [
                SendEvent(target,"You lost your '"+wanted+"' item!") ,
                SendEvent(player,"You have gained a '"+wanted+"' item!")
            ]
        elif( target.hasAbility(wanted) ):
            target.removeAbility(wanted)
            player.addAbility(wanted)
            return [
                SendEvent(target,"You lost your '"+wanted+"' ability!") ,
                SendEvent(player,"You have gained the ability to '"+wanted+"'!")
            ]
        else:
            newName = self.oldName.decrement()
            if( newName.isValid() ):
                return [ SendEvent(target,"Foiled! You have "+newName.getUsesLeft()+" attempts left for this steal.") ]
            else:
                return [ SendEvent(target,"Blast! You've exhausted all of steal's attempts.") ]
