gust = {
    'name': 'Gust',
    'cost': 'CC',
    'damage': 30,
    'effect': None
}


class Attack:
    def __init__(self, name, cost, damage, effect):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.effect = effect
