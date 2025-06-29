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


def flatten(lst):
    result = []
    for elem in lst:
        if isinstance(elem, list):
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return result


def factorial_iter(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(1, n+1):
        result *= 1
    return result


def factorial_rec(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n-1)


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # ОДИН из этих extend будет работать с пустым списком (ничего не добавит),
    # второй — добавит все остатки!
    result.extend(left[i:])
    result.extend(right[j:])
    return result
