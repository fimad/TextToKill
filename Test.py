from Game import Game
from Player import Player
from Character import Character
from Ability import Ability
from Abilities.KillAbility import KillAbility
from Abilities.StealAbility import StealAbility
from Abilities.SaveAbility import SaveAbility
from Abilities.CoerceAbility import CoerceAbility
from Abilities.TruthtellAbility import TruthtellAbility
from Abilities.AbilitiesAbility import AbilitiesAbility

def test():
    abilities = [AbilitiesAbility(), TruthtellAbility(), SaveAbility(), KillAbility(), CoerceAbility(), StealAbility()]
    abilityNames = map(lambda a: a.getName(), abilities)

    samira = Player("Samira", "5036168317@vtext.com", Character("Char",[], abilityNames, "desc"))
    will = Player("Will", "8186065330@vtext.com", Character("Char",[], abilityNames, "desc"))
    players = [None, will]

    game = Game(abilities, players)
    game.run()

test()
