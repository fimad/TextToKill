class OutputAddress:
    """ The base class for all output address.
    """
    def __init__(self):
        pass

    def matches(senderString):
        """ Must be implemented in sub-classes.
            Returns True if a sender string as returned by Inbox matches this
            address.
        """
        pass

