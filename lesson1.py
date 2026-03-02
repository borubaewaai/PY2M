class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def action(self):
        return f'{self.name}base action avtivate!!'

janka = Hero("Janka", 100,1000, 100)
marvel = Hero("Marvel", 101,1100, 101)

