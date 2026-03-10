
'''import random
class BankAccount:
    def __init__(self, login, password, balance):
        self.login = login
        self._balance = balance
        self.__password = password

    def get_balance(self, password):
        if password == self.__password:
            return self._balance

        return 'Wrong password'

    def __generate_password(self):
        return random.randint(1, 100)
    def change_password(self, password):
        if password == self.__password:
            self.__password = self.__generate_password()
            return "New password"
        return 'Wrong password'
ardager = BankAccount('ardager', 'sms', '20000')




print(ardager._BankAccount__password)
print(ardager.change_password("sms"))
print(ardager._BankAccount__password)

print(dir(ardager))
print(ardager._BankAccount__password)
print(ardager.login)
print(ardager._password)
print(ardager.get_balance('sms'))
'''

#2
'''''
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return 'Gaff gaff'

    def move(self):
        return 'Step step'

gufi = Dog()
print(gufi.make_sound())
print(gufi.move())
'''


'''
from abc import ABC, abstractmethod
class OTPSend(ABC):
    @abstractmethod
    def send(self, phone):
        pass

class KGOTPSend(OTPSend):
    @abstractmethod
    def send(self, phone):
        sms = """
             <Phone>+996700329592</Phone>
             <Text>Ваш пароль 1234</Text>
           """
        return sms

class RUOTPSend(OTPSend):
    @abstractmethod
    def send(self, phone):
        sms = {
            "Phone": "+7474759686"
            "Text": "Ваш пароль 1234"
        }
        return sms
'''







