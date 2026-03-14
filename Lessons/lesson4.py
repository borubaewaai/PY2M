class Test:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

#test_obj = Test('Jannat')
#print(test_obj)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

obj_1 = Vector(11,22)
obj_2 = Vector(33, 88)
obj_3 = obj_1 + obj_2

print(obj_3)