from abc import ABC, abstractmethod
class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        return f'Я {self.name}, мой уровень {self.level}'
    @abstractmethod
    def attack(self):
        pass

    def rest(self):
        self.__health += 1
        return f'{self.name} отдыхает...'
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} атакует мечом")

class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana
    def attack(self):
        print(f"{self.name} использует магию")

class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
    def attack(self):
        print(f"{self.name} атакует из-под тишка")

warrior = Warrior("Тор", 10,100,35,77)
mage = Mage("Мерлин", 10,100,90,55)
assassin = Assassin("Тень", 20,47,77,90)



heroes = {
    "warrior": warrior,
    "mage": mage,
    "assassin": assassin
}
for hero in heroes.values():
    print(hero.greet())
    hero.attack()
    print(hero.rest())