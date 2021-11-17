class Animal:
    numInstance = 0

    def __init__(self):
        Animal.numInstance += 1

    def voice(self):
        pass


class Dog(Animal):
    def voice(self):
        return "гав"


class Cat(Animal):
    def voice(self):
        return "мяу"


class Hamster(Animal):
    def voice(self):
        return "пск&@!?!"


def print_amount_instance():
    print('Количество экземпляров:', Animal.numInstance)


just_dog = Dog()
just_cat = Cat()
just_hamster = Hamster()
just_another_animal = Animal()

print(just_dog.voice())
print(just_cat.voice())
print(just_hamster.voice())
print_amount_instance()