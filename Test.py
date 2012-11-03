from Game import Game
from Player import Player
from Character import Character
from Ability import Ability
from Abilities.KillAbility import KillAbility
from Abilities.TruthtellAbility import TruthtellAbility
from Abilities.AbilitiesAbility import AbilitiesAbility

def test():
    samira = Player("Samira", "5036168317@vtext.com", Character("Char",[], ["Truthtell"], "desc"))
    will = Player("Will", "8186065330@vtext.com", Character("Char",[], ["Truthtell","Kill"], "desc"))
    game = Game([AbilitiesAbility(), TruthtellAbility()], [None, samira, will])
    game.run()

test()
