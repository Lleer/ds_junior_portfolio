class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age}")


person_1 = Person("Alex", 25)
person_2 = Person("Bob", 20)

person_1.introduce()
person_2.introduce()


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # защищённое поле

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Not enough funds!")

    def get_balance(self):
        return self._balance


wallet = Account("Bob", 100)
wallet.deposit(100)
wallet.withdraw(20)
print(wallet.get_balance())


class Vehicle:
    def __init__(self, model):
        self.model = model

    def info(self):
        print(f"{self.model}")


class Car(Vehicle):
    def honk(self):
        print(f"{self.model} гудит")


car = Car("Kia")
car.info()
car.honk()


class Dog:
    def bark(self):
        print("Гав")

def flatten (lst):
    result = []
    for elem in lst:
        if isinstance (elem, list):
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return result
