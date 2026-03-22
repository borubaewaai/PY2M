'''#статический метод  @staticmethod

#используется, когда методу е нужны ни self ни cls.
#обычная функция но логически относящаяся к классу

class Math:
    @staticmethod
    def add(a, b):
        return a + b
print(Math.add(1, 2))


class Bank:
    # атрибута класса
    bank_name = "Mbank"

    def __init__(self, sum, user):
        # атрибуты экземпляра класса
        self.__sum = sum
        self.user = user

    def get_sum(self):
        return self.__sum
#Метод класса classmethod
   # получает доступ к самому классу через cls
   # используется для альтернативых конструкторов или работы к классу

    @classmethod
    def get_bank_name(cls):
        return cls.bank_name
janke = Bank(112,"Jan")
print(janke.get_sum())


# decorator property
# описаие : дкоратор проперти используеься для того чтобы метд стал досткпным как атрибуты классы
# это позволяет скрывать логику вычислений или проверки делая код более чистым
# для создаия геттеров ил сеттеров

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.price

first_product = Product(100)
print(first_product.price)


#1. Что такое декораторы?
# Декоратор - это функция, которая принимает другую функцию как аргумент ивозвращает новую функци, обычно обернутую в доп функциоальость.
def simple_decorator(func):
    def wrapper():
        print("До выполнения!")
        func()
        print('После выполнения!')
    return wrapper
@simple_decorator
def say_hello():
    print("Hello")
say_hello()'''


def repeat_decorator(count):
    def decorator(func):
        def wrapper(name):
            for i in range(count):
                print(f"{i} раз!!!\n")
                print(f"Hello {name}!!")
                func()
        return wrapper
    return decorator

@repeat_decorator(5)
def greating(name):
    print(f'How are you {name}')
greating("Jack")

# Разница между декоратором с параметрами и без их вложености
# декоратор с параметрами имеет двойную влоченость
#а без параметра оду