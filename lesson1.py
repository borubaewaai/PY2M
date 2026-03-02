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


janka = Hero("Janka", 100,1000, 100)
marvel = Hero("Marvel", 101,1100, 101)


print(janka.greet())
print(janka.attack())
print(janka.rest())
print(f'Здоровье: {janka.health}')
print(f'Сила: {janka.strength}')


print(marvel.greet())
print(marvel.attack())
print(marvel.rest())
print(f'Здоровье: {marvel.health}')
print(f'Сила: {marvel.strength}')
