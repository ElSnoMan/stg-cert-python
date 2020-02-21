from typing import List

# 1. Create a class representation of Tepig


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


# 2. Create a class representation of Attack


class Attack:
    def __init__(self, name, cost, damage, effect):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.effect = effect


# 3. Write a simple program to simulate one Pokemon attacking another Pokemon


# attacks
ember = Attack(name='Ember', cost='FC', damage=30, effect='Discard an Energy attached to this Pokémon.')
thunder_shock = Attack(name='Thunder Shock', cost='EE', damage=40, effect=None)
water_gun = Attack('Water Gun', cost='W', damage=20, effect=None)

# pokemon
squirtle = Pokemon('Squirtle', 'Basic', 70, 'Water', attacks=[water_gun], weakness='Electric')
pikachu = Pokemon('Pikachu', 'Basic', 70, 'Electric', [thunder_shock], weakness='Fighting')

print(squirtle.hp)
pikachu.attack('Thunder Shock', squirtle)
print(squirtle.hp)


# 4. How would you handle if a Pokemon's attack is super effective?
