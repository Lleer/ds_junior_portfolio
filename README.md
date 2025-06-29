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
Докстринг — описание после def (тройные кавычки).
PEP8 — стандарт стиля кода. Проверка через flake8.

# --- 4. Работа с git и портфолио ---
# Все изменения — в git, каждый шаг — коммит, история сохраняется, легко показать и откатить:
Все изменения отслеживаются в git (commit, push).

Работаешь через ветки — одна задача = одна ветка, один коммит.

Пушишь код на GitHub — видно весь твой прогресс.

Историю изменений всегда можно показать или откатить.

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

#--- 7. Автотесты (pytest) и flake8 ---
# Код (классы, функции) — examples.py
# Тесты — test_examples.py

from examples import Account, Person

def test_account_deposit():
    acc = Account("Test", 100)
    acc.deposit(50)
    assert acc.get_balance() == 150
# assert проверяет, что результат такой, как ожидается.

def test_person_introduce(capsys):
    p = Person("Vasya", 30)
    p.introduce()
    captured = capsys.readouterr()
    assert "Vasya" in captured.out
# capsys — “заглушка” для проверки print. Через captured.out проверяем, что функция напечатала нужный текст.

#--- 8. CI/CD (GitHub Actions, flake8 + pytest) ---
# .github/workflows/python.yml:
name: Python package

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.11
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install flake8 pytest
    - name: Lint with flake8
      run: |
        flake8 .
    - name: Test with pytest
      run: |
        pytest

# Каждый push запускает flake8 и pytest. Вкладка Actions на GitHub показывает статус пайплайна и ошибки.

#--- 9. Функции для мини-проекта ---

# A. flatten — сплющивание вложенного списка
def flatten(lst):
    """
    Сплющивает вложенный список любой глубины.
    """
    result = []
    for elem in lst:
        if isinstance(elem, list):
            result.extend(flatten(elem))
        else:
            result.append(elem)
    return result

# Примеры:
flatten([1, [2, [3, 4]], 5])  # [1, 2, 3, 4, 5]
flatten([])                   # []
flatten([[[1]]])              # [1]

# B. factorial — факториал (итерация и рекурсия, с защитой)
def factorial_iter(n):
    """
    Вычисляет факториал числа итеративно.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

def factorial_rec(n):
    """
    Вычисляет факториал числа рекурсивно.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n-1)

# Примеры:
factorial_iter(5)  # 120
factorial_rec(0)   # 1
# factorial_iter(-1) -> ValueError

# C. merge_sort — сортировка слиянием
def merge_sort(lst):
    """
    Сортировка слиянием (merge sort) — делит список пополам и сливает через merge.
    """
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    """
    Сливает два отсортированных списка в один.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Примеры:
merge_sort([3, 2, 1])      # [1, 2, 3]
merge_sort([])             # []
merge_sort([1, 1, 2, -1])  # [-1, 1, 1, 2]

#--- 10. Примеры автотестов ---

def test_flatten_simple():
    assert flatten([1, [2, [3]], 4]) == [1, 2, 3, 4]

def test_factorial_iter():
    assert factorial_iter(5) == 120

def test_factorial_negative():
    import pytest
    with pytest.raises(ValueError):
        factorial_iter(-1)

def test_merge_sort_empty():
    assert merge_sort([]) == []

def test_merge_sort_duplicates():
    assert merge_sort([2, 1, 2, 1]) == [1, 1, 2, 2]

#--- 11. Итоговый мини-проект ---
# flatten, factorial (iter/rec), merge_sort реализованы и покрыты автотестами.
# Весь код оформлен в examples.py, тесты — test_examples.py.
# Автоматические проверки через flake8 и pytest (pipeline CI).
# Всё структурировано по best practice для портфолио.

#--- 12. Markdown-выводы (RU/EN) ---
# Выводы на русском:
# - Освоил работу с типами, функциями, коллекциями, генераторами, ООП.
# - Научился писать автотесты, оформлять код по PEP8, запускать CI на GitHub.
# - Реализовал мини-проект (flatten, factorial, merge_sort) с автотестами.

# Conclusions in English:
# - Learned how to work with Python types, functions, collections, comprehensions, and OOP.
# - Practiced writing unit tests, using PEP8, and running CI workflows on GitHub.
# - Implemented and tested core algorithms (flatten, factorial, merge_sort) as a miniproject.

#--- 13. Чек-лист по фазе 1 ---
- [x] Типы данных, коллекции, генераторы
- [x] Функции, *args, **kwargs, докстринги, PEP8, flake8
- [x] Классы, инкапсуляция, наследование, полиморфизм, абстракция
- [x] Git, коммиты, работа с портфолио
- [x] CI/CD: пайплайны, flake8, pytest
- [x] Профилирование кода
- [x] Мини-проект: flatten, factorial, merge_sort с тестами и CI

#--- 14. Дальше — ФАЗА 2 ---
# SQL (базовые запросы, join, group by, оконные функции)
# Pandas (загрузка, чистка, EDA, агрегация)
# Реальные “грязные” кейсы

