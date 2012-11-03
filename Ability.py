class Ability:
    """ An abstract class that specific Abilities should extend
    """
    def __init__(self, name, keywords):
        self.name = name
        self.keywords = keywords
    
    def guardedEventsFor(self, player, args, onSuccess, wantsOldName = False):
        """ Checks if player has this Ability and if so, removes it
            from their Ability list and calls onSuccess. If player 
            does not have this Ability, returns a SendEvent.
            wantsOldName marks whether or not the onSuccess function
            wants the old name as a parameter. Useful for names that are
            LimitedUseStrings.
        """
        if player.getCharacter().hasAbility(self.name):
            oldName = player.getCharacter().removeAbility(self.name)
            if( wantsOldName ):
                (successful, events) = onSuccess(self, player, args, oldName)
                if not successful:
                    player.getCharacter().addAbility(oldName)
                return events
            else:
                (successful, events) = onSuccess(self, player, args)
                if not successful:
                    player.getCharacter().addAbility(oldName)
                return events
        else:
            return [SendEvent(player, "You don't have that ability!")]

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

