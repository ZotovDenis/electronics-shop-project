import pytest

from src.phone import Phone


@pytest.fixture
def smartphone():
    return Phone("Смартфон", 10000, 20, 2)


def test_represent(smartphone):
    assert Phone.__repr__(smartphone) == "Phone('Смартфон', 10000, 20, 2)"


def test_number_of_sim(smartphone):
    assert smartphone.number_of_sim == 2
    smartphone.number_of_sim = 3
    assert smartphone.number_of_sim == 3
