import pytest
from cookies import Jar


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10

def test_negative_capacity():
    with pytest.raises(ValueError):
        jar = Jar(-13)

def test_str():
    jar = Jar(20)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(20)
    jar.deposit(3)
    assert jar.size == 3

def test_invalid_deposit():
    with pytest.raises(ValueError):
        jar = Jar(10)
        jar.deposit(15)

def test_withdraw():
    jar = Jar(20)
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1

def test_minus():
    with pytest.raises(ValueError):
        jar = Jar(5)
        jar.withdraw(7)





