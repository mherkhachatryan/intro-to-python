class Animal(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{0} eats {1}'.format(self.name, food))

    def show_affection(self):
        print('purr')


class Dog(Animal):

    def fetch(self, thing):
        print('{0} goes after the {1}!'.format(self.name, thing))

    @staticmethod
    def show_affection(self):
        print('{0} wags tail'.format(self.name))


d = Dog('D')
d.show_affection()
Animal.show_affection(d)


class Cat(Animal):

    def swatstring(self):
        print('{0} shreds more string'.format(self.name))

    def show_affection(self):
        print('{0} purrs'.format(self.name))

#
# for a in (Dog('Rover'),
#           Cat('Fluffy'),
#           Cat('Lucky'),
#           Dog('Scout'),
#           Animal('Nemo')):
#     a.show_affection()
