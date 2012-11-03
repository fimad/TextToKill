from Game import Game
from Player import Player
from Character import Character
from Ability import Ability
from Abilities.KillAbility import KillAbility
from Abilities.TruthtellAbility import TruthtellAbility
from Abilities.AbilitiesAbility import AbilitiesAbility

def test():
    game = Game([AbilitiesAbility(), TruthtellAbility()], [None, Player("Samira", "5036168317@vtext.com", Character("Char",[], ["Truthtell"], "desc")) ])
    game.run()

test()
