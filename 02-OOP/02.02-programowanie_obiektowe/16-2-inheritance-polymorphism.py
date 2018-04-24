'''
Spójrzmy na ten kod:
'''

'''
class Pet:
    def __init__(self, name):
        self.name = name


class Dog(Pet):
    def bark(self):
        return '{name} goes "Woof woof!"'.format(name=self.name,)


class Cat(Pet):
    def meow(self):
        return '{name} goes "Meow!"'.format(name=self.name,)


def fake_animal_sound(animal):
    if isinstance(animal, Dog):
        print(animal.bark())
    elif isinstance(animal, Cat):
        print(animal.meow())


if __name__ == '__main__':
    dog = Dog('Tony')
    fake_animal_sound(dog)

    cat = Cat('Adolf')
    fake_animal_sound(cat)
'''

'''
Co się stanie kiedy dodamy kolejne zwierzaki?
Będziemy rozbudowywać funkcję fake_animal_sound o kolejne if'y?
Nie! Użyjemy polimrofizmu!
'''

'''
class Pet:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        raise NotImplementedError('Implement this method in subclass!')
        # return('unidentifiable sound of an animal')


class Dog(Pet):
    def make_sound(self):
        return '{name} goes "Woof woof!"'.format(name=self.name,)


class Cat(Pet):
    def make_sound(self):
        return '{name} goes "Meow!"'.format(name=self.name,)


def fake_animal_sound(animal):
    print(animal.make_sound())


if __name__ == '__main__':
    dog = Dog('Tony')
    fake_animal_sound(dog)

    cat = Cat('Adolf')
    fake_animal_sound(cat)

    pet = Pet('Pat')
    fake_animal_sound(pet)
'''

'''
Możemy korzystać też korzystać z metod bazowych, 
i umieszczać w nich część logiki jeśli będzie ona wspólna
dla dziedziczących klas.
'''

'''
class Pet:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        # raise NotImplementedError('Implement this method in subclass!')
        return '{name} goes '.format(name=self.name, )


class Dog(Pet):
    def make_sound(self):
        return super().make_sound() + '"Woof woof!"'


class Cat(Pet):
    def make_sound(self):
        return super().make_sound() + '"Meow!"'


def fake_animal_sound(animal):
    print(animal.make_sound())


if __name__ == '__main__':
    dog = Dog('Tony')
    fake_animal_sound(dog)

    cat = Cat('Adolf')
    fake_animal_sound(cat)

    pet = Pet('Pat')
    fake_animal_sound(pet)
'''
