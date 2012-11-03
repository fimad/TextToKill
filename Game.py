from datetime import datetime
import time

from Inbox import Inbox
from Outbox import Outbox
from Parser import Parser
from Abilities.ErrorAbility import ErrorAbility
from PriorityQueue import PriorityQueue

class Game:
    """ Defines a running instance of a Murder Mystery.
        Handles the initialization of the various game states.
    """
    def __init__(self, abilities, players):
        self.gm = players[0]
        self.errorAbility = ErrorAbility()
        self.eventQueue = PriorityQueue()
        self.parser = Parser()
        self.inbox = Inbox()
        self.outbox = Outbox()

        self.players = {}
        for player in players[1:]:
            self.players[player.getName().lower()] = player

        self.abilities = {}
        for ability in abilities:
            self.abilities[ability.getName().lower()] = ability
            
        self.infectedPlayer = None

    def getGameMaster(self):
        return self.gm

    def addEvent(self, event):
        """ Schedules an event to be run.
        """
        self.eventQueue.put(event)

    def addEvents(self, events):
        """ Schedules a list of events to be run.
        """
        for event in events:
            self.eventQueue.put(event)

    def getOutbox(self):
        return self.outbox

    def isValidAbility(self, name):
        return name.lower() in self.abilities

    def getAbility(self, name):
        return self.abilities[name]

    def getAbilityNames(self):
        return self.abilities.keys()

    def isValidPlayer(self, name):
        return name.lower() in self.player

    def addPlayer(self, player):
        if player.getName().lower() not in self.players:
            self.players[player.getName().lower()] = player
            print "Adding player: " + player.getName()

    def getPlayer(self, name):
        return self.players[name]

    def getPlayerNames(self):
        return self.players.keys()

    def removePlayer(self, name):
        if( self.isValidPlayer(name) ):
            del self.players[name]

    def run(self):
        """ Run the game, and Don't stop.
            Ever.
        """
        print "Starting the main loop!"
        while( True ):
            self.step()
            time.sleep(5)

    def step(self):
        """ Perform one step of the game logic.
            You need to call this repeatedly to make the game run.
        """
        #process incoming messages
        newMessages = self.inbox.poll()
        commands = self.parser.parse(self, self.abilities.values(), newMessages, self.errorAbility)
        for (sender,ability,args) in commands:
            print "Handling '"+ability.getName()+"' for '"+sender+"'"
            for player in self.players.values():
                if( player.getContact() == sender ):
                    print "\tRunning the ability!"
                    self.addEvents(ability.getEventsFor(self, player, args))
                    break

        #Process the queue of events
        while( not self.eventQueue.empty() ):
            event = self.eventQueue.get()
            if( event.when() < datetime.now() ):
                print "Performing an event"
                event.perform(self)
                print self.infectedPlayer + " is now infected!"
            else:
                #Doesn't support peeking, so shove it back in the queue if it
                #shouldn't happen yet
                self.eventQueue.put(event)
                break

