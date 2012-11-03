class LimitedUseString(str):
    """ A string that is tagged with a number of uses. Useful for implementing
        Abilities that can be used a set number of times until a success occurs
    """

    def __new__(self, value, numUses):
        val = str.__new__(self, value)
        val.value = value
        val.usesLeft = numUses
        return val

    def decrement(self):
        """ Returns a new LimitedUseString that has one less use
        """
        return LimitedUseString(self.value, self.usesLeft-1)

    def getUsesLeft(self):
        """ Returns the number of uses left for this ability
        """
        return self.usesLeft

    def isValid(self):
        """ Are there any uses left? """
        return self.usesLeft > 0
