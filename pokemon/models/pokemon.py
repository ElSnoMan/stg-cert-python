from typing import Dict, List
from pokemon.models.attack import Attack


articuno = {
    'name': 'Articuno',
    'evolution': 'Basic',
    'hp': 120,
    'type': 'Water',
    'weakness': 'Electric',
    'attacks': {
    }
}


class Pokemon:
    def __init__(self, name, evolution, hp, type, attacks, weakness):
        self.name = name
        self.evolution = evolution
        self.hp = hp
        self.type = type
        self.weakness = weakness
        self.attacks: List[Attack] = attacks

    def attack(self, attack_name, pokemon_to_hit):
        """ Select the attack and hit the defending Pokemon. """
        attack = next(attack for attack in self.attacks if attack.name == attack_name)
        if pokemon_to_hit.weakness == self.type:
            pokemon_to_hit.hp -= attack.damage * 2
        else:
            pokemon_to_hit.hp -= attack.damage
