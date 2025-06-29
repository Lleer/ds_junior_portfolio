from examples import (
    Account,
    Car,
    Person,
    Dog,
    flatten,
    factorial_iter,
    factorial_rec,
    merge_sort,
)
import pytest

def test_account_deposit():
    acc = Account("Test", 100)
    acc.deposit(50)
    assert acc.get_balance() == 150


def test_account_withdraw():
    acc = Account("Test", 100)
    acc.withdraw(30)
    assert acc.get_balance() == 70


def test_account_overdraft():
    acc = Account("Test", 10)
    acc.withdraw(20)
    assert acc.get_balance() == 10  # баланс не меняется если не хватает денег


def test_person_introduce(capsys):
    p = Person("Vasya", 30)
    p.introduce()
    captured = capsys.readouterr()
    assert "Vasya" in captured.out


def test_car_honk(capsys):
    c = Car("Kia")
    c.honk()
    captured = capsys.readouterr()
    assert "гудит" in captured.out


def test_dog_bark(capsys):
    dog = Dog()
    dog.bark()
    captured = capsys.readouterr()
    assert "Гав" in captured.out


def test_flatten_simple():
    assert flatten([1, 2, 3]) == [1, 2, 3]


def test_flatten_nested():
    assert flatten([1, [2, 3], [4, [5, 6]], 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_flatten_deep():
    assert flatten([[1], [[2, [3]]]]) == [1, 2, 3]


def test_flatten_empty():
    assert flatten([]) == []


def test_flatten_mixed():
    assert flatten([[], [1, [2]], 3]) == [1, 2, 3]


def test_factorial_zero():
    assert factorial_iter(0) == 1
    assert factorial_rec(0) == 1


def test_factorial_one():
    assert factorial_iter(1) == 1
    assert factorial_rec(1) == 1


def test_factorial_general():
    assert factorial_iter(5) == 120
    assert factorial_rec(5) == 120


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial_iter(-1)
    with pytest.raises(ValueError):
        factorial_rec(-1)


def test_merge_sort_basic():
    assert merge_sort([5, 3, 8, 1]) == [1, 3, 5, 8]


def test_merge_sort_sorted():
    assert merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_merge_sort_reverse():
    assert merge_sort([4, 3, 2, 1]) == [1, 2, 3, 4]


def test_merge_sort_duplicates():
    assert merge_sort([2, 1, 2, 3]) == [1, 2, 2, 3]


def test_merge_sort_empty():
    assert merge_sort([]) == []
