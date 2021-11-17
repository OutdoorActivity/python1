class Animal:
    def voice(self):
        pass


class Dog(Animal):
    def voice(self):
        return "Гав!"


class Cat(Animal):
    def voice(self):
        return "Мяу"


class Hamster(Animal):
    def voice(self):
        return "пск&@!?!"


just_dog = Dog()
just_cat = Cat()
just_hamster = Hamster()

print(just_dog.voice())
print(just_cat.voice())
print(just_hamster.voice())