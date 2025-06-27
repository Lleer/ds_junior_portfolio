from examples import Account, Car, Person, Dog


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

