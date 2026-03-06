import random
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        return f'Привет {self.name}, мой уровень {self.level}'

    def attack(self):
        self.strength -= 1
        return f'{self.name} наносит удар!'


    def rest(self):
        self.health += 1
        return f'{self.name} отдыхает...'
class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print("Воин аттакует мечом")

class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana
    def attack(self):
        print("Маг кастует заклинание")

class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth
    def attack(self):
        print("Ассасин атакует из-под тишка")

warrior = Warrior("Thor", 10,100,35,77)
mage = Mage("Merlin", 10,100,90,55)
assassin = Assassin("Shadow", 20,47,77,90)



heros = {

    "warrior": warrior,
    "mage": mage,
    "assassin": assassin

}


#game
choice = input ("Ввыберите греоя: ").lower()
if choice in heros:
    player = heros[choice]
    enemy = random.choice(list(heros.values()))

    print(f"Вы выбрали: {player.__class__.__name__}")
    print(f"Ваш противник: {enemy.__class__.__name__}")

    player.attack()
    enemy.attack()

    player_type = player.__class__.__name__
    enemy_type = enemy.__class__.__name__

    if player_type == enemy_type:
        print("Ничья")

    elif (
            (player_type == "Warrior" and enemy_type == 'Assassin') or
            (player_type == "Assassin" and enemy_type == 'Mage') or
            (player_type == "Mage" and enemy_type == 'Warrior')
    ):
        print(f'{player_type} победил!')

    else:
        print(f'{enemy_type} победил!')











