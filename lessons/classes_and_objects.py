# How would you represent an Animal in code?
from typing import List


class Animal:
    def __init__(self, name):
        self.name = name

    def vocalize(self):
        print(f'{self.name} made a sound')


animal = Animal('foo')
animal.vocalize()


class Toy:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.has_ball = False
        self.toys: List[Toy] = []

    def vocalize(self):
        print(f'{self.name} barked')

    def fetch(self, toy: Toy):
        self.toys.append(toy)
        print(f'{self.name} fetched the {toy.name}')

    def print_toys(self):
        for toy in self.toys:
            print(toy.name)


sock = Toy('sock')
ball = Toy('ball')
rope = Toy('rope')


dog = Dog('Jazzy')
dog.vocalize()
dog.fetch(sock)
dog.fetch(ball)
dog.fetch(rope)
dog.print_toys()
