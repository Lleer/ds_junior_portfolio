# ===== DS Junior Portfolio =====
# Автор: Lleer

# ========== ФАЗА 1: Python & Git ==========

# --- 1. Типы данных и коллекции ---
# Изучаем, как объявлять переменные всех основных типов и коллекций:
a=3                  # int
b=1.5                # float
c='cnn'              # str
d=True               # bool
e=[1,2,3]            # list (изменяемый, допускает дубликаты, доступ по индексу)
f=(1,2,3)            # tuple (НЕизменяемый, допускает дубликаты, доступ по индексу)
g={1,2,3}            # set (уникальные значения, порядок не гарантирован, нет доступа по индексу)
h={'a':1,'b':2}      # dict (пары ключ-значение, доступ по ключу)

# --- 2. Генераторы списков и множеств, for-цикл ---
# Создание новых коллекций из существующих. List и set comprehensions:
list_1=[1,2,3,4,5]
result=[x*10 for x in list_1]   # [10,20,30,40,50]
result2=[]
for x in list_1:
    result2.append(x*10)

list_4=[1,1,2,3,3,4]
set_1={x**2 for x in list_4}    # {16, 1, 4, 9}  # квадраты без дубликатов

# --- 3. Функции, *args, **kwargs, докстринги, PEP8 ---
# Пишем универсальные функции с любым количеством аргументов.
# Документируем (докстринг — после def, тройные кавычки).
def summ_all(*args):
    """
    Складывает все переданные числа.
    """
    return sum(args)

def show_info(**kwargs):
    """
    Печатает все пары ключ-значение.
    """
    for key, value in kwargs.items():
        print(key, value)

# Пример вызова:
summ_all(1,2,3,4)                # => 10
show_info(a=5, b=7)              # => a 5 \n b 7

# --- PEP8 ---
# Код проверяем через flake8, отступы — 4 пробела, названия функций — snake_case.

# --- 4. Работа с git и портфолио ---
# Все изменения — в git, каждый шаг — коммит, история сохраняется, легко показать и откатить:
git init
git add .
git commit -m "feat: add functions and args practice"
git remote add origin https://github.com/Lleer/ds_junior_portfolio.git
git push -u origin main

# Инструкция по регулярному пушу изменений:
git add .
git commit -m "feat: readme + полное завершение Фазы 1"
git push

# --- 5. Профилирование кода (cProfile) ---
# Узнаём, где в коде "тормоза", измеряем производительность функций:
import cProfile
def sum_list(lst):
    total=0
    for x in lst:
        total+=x
    return total
lst=list(range(1,10001))
cProfile.run('sum_list(lst)')
# Вывод: сколько вызовов функций, сколько времени, где узкие места

# --- 6. Основы ООП: классы, инкапсуляция, наследование, переопределение, полиморфизм ---

# === Классы ===
# Класс создаёт собственный тип данных. Всё начинается с class ИмяКласса:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age}")

p = Person("Иван", 30)
p.introduce()       # Меня зовут Иван, мне 30

# === Инкапсуляция ===
# Прячем детали: public, protected, private
class Account:
    def __init__(self, owner, balance):
        self.owner = owner         # public (все видят)
        self._balance = balance    # protected (по соглашению: "не лезь")
        self.__secret = 42         # private (скрыто, извне не достать)
    def deposit(self, amount):
        self._balance += amount
    def get_secret(self):
        return self.__secret

acc = Account("Bob", 100)
print(acc.owner)          # Bob
print(acc._balance)       # 100 (можно, но не принято)
# print(acc.__secret)     # Ошибка! Доступ запрещён
print(acc.get_secret())   # 42 (доступ через метод)

# === Наследование ===
# Дочерний класс берёт всё от родителя + добавляет/меняет своё:
class Vehicle:
    def __init__(self, name):
        self.name = name
    def start(self):
        print(f"{self.name} поехал!")

class Car(Vehicle):
    def start(self):
        super().start()           # вызываем поведение родителя
        print(f"{self.name} — это автомобиль")

car = Car("Toyota")
car.start()
# Toyota поехал!
# Toyota — это автомобиль

# === Переопределение (overriding) ===
# Переопределяем любой метод с тем же именем — вызывается у дочернего, а не родителя.
# Можно (и иногда нужно) вызвать родительский через super() — тогда логика родителя + новая логика.

# === Полиморфизм ===
# Функция работает с разными объектами, если у них общий метод — неважно, какой класс:
class Cat:
    def speak(self):
        print("Мяу!")
class Dog:
    def speak(self):
        print("Гав!")
def animal_speak(animal):
    animal.speak()
for pet in [Cat(), Dog()]:
    animal_speak(pet)
# Мяу!
# Гав!

# === Абстракция (дополнительно) ===
# Можно создать "шаблонный" класс (через abc), чтобы все наследники реализовывали нужные методы:
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

# === Итоговый чек-лист (по фазе 1) ===
# [x] Типы данных, коллекции
# [x] Генераторы списков, set comprehension
# [x] Функции, *args, **kwargs, докстринги, PEP8
# [x] Git, коммиты, push на GitHub
# [x] Профилирование кода
# [x] ООП: классы, инкапсуляция, наследование, полиморфизм, абстракция

# --- TODO ---
# - Каждый блок: задача -> код -> выводы (и в git)
# - Далее: pandas, SQL, EDA, визуализация
# - README.md — навигатор, всегда обновлять!

# === ФАЗА 1 ЗАВЕРШЕНА ===
# Дальше: SQL & pandas
